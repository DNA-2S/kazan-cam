import base64
import json
import time
from multiprocessing import Pool
import os

import redis
from tornado import websocket, web, ioloop

from recorder import create_videostream

MAX_FPS = 24


class IndexHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    """ Handler for the root static page. """

    def get(self):
        """ Retrieve the page content. """
        self.write({'message': 'hello root world'})


class RestHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.write({'message': 'hello test world'})


class CameraListRequestHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        with open('mock/camera_info.json', encoding='utf-8') as f:
            mocked_camera_info_list = json.load(f)

        self.write(json.dumps(mocked_camera_info_list))


class CameraImageRequestHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, cam_id):
        mocked_camera_image_file = f"mock/cams/{cam_id}.jpg"
        image = open(mocked_camera_image_file, 'rb')
        image_read = image.read()
        image_64_encode = base64.b64encode(image_read)

        returned_data = {
            "image": image_64_encode.decode("utf-8")
        }

        self.write(returned_data)


class CameraTrashInfoRequestHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, cam_id):
        # TODO Сейчас данные по заполнености корзины читаются из мок-файлов. Далее планируется применить нейросеть для
        # TODO определения заполннености
        with open('mock/camera_info.json', encoding='utf-8') as f:
            mocked_camera_info_list = json.load(f)

        for camera_info in mocked_camera_info_list:
            if camera_info['id'] == int(cam_id):
                returned_data = {
                    "filledContainers": camera_info['containers'].count(True),
                    "totalContainers": len(camera_info['containers'])
                }

                self.write(returned_data)


class SocketHandler(websocket.WebSocketHandler):
    """ Handler for the websocket URL. """

    def __init__(self, *args, **kwargs):
        """ Initialize the Redis store and framerate monitor. """

        super().__init__(*args, **kwargs)
        if "REDIS_URL" in os.environ:
            self._store = redis.Redis().from_url(os.environ['REDIS_URL'])
        else:
            self._store = redis.Redis()

        self._prev_image_id = None

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        """ Retrieve image ID from database until different from last ID,
        then retrieve image, de-serialize, encode and send to client. """

        while True:
            time.sleep(1. / MAX_FPS)
            image_id = self._store.get('image_id')
            if image_id != self._prev_image_id:
                break
        self._prev_image_id = image_id
        image = self._store.get('image')
        image = base64.b64encode(image)
        self.write_message(image)


app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/test', RestHandler),
    (r'/api/camera', CameraListRequestHandler),
    (r'/api/camera/([^/]*)/image', CameraImageRequestHandler),
    (r'/api/camera/([^/]*)/trash', CameraTrashInfoRequestHandler),
])


def create_app():
    port = int(os.environ.get('PORT', 9000))
    print(port)
    app.listen(port)
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    pool = Pool(processes=2)
    stream = pool.apply_async(create_app)
    server = pool.apply_async(create_videostream)

    pool.close()
    pool.join()

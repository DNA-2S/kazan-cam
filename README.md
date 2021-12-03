<h4>Реализованная функциональность</h4>
<ul>
    <li></li>
</ul>

<h4>Особенность проекта в следующем:</h4>
<ul>
	<li></li>
</ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Python 3+.</li>
	<li>HTML, CSS, JavaScript, TypeScript.</li>
	<li>SCSS.</li>
	<li>Gulp, Webpack, Babel.</li>
	<li>Vue.</li>
	<li>Git.</li>
	<li>Heroku.</li>
	<li>Vercel.</li>
 </ul>

<h4>Демо</h4>
Демо сервиса доступно по адресу: https://kazan-cam.vercel.app/

Бэкенд располагается по адресу: https://kazan-cam.herokuapp.com/

Установка и запуск
------------
 Сервер
------

### Сборка и запуск на Linux
```bash
sudo apt-get update
sudo apt-get install -y software-properties-common python3.9 python3-pip install ffmpeg libsm6 libxext6 -y

cd kazan-cam/server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker run -d -p 6379:6379 --name realtime-redis redis 
python -m server
```

### Сборка и запуск с помощью Docker
```bash
cd kazan-cam/server
docker build --tag kazan-cam-backend .
docker run -d -p 6379:6379 --name realtime-redis redis 
docker run -d -p 9000:9000 --name realtime-backend kazan-cam-backend 
```

###Эндпоинты

Сваггер находится тут: https://app.swaggerhub.com/apis/stepan14041999/kazan-cam/1.0.0#/

Также имеется файл server/kazan-cam-1.0.0-swagger.yaml для локальной загрузки

Базовый URL (Для локального окружения): http://localhost:9000

Список:
- /api/camera - Получение информации по камерам (Город, улица, ID)
- /api/camera/{id}/image - Получение замоканного изображения с камеры
- /api/cabera/{id}/trash - Получение результата нейросети о состоянии мусорных корзин на изображении с камеры

***

 Клиент
------

### Среда запуска

- NodeJS, NPM 14.17.0+ 
- Yarn 1.22.5+

### Установка
```
git clone git@github.com:DNA-2S/kazan-cam.git
cd kazan-cam/client
yarn install
```

### Компиляция
```
yarn serve
```

### Сборка
```
yarn build
```

## Разработчики

<h4>Шерстнев Никита - Data Science, Backend https://t.me/iewkw</h4>
<h4>Давидович Артем - Full-Stack https://t.me/artyom_d </h4>
<h4>Сандуляк Степан - Backend https://t.me/developmc </h4>
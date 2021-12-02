<template>
  <div id="map" class="q-map"></div>
  <template :key="cam.id" v-for="cam in cams">
    <k-garbage-icon :id="cam.id" v-if="text === '0'"></k-garbage-icon>
    <k-camera-icon :id="cam.id" v-else-if="text === '1'"></k-camera-icon>
    <k-car-icon :id="cam.id" v-else-if="text === '2'"></k-car-icon>
  </template>
  <div class="test">
    <input v-model="text" type="text" />
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref } from "vue";
import { Camera } from "@/types";
import KGarbageIcon from "@/components/KGarbageIcon.vue";
import KCameraIcon from "@/components/KCameraIcon.vue";
import KCarIcon from "@/components/KCarIcon.vue";

export default defineComponent({
  name: "KMap",
  components: { KCarIcon, KCameraIcon, KGarbageIcon },
  emits: ["select"],
  props: {
    cams: {
      type: Object as PropType<Camera[]>,
      required: true,
    },
  },
  setup(props, { emit }) {
    const ymaps = (window as any).ymaps;
    let myMap: any = null;
    const text = ref("1");

    const init = function () {
      myMap = new ymaps.Map(
        "map",
        {
          center: [55.796, 49.106],
          zoom: 13,
          controls: [],
        },
        {
          yandexMapDisablePoiInteractivity: true,
        }
      );

      props.cams.forEach((item, index) => {
        ymaps
          .geocode(item.address, {
            results: 1,
          })
          .then((res: any) => {
            const geoObject = res.geoObjects.get(0);

            if (geoObject) {
              addGeoPoint(geoObject, item.address, item.id);
            } else {
              console.log(index);
            }
          });
      });
    };

    const addGeoPoint = (geoObject: any, label: string, id: number) => {
      const MyIconLayout = ymaps.templateLayoutFactory.createClass(
        [
          '<svg width="92" height="92" style="position: absolute; top: -23px; left: -23px;">',
          `<use href="#sym${id}"/>`,
          "</svg>",
        ].join("")
      );

      const myPlacemark = new ymaps.Placemark(
        geoObject.geometry.getCoordinates(),
        {
          hintContent: label,
          balloonContent: label,
          iconContent: "XXX",
        },
        {
          iconLayout: MyIconLayout,
          iconShape: {
            type: "Circle",
            coordinates: [0, 0],
            radius: 23,
          },
        }
      );

      myMap.geoObjects.add(myPlacemark);
    };

    ymaps.ready(init);

    return {
      text,
    };
  },
});
</script>

<style scoped lang="scss">
.q-map {
  width: 100%;
  height: 100%;
}

.test {
  position: absolute;
  top: 100px;
  left: 100px;
}
</style>

<template>
  <div id="map" class="q-map"></div>
  <k-garbage-icon :id="0"></k-garbage-icon>
  <div class="test">
    <input v-model="text" type="text" />
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref } from "vue";
import { Camera } from "@/types";
import KGarbageIcon from "@/components/KGarbageIcon.vue";

export default defineComponent({
  name: "KMap",
  components: { KGarbageIcon },
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
    const text = ref("");

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
              addGeoPoint(geoObject, item.address);
            } else {
              console.log(index);
            }
          });
      });
    };

    const addGeoPoint = (geoObject: any, label: string) => {
      const MyIconLayout = ymaps.templateLayoutFactory.createClass(
        [
          '<svg width="92" height="92" style="position: absolute; top: -23px; left: -23px;">',
          '<use href="#sym0"/>',
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

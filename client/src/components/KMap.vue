<template>
  <div id="map" class="q-map"></div>
  <template :key="cam.id" v-for="cam in cams">
    <k-garbage-icon
      :id="cam.id"
      v-if="viewType === ViewType.DUMPSTER"
      color="#FFB90B"
    ></k-garbage-icon>
    <k-camera-icon
      :id="cam.id"
      color="#6E4CF5"
      v-else-if="viewType === ViewType.CAMS"
    ></k-camera-icon>
    <k-car-icon
      :id="cam.id"
      v-else-if="viewType === ViewType['PARKING-AREA']"
    ></k-car-icon>
  </template>
</template>

<script lang="ts">
import { computed, defineComponent, PropType, ref, watch } from "vue";
import { Camera, ViewType } from "@/types";
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
    viewType: {
      type: Number,
      default: ViewType.CAMS,
    },
  },
  setup(props, { emit }) {
    const ymaps = (window as any).ymaps;
    let myMap: any = null;

    const camsIds = computed(() => {
      return props.cams.map((item) => item.id);
    });

    watch(
      () => camsIds.value,
      (value) => {
        myMap.geoObjects.each((geoObject: any) => {
          geoObject.options.set(
            "visible",
            value.indexOf(geoObject.properties.get("idCam")) !== -1
          );
        });
      }
    );

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
          idCam: id,
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
      ViewType,
    };
  },
});
</script>

<style scoped lang="scss">
.q-map {
  width: 100%;
  height: 100%;
}
</style>

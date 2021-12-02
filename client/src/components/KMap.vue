<template>
  <div id="map" class="q-map"></div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { Camera } from "@/types";

export default defineComponent({
  name: "KMap",
  emits: ["select"],
  props: {
    cams: {
      type: Object as PropType<Camera[]>,
      required: true,
    },
  },
  setup(_, { emit }) {
    const init = function () {
      const myMap = new (window as any).ymaps.Map(
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

      (window as any).ymaps
        .geocode(myMap.getCenter(), {
          results: 1,
        })
        .then(function (res: any) {
          res.geoObjects.each((geoObject: any) => {
            if (geoObject.getPremise()) {
              geoObject.options.set("preset", "islands#redCircleIcon");
              myMap.geoObjects.add(geoObject);
              geoObject.events.add("click", function (event: any) {
                let geoObject = event.get("target");
                emit("select", {
                  name: geoObject.getPremise(),
                  coords: geoObject.geometry.getCoordinates(),
                });
              });
            }
          });
        });
    };

    (window as any).ymaps.ready(init);
  },
});
</script>

<style scoped lang="scss">
.q-map {
  width: 100%;
  height: 100%;
}
</style>

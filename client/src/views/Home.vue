<template>
  <div class="k-home" :class="{ details: detailsCam }">
    <aside class="k-sidebar">
      <k-title-bar />

      <template v-if="!detailsCam">
        <div class="k-sidebar__input-wrapper">
          <i class="fas fa-search k-sidebar__input-icon"></i>
          <input type="text" class="k-sidebar__input" v-model="search" />
        </div>

        <div class="k-sidebar__items">
          <k-item-card
            v-for="item in filteredData"
            :key="item.id"
            :camera="item"
            :active="selectedCam === item.id"
            @click="selectedCam = item.id"
            @details="$router.push({ path: '/', query: { camId: $event.id } })"
          />
        </div>
      </template>
      <template v-else>
        <k-camera-info
          @back="
            $router.push({ path: '/' });
            detailsCam = undefined;
          "
          :cam="detailsCam"
        />
      </template>
    </aside>
    <main class="k-map-container">
      <div class="k-map-container__selector">
        <k-view-type-selector
          :view-type="viewType"
          @select="viewType = $event"
        />
      </div>
      <k-logs :logs="logs" class="k-map-container__logs" />
      <k-map
        :select-cam="selectedCam"
        :view-type="viewType"
        :cams="filteredData"
        @details="$router.push({ path: '/', query: { camId: $event } })"
        v-if="isLoaded"
      ></k-map>
    </main>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, inject, onMounted, ref, watch } from "vue";
import KMap from "@/components/KMap.vue";
import camsJson from "@/data/cams.json";
import { Camera, LogObject, ViewType } from "@/types";
import KItemCard from "@/components/KItemCard.vue";
import KViewTypeSelector from "@/components/KViewTypeSelector.vue";
import KTitleBar from "@/components/KTitleBar.vue";
import KCameraInfo from "@/components/KCameraInfo.vue";
import * as random from "random-seed";
import KLogs from "@/components/KLogs.vue";
import { useRoute } from "vue-router";

export default defineComponent({
  name: "Home",
  components: {
    KLogs,
    KCameraInfo,
    KTitleBar,
    KViewTypeSelector,
    KItemCard,
    KMap,
  },
  setup() {
    const isLoaded = ref(false);
    const search = ref("");
    const viewType = ref<ViewType>(ViewType.CAMS);
    const selectedCam = ref(-1);
    const detailsCam = ref<Camera>();
    const logs = ref<LogObject[]>([]);
    const cams = ref<Camera[]>([]);

    const route = useRoute();

    watch(
      () => route.query,
      (value) => {
        if (value["camId"]) {
          detailsCam.value = camById(parseInt(value["camId"][0] || ""));
        }
      }
    );

    onMounted(() => {
      if (route.query["camId"]) {
        setTimeout(
          (camId: string) =>
            (detailsCam.value = camById(parseInt(camId || ""))),
          500,
          route.query["camId"][0]
        );
      }

      const r = random.create();

      cams.value = (camsJson as Camera[]).map((item) => {
        const value = r.range(100) / 100;

        log({
          timestamp: Date.now(),
          message: "Пробное сообщение в лог",
          cam: item,
        });

        return {
          ...item,
          value,
        };
      });

      if (
        document.head.querySelectorAll(
          'script[src*="https://api-maps.yandex.ru/2.1/"]'
        ).length > 0
      ) {
        return;
      }
      let ymapsScript = document.createElement("script");
      ymapsScript.setAttribute(
        "src",
        `https://api-maps.yandex.ru/2.1/?apikey=${process.env.VUE_APP_MAP_KEY}&lang=ru_RU`
      );
      document.head.appendChild(ymapsScript);

      setTimeout(() => (isLoaded.value = true), 600);
    });

    const filteredData = computed(() => {
      return cams.value
        .filter((item) => {
          return (
            (viewType.value === ViewType.DUMPSTER && item?.dumpster) ||
            (viewType.value === ViewType["PARKING-AREA"] &&
              item?.["parking-area"]) ||
            viewType.value === ViewType.CAMS
          );
        })
        .filter((item) =>
          item.address.toLowerCase().includes(search.value.toLowerCase())
        );
    });

    const camById = (id: number): Camera => {
      return cams.value.filter((item) => item.id === id)[0];
    };

    const log = (obj: LogObject): void => {
      logs.value.push(obj);
    };

    inject("log", log);

    return {
      isLoaded,
      camsJson,
      filteredData,
      search,
      viewType,
      ViewType,
      selectedCam,
      detailsCam,
      camById,
      logs,
    };
  },
});
</script>

<style lang="scss" scoped>
.k-home {
  height: 100%;
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-areas: "sidebar map";
  grid-template-columns: 480px 1fr;
  grid-template-rows: 1fr;

  &.details {
    grid-template-columns: 40% 1fr;
  }
}

.k-sidebar {
  grid-area: sidebar;
  height: 100%;
  width: 100%;
}

.k-map-container {
  grid-area: map;
  height: 100%;
  width: 100%;
  overflow: hidden;
  position: relative;

  &__logs {
    position: absolute;
    bottom: 10px;
    right: 10px;
    z-index: 999;
  }

  &__selector {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 999;
    user-select: none;
  }
}

.k-sidebar {
  background: #fff;
  border-radius: 15px;
  padding: 15px;
  box-shadow: 2px 2px 15px 0 rgba(#000, 0.25);
  overflow: hidden;

  &__title {
    font-weight: bolder;
    text-transform: capitalize;
    font-size: 1.3em;
    text-align: center;
  }

  &__nav {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 20px auto 15px auto;
  }

  &__items {
    width: calc(100% - 30px);
    height: calc(100% - 175px);
    overflow-y: auto;
  }

  &__input-wrapper {
    height: 36px;
    width: calc(100% - 30px);
    position: relative;
    box-sizing: border-box;
    margin: 22px 0 12px 0;
  }

  &__input-icon {
    position: absolute;
    top: 12px;
    left: 12px;
    color: rgba(#000, 0.6);
  }

  &__input {
    width: calc(100% - 45px);
    height: calc(100% - 4px);
    border-radius: 12px;
    outline: none;
    border: 1px solid rgba(#000, 0.15);
    box-shadow: 0 2px 5px 0 rgba(#000, 0.15);
    padding: 2px 5px 2px 40px;
    font-weight: 500;
    font-size: 1.1em;
    transition: 250ms;

    &:focus {
      border: 1px solid rgba(#269ef1, 0.7);
      box-shadow: 0 1px 3px 0 rgba(#000, 0.25);
    }
  }
}
</style>

<template>
  <div class="k-home">
    <aside class="k-sidebar">
      <div class="k-sidebar__input-wrapper">
        <i class="fas fa-search k-sidebar__input-icon"></i>
        <input type="text" class="k-sidebar__input" v-model="search" />
      </div>

      <div class="k-sidebar__items">
        <k-item-card
          v-for="item in filteredData"
          :key="item.id"
          :name="item.address"
          :desc="item.address"
          :active="selectedCam === item.id"
          @click="selectedCam = item.id"
        />
      </div>
    </aside>
    <main class="k-map-container">
      <div class="k-map-container__selector">
        <k-view-type-selector
          :view-type="viewType"
          @select="viewType = $event"
        />
      </div>
      <k-map
        :select-cam="selectedCam"
        :view-type="viewType"
        :cams="filteredData"
        v-if="isLoaded"
      ></k-map>
    </main>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from "vue";
import KMap from "@/components/KMap.vue";
import camsJson from "@/data/cams.json";
import { Camera, ViewType } from "@/types";
import KItemCard from "@/components/KItemCard.vue";
import KViewTypeSelector from "@/components/KViewTypeSelector.vue";

export default defineComponent({
  name: "Home",
  components: { KViewTypeSelector, KItemCard, KMap },
  setup() {
    const isLoaded = ref(false);
    const search = ref("");
    const viewType = ref<ViewType>(ViewType.CAMS);
    const selectedCam = ref(-1);

    onMounted(() => {
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
      return (camsJson as Camera[])
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

    return {
      isLoaded,
      camsJson,
      filteredData,
      search,
      viewType,
      ViewType,
      selectedCam,
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
  position: relative;

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
    height: calc(100% - 115px);
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

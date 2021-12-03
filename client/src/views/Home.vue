<template>
  <div class="k-home">
    <aside class="k-sidebar">
      <div class="k-sidebar__input-wrapper">
        <i class="fas fa-search k-sidebar__input-icon"></i>
        <input type="text" class="k-sidebar__input" v-model="search" />
      </div>

      <div class="k-sidebar__items">
        <k-item-card
          v-for="item in camsJson"
          :key="item.id"
          :name="item.address"
          :desc="item.address"
          :active="false"
        />
      </div>
    </aside>
    <main class="k-map-container">
      <k-map
        :view-type="ViewType.CAMS"
        :cams="camsJson"
        v-if="isLoaded"
      ></k-map>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import KMap from "@/components/KMap.vue";
import camsJson from "@/data/cams.json";
import { Camera, ViewType } from "@/types";
import KItemCard from "@/components/KItemCard.vue";

export default defineComponent({
  name: "Home",
  components: { KItemCard, KMap },
  setup() {
    const isLoaded = ref(false);
    const search = ref("");

    onMounted(() => {
      let ymapsScript = document.createElement("script");
      ymapsScript.setAttribute(
        "src",
        `https://api-maps.yandex.ru/2.1/?apikey=${process.env.VUE_APP_MAP_KEY}&lang=ru_RU`
      );
      document.head.appendChild(ymapsScript);

      setTimeout(() => (isLoaded.value = true), 300);
    });

    return {
      isLoaded,
      camsJson,
      search,
      ViewType,
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

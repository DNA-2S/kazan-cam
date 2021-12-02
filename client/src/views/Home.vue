<template>
  <div class="k-home">
    <k-map :cams="camsJson" v-if="isLoaded"></k-map>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import KMap from "@/components/KMap.vue";
import camsJson from "@/data/cams.json";

export default defineComponent({
  name: "Home",
  components: { KMap },
  setup() {
    const isLoaded = ref(false);

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
    };
  },
});
</script>

<style lang="scss" scoped>
.k-home {
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
}
</style>

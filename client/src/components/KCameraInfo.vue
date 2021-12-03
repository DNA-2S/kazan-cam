<template>
  <div class="k-camera-info">
    <img :src="getImgById(cam.id)" class="k-camera-info__img" alt="Cam" />
    <el-button size="large">Назад</el-button>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { Camera } from "@/types";

export default defineComponent({
  name: "KCameraInfo",
  props: {
    cam: {
      type: Object as PropType<Camera>,
    },
  },
  setup() {
    const getImgById = (id: number) => {
      return require(`../assets/cams/${id}.jpg`);
    };

    return {
      getImgById,
    };
  },
});
</script>

<style lang="scss" scoped>
.k-camera-info {
  width: 100%;

  &__img {
    width: 100%;
  }
}
</style>

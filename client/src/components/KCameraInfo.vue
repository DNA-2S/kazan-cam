<template>
  <div class="k-camera-info">
    <img :src="getImgById(cam.id)" class="k-camera-info__img" alt="Cam" />
    <el-button @click="$emit('back')" size="large">Назад</el-button>
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
  emits: ["back"],
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
  width: calc(100% - 30px);
  position: relative;

  &__img {
    width: 100%;
  }
}
</style>

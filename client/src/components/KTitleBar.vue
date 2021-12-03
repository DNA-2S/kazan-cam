<template>
  <div class="k-title-bar">
    <img src="@/assets/logo.png" class="k-title-bar__logo" alt="Logo" />
    <div class="k-title-bar__title">Зилант</div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "KTitleBar",
});
</script>

<style lang="scss" scoped>
.k-title-bar {
  display: flex;
  justify-content: center;
  height: 80px;
  width: 100%;
  gap: 1rem;
  align-items: center;

  &__logo {
    width: 100px;
  }

  &__title {
    font-weight: bolder;
    font-size: 41px;
    line-height: 80px;
    padding-top: 12px;
  }
}
</style>

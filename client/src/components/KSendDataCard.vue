<template>
  <div class="k-send-data-card" @click="active = !active" :class="{ active }">
    <div class="k-send-data-card__img">
      <slot></slot>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "KSendDataCard",
  setup() {
    const active = ref(true);

    return {
      active,
    };
  },
});
</script>

<style lang="scss" scoped>
.k-send-data-card {
  width: 60px;
  height: 60px;
  overflow: hidden;
  border: 1px solid rgba(#000, 0.1);
  box-shadow: 0 2px 10px 0 rgba(#000, 0.1);
  margin: 15px 7px;
  text-align: left;
  background: #fff;
  transition: 250ms;

  &.active {
    background: rgba(#269ef1, 0.15);
    border: 1px solid rgba(#269ef1, 0.55);
    box-shadow: 0 1px 5px 0 rgba(#000, 0.1);
  }
}
</style>

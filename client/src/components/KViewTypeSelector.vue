<template>
  <div
    class="k-view-type-selector"
    :style="{ '--k-select-color': selectColor }"
  >
    <div
      class="k-view-type-selector__option"
      :class="{ selected: viewType === ViewType.DUMPSTER }"
      ref="dumpsters"
      @click="$emit('select', ViewType.DUMPSTER)"
    >
      <i class="fas fa-trash-alt"></i>
      Мусор
    </div>
    <div
      class="k-view-type-selector__option"
      :class="{ selected: viewType === ViewType.CAMS }"
      ref="cams"
      @click="$emit('select', ViewType.CAMS)"
    >
      <i class="fas fa-video"></i>
      Камеры
    </div>
    <div
      class="k-view-type-selector__option"
      :class="{ selected: viewType === ViewType['PARKING-AREA'] }"
      ref="cars"
      @click="$emit('select', ViewType['PARKING-AREA'])"
    >
      <i class="fas fa-car"></i>
      Авто
    </div>
    <div
      class="k-view-type-selector__select"
      :style="{ left: `${selectPos - 5}px` }"
    ></div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from "vue";
import { ViewType } from "@/types";

export default defineComponent({
  name: "KViewTypeSelector",
  props: {
    viewType: {
      type: Number,
      require: true,
    },
  },
  emits: ["select"],
  setup(props) {
    const cars = ref<HTMLDivElement>();
    const cams = ref<HTMLDivElement>();
    const dumpsters = ref<HTMLDivElement>();

    const selectColor = computed(() => {
      if (props.viewType === ViewType.CAMS) {
        return "#6E4CF5";
      } else if (props.viewType === ViewType.DUMPSTER) {
        return "#FFB90B";
      } else {
        return "#7DC33A";
      }
    });

    const selectPos = computed(() => {
      let div = null;
      if (props.viewType === ViewType.CAMS) {
        div = cams.value;
      } else if (props.viewType === ViewType.DUMPSTER) {
        div = dumpsters.value;
      } else {
        div = cars.value;
      }

      return div?.offsetLeft || 155;
    });

    return {
      cars,
      cams,
      dumpsters,

      selectColor,
      selectPos,

      ViewType,
    };
  },
});
</script>

<style lang="scss" scoped>
.k-view-type-selector {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 450px;
  height: 46px;
  background: #fff;
  border-radius: 13px;
  position: relative;
  box-shadow: 2px 2px 15px 0 rgba(#000, 0.25);

  &__select {
    border-radius: 13px;
    height: 46px;
    width: 150px;
    position: absolute;
    background: var(--k-select-color);
    z-index: 1;
    transition: 400ms;
  }

  &__option {
    transition: 400ms;
    z-index: 2;
    box-sizing: border-box;
    height: 46px;
    width: 150px;
    padding: 8px 15px;
    line-height: 30px;
    margin: 0 5px;
    border-radius: 13px;
    background: transparent;
    color: #2c3e50;
    cursor: pointer;

    &.selected {
      font-weight: bold;
      color: #fff;
    }
  }
}
</style>

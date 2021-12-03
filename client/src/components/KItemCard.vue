<template>
  <div
    class="k-item-card"
    :class="{ active }"
    :style="{ '--k-base-color': color }"
    @mouseenter="showButton = true"
    @mouseleave="showButton = false"
  >
    <div class="k-item-card__indicator"></div>
    <div class="k-item-card__container">
      <div class="k-item-card__city">
        <i class="fas fa-map-marker-alt marker"></i> {{ camera.city }}
      </div>
      <div class="k-item-card__id">#{{ camera.id }}</div>
      <div class="k-item-card__title" :title="camera.name">
        {{ camera.name }}
      </div>
      <div
        class="k-item-card__btn"
        @click.prevent.stop.capture="showDetails"
        v-if="showButton"
      >
        Подробнее
      </div>
      <div class="empty">-</div>
      <div
        class="k-item-card__comment"
        :title="camera.comment"
        :class="{ btn: showButton }"
        v-if="camera.comment"
      >
        {{ camera.comment }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, PropType, ref } from "vue";
import { Camera } from "@/types";
import Color from "color";
import * as random from "random-seed";

export default defineComponent({
  name: "KItemCard",
  props: {
    camera: {
      type: Object as PropType<Camera>,
      required: true,
    },
    active: {
      type: Boolean,
      required: true,
    },
  },
  emits: ["details"],
  setup(props, { emit }) {
    const color = computed(() => {
      const r = random.create(props.camera.address);

      return Color(
        `hsla(${r.range(40) + 36 + props.camera.id}, 77%, 70%, 1)`
      ).hex();
    });

    const showButton = ref(false);

    const showDetails = () => {
      emit("details", props.camera);
    };

    return {
      color,
      showButton,
      showDetails,
    };
  },
});
</script>

<style scoped lang="scss">
.k-item-card {
  width: calc(100% - 44px);
  height: 130px;
  border: 1px solid rgba(#000, 0.1);
  box-shadow: 0 2px 10px 0 rgba(#000, 0.1);
  margin: 15px 7px;
  text-align: left;
  background: #fff;
  transition: 250ms;
  overflow: hidden;
  border-radius: 14px;
  cursor: pointer;
  display: flex;
  justify-content: space-around;
  flex-direction: row;

  &.active {
    background: rgba(#269ef1, 0.15);
    border: 1px solid rgba(#269ef1, 0.55);
    box-shadow: 0 1px 5px 0 rgba(#000, 0.1);
  }

  &__indicator {
    border-radius: 14px;
    width: 7px;
    height: 100%;
    padding: 0;
    margin: 0;
    background: var(--k-base-color);
  }

  &__container {
    width: calc(100% - 37px);
    height: calc(100% - 30px);
    margin: 10px;
    padding: 5px;
    display: flex;
    position: relative;
    flex-wrap: wrap;
    justify-content: space-between;
    flex-direction: row-reverse;
  }

  &__id {
    font-weight: lighter;
    color: #969696;
    margin-right: 25px;
    height: 25px;
    line-height: 25px;
  }

  &__city {
    font-weight: normal;
    width: calc(200px);
    color: #474747;
    height: 25px;
    line-height: 25px;
    text-align: right;
  }

  &__title {
    font-weight: 500;
    font-size: 1.3em;
    color: #000;
    width: 100%;
    margin: 15px 0;
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  &__comment {
    color: #4a4a4a;
    background: #ededed;
    border: 1px solid #b8b8b8;
    padding: 3px 10px;
    border-radius: 7px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: calc(100% - 30px);

    &.btn {
      max-width: calc(100% - 150px);
    }
  }

  &__btn {
    background: var(--k-base-color);
    padding: 3px 10px;
    border-radius: 6px;
    color: #fff;
    position: absolute;
    right: 7px;
    bottom: -2px;

    &:hover {
      box-shadow: 0 1px 10px 0 inset rgba(#000, 0.05);
    }

    &:active {
      box-shadow: 0 1px 10px 0 inset rgba(#000, 0.15);
    }
  }
}

.marker {
  color: #ff2f00;
}

.empty {
  color: transparent;
  user-select: none;
  height: 30px;
  width: 1px;
}
</style>

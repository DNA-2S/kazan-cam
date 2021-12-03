<template>
  <div
    class="k-logs"
    :class="{ hover, collapse }"
    @mouseenter="hover = true"
    @mouseleave="hover = false"
  >
    <div class="k-logs__header" @click="collapse = !collapse">
      <div class="k-logs__header-icon" :class="{ rotate: collapse }">
        <i class="fas fa-chevron-down"></i>
      </div>
      <div class="k-logs__header-title">Журнал событий</div>
    </div>
    <div class="k-logs__container" :class="{ collapse }">
      <div class="k-logs__line" :key="line.message" v-for="line in logs">
        <span class="k-logs__line-timestamp">
          [{{ formattedTimestamp(line.timestamp) }}]
        </span>
        <span
          @click="$router.push({ path: '/', query: { camId: line.cam.id } })"
          class="k-logs__line-cam"
          >{{ `(#${line.cam.id}) ${line.cam.name}` }}</span
        >
        <span class="k-logs__line-message">{{ line.message }}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref } from "vue";
import { LogObject } from "@/types";
import moment from "moment";

export default defineComponent({
  name: "KLogs",
  emit: ["details"],
  props: {
    logs: {
      type: Object as PropType<LogObject[]>,
      required: true,
    },
  },
  setup() {
    const hover = ref(false);
    const collapse = ref(false);

    const formattedTimestamp = (timestamp: number): string => {
      return moment(timestamp).format("DD.MM.YYYY HH:mm:ss");
    };

    return {
      formattedTimestamp,
      hover,
      collapse,
    };
  },
});
</script>

<style lang="scss" scoped>
.k-logs {
  height: 330px;
  width: 580px;
  background: rgba(#000, 0.6);
  border-radius: 8px;
  overflow-y: auto;
  transition: 400ms;
  opacity: 0.3;

  &.hover {
    opacity: 1;
  }

  &.collapse {
    padding: 0;
    margin: 0;
    height: 30px;
    overflow: hidden;
  }

  &__header {
    height: 30px;
    width: calc(100% - 60px);
    background: rgba(#000, 0.3);
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 30px;
    gap: 1rem;
    cursor: pointer;
    position: absolute;
    top: 0;
    left: 0;

    &-icon {
      transition: 250ms;

      &.rotate {
        transform: rotate(180deg);
      }
    }

    &-title {
      font-weight: bolder;
    }
  }

  &__container {
    margin-top: 30px;
    padding: 10px;
    width: calc(100% - 20px);
    height: auto;
    transition: 250ms;

    &.collapse {
      padding: 0;
      margin: 0;
      height: 0;
      overflow: hidden;
    }
  }

  &__line {
    color: #fff;
    text-align: left;
    border-bottom: 1px solid #cdcdcd;
    padding-bottom: 3px;
    margin-bottom: 3px;

    &-timestamp {
      margin-right: 5px;
    }

    &-cam {
      font-weight: bolder;
      cursor: pointer;
      margin-right: 7px;
    }
  }

  &::-webkit-scrollbar-thumb {
    background: rgba(#fff, 0.3);
    border-radius: 25px;
  }

  &::-webkit-scrollbar-thumb:hover {
    background: rgba(#fff, 0.3);
  }

  &::-webkit-scrollbar-thumb:active {
    background: rgba(#fff, 0.5);
  }
}
</style>

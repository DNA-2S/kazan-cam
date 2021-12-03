<template>
  <svg style="display: none">
    <symbol :id="`sym${id}`">
      <g>
        <path
          d="m25.605 4.3945c5.8594 5.8555 5.8594 15.355 0 21.211-5.8555 5.8594-15.355 5.8594-21.211 0-5.8594-5.8555-5.8594-15.355 0-21.211 5.8555-5.8594 15.355-5.8594 21.211 0z"
          :fill="color"
        />
        <path
          d="m7.9414 10.555v13.77c0 0.18359 0.24609 0.33594 0.54688 0.33594h13.023c0.30078 0 0.54688-0.14844 0.54688-0.33594v-13.77zm4.0039 12.141c0 0.30078-0.24609 0.54688-0.54687 0.54688h-0.66797c-0.30469 0-0.55078-0.24609-0.54688-0.54688v-10.176c0-0.30078 0.24219-0.54688 0.54688-0.54688h0.66797c0.30078 0 0.54687 0.24609 0.54687 0.54688zm3.9375 0c0 0.30078-0.24609 0.54688-0.54687 0.54688h-0.67188c-0.30078 0-0.54687-0.24609-0.54687-0.54688v-10.176c0-0.30078 0.24609-0.54688 0.54687-0.54688h0.67188c0.30078 0 0.54687 0.24609 0.54687 0.54688zm3.9375 0c0 0.30078-0.24609 0.54688-0.54687 0.54688h-0.67188c-0.30078 0-0.54687-0.24609-0.54687-0.54688v-10.176c0-0.30078 0.24609-0.54688 0.54687-0.54688h0.66797c0.30469 0 0.54688 0.24609 0.54688 0.54688z"
          fill="#fff"
        />
        <path
          d="m21.512 7.5977h-3.457v-1.3008c0-0.52734-0.42969-0.95703-0.95703-0.95703h-4.1953c-0.52734 0-0.95703 0.42969-0.95703 0.95703v1.3008h-3.457c-0.30078 0-0.54688 0.24219-0.54688 0.54688v1.2852h14.117v-1.2852c0-0.30469-0.24609-0.54688-0.54688-0.54688zm-8.75-1.3008c0-0.078125 0.0625-0.14062 0.14062-0.14062h4.1953c0.078125 0 0.14062 0.0625 0.14062 0.14062v1.3008h-4.4766z"
          fill="#fff"
        />
      </g>
      <text
        x="15 "
        y="46"
        font-size="18px"
        fill="#000"
        font-family="Arial"
        text-anchor="middle"
      >
        {{ `#${id}` }}
      </text>
      <text
        x="15"
        y="45"
        font-size="18px"
        :fill="color"
        font-family="Arial"
        text-anchor="middle"
      >
        {{ `#${id}` }}
      </text>
    </symbol>
  </svg>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import Color from "color";

export default defineComponent({
  name: "KGarbageIcon",
  props: {
    id: {
      type: Number,
      required: true,
    },
    minColor: {
      type: String,
      default: "#78BC2A",
    },
    maxColor: {
      type: String,
      default: "#f94100",
    },
    value: {
      type: Number,
      default: 0,
    },
  },
  setup(props) {
    const color = computed(() => {
      return Color(props.minColor)
        .mix(Color(props.maxColor), props.value)
        .hex();
    });

    return {
      color,
    };
  },
});
</script>

<style lang="scss" scoped></style>

<template>
  <div class="k-app">
    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from "vue";

export default defineComponent({
  name: "App",
  setup() {
    onMounted(() => {
      fetch("/api/camera")
        .then((res) => res.json())
        .then((res) => console.log(res));
    });
  },
});
</script>

<style lang="scss">
html,
body,
#app,
.k-app {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}

#app {
  font-family: Gilroy, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<template>
  <div class="k-camera-info">
    <div class="k-camera-info__info">
      <div class="k-camera-info__id">#{{ cam.id }}</div>
      <div class="k-camera-info__city">
        <i class="fas fa-map-marker-alt marker"></i> {{ cam.city }}
      </div>
      <div class="k-camera-info__title" :title="cam.name">
        {{ cam.name }}
      </div>
    </div>
    <div class="k-camera-info__img-wrapper">
      <img :src="getImgById(cam.id)" class="k-camera-info__img" alt="Cam" />
    </div>
    <div class="k-camera-info__container-wrapper">
      <div class="k-camera-info__container">
        <h3>Информация по мусоркам</h3>
        <el-table
          :data="containersData"
          v-if="containersData.length !== 0"
          style="width: 380px"
        >
          <el-table-column prop="name" label="Контейнер" width="180" />
          <el-table-column prop="status" label="Статус" width="180" />
        </el-table>
        <div class="empty" v-else>Данные отсутствуют</div>
        <h3>Информация по авто без номеров</h3>
        <el-table
          :data="carsData"
          v-if="carsData.length !== 0"
          style="width: 380px"
        >
          <el-table-column prop="name" label="Свойство" width="180" />
          <el-table-column prop="status" label="Значение" width="180" />
        </el-table>
        <div class="empty" v-else>Данные отсутствуют</div>
      </div>
    </div>
    <div class="k-camera-info__actions">
      <el-button @click="$emit('back')" size="large">Назад</el-button>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, PropType } from "vue";
import { Camera } from "@/types";

interface ContainerData {
  name: string;
  status: string;
}

export default defineComponent({
  name: "KCameraInfo",
  props: {
    cam: {
      type: Object as PropType<Camera>,
    },
  },
  emits: ["back"],
  setup(props) {
    const getImgById = (id: number) => {
      return require(`../assets/cams/${id}.jpg`);
    };

    const containersData = computed<ContainerData[]>(() => {
      let containers = [] as ContainerData[];
      let localData = props.cam?.containers || [];
      for (let i = 0; i < localData.length; i++) {
        containers.push({
          name: `Контейнер №${i + 1}`,
          status: localData[i] ? "Заполнен" : "Пуст",
        });
      }

      return containers;
    });

    const carsData = computed<ContainerData[]>(() => {
      let containers = [] as ContainerData[];
      containers.push({
        name: `Кол-во машин без номеров`,
        status: Math.floor((props.cam?.value || 1) * 10) + "",
      });

      return containers;
    });

    return {
      getImgById,
      containersData,
      carsData,
    };
  },
});
</script>

<style lang="scss" scoped>
.k-camera-info {
  width: calc(100% - 30px);
  height: calc(100% - 110px);
  position: relative;
  display: grid;
  grid-template-areas:
    "info"
    "img"
    "container"
    "actions";
  grid-template-columns: 1fr;
  grid-template-rows: 100px 1fr 1fr 80px;

  &__container-wrapper {
    grid-area: container;
    height: 100%;
    overflow-y: auto;
  }

  &__container {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
  }

  &__info {
    grid-area: info;
    width: calc(100% - 37px);
    height: calc(100% - 30px);
    margin: 10px;
    padding: 5px;
    display: flex;
    position: relative;
    flex-wrap: wrap;
    justify-content: space-between;
    flex-direction: row;
    font-size: 1.3em;
  }

  &__id {
    font-weight: normal;
    color: #969696;
    margin-right: 25px;
    height: 25px;
    width: 50px;
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

  &__img-wrapper {
    grid-area: img;
    overflow: hidden;
    width: 100%;
    height: 100%;
    position: relative;
  }

  &__img {
    height: 100%;
  }

  &__actions {
    grid-area: actions;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
  }
}

.marker {
  color: #ff2f00;
}
</style>

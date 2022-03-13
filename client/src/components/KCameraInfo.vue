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
      <img
        :src="`data:image/jpg;base64,${image}`"
        class="k-camera-info__img"
        alt="Cam"
        v-if="image !== ''"
      />
      <div v-else>Loading...</div>
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
          <el-table-column prop="property" label="Свойство" width="180" />
          <el-table-column prop="value" label="Значение" width="180" />
        </el-table>
        <div class="empty" v-else>Данные отсутствуют</div>
      </div>
    </div>
    <div class="k-camera-info__actions">
      <el-button type="warning" @click="dialogVisible = true" size="large">
        Отправить данные
      </el-button>
      <el-button @click="$emit('back')" size="large">Назад</el-button>
    </div>
  </div>

  <el-dialog
    v-model="dialogVisible"
    title="Отправка данных"
    width="30%"
    center
    :close-on-click-modal="true"
    :close-on-press-escape="true"
    :show-close="true"
  >
    <div class="k-send-data">
      <div class="k-send-data__buttons">
        <k-send-data-card>
          <img
            src="@/assets/garbage-truck.png"
            alt="icon"
            style="width: 60px; height: 60px"
          />
        </k-send-data-card>
        <k-send-data-card>
          <img
            src="@/assets/tow-truck.png"
            alt="icon"
            style="width: 60px; height: 60px"
          />
        </k-send-data-card>
      </div>
    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="send" type="warning"> Отправить </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script lang="ts">
import {
  computed,
  defineComponent,
  inject,
  onMounted,
  PropType,
  ref,
  watch,
} from "vue";
import { Camera, LogObject } from "@/types";
import KSendDataCard from "@/components/KSendDataCard.vue";

interface ContainerData {
  name: string;
  status: string;
}

interface CarData {
  property: string;
  value: string;
}

export default defineComponent({
  name: "KCameraInfo",
  components: { KSendDataCard },
  props: {
    cam: {
      type: Object as PropType<Camera>,
      required: true,
    },
  },
  emits: ["back"],
  setup(props) {
    const dialogVisible = ref(false);
    const image = ref("");

    watch(
      () => props.cam,
      (value: Camera) => {
        image.value = "";
        fetch(`/api/camera/${value.id}/image`)
          .then((res) => res.json())
          .then((res: { image: string }) => {
            image.value = res.image;
          });
      }
    );

    onMounted(() => {
      fetch(`/api/camera/${props.cam.id}/image`)
        .then((res) => res.json())
        .then((res: { image: string }) => {
          image.value = res.image;
        });
    });

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

    const carsData = computed<CarData[]>(() => {
      let containers = [] as CarData[];
      if (!props.cam["parking-area"]) {
        return [];
      }

      containers.push({
        property: `Кол-во машин без номеров`,
        value: Math.floor((props.cam?.value || 1) * 10) + "",
      });

      return containers;
    });

    const log = inject<(obj: LogObject) => void>("log");

    const send = () => {
      dialogVisible.value = false;
      if (log && props.cam) {
        log({
          timestamp: Date.now(),
          message: "Данные отправлены",
          cam: props.cam,
        });
      }
    };

    return {
      containersData,
      carsData,
      dialogVisible,
      send,
      image,
    };
  },
});
</script>

<style lang="scss" scoped>
.k-send-data {
  &__buttons {
    display: flex;
    justify-content: center;
    align-items: center;
  }
}

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

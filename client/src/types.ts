export interface Camera {
  address: string;
  id: number;
  dumpster?: boolean;
  ["parking-area"]?: boolean;
}

export enum ViewType {
  DUMPSTER,
  "PARKING-AREA",
  CAMS,
}

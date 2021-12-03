export interface Camera {
  address: string;
  id: number;
  dumpster?: boolean;
  ["parking-area"]?: boolean;
  comment?: string;
  city?: string;
  name?: string;
}

export enum ViewType {
  DUMPSTER,
  "PARKING-AREA",
  CAMS,
}

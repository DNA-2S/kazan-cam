export interface Camera {
  address: string;
  id: number;
  dumpster?: boolean;
  ["parking-area"]?: boolean;
  comment?: string;
  city?: string;
  name?: string;
  value?: number;
}

export enum ViewType {
  DUMPSTER,
  "PARKING-AREA",
  CAMS,
}

export interface LogObject {
  message: string;
  cam: Camera;
  timestamp: number;
}

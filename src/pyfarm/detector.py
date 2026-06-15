import numpy as np
from pathlib import Path
from typing import List, Optional, Union
from pytest import Config

from pyfarm.weight import ModelDownloader, downloader
from ultralytics import YOLO

_model: Optional[YOLO] = None

class YOLODetector:
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self._model: Optional[YOLO] = None

    @property
    def model(self) -> YOLO:
        global _model
        if _model is None:
            downloader = ModelDownloader(self.config)
            model_path = downloader.download()
            _model = YOLO(model_path)
        self._model = _model
        return self._model
    
    def predict(
            self,
            source: Union[str, Path, np.ndarray, List],
            conf_threshold: Optional[float] = None,
            iou_threshold: Optional[float] = None,
            img_size: Optional[int] = None,
            **kwargs
    ):
        
        conf = conf_threshold if conf_threshold is not None else self.config.conf_threshold
        iou = iou_threshold if iou_threshold is not None else self.config.iou_threshold
        imgsz = img_size if img_size is not None else self.config.img_size

        return self.model.predict(
            source=source,
            conf=conf,
            iou=iou,
            imgsz=imgsz,
            **kwargs
        )

def load_detector(
        conf_threshold: Optional[float] = None,
        iou_threshold: Optional[float] = None,
        img_size: Optional[int] = None,
        **kwargs
) -> YOLODetector:
    
    config = Config.create(
        conf_threshold=conf_threshold,
        iou_threshold=iou_threshold,
        img_size=img_size,
        **kwargs
    )

    return YOLODetector(config)

def get_model():
    detector = load_detector()
    return detector.model
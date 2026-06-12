from pyfarm.weight import downloader
from ultralytics import YOLO

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = downloader.download()
        _model = YOLO(model_path)
    return _model
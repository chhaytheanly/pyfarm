from .weight import downloader
from ultralytics import YOLO

model_path = downloader.download()
model = YOLO(model_path)
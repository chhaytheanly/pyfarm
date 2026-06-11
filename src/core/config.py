import os
from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class Config:
    github_repo: str = os.getenv("GITHUB_REPO", "https://github.com/chhaytheanly/pyfarm")
    tag: str = os.getenv("TAG", "v0.0.1")
    model_filename: str = os.getenv("MODEL_FILENAME", "fine_tuning_v0.pt") 

    cache_dir: Path = field(init=False)

    # Default parameters for model inference, can be overridden by environment variables
    conf_threshold: float = float(os.getenv("CONF_THRESHOLD", "0.45"))
    iou_threshold: float = float(os.getenv("IOU_THRESHOLD", "0.45"))
    img_size: int = int(os.getenv("IMG_SIZE", "640"))
    use_onnx: bool = os.getenv("USE_ONNX", "True").lower() in ("true", "1", "t")
    tile_overlap_ratio: float = float(os.getenv("TILE_OVERLAP_RATIO", "0.35"))
    tile_min_overlap_px: int = int(os.getenv("TILE_MIN_OVERLAP_PX", "128"))
    tile_use_reflect_padding: bool = os.getenv("TILE_USE_REFLECT_PADDING", "True").lower() in ("true", "1", "t")
    tile_enable_tta: bool = os.getenv("TILE_ENABLE_TTA", "True").lower() in ("true", "1", "t")
    tile_soft_nms: bool = os.getenv("TILE_SOFT_NMS", "True").lower() in ("true", "1", "t")
    tile_soft_nms_sigma: float = float(os.getenv("TILE_SOFT_NMS_SIGMA", "0.5"))

    def __post_init__(self):
        cache_dir_env = os.getenv("CACHE_DIR")
        if cache_dir_env:
            self.cache_dir = Path(cache_dir_env)
        else:
            self.cache_dir = Path.home() / ".cache" / "pyfarm"
        
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    @property
    def default_model_params(self) -> dict:
        return {
            "conf": self.conf_threshold,
            "iou": self.iou_threshold,
            "imgsz": self.img_size,
        }

config = Config()
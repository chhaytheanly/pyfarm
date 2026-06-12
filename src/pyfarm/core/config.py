import os
from pathlib import Path
from dataclasses import dataclass, field


def _env_str(key: str, default: str) -> str:
    return os.getenv(key, default)


def _env_float(key: str, default: str) -> float:
    return float(os.getenv(key, default))


def _env_int(key: str, default: str) -> int:
    return int(os.getenv(key, default))


def _env_bool(key: str, default: str) -> bool:
    return os.getenv(key, default).lower() in ("true", "1", "t")


@dataclass
class Config:
    github_repo: str = field(default_factory=lambda: _env_str("GITHUB_REPO", "https://github.com/chhaytheanly/pyfarm"))
    tag: str = field(default_factory=lambda: _env_str("TAG", "v0.0.1"))
    model_filename: str = field(default_factory=lambda: _env_str("MODEL_FILENAME", "fine_tuning_v0.pt"))

    cache_dir: Path = field(init=False)

    conf_threshold: float = field(default_factory=lambda: _env_float("CONF_THRESHOLD", "0.45"))
    iou_threshold: float = field(default_factory=lambda: _env_float("IOU_THRESHOLD", "0.45"))
    img_size: int = field(default_factory=lambda: _env_int("IMG_SIZE", "640"))
    use_onnx: bool = field(default_factory=lambda: _env_bool("USE_ONNX", "True"))
    tile_overlap_ratio: float = field(default_factory=lambda: _env_float("TILE_OVERLAP_RATIO", "0.35"))
    tile_min_overlap_px: int = field(default_factory=lambda: _env_int("TILE_MIN_OVERLAP_PX", "128"))
    tile_use_reflect_padding: bool = field(default_factory=lambda: _env_bool("TILE_USE_REFLECT_PADDING", "True"))
    tile_enable_tta: bool = field(default_factory=lambda: _env_bool("TILE_ENABLE_TTA", "True"))
    tile_soft_nms: bool = field(default_factory=lambda: _env_bool("TILE_SOFT_NMS", "True"))
    tile_soft_nms_sigma: float = field(default_factory=lambda: _env_float("TILE_SOFT_NMS_SIGMA", "0.5"))

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
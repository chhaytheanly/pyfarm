import os
from pathlib import Path
from pyfarm.core.config import Config


def test_config_defaults():
    cfg = Config()
    assert cfg.conf_threshold == 0.45
    assert cfg.iou_threshold == 0.45
    assert cfg.img_size == 640
    assert cfg.use_onnx is True
    assert cfg.tile_overlap_ratio == 0.35


def test_config_env_overrides(monkeypatch):
    monkeypatch.setenv("CONF_THRESHOLD", "0.5")
    monkeypatch.setenv("IMG_SIZE", "1280")
    monkeypatch.setenv("CACHE_DIR", "/tmp/pyfarm_test")
    cfg = Config()
    assert cfg.conf_threshold == 0.5
    assert cfg.img_size == 1280
    assert cfg.cache_dir == Path("/tmp/pyfarm_test")


def test_default_model_params():
    cfg = Config()
    params = cfg.default_model_params
    assert params["conf"] == 0.45
    assert params["iou"] == 0.45
    assert params["imgsz"] == 640

# PyFarm

A YOLO-based package for detecting and counting industrial objects, powered by [Ultralytics](https://github.com/ultralytics/ultralytics).

## Installation

```bash
pip install pyfarm-detection
```

### From source

```bash
git clone https://github.com/chhaytheanly/pyfarm.git
cd pyfarm
pip install -e ".[test]"
```

## Usage

### CLI

```bash
pyfarm
```

### Python API

```python
from pyfarm.detector import get_model

model = get_model()
results = model("image.jpg")
results[0].show()
```

The model is downloaded from GitHub releases on first use and cached locally.

## Configuration

All settings are configured via environment variables:

| Variable | Default | Description |
|---|---|---|
| `GITHUB_REPO` | `https://github.com/chhaytheanly/pyfarm` | Repository hosting model weights |
| `TAG` | `v0.0.1` | Release tag for model weights |
| `MODEL_FILENAME` | `640_yolo.pt` | Model weights filename |
| `CACHE_DIR` | `~/.cache/pyfarm` | Model download cache directory |
| `CONF_THRESHOLD` | `0.45` | Detection confidence threshold |
| `IOU_THRESHOLD` | `0.45` | NMS IoU threshold |
| `IMG_SIZE` | `640` | Input image size |
| `USE_ONNX` | `True` | Enable ONNX export |
| `TILE_OVERLAP_RATIO` | `0.35` | Tiling overlap ratio |
| `TILE_MIN_OVERLAP_PX` | `128` | Minimum overlap in pixels |
| `TILE_USE_REFLECT_PADDING` | `True` | Use reflect padding for tiles |
| `TILE_ENABLE_TTA` | `True` | Enable test-time augmentation |
| `TILE_SOFT_NMS` | `True` | Enable soft NMS for tiles |
| `TILE_SOFT_NMS_SIGMA` | `0.5` | Soft NMS sigma parameter |

### Example

```bash
export TAG=v0.0.1
export CONF_THRESHOLD=0.5
pyfarm
```

> **Note:** The `.env` file is not automatically loaded. Set variables in your shell or use `export` / `$env:` (PowerShell).

## Private repositories

If your model weights are hosted in a private GitHub repository, set a `GITHUB_TOKEN` environment variable with a [Personal Access Token](https://github.com/settings/tokens) that has `contents: read` access.

```bash
export GITHUB_TOKEN=ghp_...
```

## Development

```bash
pip install -e ".[test]"
pytest test/ -v
```

## Project structure

```
src/
└── pyfarm/
    ├── __init__.py
    ├── __main__.py       # CLI entry point
    ├── detector.py        # Model loading (get_model)
    ├── weight.py          # Model downloader from GitHub releases
    ├── core/
    │   ├── __init__.py
    │   └── config.py      # Configuration dataclass
    └── utils/
        └── __init__.py
```

## License

MIT

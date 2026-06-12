# PyFarm

A YOLO-based package for detecting and counting industrial objects.

## Installation

```bash
pip install pyfarm
```

## Usage

```bash
pyfarm
```

Or via Python:

```python
from pyfarm.detector import get_model

model = get_model()
results = model("image.jpg")
```

## Configuration

Configuration is handled via environment variables or the `Config` dataclass:

| Variable | Default | Description |
|----------|---------|-------------|
| `CONF_THRESHOLD` | 0.45 | Detection confidence threshold |
| `IOU_THRESHOLD` | 0.45 | NMS IoU threshold |
| `IMG_SIZE` | 640 | Input image size |
| `CACHE_DIR` | `~/.cache/pyfarm` | Model download cache directory |
| `GITHUB_REPO` | `https://github.com/chhaytheanly/pyfarm` | Model repository |
| `TAG` | v0.0.1 | Release tag for model weights |
| `MODEL_FILENAME` | fine_tuning_v0.pt | Model weights filename |

## License

MIT

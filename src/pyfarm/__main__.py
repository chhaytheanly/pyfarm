from pyfarm.detector import load_detector


def main():
    print("PyFarm v0.1.0 - Initializing detector...")

    detector = load_detector()

    print(f"Model loaded successfully!")
    print(f"   Model: {detector.model.model_name}")
    print(f"   Config: conf={detector.config.conf_threshold}, "
          f"iou={detector.config.iou_threshold}, "
          f"imgsz={detector.config.img_size}")


if __name__ == "__main__":
    main()
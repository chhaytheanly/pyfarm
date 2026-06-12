from pyfarm.detector import get_model

def main():
    model = get_model()
    print(f"PyFarm v0.1.0 - Model loaded: {model}")

if __name__ == "__main__":
    main()

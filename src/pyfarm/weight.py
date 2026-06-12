import os
import urllib.request
import urllib.error
from pathlib import Path
from pyfarm.core.config import config

class ModelDownloader:
    def __init__(self):
        self.model_path = config.cache_dir / config.model_filename
        self.url = f"{config.github_repo}/releases/download/{config.tag}/{config.model_filename}"

    def download(self) -> str:

        if self.model_path.exists():
            print(f"Model already exists at {self.model_path}. Skipping download.")
            return str(self.model_path)
        
        print(f"Downloading model from {self.url} to {self.model_path}...")
        
        request = urllib.request.Request(self.url)
        github_token = os.environ.get("GITHUB_TOKEN")
        if github_token:
            request.add_header("Authorization", f"token {github_token}")

        try:
            with urllib.request.urlopen(request) as response, open(self.model_path, 'wb') as out_file:
                while chunk := response.read(8192):
                    out_file.write(chunk)
                    
            print(f"Model downloaded successfully to {self.model_path}.")
            return str(self.model_path)
        
        # 4. Proper Error Handling
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise RuntimeError(
                    f"Model not found at {self.url}.\n"
                    f"Please verify your config: tag='{config.tag}', file='{config.model_filename}'"
                )
            elif e.code == 403:
                raise RuntimeError(
                    "Access denied (403 Forbidden).\n"
                    "If this is a private repository, you must set the GITHUB_TOKEN environment variable."
                )
            else:
                raise RuntimeError(f"Failed to download model weights: {e}")
                
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred during download: {e}")

downloader = ModelDownloader()
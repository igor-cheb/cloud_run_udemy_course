from pathlib import Path
from decouple import Config, RepositoryEnv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
CONFIG = Config(RepositoryEnv(ENV_PATH))
# def get_config():
#     return Config(RepositoryEnv(ENV_PATH))
# config = get_config()
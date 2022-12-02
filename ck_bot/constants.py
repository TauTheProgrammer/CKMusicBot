from .types.env import EnvDict
from .utils import parse_env_file

# Env
CONFIG: EnvDict = parse_env_file()

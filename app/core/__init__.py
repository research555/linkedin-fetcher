import os
from dotmap import DotMap
import yaml
from .config import settings

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)

with open(os.path.join(current_dir, 'params.yml'), 'r') as f:
    data = yaml.safe_load(f)

def prepend_base_dir(item):
    if isinstance(item, str):
        return os.path.join(base_dir, item.lstrip("./"))
    elif isinstance(item, dict):
        return {k: prepend_base_dir(v) for k, v in item.items()}
    else:
        return item

#data['paths'] = prepend_base_dir(data['paths'])

config = DotMap(data)
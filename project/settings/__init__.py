import os
from base import *

env_settings = os.environ.get('ENV_SETTINGS', None)

if env_settings != None:
    __import__(env_settings)

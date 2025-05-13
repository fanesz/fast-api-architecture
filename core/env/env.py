import os
import sys
from dotenv import load_dotenv
from .env_check import validate_environment
from package.index import Logger

load_dotenv()

class _Env:
    _instance = None
    _initialized = False
    isDevelopment = True
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(_Env, cls).__new__(cls)
            cls._instance._env = {}
                        
            # to assign default value to env variable
            cls._instance._defaults = {
                'environment': 'development',
                'BE_HOST': '0.0.0.0',
                'BE_PORT': 5000,
                'API_KEY': 'default_api_key',
            }
            
        return cls._instance
        
    def initialize(self):
        if not self._initialized:
            self._env = {}
            self._env['environment'] = os.environ.get('environment') or self._defaults.get('environment')
            self._env['BE_HOST'] = os.environ.get('BE_HOST') or self._defaults.get('BE_HOST')
            self._env['BE_PORT'] = int(os.environ.get('BE_PORT')) or self._defaults.get('BE_PORT')
            self._env['API_KEY'] = os.environ.get('API_KEY') or self._defaults.get('API_KEY')
            self._validate_env()
            self.__class__._initialized = True
            Logger.info("Env Initialized...")
            
            self.isDevelopment = self._env['environment'] == "development"
        return self

    def _validate_env(self):
        validate_environment(self._env)
        Logger.info("All envs are valid...")

    def get(self, key, default=None):
        if not self._initialized:
            Logger.error("Env class not initialized...")
            sys.exit(1)
            
        if key not in self._env:
            return default if default is not None else self._defaults.get(key)
        return self._env.get(key)
    
Env = _Env()
from schema import Schema, Optional, Use, SchemaError
from package.index import Logger

EnvSchema = Schema({
    'environment': str,
    'BE_HOST': str,
    'BE_PORT': int,
    'API_KEY': str,
})

def validate_environment(env_data):
    try:
        EnvSchema.validate(env_data)
        return True
    except SchemaError as e:
        Logger.error(f"Environment validation failed: {e}")
        return False
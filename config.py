"""
provides a config factory to generate a environment-specific config object
based on environmental variables provided in a .env file or already laoded
"""
import os
from dotenv import load_dotenv

# loads the contents of .env file at runtime
# if environmental variables have been set already then load_dotenv will not
# overwrite them
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    
    def __init__(self, env):

        self.environment = env

        # db connection configuration, private attributes accessed
        # via db_conn_str
        self._db_name = os.getenv('DB_NAME')
        self._db_host = os.getenv('DB_HOST')
        self._db_port = os.getenv('DB_PORT') or 5432  # how we can set defaults
        self._db_user = os.getenv('DB_USER')
        self._db_password = os.getenv('DB_PASSWORD')

        # some other generic config stuff that should be inherited by all
        # configs
        self.delete_that_thing = False

    @property
    def db_conn_str(self):

        return (f'postgresql+psycopg2://{self._db_user}:{self._db_password}@'
            f'{self._db_host}:{self._db_port}/{self._db_name}')

    def __repr__(self):

        return f'config: {self.environment}'


class TestingConfig(Config):

    # environment-specific config options
    testing = True
    debug = True


class ProductionConfig(Config):

    testing = False
    debug = False


class DevelopmentConfig(Config):

    testing = False
    debug = True


class ConfigFactory:

    def factory():

        env = os.getenv('ENV') or 'development'

        if env == 'testing':
            return TestingConfig(env)

        elif env == 'production':
            return ProductionConfig(env)

        elif env == 'development':
            return DevelopmentConfig(env)

        else:
            raise RuntimeError('unrecognised environment')


if __name__ == '__main__':

    c = ConfigFactory.factory()

    print(c)

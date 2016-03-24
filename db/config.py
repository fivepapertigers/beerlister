DATABASES = {
  'default': {
    'migrations_dir': './db/migrations/',
    'engine': 'postgres',
    'dsn': 'host=127.0.0.1 dbname=brew user=postgres',
  }
}

LOG_FILE = '/tmp/mtest1.log'
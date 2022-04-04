BINARY_DOCKER_COMPOSE_VERSION = '1.29.2'
DEFAULT_DIRECTORY_BASE = '/opt/'
DEFAULT_DIRECTORY_INSTALLATION = '/opt/mayan-edms/'
DEFAULT_DIRECTORY_MEDIA_ROOT = '/opt/mayan-edms/media/'
DEFAULT_DATABASE_NAME = 'mayan'
DEFAULT_DATABASE_PASSWORD = 'mayanuserpass'
DEFAULT_DATABASE_USER = 'mayan'
DEFAULT_OS_DISTRIBUTION = '"Debian 11"'
DEFAULT_OS_GROUP = 'mayan'
DEFAULT_OS_USERNAME = 'mayan'
DEFAULT_RABBITMQ_PASSWORD = 'mayanrabbitmqpassword'
DEFAULT_RABBITMQ_USER = 'mayan'
DEFAULT_RABBITMQ_VHOST = 'mayan'
DEFAULT_REDIS_PASSWORD = 'mayanredispassword'
DEFAULT_SECRET_KEY = 'secret-key-missing!'
DEFAULT_USER_SETTINGS_FOLDER = 'user_settings/'
DEFAULT_USER_SETTINGS_MODULE = 'user_settings'
DOCKER_HOST_REGISTRY_NAME = 'docker-registry.local'
DOCKER_HOST_REGISTRY_PORT = 5000
DOCKER_IMAGE_MAYAN_NAME = 'mayanedms/mayanedms'
DOCKER_DIND_IMAGE_VERSION = 'docker:20-dind'
DOCKER_ELASTIC_IMAGE_VERSION = 'elasticsearch:7.14.2'
DOCKER_LINUX_IMAGE_VERSION = 'debian:11.2-slim'
DOCKER_MYSQL_IMAGE_VERSION = 'mysql:8.0'
DOCKER_ORACLE_IMAGE_VERSION = 'wnameless/oracle-xe-11g-r2'
DOCKER_POSTGRES_IMAGE_VERSION = 'postgres:12.9-alpine'
DOCKER_PYTHON_IMAGE_VERSION = 'python:3.11-slim'
DOCKER_RABBITMQ_IMAGE_VERSION = 'rabbitmq:3.9-alpine'
DOCKER_REDIS_IMAGE_VERSION = 'redis:6.2-alpine'
GUNICORN_LIMIT_REQUEST_LINE = 4094
GUNICORN_MAX_REQUESTS = 500
GUNICORN_REQUESTS_JITTER = 50
GUNICORN_TIMEOUT = 120
GUNICORN_WORKER_CLASS = 'sync'
GUNICORN_WORKERS = 3
PYTHON_AMQP_VERSION = '5.0.9'
PYTHON_MYSQL_VERSION = '2.0.3'
PYTHON_ORACLE_VERSION = '8.1.0'
PYTHON_PIP_VERSION = '21.3.1'
PYTHON_PSYCOPG2_VERSION = '2.9.2'
PYTHON_PSYCOPG2_VERSION_PREVIOUS = '2.8.6'
PYTHON_PSUTIL_VERSION = '5.8.0'
PYTHON_REDIS_VERSION = '4.0.2'
SOURCE_CODE_REPOSITORY = 'https://gitlab.com/mayan-edms/mayan-edms/'
SOURCE_CODE_GIT = 'https://gitlab.com/mayan-edms/mayan-edms.git'
SOURCE_CODE_ISSUES = 'https://gitlab.com/mayan-edms/mayan-edms/issues/'
SECRET_KEY_FILENAME = 'SECRET_KEY'
SYSTEM_DIR = 'system'
SUPERVISOR_CONFIGURATION_DIRECTORY = '/etc/supervisor/conf.d/'
SUPERVISOR_CONFIGURATION_FILENAME = 'mayan-edms.conf'
MAYAN_WORKER_A_CONCURRENCY = 0
MAYAN_WORKER_A_MAX_MEMORY_PER_CHILD = 300000
MAYAN_WORKER_A_MAX_TASKS_PER_CHILD = 100
MAYAN_WORKER_B_CONCURRENCY = 0
MAYAN_WORKER_B_MAX_MEMORY_PER_CHILD = 300000
MAYAN_WORKER_B_MAX_TASKS_PER_CHILD = 100
MAYAN_WORKER_C_CONCURRENCY = 0
MAYAN_WORKER_C_MAX_MEMORY_PER_CHILD = 300000
MAYAN_WORKER_C_MAX_TASKS_PER_CHILD = 100
MAYAN_WORKER_D_CONCURRENCY = 1
MAYAN_WORKER_D_MAX_MEMORY_PER_CHILD = 300000
MAYAN_WORKER_D_MAX_TASKS_PER_CHILD = 10

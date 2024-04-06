import logging


# Фильтр для критических логов
class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname in ('ERROR', 'CRITICAL')


# Словарь настроек логгирования
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'formatter_1': {
            'format': '%(filename)s:%(lineno)d #%(levelname)-8s '
                    '[%(asctime)s] - %(name)s - %(message)s'
        },
    },

    'filters': {
        'error_filter': {
            '()': ErrorLogFilter,
        }
    },

    'handlers': {
        'all': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_1',
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': 'ERROR.txt',
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'formatter_1',
            'filters': ['error_filter']
        },
    },


    'root': {
        'level': 'DEBUG',
        'formatter': 'formatter_1',
        'handlers': ['all', 'error_file']
    }
}
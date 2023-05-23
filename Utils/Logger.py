import logging
import time

INFO = 'info'
WARNING = 'warning'
ERROR = 'error'


def GetITime():
    # 获取当前时间戳，精确到秒
    timestamp = int(time.time())
    # 将时间戳转换为本地时间
    local_time = time.localtime(timestamp)
    # 将时间格式化为字符串，精确到秒
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return time_str


def LogPrint(level, time_str, message):
    Logger = logging.getLogger(__name__)
    if level == 'info':
        Logger.setLevel(logging.INFO)
        formatter = logging.Formatter('{} [%(levelname)s]：%(message)s'.format(time_str))
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        Logger.addHandler(console_handler)

        Logger.info(message)
    elif level == 'warning':
        Logger.setLevel(logging.WARNING)
        formatter = logging.Formatter('{} [%(levelname)s]：%(message)s'.format(time_str))
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(formatter)
        Logger.addHandler(console_handler)

        Logger.warning(message)
    else:
        Logger.setLevel(logging.ERROR)
        formatter = logging.Formatter('{} [%(levelname)s]：%(message)s'.format(time_str))
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(formatter)
        Logger.addHandler(console_handler)

        file_handler = logging.FileHandler('app.log')
        file_handler.setLevel(logging.ERROR)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(formatter)

        Logger.addHandler(file_handler)
        Logger.addHandler(file_handler)
        Logger.error(message)

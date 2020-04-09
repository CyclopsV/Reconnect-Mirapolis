import logging

# Настройки логера
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
format_log = logging.Formatter(fmt='%(levelname)s:%(name)s:%(asctime)s: %(message)s', datefmt='%H:%M:%S')
handler.setFormatter(format_log)
logger.addHandler(handler)

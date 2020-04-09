import subprocess

from config import logger


def start():
    logger.info('Приложение запущено')

    proc = subprocess.Popen(['python', 'main.py'])
    while True:
        logger.info('Для завершения приложения введите z')
        inp = input('>>> ')
        if (inp == 'z') or (inp == 'Z'):
            proc.terminate()
            logger.info('Приложение завершено')
            break



start()

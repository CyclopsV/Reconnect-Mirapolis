from numpy import intc
from pyautogui import locateCenterOnScreen, click, alert
from pyscreeze import Point
from time import sleep
from winsound import PlaySound, SND_ALIAS

from config import logger


def find_button(name_tamp: str) -> bool:
    tpl: Point = locateCenterOnScreen(name_tamp, grayscale=True, confidence=0.7)
    if tpl:
        logger.warning(f'Найден {name_tamp} ({tpl})')
        x: intc = tpl[0]
        y: intc = tpl[1]
        if name_tamp == 'first_template.png':
            y = y + 30
        else:
            y = y + 22
        click(x, y)
        PlaySound('SystemAsterisk', SND_ALIAS)
        return True
    return False


def main():
    logger.info('Запуск мониторинга экрана')
    while True:
        sleep(5)
        fb = None
        fb: bool = find_button('first_template.png')
        if fb:
            fb = None
            for i in range(3):
                sleep(2)
                logger.info(f'Поиск кнопки авторизаци (Попытка #{i + 1})')
                fb: bool = find_button('second_tamlate.png')
                if fb:
                    break
            else:
                PlaySound('SystemHand', SND_ALIAS)
                logger.warning('Кнопка авторизации не найдена. Пожалуйста нажмите ее сами')
                alert('Кнопка для авторизации не найдена.')


main()

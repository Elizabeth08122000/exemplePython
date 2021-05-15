import datetime
import os
import time
import sys,traceback
from PIL import Image, ImageGrab, ImageFont, ImageDraw

FONT = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 16)


def get_current_date():
    return datetime.datetime.today()


def get_current_station():
    return os.environ.get('COMPUTERNAME')


def get_current_user():
    return os.environ.get('USERNAME')


def connect():
    return os.path.exists('C:\Screens')


def create_folder():
    folder_name_workstation = get_current_station()
    folder_name_date = get_current_date().strftime('%m-%d-%Y')
    folder_name_time = get_current_date().strftime('%H' + '.00-' + '%H' + '.59')
    path_to_folder = fr'C:\Screens\{folder_name_workstation}\{folder_name_date}\{folder_name_time}'
    if not os.path.exists(path_to_folder):
        os.makedirs(path_to_folder)


def take_screen():
        raise ValueError('Тестовая ошибка')
        workstation_name = get_current_station()
        current_date = get_current_date().strftime('%m-%d-%Y')
        while True:
            folder_current_time = get_current_date().strftime('%H' + '.00-' + '%H' + '.59')
            current_time = get_current_date().strftime('%H-%M-%S')
            screenshot = ImageGrab.grab().convert('L').resize((960, 540), Image.ANTIALIAS)
            draw = ImageDraw.Draw(screenshot)
            create_folder()
            text_on_screen = f"{get_current_date().strftime('%d/%m/%Y %H:%M')}\n{get_current_station()}, {get_current_user()} "
            draw.text((10, 470), text=text_on_screen, fill='white', font=FONT, stroke_width=2, stroke_fill='black')
            screenshot.save(fr'C:\Screens\{workstation_name}\{current_date}\{folder_current_time}\{current_time}.png', quality=85,
                            optimize=True)
            time.sleep(10)


if __name__ == "__main__":
    try:
        create_folder()
        take_screen()
    except Exception as e:
        if connect() == True:
            with open(fr'C:\Screens\CropDebug\{get_current_station()}_error.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n{get_current_user()} {datetime.datetime.now()} {e} \n{traceback.format_exc(10)}")
        else:
            with open(fr'C:\Linphone\error.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n{get_current_user()} {datetime.datetime.now()} {e} \n{traceback.format_exc(10)}")

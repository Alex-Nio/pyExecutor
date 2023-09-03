import os
from os.path import expanduser
import time
import json
import datetime
from colorama import init, Fore, Style
from tqdm import tqdm

error_duration = 1
instructions_duration = 5

def show_error():
    print(Fore.RED + "Недопустимый выбор, повторите ввод" + Style.RESET_ALL)
    time.sleep(error_duration)

def show_instructions():
    print(Fore.MAGENTA + "===================== Инструкции ===============================")
    print(Fore.BLUE + "Шаг 1. Скопируйте путь подходящей папки для анализа")
    print(Fore.BLUE + "Шаг 2. Добавьте скопированный путь в программу")
    print(Fore.BLUE + "Шаг 3. Укажите куда сгенерировать файл")
    print(Fore.BLUE + "Шаг 4. В указанную директорию будет добавлен файл в формате json")
    print(Fore.BLUE + "Шаг 5. Файл в формате json содержит всю информацию по анализу данных")
    print(Fore.MAGENTA + "================================================================")
    time.sleep(instructions_duration)

def show_main_actions():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + "======================= Действия ===============================")
    print(Fore.BLUE + "1. Указать папку для анализа")
    print(Fore.BLUE + "2. Выбрать папку в которой расположена программа")
    print(Fore.BLUE + "3. Выход")
    print(Fore.BLUE + "4. Показать инструкции")
    print(Fore.MAGENTA + "========================= ВВОД =================================")
    choice = input(Fore.GREEN + "Выберите вариант: " + Style.RESET_ALL)
    return choice

def show_upload_actions():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "================================================================")
    print(Fore.GREEN + "1. Выгрузить файл в определенную папку" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Выгрузить файл в текущую папку" + Style.RESET_ALL)
    print(Fore.GREEN + "3. Выгрузить на рабочий стол" + Style.RESET_ALL)
    print(Fore.GREEN + "4. Выход" + Style.RESET_ALL)
    print(Fore.CYAN + "================================================================")
    upload = input(Fore.GREEN + "Выберите действие: " + Style.RESET_ALL)
    return upload

def show_result(path):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "==============================================================")
    print(Fore.GREEN + "========================= ГОТОВО !!! =========================")
    print(Fore.GREEN + "==============================================================")
    print(Fore.CYAN + "Путь к сгенерированному файлу:" + " " + path)

while True:
    choice = show_main_actions()

    if choice == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        folder_path = input(Fore.GREEN + "Введите полный путь к папке: " + Style.RESET_ALL)
    elif choice == "2":
        folder_path = os.getcwd()
    elif choice == "3":
        exit()
    elif choice == "4":
        show_instructions()
        continue
    else:
        show_error()
        continue

    upload = show_upload_actions()

    if upload == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "================================================================")
        file_path = input(Fore.GREEN + "Введите куда выгрузить результат: " + Style.RESET_ALL)
        filename = "data" + datetime.datetime.now().strftime("%d_%m_%Y_%S") + ".json"
        file_path = os.path.join(file_path, filename)
    elif upload == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        filename = "data" + datetime.datetime.now().strftime("%d_%m_%Y_%S") + ".json"
        file_path = filename
        break
    elif upload == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        onedrive_path = os.path.join(os.path.expanduser("~"), "OneDrive")

        if os.path.exists(onedrive_path):
            if os.path.exists(os.path.join(onedrive_path, "Рабочий стол")):
                desktop_path = os.path.join(onedrive_path, "Рабочий стол")
            elif os.path.exists(os.path.join(onedrive_path, "Desktop")):
                desktop_path = os.path.join(onedrive_path, "Desktop")

        filename = "data" + datetime.datetime.now().strftime("%d_%m_%Y_%S") + ".json"
        file_path = os.path.join(desktop_path, filename)
    elif upload == "4":
        exit()
    else:
        print(Fore.RED + "Недопустимый выбор, повторите ввод" + Style.RESET_ALL)
        break
    break


def parse_folder(folder_path):
    result = {"folder_name": os.path.basename(folder_path), "folders": [], "files": []}

    for name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, name)

        if os.path.isdir(item_path):
            folder_item = parse_folder(item_path)
            if folder_item:
                result["folders"].append(folder_item)
        else:
            result["files"].append(name)

    return result

def parse_root_folder(folder_path, progress_bar=None):
    parsed_data = {"data": []}
    files_data = {"root_files": []}

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        items = os.listdir(folder_path)
        if progress_bar:
            items = tqdm(items, desc="Прогресс", unit="файлов", dynamic_ncols=True)  # Создаем прогресс-бар

        for item_name in items:
            item_path = os.path.join(folder_path, item_name)

            if os.path.isdir(item_path):
                item_data = parse_folder(item_path)
                if item_data:
                    parsed_data["data"].append(item_data)
            else:
                files_data["root_files"].append(item_name)

    parsed_data["data"].append(files_data)
    print(Fore.MAGENTA + "============== Файл добавлен в текущую папку ===================")
    return parsed_data

result_json = parse_root_folder(folder_path, progress_bar=True)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(result_json, f, ensure_ascii=False, indent=4)
    file_path = file_path.replace(" ", "\u00A0")
    show_result(file_path)


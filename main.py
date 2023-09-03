import os
import json
import datetime
from colorama import init, Fore, Style

while True:
    print(Fore.MAGENTA + "===================== Инструкции ===============================")
    print(Fore.BLUE + "1. Укажите папку для вывода")
    print(Fore.BLUE + "2. Укажите путь для создания файла")
    print(Fore.MAGENTA + "======================= Действия ===============================")
    print(Fore.BLUE + "1. Указать папку")
    print(Fore.BLUE + "2. Выбрать папку в которой расположена программа")
    print(Fore.BLUE + "3. Выход")
    print(Fore.MAGENTA + "========================= ВВОД =================================")
    choice = input(Fore.GREEN + "Выберите вариант: " + Style.RESET_ALL)


    if choice == "1":
        folder_path = input(Fore.GREEN + "Введите полный путь к папке: " + Style.RESET_ALL)
        print(Fore.CYAN + "================================================================")
    elif choice == "2":
        folder_path = os.getcwd()
    elif choice == "3":
        exit()

    print(Fore.CYAN + "================================================================")
    print(Fore.GREEN + "1. Выгрузить файл в определенную папку" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Выгрузить файл в текущую папку" + Style.RESET_ALL)
    print(Fore.GREEN + "3. Выход" + Style.RESET_ALL)
    upload = input(Fore.GREEN + "Выберите действие: " + Style.RESET_ALL)

    if upload == "1":
        print(Fore.CYAN + "================================================================")
        file_path = input(Fore.GREEN + "Введите куда выгрузить результат: " + Style.RESET_ALL)
        filename = "data" + datetime.datetime.now().strftime("%d_%m_%Y_%S") + ".json"
        file_path = os.path.join(file_path, filename)
    elif upload == "2":
        filename = "data" + datetime.datetime.now().strftime("%d_%m_%Y_%S") + ".json"
        file_path = filename
        print(Fore.MAGENTA + "============== Файл добавлен в текущую папку ===================")
        break
    elif upload == "3":
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

def parse_root_folder(folder_path):
    parsed_data = {"data": []}
    files_data = {"root_files": []}

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for item_name in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item_name)

            if os.path.isdir(item_path):
                item_data = parse_folder(item_path)
                if item_data:
                    parsed_data["data"].append(item_data)
            else:
                files_data["root_files"].append(item_name)

    parsed_data["data"].append(files_data)
    return parsed_data

result_json = parse_root_folder(folder_path)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(result_json, f, ensure_ascii=False, indent=4)

print(Fore.CYAN + "==============================================================")
print(Fore.GREEN + "==============================================================")
print(Fore.GREEN + "========================= ГОТОВО !!! =========================")
print(Fore.GREEN + "==============================================================")
print(Fore.GREEN + "==============================================================")

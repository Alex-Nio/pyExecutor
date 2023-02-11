import os
import json
import datetime
from colorama import init, Fore, Style

while True:
    print(Fore.MAGENTA + '========================= ОПЦИИ =================================')
    print(Fore.BLUE + "1. Выбрать папку с курсами")
    print(Fore.BLUE + "2. Указать путь к папке")
    print(Fore.MAGENTA + '================================================================')
    print(Fore.BLUE + "3. Выход")
    print(Fore.MAGENTA + '========================= ВВОД =================================')
    choice = input(Fore.GREEN + "Выберите вариант: " + Style.RESET_ALL)

    if choice == "1":
        folder_path = r"D:\Programs\OpenServer\domains\hosting\vh\dist\courses\data\Курсы"
        file_path = "courses.json"
        break
    elif choice == "2":
        print(Fore.CYAN + '================================================================')
        print(Fore.CYAN + '================================================================')
        print(Fore.CYAN + '================================================================')
        folder_path = input(Fore.GREEN + "Введите путь к папке: " + Style.RESET_ALL)
        print(Fore.CYAN + '================================================================')
        upload = input(Fore.GREEN + "Хотите выгрузить файл в определенную папку? (1-Да / 2-Нет | Файл будет добавлен в текущую папку) " + Style.RESET_ALL)
        if upload == "1":
            print(Fore.CYAN + '================================================================')
            file_path = input(Fore.GREEN + "Введите куда выгрузить результат: " + Style.RESET_ALL)
            filename = "data" + datetime.datetime.now().strftime("%d_%m_%Y_%S") + ".json"
            file_path = os.path.join(file_path, filename)
        elif upload == "2":
            filename = "data" + datetime.datetime.now().strftime("%d_%m_%Y_%S") + ".json"
            file_path = filename
            print(Fore.MAGENTA + '============== Файл добавлен в текущую папку ===================')
            break
        else:
            print(Fore.RED + "Недопустимый выбор, повторите ввод" + Style.RESET_ALL)
            break
        break
    elif choice == "3":
        print(Fore.RED + "Выход из программы" + Style.RESET_ALL)
        exit()
    else:
        print(Fore.RED + "Недопустимый выбор, повторите ввод" + Style.RESET_ALL)

def parse_folder(folder_path, result=None):
    if result is None:
        result = {}
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            course = {"Папка": item}
            result[item] = parse_folder(item_path, course)
        else:
            current_lesson = result.get("Файлы", [])
            current_lesson.append(item)
            result["Файлы"] = current_lesson
    return result

parsed_data = {"Курсы": []}
for course in os.listdir(folder_path):
    course_path = os.path.join(folder_path, course)
    if os.path.isdir(course_path):
        course_data = {}
        course_data[course] = parse_folder(course_path)
        parsed_data["Курсы"].append(course_data)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)

print(Fore.CYAN + "==============================================================")
print(Fore.GREEN + "==============================================================")
print(Fore.GREEN + "========================= ГОТОВО !!! =========================")
print(Fore.GREEN + "==============================================================")
print(Fore.GREEN + "==============================================================")

# pyExecutor

pyExecutor - это программа, разработанная исключительно в благих целях, для обработки и анализа файловой структуры в операционной системе Windows. Программа предоставляет пользователю возможность выбрать папку для анализа и опционально указать путь для сохранения результата.

**Важное замечание:** Данная программа предназначена исключительно для честного и законного использования. Автор не несет ответственности за незаконное использование программы в целях взлома или присвоения чужих данных.

## Инструкции

1. Запустите скрипт, выполнив следующую команду в командной строке:

   ```
   python main.py
   ```

2. Выберите один из вариантов:
   - Укажите папку, которую вы хотите проанализировать.
   - Используйте текущую рабочую папку, в которой находится программа.
   - Выйдите из программы.

3. После выбора папки, у вас будет возможность:
   - Выгрузить результат анализа в определенную папку.
   - Выгрузить результат анализа в текущую рабочую папку.
   - Выйти из программы.

## Результат работы программы

Программа анализирует выбранную папку и создает JSON-файл, содержащий информацию о структуре папки, включая вложенные папки и файлы. Имя JSON-файла будет содержать дату и время создания для уникальности.

**Примечание:** Программа также предоставляет прогресс-бар для отслеживания хода выполнения анализа.

Полученный JSON-файл можно использовать для дальнейшего анализа данных.

После успешного завершения работы, программа выведет сообщение о завершении работы.

**Обратите внимание:** Эта программа предназначена для удобства анализа файловой структуры и не предоставляет возможности вмешательства в файлы или папки операционной системы.

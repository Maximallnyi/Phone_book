import csv
import interface
from tempfile import NamedTemporaryFile
import shutil

global count_rows # Количество строк в файле
count_rows = 5


# Проверка корректности введённого номера
def check_number(number):
    if number.isdigit() and len(number)==11:
        return True
    else:
        return False

# Проверка корректности ввведённого ФИО
def check_name(name):
    if any(map(str.isdigit, name)):
        return False
    else:
        return True

# Добавление новый информации в файл
def add_info():
    surname = input('Введите фамилию: ')
    while (not check_name(surname)):
        print("Некорректно, должны присутствовать только буквы")
        surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    while (not check_name(name)):
        print("Некорректно, должны присутствовать только буквы")
        name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    while (not check_name(middle_name)):
        print("Некорректно, должны присутствовать только буквы")
        middle_name = input('Введите отчество: ')
    job = input('Название организации: ')
    job_number = input('Введите рабочий номер: ')
    while (not check_number(job_number)):
        print("Некорректно набран номер (требуется 11 цифр без знака '+'")
        job_number = input('Введите рабочий номер: ')
    personal_number = input('Введите личный номер: ')
    while (not check_number(personal_number)):
        print("Некорректно набран номер (требуется 11 цифр без знака '+'")
        personal_number = input('Введите личный номер: ')
    with open("phone_book.csv", "a",newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([surname,name,middle_name,job,job_number,personal_number])
        count_rows += 1
    interface.start()

# Поиск информации в файле
def find_info():
    surname = ''
    name = ''
    middle_name = ''
    job = ''
    job_number = ''
    personal_number = ''
    print('Выберите по каким параметрам вы хотите найти запись (укажите через запятую):')
    print('------------------------------------')
    print('1. Фамилия')
    print('2. Имя')
    print('3. Отчество')
    print('4. Название организации')
    print('5. Рабочий номер')
    print('6. Личный номер')
    answer = input('Введите параметры: ')
    answer = answer.split(',')
    par_arr = []
    for par in answer:
        if par == '1':
            surname = input('Введите фамилию: ')
            while (not check_name(surname)):
                print("Некорректно, должны присутствовать только буквы")
                surname = input('Введите фамилия: ')
        if par == '2':
            name = input('Введите имя: ')
            while (not check_name(name)):
                print("Некорректно, должны присутствовать только буквы")
                name = input('Введите имя: ')
        if par == '3':
            middle_name = input('Введите отчество: ')
            while (not check_name(middle_name)):
                print("Некорректно, должны присутствовать только буквы")
                middle_name = input('Введите отчество: ')
        if par == '4':
            job = input('Введите название организации: ')
        if par == '5':
            job_number = input('Введите рабочий номер: ')
            while (not check_number(job_number)):
                print("Некорректно набран номер (требуется 11 цифр без знака '+'")
                job_number = input('Введите рабочий номер: ')
        if par == '6':
            personal_number = input('Введите личный номер: ')
            while (not check_number(personal_number)):
                print("Некорректно набран номер (требуется 11 цифр без знака '+'")
                personal_number = input('Введите личный номер: ')
    finding = False
    with open("phone_book.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        print('{0: <23}'.format('Фамилия'), end=' ')
        print('{0: <23}'.format('Имя'), end=' ')
        print('{0: <23}'.format('Отчество'), end=' ')
        print('{0: <23}'.format('Название организации'), end=' ')
        print('{0: <23}'.format('Рабочий телефон'), end=' ')
        print('{0: <23}'.format('Личный телефон'))
        for row in file_reader:
            if (surname == row[0] or surname == '') and (name == row[1] or name == '') and (middle_name == row[2] or middle_name == '') \
                        and (job == row[3] or job == '') and (job_number == row[4] or job_number == '') and\
                (personal_number == row[5] or personal_number == ''):
                finding = True
                for el in row:
                    print('{0: <23}'.format(el), end=' ')
                print()
    if finding == False:
        print('Запись не найдена')
    interface.start()
    print('------------------------------------')

# Вывод содержимого файла в консоль
def show_info():
    with open("phone_book.csv", "r",encoding='utf-8-sig') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            for el in row:
                print('{0: <23}'.format(el), end=' ')
            print()
    print('------------------------------------')
    interface.start()

# Редактирование информации в файле
def change_info():
    surname = input('Введите фамилию: ')
    while (not check_name(surname)):
        print("Некорректно, должны присутствовать только буквы")
        surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    while (not check_name(name)):
        print("Некорректно, должны присутствовать только буквы")
        name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    while (not check_name(middle_name)):
        print("Некорректно, должны присутствовать только буквы")
        middle_name = input('Введите отчество: ')
    job = input('Название организации: ')
    job_number = input('Введите рабочий номер: ')
    while (not check_number(job_number)):
        print("Некорректно набран номер (требуется 11 цифр без знака '+'")
        job_number = input('Введите рабочий номер: ')
    personal_number = input('Введите личный номер: ')
    while (not check_number(personal_number)):
        print("Некорректно набран номер (требуется 11 цифр без знака '+'")
        personal_number = input('Введите личный номер: ')
    finding = False

    filename = 'phone_book.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

    fields = ['Фамилия', 'Имя', 'Отчество', 'Название организации','Рабочий телефон','Личный телефон']

    with open(filename, 'r', newline='',encoding='utf-8-sig') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if (surname == row[fields[0]]) and (name == row[fields[1]]) and (middle_name == row[fields[2]]) and (job == row[fields[3]])\
                    and (job_number == row[fields[4]]) and (personal_number == row[fields[5]]):
                finding = True
                print('Выберите параметры, которые хотите изменить (перечислите через запятую):')
                print('------------------------------------')
                print('1. Фамилия')
                print('2. Имя')
                print('3. Отчество')
                print('4. Название организации')
                print('5. Рабочий номер')
                print('6. Личный номер')
                answer = input('Введите параметры: ')
                answer = answer.split(',')
                for par in answer:
                    if par == '1':
                        surname = input('Введите фамилию: ')
                        while (not check_name(surname)):
                            print("Некорректно, должны присутствовать только буквы")
                            surname = input('Введите фамилию: ')
                        row['Фамилия'] = surname
                    if par == '2':
                        name = input('Введите имя: ')
                        while (not check_name(name)):
                            print("Некорректно, должны присутствовать только буквы")
                            name = input('Введите имя: ')
                        row['Имя'] = name
                    if par == '3':
                        middle_name = input('Введите отчество: ')
                        while (not check_name(middle_name)):
                            print("Некорректно, должны присутствовать только буквы")
                            middle_name = input('Введите отчество: ')
                        row['Отчество'] = middle_name
                    if par == '4':
                        job = input('Введите название организации: ')
                        row['Название организации'] = job
                    if par == '5':
                        job_number = input('Введите рабочий номер: ')
                        while (not check_number(job_number)):
                            print("Некорректно набран номер (требуется 11 цифр без знака '+'")
                            job_number = input('Введите рабочий номер: ')
                        row['Рабочий телефон'] = job_number
                    if par == '6':
                        personal_number = input('Введите личный номер: ')
                        while (not check_number(personal_number)):
                            print("Некорректно набран номер (требуется 11 цифр без знака '+'")
                            personal_number = input('Введите личный номер: ')
                        row['Личный телефон'] = personal_number

            row = {'Фамилия': row['Фамилия'], 'Имя': row['Имя'], 'Отчество': row['Отчество'], 'Название организации'\
                : row['Название организации'], 'Рабочий телефон': row['Рабочий телефон'], 'Личный телефон': row['Личный телефон']}
            writer.writerow(row)

    if finding:
        shutil.move(tempfile.name, filename)
        print('Изменения сохранены')
    else:
        print('Запись не найдена')
    print('------------------------------------')
    interface.start()

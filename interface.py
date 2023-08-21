from data import add_info, change_info, find_info, show_info

def start():
    print('Выберите, что вы хотите сделать:')
    print('------------------------------------')
    print('1. Вывести записи')
    print('2. Добавить новую запись в справочник')
    print('3. Редактировать запись в справочнике')
    print('4. Поиск записи в справочнике')
    print('5. Выйти из программы')
    answer = input('Ваше действие: ')
    if answer == '1':
        show_info()
    if answer == '2':
        add_info()
    if answer == '3':
        change_info()
    if answer == '4':
        print(1)
        find_info()
    if answer == '5':
        exit()
    else:
        print('Некорректная команда, повторите снова')
        start()


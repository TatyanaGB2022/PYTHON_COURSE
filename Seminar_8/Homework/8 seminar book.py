# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    

    while choice!= 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            lastname = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите новые данные: ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 7:  
            src_file = input('Введите имя исходного файла: ')
            dst_file = input('Введите имя целевого файла: ')
            line_num = int(input('Введите номер строки для копирования: '))
            copy_line(src_file, dst_file, line_num)
            print(f'Строка {line_num} из файла {src_file} скопирована в файл {dst_file}')

        choice = show_menu()
        if choice == 8:
            write_txt('phonebook.txt', phone_book)
            break

def show_menu():
    print('Меню:')
    print('1. Показать телефонную книгу')
    print('2. Найти по фамилии')
    print('3. Изменить номер')
    print('4. Удалить по фамилии')
    print('5. Найти по номеру')
    print('6. Добавить новый контакт')
    print('7. Копировать данные из одного файла в другой')
    print('8. Выход')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 1 <= choice <= 8:
                return choice
            else:
                print('Неверный выбор. Пожалуйста, выберите пункт от 1 до 8.')
        except ValueError:
            print('Неверный ввод. Пожалуйста, введите число.')

def read_txt(filename):
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'], line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            phout.write(','.join(record.values()) + '\n')

def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    result = [record for record in phone_book if record['Фамилия'] == last_name]
    if result:
        return result
    else:
        return 'Контакт не найден'

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return 'Номер изменен'
    return 'Контакт не найден'

def delete_by_lastname(phone_book, lastname):
    phone_book[:] = [record for record in phone_book if record['Фамилия']!= lastname]
    return 'Контакт удален'

def find_by_number(phone_book, number):
    result = [record for record in phone_book if record['Телефон'] == number]
    if result:
        return result
    else:
        return 'Контакт не найден'

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)

def copy_line(src_file, dst_file, line_num):
    with open(src_file, 'r', encoding='utf-8') as src:
        lines = src.readlines()
        if line_num > 0 and line_num <= len(lines):
            line_to_copy = lines[line_num - 1]
            with open(dst_file, 'a', encoding='utf-8') as dst:
                dst.write(line_to_copy)
        else:
            print('Неверный номер строки')

work_with_phonebook()
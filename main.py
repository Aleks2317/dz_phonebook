file_name = 'phonebook.txt'


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book


def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep='\n')
    return int(input())


#  функция для записи
def write_phone_book(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in phone_book:
            file.write(f"{contact['Фамилия']}, "
                       f"{contact['Имя']}, "
                       f"{contact['Телефон']}, "
                       f"{contact['Описание']}\n")


# 2. Найти телефон по фамилии
def find_by_lastname(phone_book, last_name):
    if last_name not in [name_["Фамилия"] for name_ in phone_book]:
        return f"Фамилии '{last_name}' нет в справочнике!!!"
    return list(filter(lambda l: l['Фамилия'] == last_name, phone_book))[0]


# 3. Изменить номер телефона
def change_number(phone_book, last_name, new_number):
    # проверка на пользователя
    last_name_contact = find_by_lastname(phone_book, last_name)
    if type(last_name_contact) != dict:
        print(last_name_contact)
        return
    # изменение номера контакта
    for i_contact in range(len(phone_book)):
        if phone_book[i_contact] == last_name_contact:
            phone_book[i_contact]['Телефон'] = new_number
    return write_phone_book(file_name, phone_book)


# 4. Удалить запись
def delete_by_lastname(phone_book, last_name):
    # проверка на пользователя
    last_name_contact = find_by_lastname(phone_book, last_name)
    if type(last_name_contact) != dict:
        print(last_name_contact)
        return
    for i_contact in range(len(phone_book)):
        if phone_book[i_contact] == last_name_contact:
            del phone_book[i_contact]
            print(f"Контакт {last_name} удален.")
            return write_phone_book(file_name, phone_book)


# 5. Найти абонента по номеру телефона'
def find_by_number(phone_book, number):
    result = sorted(phone_book, key=lambda l: l['Телефон'] == number)[-1]
    if result['Телефон'] != number:
        print(f"Номера телефона {number} в справочнике не найден.")
        return
    print(result)
    return


# 6. Добавить абонента в справочник'
def add_user(phone_book, user_data):
    user_data = [i.strip() for i in user_data.split(',')]
    while len(user_data) < 4:
        user_data.append(None)
    if len(user_data) > 4:
        user_data = user_data[:3]
    contact = {}
    for key, value in zip(["Фамилия", "Имя", "Телефон", "Описание"], user_data):
        contact[key] = value
    phone_book.append(contact)
    print(f"Новый контакт {user_data} записан!")
    return write_phone_book(file_name, phone_book)


#  если choice == 7 выход из цикла и завершение работы
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt(file_name)
    while choice != 7:
        # 1. Start Распечатать справочник
        if choice == 1:
            for x in phone_book:
                for key, value in x.items():
                    print(key, "---", value)
                print()
        # 2. Start Найти телефон по фамилии
        if choice == 2:
            last_name = input('Фамилия: ')
            print(find_by_lastname(phone_book, last_name))
        # 3. Start Изменить номер телефона
        if choice == 3:
            last_name = input('Фамилия: ')
            new_number = input('новый номер телефона: ')
            change_number(phone_book, last_name, new_number)
        # 4. Start Удалить запись
        if choice == 4:
            lastname = input('Фамилия: ')
            delete_by_lastname(phone_book, lastname)
        # 5. Start Найти абонента по номеру телефона'
        if choice == 5:
            number = input('номер телефона: ')
            find_by_number(phone_book, number)
        # 6. Start Добавить абонента в справочник'
        if choice == 6:
            user_data = input('Новый контакт\n введите согласно инструкции\n "Фамилия, Имя, Телефон, Описание":\n ')
            add_user(phone_book, user_data)

        choice = show_menu()
    return "Выход"


print(work_with_phonebook())

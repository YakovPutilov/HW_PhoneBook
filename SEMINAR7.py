
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while (choice!=8):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name = input('lastname ')
            print(*find_by_lastname(phone_book ,last_name))
        elif choice==3:
            number = input('number ')
            print(*find_by_number(phone_book, number))
        elif choice==4:
            phone_book = add_abonent(phone_book)
        elif choice==5:
            last_name = input('lastname ')
            phone_book=change_parameter(phone_book, last_name)
        elif choice==6:
            from_book = read_txt('addbook.txt')
            row_num = int(input('Input row: '))
            phone_book = add_from_file_row(phone_book, from_book, row_num)
        elif choice==7:

            write_txt('phonebook.txt' ,phone_book)
        choice = show_menu()
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные\n"
          "6. Добавить из файла\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

# Иванов,       Иван ,   111,  описание Иванова
# Петров,      Петр ,    222,  описание Петрова
#
# Васичкина , Василиса , 333 , описание Васичкиной
#
# Питонов,    Антон,     777,    умеет в Питон

def read_txt(filename):
    phone_book =[]
    fields =['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename ,'r' ,encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
        # dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            phone_book.append(record)
    return phone_book
def write_txt(filename, phone_book):
    with open('phonebook.txt' ,'w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for j in phone_book[i].values():
                s = s + j +','
            phout.write(f'{s[:-1]}')

def print_result(book):
    for i in book:
        print(i)

def find_by_lastname(book,last_name):
    for i in book:
        if i.get('Фамилия') == last_name:
            return i.values()
    return 'not found'

def find_by_number(book,number):
    for i in book:
        if i.get('Телефон') == number:
            return i.values()
    return 'not found'

def change_parameter(phone_book, last_name):
    flag = False
    for i in phone_book:
        if i.get('Фамилия') == last_name:
            for j in i:
                temp_text = ''
                print('Введите '+ j + ':')
                temp_text = input()
                if temp_text != '':
                    i[j] = temp_text
            flag = True
    if flag:
        return phone_book
    else:
        print('not found')
        return phone_book

def add_from_file_row(phone_book, from_book, row_num):
    phone_book.append(from_book[row_num])
    return phone_book

def add_abonent(phone_book):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    line = fields[:]
    for i in range(len(line)):
        line[i] = input('Введите '+ line[i] + ':')
    line[-1] = line[-1]+'\n'
    record = dict(zip(fields, line))
    phone_book.append(record)
    return phone_book

work_with_phonebook()


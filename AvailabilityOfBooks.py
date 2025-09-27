# для создания нужных txt файлов этой программы не вручную можно запустить этот скрипт 


with open("users.txt", "w") as f:
    f.write("admin,admin1\nmanager1,password123\nmanager2,password321")

with open("phones.txt", "w") as f:
    f.write("Apple,iPhone 13,4,128,6.1,Black,799\n")
    f.write("Samsung,Galaxy S21,8,256,6.2,White,899\n")
    f.write("Xiaomi,Redmi Note 10,6,128,6.43,Blue,299\n")
    f.write("Google,Pixel 6,8,128,6.4,Black,699\n")
    f.write("OnePlus,9 Pro,12,256,6.7,Green,999\n")

print("Файлы users.txt и phones.txt успешно созданы с начальными данными ")











import os
from getpass import getpass











RED = '\033[91m'
RESET = '\033[0m'

def print_error(message):
    print(f"{RED}{message}{RESET}")







USERS_FILE = "users.txt"
PHONES_FILE = "phones.txt"





# Создает пустой словарь для пользователей

# Проверяет существование файла users.txt

# Если файл существует, читает его построчно

# Каждую строку разделяет по запятой на имя пользователя и пароль

# Добавляет пару в словарь users

# При ошибках выводит сообщение, но продолжает работу
def load_users():
    users = {}
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    users[username] = password
    except Exception as e:
        print_error(f"Ошибка при загрузке пользователей: {e}")
    return users


















# Открывает файл users.txt для записи

# Записывает каждую пару имя-пароль из словаря users в файл

# Обрабатывает возможные ошибки записи
def save_users(users):
    try:
        with open(USERS_FILE, 'w') as file:
            for username, password in users.items():
                file.write(f"{username},{password}\n")
    except Exception as e:
        print_error(f"Ошибка при сохранении пользователей: {e}")








#Создает пустой список для телефонов

# Читает файл phones.txt построчно

# Каждую строку преобразует в словарь с характеристиками телефона

# Добавляет словарь в список phones
def load_phones():
    phones = []
    try:
        if os.path.exists(PHONES_FILE):
            with open(PHONES_FILE, 'r') as file:
                for line in file:
                    phone_data = line.strip().split(',')
                    phone = {
                        'brand': phone_data[0],
                        'model': phone_data[1],
                        'ram': phone_data[2],
                        'storage': phone_data[3],
                        'screen_size': phone_data[4],
                        'color': phone_data[5],
                        'price': phone_data[6]
                    }
                    phones.append(phone)
    except Exception as e:
        print_error(f"Ошибка при загрузке телефонов: {e}")
    return phones





# Цикл for перебирает все телефоны в списке phones

# Для каждого телефона формируется строка в формате CSV:
# Значения разделяются запятыми
# Порядок полей: brand, model, ram, storage, screen_size, color, price
# \n в конце - перенос строки

# Используется f-строка для подстановки значений
def save_phones(phones):
    try:
        with open(PHONES_FILE, 'w',encoding="utf-8") as file:
            for phone in phones:
                file.write(f"{phone['brand']},{phone['model']},{phone['ram']},{phone['storage']},"
                          f"{phone['screen_size']},{phone['color']},{phone['price']}\n")
    except Exception as message:
        print_error(f"Ошибка при сохранении телефонов: {message}")














# В цикле запрашивает имя пользователя и пароль

# Проверяет их соответствие данным из словаря users

# При успешной проверке возвращает имя пользователя
def login(users):
    while True:
        print("\n--- Страница входа ---")
        username = input("Имя пользователя: ").strip()
        password = getpass("Пароль: ").strip()
        
        if username in users and users[username] == password:
            print("\nУспешный вход!")
            return username
        else:
            print_error("\nНеверное имя пользователя или пароль! Попробуйте снова!")




















# Запрашивает новое имя пользователя с проверками:
# Не пустое
# Уникальное

# Запрашивает пароль с проверками:
# Не пустой
# Не совпадает с именем
# Подтверждение совпадает


# Добавляет пользователя в словарь

# Сохраняет обновленный словарь
def add_manager(users):
    print("\n--- Добавление нового менеджера ---")
    while True:
        username = input("Введите новое имя пользователя: ").strip()
        if not username:
            print_error("Имя пользователя не может быть пустым!")
            continue
        if username in users:
            print_error("Это имя пользователя уже занято!")
            continue
        break
    
    while True:
        password = getpass("Введите пароль: ").strip()
        if not password:
            print_error("Пароль не может быть пустым!")
            continue
        if password == username:
            print_error("Пароль не может совпадать с именем пользователя!")
            continue
        password_confirm = getpass("Подтвердите пароль: ").strip()
        if password == password_confirm:
            break
        print_error("Пароли не совпадают!")
    
    users[username] = password
    save_users(users)
    print(f"\nМенеджер {username} успешно добавлен!")

















# Запрашивает все характеристики нового телефона

# Выводит для подтверждения

# После подтверждения добавляет в список

# Сохраняет обновленный список
def add_phone(phones):
    print("\n--- Добавление нового телефона ---")
    phone = {}
    
    phone['brand'] = input("Марка: ").strip()
    phone['model'] = input("Модель: ").strip()
    phone['ram'] = input("ОЗУ (ГБ): ").strip()
    phone['storage'] = input("Память (ГБ): ").strip()
    phone['screen_size'] = input("Размер экрана (дюймы): ").strip()
    phone['color'] = input("Цвет: ").strip()
    phone['price'] = input("Цена: ").strip()
    
    
    
    print("\n--- Подтвердите добавление телефона ---")
    print(f"Марка: {phone['brand']}")
    print(f"Модель: {phone['model']}")
    print(f"ОЗУ: {phone['ram']} ГБ")
    print(f"Память: {phone['storage']} ГБ")
    print(f"Размер экрана: {phone['screen_size']} дюймов")
    print(f"Цвет: {phone['color']}")
    print(f"Цена: {phone['price']}")
    
   
   
    while True:
        choice = input("\nПодтвердить добавление? (Y/N): ").upper()
        if choice == 'Y':
            phones.append(phone)
            save_phones(phones)
            print("\nТелефон успешно добавлен!")
            return phones
        elif choice == 'N':
            print_error("\nДобавление телефона отменено!")
            return phones
        else:
            print_error("Неверный выбор! Введите Y (да) или N (нет)!")













# Выводит все характеристики выбранного телефона

# Предлагает варианты действий:
# Удалить (возвращает 'delete')
# Вернуться назад

# Обрабатывает выбор пользователя
def view_phone_details(phone, index):
    while True:
        print("\n--- Детали телефона ---")
        print(f"1. Марка: {phone['brand']}")
        print(f"2. Модель: {phone['model']}")
        print(f"3. ОЗУ: {phone['ram']} ГБ")
        print(f"4. Память: {phone['storage']} ГБ")
        print(f"5. Размер экрана: {phone['screen_size']} дюймов")
        print(f"6. Цвет: {phone['color']}")
        print(f"7. Цена: {phone['price']}")
        print("D. Удалить телефон")
        print("0. Назад")
        
        choice = input("Выберите действие: ").upper()
        
        if choice == '0':
            break
        elif choice == 'D':
            return 'delete'
        else:
            print_error("Неверный выбор! Попробуйте снова!")



















# Выводит список всех телефонов в сокращенном формате

# Предлагает варианты:
# Добавить телефон (вызывает add_phone())
# Просмотреть детали (вызывает view_phone_details())
# Удалить телефон (если получен сигнал 'delete')

# Сохраняет изменения после модификации списка
def phone_list(phones):
    while True:
        print("\n--- Список телефонов ---")
        if not phones:
            print_error("Нет доступных телефонов.")
        else:
            for i, phone in enumerate(phones, 1):
                print(f"{i}. {phone['brand']} {phone['model']}")
        
        print("A. Добавить телефон")
        print("0. Назад")
        
        choice = input("Выберите действие: ").upper()
        
        if choice == '0':
            break
        elif choice == 'A':
            phones = add_phone(phones)
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(phones):
                action = view_phone_details(phones[index], index)
                if action == 'delete':
                    del phones[index]
                    save_phones(phones)
                    print_error("Телефон удален!")
            else:
                print_error("Неверный номер телефона!")
        else:
            print_error("Неверный выбор! Попробуйте снова!")
        












# Проверяет, что текущий пользователь - admin

# Проверяет, что пользователь не удаляет себя

# Запрашивает подтверждение паролем

# Запрашивает подтверждение действия

# Удаляет пользователя и сохраняет изменения
def delete_manager(users, current_user):
    print_error("\n--- Удаление менеджера ---")
    
    if current_user != 'admin':
        print_error("Только администратор может удалять менеджеров!")
        return users
    
    username = input("Введите имя пользователя для удаления: ").strip()
    
    if username not in users:
        print_error("Такого пользователя не существует!")
        return users
    
    if username == current_user:
        print_error("Вы не можете удалить самого себя!")
        return users
    
    password = getpass("Введите пароль администратора для подтверждения: ").strip()
    
    if users[current_user] != password:
        print_error("Неверный пароль!")
        return users
    
   
    confirm = input(f"Вы уверены, что хотите удалить менеджера {username}? (y/n): ").lower()
    if confirm != 'y':
        print_error("Удаление отменено!")
        return users
    
    del users[username]
    save_users(users)
    print_error(f"\nМенеджер {username} успешно удален!")
    return users








# Выводит главное меню с вариантами действий

# Обрабатывает выбор пользователя:
# Управление телефонами (phone_list())
# Добавление менеджера (add_manager())
# Удаление менеджера (delete_manager())

# Выход из программы
def main_menu(username, users, phones):
    while True:
        print(f"\n--- Главное меню (пользователь: {username}) ---")
        print("1. Телефоны")
        print("2. Добавить менеджера")
        print_error("3. Удалить менеджера")  
        print("0. Выход")
        
        try:
            choice = input("Выберите действие: ")
            
            if choice == '0':
                print("Выход из системы...")
                break
            elif choice == '1':
                phone_list(phones)
            elif choice == '2':
                add_manager(users)
            elif choice == '3':
                users = delete_manager(users, username)
            else:
                print_error("Неверный выбор! Попробуйте снова!")
        except Exception as e:
            print_error(f"Произошла ошибка: {e}")












#Загружает данные пользователей и телефонов

# Если нет пользователей, создает администратора по умолчанию

# Выполняет вход (login())

# Запускает главное меню
def main():
    users = load_users()
    phones = load_phones()
    
    # Если скрипта не будет или он не срабоает то система по умолчанию создаст аккаунт 
    if not users:
        print("Создание администратора по умолчанию...")
        users['admin'] = 'admin1'
        save_users(users)
    
    username = login(users)
    
    main_menu(username, users, phones)


main()

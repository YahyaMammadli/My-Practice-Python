# для создания нужных txt файлов этой программы не вручную можно запустить этот скрипт 
# with open("users.txt", "w") as f:
#     f.write("admin,admin\nmanager1,password123\nmanager2,password321")

# with open("phones.txt", "w") as f:
#     f.write("Apple,iPhone 13,4,128,6.1,Black,799\n")
#     f.write("Samsung,Galaxy S21,8,256,6.2,White,899\n")
#     f.write("Xiaomi,Redmi Note 10,6,128,6.43,Blue,299\n")
#     f.write("Google,Pixel 6,8,128,6.4,Black,699\n")
#     f.write("OnePlus,9 Pro,12,256,6.7,Green,999\n")

# print("Файлы users.txt и phones.txt успешно созданы с начальными данными ")











# import os
# from getpass import getpass















# USERS_FILE = "users.txt"
# PHONES_FILE = "phones.txt"

# def load_users():
#     users = {}
#     try:
#         if os.path.exists(USERS_FILE):
#             with open(USERS_FILE, 'r') as file:
#                 for line in file:
#                     username, password = line.strip().split(',')
#                     users[username] = password
#     except Exception as e:
#         print(f"Ошибка при загрузке пользователей: {e}")
#     return users

# def save_users(users):
#     try:
#         with open(USERS_FILE, 'w') as file:
#             for username, password in users.items():
#                 file.write(f"{username},{password}\n")
#     except Exception as e:
#         print(f"Ошибка при сохранении пользователей: {e}")

# def load_phones():
#     phones = []
#     try:
#         if os.path.exists(PHONES_FILE):
#             with open(PHONES_FILE, 'r') as file:
#                 for line in file:
#                     phone_data = line.strip().split(',')
#                     phone = {
#                         'brand': phone_data[0],
#                         'model': phone_data[1],
#                         'ram': phone_data[2],
#                         'storage': phone_data[3],
#                         'screen_size': phone_data[4],
#                         'color': phone_data[5],
#                         'price': phone_data[6]
#                     }
#                     phones.append(phone)
#     except Exception as e:
#         print(f"Ошибка при загрузке телефонов: {e}")
#     return phones

# def save_phones(phones):
#     try:
#         with open(PHONES_FILE, 'w') as file:
#             for phone in phones:
#                 file.write(f"{phone['brand']},{phone['model']},{phone['ram']},{phone['storage']},"
#                           f"{phone['screen_size']},{phone['color']},{phone['price']}\n")
#     except Exception as message:
#         print(f"Ошибка при сохранении телефонов: {message}")

# def login(users):
#     while True:
#         print("\n--- Страница входа ---")
#         username = input("Имя пользователя: ").strip()
#         password = getpass("Пароль: ").strip()
        
#         if username in users and users[username] == password:
#             print("\nУспешный вход!")
#             return username
#         else:
#             print("\nНеверное имя пользователя или пароль! Попробуйте снова!")

# def add_manager(users):
#     print("\n--- Добавление нового менеджера ---")
#     while True:
#         username = input("Введите новое имя пользователя: ").strip()
#         if not username:
#             print("Имя пользователя не может быть пустым!")
#             continue
#         if username in users:
#             print("Это имя пользователя уже занято!")
#             continue
#         break
    
#     while True:
#         password = getpass("Введите пароль: ").strip()
#         if not password:
#             print("Пароль не может быть пустым!")
#             continue
#         if password == username:
#             print("Пароль не может совпадать с именем пользователя!")
#             continue
#         password_confirm = getpass("Подтвердите пароль: ").strip()
#         if password == password_confirm:
#             break
#         print("Пароли не совпадают!")
    
#     users[username] = password
#     save_users(users)
#     print(f"\nМенеджер {username} успешно добавлен!")

# def add_phone(phones):
#     print("\n--- Добавление нового телефона ---")
#     phone = {}
    
#     phone['brand'] = input("Марка: ").strip()
#     phone['model'] = input("Модель: ").strip()
#     phone['ram'] = input("ОЗУ (ГБ): ").strip()
#     phone['storage'] = input("Память (ГБ): ").strip()
#     phone['screen_size'] = input("Размер экрана (дюймы): ").strip()
#     phone['color'] = input("Цвет: ").strip()
#     phone['price'] = input("Цена: ").strip()
    
#     phones.append(phone)
#     save_phones(phones)
#     print("\nТелефон успешно добавлен!")
#     return phones

# def view_phone_details(phone, index):
#     while True:
#         print("\n--- Детали телефона ---")
#         print(f"1. Марка: {phone['brand']}")
#         print(f"2. Модель: {phone['model']}")
#         print(f"3. ОЗУ: {phone['ram']} ГБ")
#         print(f"4. Память: {phone['storage']} ГБ")
#         print(f"5. Размер экрана: {phone['screen_size']} дюймов")
#         print(f"6. Цвет: {phone['color']}")
#         print(f"7. Цена: {phone['price']}")
#         print("D. Удалить телефон")
#         print("0. Назад")
        
#         choice = input("Выберите действие: ").upper()
        
#         if choice == '0':
#             break
#         elif choice == 'D':
#             return 'delete'
#         else:
#             print("Неверный выбор! Попробуйте снова!")

# def phone_list(phones):
#     while True:
#         print("\n--- Список телефонов ---")
#         if not phones:
#             print("Нет доступных телефонов.")
#         else:
#             for i, phone in enumerate(phones, 1):
#                 print(f"{i}. {phone['brand']} {phone['model']}")
        
#         print("A. Добавить телефон")
#         print("0. Назад")
        
#         choice = input("Выберите действие: ").upper()
        
#         if choice == '0':
#             break
#         elif choice == 'A':
#             phones = add_phone(phones)
#         elif choice.isdigit():
#             index = int(choice) - 1
#             if 0 <= index < len(phones):
#                 action = view_phone_details(phones[index], index)
#                 if action == 'delete':
#                     del phones[index]
#                     save_phones(phones)
#                     print("Телефон удален!")
#             else:
#                 print("Неверный номер телефона!")
#         else:
#             print("Неверный выбор! Попробуйте снова!")

# def main_menu(username, users, phones):
#     while True:
#         print(f"\n--- Главное меню (пользователь: {username}) ---")
#         print("1. Телефоны")
#         print("2. Добавить менеджера")
#         print("0. Выход")
        
#         try:
#             choice = input("Выберите действие: ")
            
#             if choice == '0':
#                 print("Выход из системы...")
#                 break
#             elif choice == '1':
#                 phone_list(phones)
#             elif choice == '2':
#                 add_manager(users)
#             else:
#                 print("Неверный выбор! Попробуйте снова!")
#         except Exception as e:
#             print(f"Произошла ошибка: {e}")

# def main():
#     users = load_users()
#     phones = load_phones()
    
#     if not users:
#         print("Создание администратора по умолчанию...")
#         users['admin'] = 'admin'
#         save_users(users)
    
#     username = login(users)
    
#     main_menu(username, users, phones)

# main()
import os
import sys
import shutil


while True:
    print('1. создать папку')
    print('2. удалить файл/папку')
    print('3. копировать файл/папку')
    print('4. переименовать файл/папку')
    print('5. определить размер файла')
    print('6. посмотреть только файлы')
    print('7. посмотреть только папки')
    print('8. показать путь к папке')
    print('9. просмотреть содержимое рабочей директории')
    print('10. сменить рабочую директорию')
    print('11. показать свободное место на диске')
    print('12. информации об ОС')
    print('13  версия python на компьютере')
    print('14. создатель программы')
    print('15. играть в викторину')
    print('16. мой банковский счет')
    print('17. выход')


    choice = input('Выберите пункт меню:')

# создание папки в рабочей директории
    if choice == '1':
        while True:
           print(input('выберите название папки:'))
           os.mkdir('ПАПКА')
           break

# удаление папки в рабочей директории
    if choice == '2':
        while True:
            print(input('выберите название папки для удаления:'))
            os.rmdir('ПАПКА')
            break

# копирование файла
    if choice == '3':
        while True:
            print(input('выберите название файла для копирования:'))
            path = r'C:\Users\Юрий\boxx'
            source = r'C:\Users\Юрий\boxx\lesson.txt'
            destinationfile = r'C:\Users\Юрий\boxx\lesson(copy).txt'
            copying = shutil.copy(source,destinationfile)
            break

# переименовываем папку
    if choice == '4':
        while True:
            print(input('какую папку переименовать:'))
            os.rename(r'C:\Users\Юрий\box', r'C:\Users\Юрий\folder')
            break

# определяем размер файла
    if choice == '5':
        while True:
           print(input('название файла:'))
           print(os.path.getsize(r'C:\\Users\Юрий\\folder\\best.txt'))
           break

# второй вариант
    if choice == '5':
        while True:
            print(input('название файла:'))
            print(os.stat(r'C:\\Users\Юрий\\folder\\best.txt').st_size)
            break

# список файлов в текущей директории
    if choice == '6':
        while True:
            path = os.getcwd()
            with os.scandir(path) as listOfEntries:
                for entry in listOfEntries:
                    if entry.is_file():
                        print(entry.name)
            break

# список папок в текущей директории
    if choice == '7':
        while True:
            path = ()
            for it in os.scandir():
                if it.is_dir():
                    print(it.path)
            break

# показываем путь к папке(в текущей директории)
    if choice == '8':
        while True:
            print(input('название папки:'))
            print(os.path.abspath("."))
            break

# содержимое рабочей директории
    if choice == '9':
        while True:
            print(os.listdir(path="."))
            break

# меняем рабочую(текущую)(C:\) директорию
    if choice == '10':
        while True:
            print(input('укажите путь директории:'))
            print(os.getcwd())
            os.chdir(r'D:\exercise')
            print(os.getcwd())
            break

# определяем свободное место на диске
    if choice =='11':
        while True:
           print(input('название диска:'))
           print(shutil.disk_usage(r'C:\\'))
           break

# инфа об ОС
    if choice =='12':
        while True:
            print(os.name)
            print(sys.platform)
            break

# инфа об установленной версии python на компьютере
    if choice == '13':
        while True:
            print(sys.version)
            break

# создатель программы
    if choice =='14':
        while True:
            print(os.stat(r'D:\exercise\user.doc'))
            break

# викторина
    if choice == '15':
        while True:
            def year_born():
                _year_ = input('Введите год рождения А.С.Пушкина:')
                while _year_ != '1799':
                    print("Не верно")
                    _year_ = input('Введите год рождения А.С.Пушкина:')
                print('Верно')
            year_born()


            def day_born():
                _day_ = input('Введите день рождения Пушкин?')
                while _day_ != '6':
                    print("Не верно")
                    _day_ = input('В какой день июня родился Пушкин?')
                print('Верно')
            day_born()
            break

# банковский счёт
    if choice == '16':
        while True:
            money_ = 0
            buy_dict = {'одежда, руб.': 30000, 'косметика, руб.': 80000,
                        'автозапчасти, руб.': 990000}
            inverse_buy_dict = {buy_dict[k]: k for k in buy_dict}
            my_buy_dict = {}

            while True:
                if money_ == 0:
                    print('На вашем счёте 0 руб.')
                    print('1. пополнение счета')
                    print('2. покупка')
                    print('3. история покупок')
                    print('4. выход')
                choice = input('Выберите пункт меню:')

                if choice == '1':
                    while True:
                        z = int(input('Введите сумму:'))
                        money_ = money_ + z
                        print(f'У вас на счете {money_} руб.')
                        choice = input('Выберите пункт меню:')
                        if money_ == max(buy_dict.values()):
                            print((buy_dict))
                        break

                if choice == '2':
                    while True:
                        sum_buy = int(input('Введите сумму покупки:'))
                        if money_ < sum_buy:
                            print('у Вас недостаточно средств')
                            choice = input('Выберите пункт меню:')
                        if money_ >= sum_buy:
                            key = inverse_buy_dict.get(sum_buy)
                            money_ = money_ - sum_buy
                            my_buy_dict[sum_buy] = key
                            print(f'мои покупки {my_buy_dict}')
                            print(f'У вас на счете {money_} руб.')
                            choice = input('Выберите пункт меню:')
                        break

                if choice == '3':
                    while True:
                        print(f'мои покупки {my_buy_dict}')
                        break

                if choice == '4':
                    break
            break

    if choice == '17':
        break



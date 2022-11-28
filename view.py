import operation


def start():
    while True:
        start = input("Телефонный справочник. Продолжить или завершить? (Y/N): ")
        if start == "Y" or start == "y":
            print("1 - Сделать запись.  2 - Найти телефон.")
            vibor = int(input("Ваш выбор: "))
            if vibor == 1:
                operation.record()
            elif vibor == 2:
                operation.search()
            else : 
                print("Сделайте правильный выбор.") 
        elif start == "N" or start == "n":
            print("Всего хорошего")
            break
        else : 
            print("Сделайте правильный выбор.")
    

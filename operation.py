def record():
    print('запись:')
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    remark = input('Введите примечание: ')
    print(f'Вы ввели: {surname} {name} {phone} {remark}')
    s = surname + ' ' + name + ' ' + phone + ' ' + remark
    vibor = input('Если все верно нажмите 1, если исправить - 2: ')
    if vibor == '1':
            f1 = open('catalog.txt', 'a', encoding='utf-8')
            f1.write(s + '\n')
            f1.close()
    else :
        record()
    

def search():
    count=0
    print('поиск по фамилии: ')
    surname = input('Введите фамилию: ')
    for i in open('catalog.txt', encoding='utf-8'):
        if surname in i:
            print('Искомые данные: ' + i)
            count +=1
    if count == 0:
        print('Такой фамилии нет.')
        







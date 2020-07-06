print('Что нужно сделать с файлом write/read')
x=input()
if x=='write':
    text = open("b.bin", "w")
    data = text.write(input('Введите,что нужно записать'))
    text.close()
if x=='read':
    text = open("b.bin", "r")
    data = text.read()
    print(data)
    text.close()
'''
Developers:
Baidalakova B.
Komarova E.
'''
import os
import os.path
import ru_local

def main():
    '''Основная программа, которая выводит путь к текущему каталогу и меню. Вызывает функцию выполнения команд.'''
    while True:
       print(os.getcwd())
       print(ru_local.MENU)
       command = acceptCommand()
       runCommand(command)
       if command == ru_local.QUIT:
          print('Работа программы завершена.')
          break


def acceptCommand():
    '''Запрашивает номер команды и в случае если номер команды указан некорректно,
    выводит сообщение об ошибке. Запрос команд осуществляется до тех пор,
    пока не введен корректный номер команды. Возвращает корректный номер команды.'''
    while True:
        command = int(input())
        if command in range(1, 8):
            break
    return command


def runCommand(command):
    '''Определяет по номеру команды command, какую функцию следует выполнить.'''
    if command == 1:
        print(catalog())
    if command == 2:
        moveUp()
    if command == 3:
        current = input(ru_local.CURRENT_DIR)
        moveDown(current)
    if command == 4:
        return 'countFiles(path)'
    if command == 5:
        path = os.getcwd()
        bytes = 0
        print(countBytes(path, bytes))
    if command == 6:
        return 'def findFiles(target, path)'


def catalog():
    dic_now = os.getcwd()
    return os.listdir(dic_now)


def moveUp():
    '''Делает текущим родительский каталог. Возвращает переход в новый каталог по новому пути'''
    dic_now = os.getcwd()
    num = dic_now.rfind('\\')
    return os.chdir(dic_now[:num])


def moveDown(current):
    '''Запрашивает имя подкаталога. Если имя указано корректно делает каталог находящийся в current текущим,
     иначе выводит сообщение об ошибке.'''
    try:
        dic_now = os.getcwd()
        dic_now = os.path.join(dic_now, current)
        return os.chdir(dic_now)
    except FileNotFoundError:
        print(ru_local.ERROR_DOWN)


def countFiles(path):
    '''Рекурсивная функция подсчитывающая количество файлов в указанном каталоге path.
    В подсчет включаются все файлы, находящиеся в подкаталогах. Возвращает количество файлов.'''


def countBytes(path, bytes):
    '''Рекурсивная функция подсчитывающая суммарный объем (в байтах) всех файлов в указанном каталоге path.
    В подсчет включаются все файлы, находящиеся в подкаталогах. Возвращает суммарное количество байт.'''
    os.chdir(path)
    main_list = os.listdir(path)
    for i in main_list:
        if os.path.isfile(path + '\\' + i):
            bytes += os.path.getsize(path + '\\' + i)
        if os.path.isdir(path + '\\' + i):
            countBytes(path + '\\' + i, bytes)
    return bytes


def findFiles(target, path):
    '''Рекурсивная функция, формирующая список путей к файлам, в имени которых содержится target.
     В поиск включаются все подкаталоги каталога path. В случае если файлы не найдены,
    выводит соответствующее сообщение.'''


if __name__ == '__main__':
    main()

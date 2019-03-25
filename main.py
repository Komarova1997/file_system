'''
Developers:
Baidalakova B.
Komarova E.
'''
import os
import os.path
import ru_local

def main():
    '''The main program that displays the path to the current directory and menu. Invokes
     the command execution function.'''
    while True:
       print(os.getcwd())
       print(ru_local.MENU)
       command = acceptCommand()
       runCommand(command)
       if command == ru_local.QUIT:
          print(ru_local.END)
          break


def acceptCommand():
    '''Requests the command number and in case the command number is specified incorrectly,
    displays an error message. Command request is carried out
    until the correct command number is entered. Returns the correct command number.'''
    while True:
        command = int(input())
        if command in range(1, 8):
            break
    return command


def runCommand(command):
    '''Determines by the command number "command" what function should be performed.'''
    if command == 1:
        print(catalog())
    if command == 2:
        moveUp()
    if command == 3:
        current = input(ru_local.CURRENT_DIR)
        moveDown(current)
    if command == 4:
        path = os.getcwd()
        print(countFiles(path))
        os.chdir(path)
    if command == 5:
        path = os.getcwd()
        print(countBytes(path))
        os.chdir(path)
    if command == 6:
        target = input(ru_local.INPUT_FILE)
        path = os.getcwd()
        a = findFiles(target, path)
        if a is True:
            print(ru_local.TRUE_FILE)
        else:
            print(ru_local.FALSE_FILE)


def catalog():
    dic_now = os.getcwd()
    return os.listdir(dic_now)


def moveUp():
    '''Makes  the parent directory current directory. Returns the transition to a new directory in a new way.'''
    dic_now = os.getcwd()
    num = dic_now.rfind('\\')
    return os.chdir(dic_now[:num])


def moveDown(current):
    '''Requests a subdirectory name. If the name specified correctly makes the directory in the "current" current,
     otherwise displays an error message.'''
    try:
        dic_now = os.getcwd()
        dic_now = os.path.join(dic_now, current)
        return os.chdir(dic_now)
    except FileNotFoundError:
        print(ru_local.ERROR_DOWN)


def moveDown_1(current):
    '''Auxiliary function'''
    try:
        dic_now = os.getcwd()
        dic_now = os.path.join(dic_now, current)
        return os.chdir(dic_now)
    except FileNotFoundError:
        return


def countFiles(path):
    '''A recursive function that counts the number of files in the specified  directory "path".
    All files in subdirectories are included in the calculation. Returns the number of files.'''
    global counter
    for file in catalog():
        if os.path.isfile(path + '\\' + file):
            counter += 1
        if os.path.isdir(path + '\\' + file):
            moveDown_1(file)
            countFiles(path + '\\' + file)
    return counter


def countBytes(path):
    '''A recursive function that counts the total amount (in bytes) of all files in the specified "path" directory.
    All files in subdirectories are included in the calculation. Returns the total number of bytes.'''
    global bytes
    for file in catalog():
        if os.path.isfile(path + '\\' + file):
            bytes += os.path.getsize(path + '\\' + file)
        if os.path.isdir(path + '\\' + file):
            moveDown_1(file)
            countBytes(path + '\\' + file)
    return bytes


def findFiles(target, path):
    '''A recursive function that generates a list of paths to files whose name contains the "target".
     All subdirectories of the path directory are included in the search. If no files were found,
    displays the appropriate message.'''
        if target in catalog():
        return True
    for file in catalog():
        if os.path.isdir(path + '\\' + file):
            moveDown_1(file)
            findFiles(os.getcwd(), target)


# Additional block
counter = 0
bytes = 0

if __name__ == '__main__':
    main()

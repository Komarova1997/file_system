'''
Developers:
Baidalakova B.
Komarova E.
'''
import os
import os.path
import ru_local

def main():
    '''The main program that displays the path to the current directory and menu. Invokes the command execution function.'''
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
    if command == 5:
        path = os.getcwd()
        bytes = 0
        print(countBytes(path, bytes))
    if command == 6:
        path = os.getcwd()
        print(findFiles(target, path))


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


def countFiles(path):
    '''A recursive function that counts the number of files in the specified  directory "path".
    All files in subdirectories are included in the calculation. Returns the number of files.'''
    count = 0
    for root, dirs, files in os.walk(path):
        for i in files:
            count += 1
    return count
def countBytes(path, bytes):
    '''A recursive function that counts the total amount (in bytes) of all files in the specified "path" directory.
    All files in subdirectories are included in the calculation. Returns the total number of bytes.'''
    os.chdir(path)
    main_list = os.listdir(path)
    for i in main_list:
        if os.path.isfile(path + '\\' + i):
            bytes += os.path.getsize(path + '\\' + i)
        if os.path.isdir(path + '\\' + i):
            countBytes(path + '\\' + i, bytes)
    return bytes


def findFiles(target, path):
    '''A recursive function that generates a list of paths to files whose name contains the "target".
     All subdirectories of the path directory are included in the search. If no files were found,
    displays the appropriate message.'''

if __name__ == '__main__':
    main()
    

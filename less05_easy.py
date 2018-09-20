import os, sys, shutil

#easy
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dir(dir_name, dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))
    print('Директория {} создана'.format(dir_name))


def remove_dir(dir_name, dir_path):
    os.rmdir(dir_path)
    print('Директория {} удалена'.format(dir_name))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dir():
    folder = []
    for i in os.walk(os.getcwd()):
        folder.append(i)
    for value in folder[0][1]:
        print(value)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_curr_dir():
    start_file = sys.argv[0]
    copy_file = os.path.splitext(start_file)[0] + '_copy.py'
    shutil.copyfile(start_file,copy_file)


if __name__ == '__main__':
    print("Задание 1.1")
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        dir_path = os.path.join(os.getcwd(), dir_name)
        make_dir(dir_name, dir_path)
        remove_dir(dir_name, dir_path)
    print("Задание 1.2")
    show_dir()
    print("Задание 1.3")
    copy_curr_dir()



import os
from re import findall


def task1():
    # в папке test найти все файлы filenames вывести колличество
    root = "test"
    count = 0
    for dirs, folders, files in os.walk((root)):
        count += len(files)
    print(count)
    return count


def task2():
    # в папке test найти все email адреса записанные в файлы
    root = "test"
    pattern = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    result = {}
    for dirs, folders, files in os.walk((root)):
        for name_file in files:
            with open(f"{dirs}/{name_file}", "r", encoding="utf-8") as file:
                data = file.read()
                emails = list(findall(pattern, data))
                if emails:
                    print(f"{name_file}) - {emails}")
                    result[f"{name_file}"] = emails
    return result


def main():
    task1()
    print("-------------")
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()

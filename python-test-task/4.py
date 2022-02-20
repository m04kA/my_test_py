from sys import argv
import json


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    data = data['game']
    count = 0
    for el in data['rounds']:
        count += len(el['questions'])
    print(count)


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    data = data['game']
    for el in data['rounds']:
        for quest in el['questions']:
            print(quest['correct_answer'])


def print_max_answer_time(data: dict):
    """
    Тут было не совсем ясно, какие именно данные у нас будут.
    По-этому в дальнейшем можно добавить валидацию, проверки и т.д.
    """
    # вывести максимальное время ответа (time_to_answer)
    data = data['game']
    max_time_answer = 0
    for el in data['rounds']:
        if el['settings']['time_to_answer'] >= max_time_answer:
            max_time_answer = el['settings']['time_to_answer']
        for quest in el['questions']:
            list_keys = list(quest.keys())
            if 'time_to_answer' in list_keys:
                if quest['time_to_answer'] >= max_time_answer:
                    max_time_answer = quest['time_to_answer']
    print(max_time_answer)


def main(args):
    try:
        with open(args, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Вы ввели неправильное название файла.")
        exit(-1)
    except json.decoder.JSONDecodeError:
        print("Содержимое файла не соответствует структуре json")
        exit(-1)
    except Exception as ex:
        print(ex)
        exit(-1)
    count_questions(data)
    print('----------------------')
    print_right_answers(data)
    print('----------------------')
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    # try:
    #     script_name, file_name = argv
    # except Exception as ex:
    #     print("Вы ввели неправильные данные")
    #     exit(-1)

    file_name = 'test.json'
    main(file_name)

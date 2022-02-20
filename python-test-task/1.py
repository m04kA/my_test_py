def black_box(page: int):
    true_page = 7922400
    if page <= true_page:
        return True
    else:
        return False


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.

    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_box) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.

    Уточнение:
        black_box возвращает True, если страница последняя
                  возвращает False, если страница не последняя.


    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    # тут явно нужен алгоритм
    start = 1
    end = 10000000
    step = end // 2
    while end - start > 2 and step != 1:
        if black_box(start + step):
            start += step
        else:
            end = start + step
        step //= 2
    for num in range(start, end + 1):
        if not black_box(num):
            print(num - 1)
            break


if __name__ == '__main__':
    main()

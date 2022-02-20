import asyncio
import random
from pprint import pprint
from typing import List
import time


# Разделяемое между запросами состояние сервера
class SharedState:
    items: List[int]

    def __init__(self):
        self.items = []

    # функция, модифицирующая состояние сервера
    # asyncio.sleep используется для имитации долгой работы функции
    async def modify(self, value: int, first=True):
        if first:
            await asyncio.sleep(random.randint(1, 2))
        if len(self.items) == 0 and value == 0:
            self.items.append(value)
        else:
            if len(self.items) != 0:
                if value - self.items[-1] == 1:
                    self.items.append(value)
                else:
                    await asyncio.sleep(0.01)
                    await self.modify(value, first=False)
            else:
                await asyncio.sleep(0.01)
                await self.modify(value, first=False)
        # print(f"m done: {value}")


# Имитация сервера, обрабатывающего запросы
# В нашем случае "запросы" модифицируют состояние сервера
# добавляя элементы в конец списка 'items'
class Server:
    state: SharedState

    def __init__(self, state: SharedState):
        self.state = state

    async def handle_request(self, value: int):
        stat = time.time()
        await self.state.modify(value)
        print(f"H: {value} is finish for {time.time() - stat:.3f}")


async def main():
    state = SharedState()
    server = Server(state)

    # имитируем запуск 10 запросов к серверу
    requests = [server.handle_request(value) for value in range(10)]
    await asyncio.gather(*requests)

    '''
    !!! В данной задаче нельзя модифицировать код - только добавлять новый !!!
    
    задача заключается в том, чтобы только средствами asyncio
    заставить запросы работать последовательно (исключить data race)
    state в результате обработки запросов должен удовлетворять следующему условию:
    '''

    print("-------------------")

    print(state.items == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    for item in state.items:
        print(item)


if __name__ == '__main__':
    asyncio.run(main())

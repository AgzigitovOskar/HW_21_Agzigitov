from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import BaseError

shop = Shop(
    items={
        'смартфон': 3,
        'ноутбук': 15,
        'наушники': 1,
        'игрушки': 2,
        'кепка': 1,
    },
)

store = Store(
    items={
        'смартфон': 10,
        'ноутбук': 20,
        'компьютер': 1,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():

    while True:
        # TODO: Вывести содержимое складов.
        for storage_name in storages:
            print(f'{storage_name} хранятся: {storages[storage_name].get_items()}')

        # TODO: Запросить у пользователя строку.
        user_input = input(
            'Введите строку в формате:\nДоставить 3 ноутбук из склад в магазин.\n' 
            'Введите "stop" или "стоп", что бы продолжить:\n',
        )

        if user_input in ('stop', 'стоп'):
            break

        # TODO: Обработать строку, проверить на ошибки, определить товар, количество, точки отправления и назначения.
        try:
            request = Request(request_str=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        couier = Courier(request=request, storages=storages)
        try:
            # TODO: Доставить товар.
            couier.move()
        except BaseError as error:
            couier.cancel()
            print(error.message)


if __name__ == '__main__':
    main()
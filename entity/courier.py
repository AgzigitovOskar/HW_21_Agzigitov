from typing import Dict, Type

from entity.abstract_storage import AbstractStorage
from entity.request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.__from = storages[self.__request.departure]
        self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove(name=self.__request.product, amount=self.__request.amout)
        print(f'Курьер забрал {self.__request.amout} {self.__request.product} из {self.__request.departure}')

        print(f'Курьер везет {self.__request.amout} {self.__request.product}')

        self.__to.add(name=self.__request.product, amount=self.__request.amout)
        print(f'Курьер доставил {self.__request.amout} {self.__request.product}')

    def cancel(self):
        ...


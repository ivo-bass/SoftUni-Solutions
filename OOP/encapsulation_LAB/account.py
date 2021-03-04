class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def __is_wrong_pin(self, pin):
        if not pin == self.__pin:
            return 'Wrong pin'

    def get_id(self, pin):
        validation = self.__is_wrong_pin(pin)
        if validation:
            return validation
        return self.__id

    def change_pin(self, old_pin, new_pin):
        validation = self.__is_wrong_pin(old_pin)
        if validation:
            return validation
        self.__pin = new_pin
        return 'Pin changed'

#
# account = Account(8827312, 100, 3421)
# print(account.get_id(1111))
# print(account.get_id(3421))
# print(account.balance)
# print(account.change_pin(2212, 4321))
# print(account.change_pin(3421, 1234))

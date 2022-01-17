"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
"""
Продолжить работу над первым заданием. Разработать методы, 
отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру, например словарь.
"""
"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый 
тип данных.
"""


def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print("Have not so much of technics")
        except KeyError:
            print("Have not what are you want")
    return wrapper


class Storage:
    """
    equipment_units include
    equipment_units = {
    "equipment_type": {
    "name": {
    "model": {
    "count": ""
    }
    }
    }
    }
    """
    equipment_units = {}

    @classmethod
    @validate
    def storage_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.equipment_units[unit_type][unit_name][unit_model]["count"] += unit_count

    @classmethod
    @validate
    def storage_from(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.equipment_units[unit_type][unit_name][unit_model]["count"]
        if current_count < unit_count:
            raise ValueError
        else:
            cls.equipment_units[unit_type][unit_name][unit_model]["count"] -= unit_count

    @staticmethod
    def get_all_equipment():
        for key, value in Storage.equipment_units.items():
            print(key, value)


class Equipment:
    def __init__(self, name, model, eq_type, count=0):
        self.name = name
        self.model = model
        self.eq_type = eq_type
        try:
            if type(count) not in int:
                self.__count = 0
                raise TypeError
        except TypeError:
            print("Wrong data input!!!!")
        else:
            self.__count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):
        equipment_storage_info = Storage.equipment_units.get(self.eq_type, {})
        if self.name in equipment_storage_info.keys():
            equipment_storage_info_by_name = equipment_storage_info[self.name]
            if self.model in equipment_storage_info_by_name.keys():
                equipment_storage_info_by_model = equipment_storage_info_by_name[self.model]
                equipment_storage_info_by_model["count"] += self.__count
            else:
                equipment_storage_info_by_name[self.model] = {"count": self.__count}
        else:
            equipment_storage_info[self.name] = {
                self.model: {"count": self.__count}
            }

        Storage.equipment_units[self.eq_type] = equipment_storage_info


class Printer(Equipment):
    def __init__(self, name, model, count, network):
        super().__init__(name, model, "Printer", count)
        self.network = network


class Scanner(Equipment):
    def __init__(self, name, model, count, colors):
        super().__init__(name, model, "Scanner", count)
        self.colors = colors


class Xerox(Equipment):
    def __init__(self, name, model, count, network):
        super().__init__(name, model, "Xerox", count)
        self.network = network


my_printer_1 = Printer('Ricoh', 'MPC2004', 3, 'yes')
my_printer_2 = Printer('Ricoh', 'MPC2003', 2, 'yes')

my_scanner_1 = Scanner('Sony', '9000', 6, 'no')
my_scanner_2 = Scanner('HP', '456H', 2, 'yes')

my_xerox_1 = Xerox('Xerox', 'R4000', 1, 'yes')


Storage.storage_to(unit_type="Printer", unit_name="Ricoh", unit_model="MPC2004", unit_count=2)
Storage.storage_from(unit_type="Scanner", unit_name="HP", unit_model="456H", unit_count='A')
Storage.get_all_equipment()

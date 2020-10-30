from OfficeEquipFabric import OfficeEquipFabric


class OfficeEquipStorage:
    """
    Класс Склад оргтехники
    """

    def __init__(self, config_base={"printer": [], "scaner": [], "copyer": []}):
        self._storage_base = config_base  # основное хранилище

    def get_cmd(self, val: str):
        """"
        поиск товара по типу
        """
        if val in self._storage_base.keys():
            str_eq = ""
            eq_lst = self._storage_base.get(val)
            for eq in eq_lst:
                str_eq += f"{eq}\n"
            return str_eq
        else:
            if val == "all":
                return f"{self}"
            else:
                return "По запросу ничего не найдено"

    def get_eq_id(self, id: int):
        """
        Поиск товара по id
        :param id:
        :return:
        """
        for k in self._storage_base.keys():
            for eq in self._storage_base[k]:
                if eq.get_id == id:
                    return eq
        return False

    def append_eq(self, equip):
        """
        Приём техники на склад если такого типа техники нет - создать тип в БД
        :param equip:
        :return:
        """
        equip_type = equip.get_eq_data["type"]
        if equip_type in self._storage_base:
            equip_list = self._storage_base[equip_type]
            equip_list.append(equip)
        else:
            self._storage_base = {equip_type: []}
            equip_list = self._storage_base[equip_type]
            equip_list.append(equip)

    def request_storage_EQ(self):
        """
        Пользовательский запрос к складу OfficeEquipStorage
        :return: результат запроса, возможность добавить в корзину
        """
        input_cmd = input("Введите запрос к складу:")
        if input_cmd == "q":
            exit()

        input_cmd = input_cmd.strip(' ').split()
        print(input_cmd)
        if len(input_cmd) > 2:
            print("Ошибка ввода: слишком длинная комманда")
        elif input_cmd[0] == "get":
            if input_cmd[1].isdigit():
                eq = self.get_eq_id(int(input_cmd[1]))
                basket = True
            else:
                eq = self.get_cmd(input_cmd[1])
                basket = False
            return eq, basket
        elif input_cmd[0] == "set":
            type_inp = input("Введите тип устройства (printer,scaner,copyer):")
            type_eq = (type_inp.strip(' ').split())[0]
            if type_eq == "printer" or type_eq == "scaner" or type_eq == "copyer":
                print("OK")
            else:
                return "Ошибка типа устройства", False

            manuf_inp = input("Введите производителя устройства (Xerox,Canon,Hp,...):")
            manuf_eq = (manuf_inp.strip(' ').split())[0]
            print("OK")

            model_inp = input("Введите модель устройства (L800,Phaser,Inkjet,...):")
            model_eq = (model_inp.strip(' ').split())[0]
            print("OK")

            config_dict = {"type": type_eq, "manuf": manuf_eq, "model": model_eq}
            fab = OfficeEquipFabric()
            fab.create_eq(config_dict, self)

            return "Устройство уже а складе! \n", False
        else:
            return "Ошибка ввода комманды \n", False

    def __str__(self):
        view_str = ""
        for k in self._storage_base.keys():
            view_str += f"{k}:\n"
            type_lst = self._storage_base[k]
            for v in type_lst:
                view_str += f"\t{v}\n"

        return view_str

from random import randint
from OfficeEquip import PrinterOE, ScanerOE, CopyMachineOE


class OfficeEquipFabric:
    """
    Класс создаёт оффисную технику
    OfficeEquipFabric obj.create_eq("printer") - создаст принтер
    """
    def __init__(self):
        self._model_eq = [["Epson",["L200","L860","L4160"]], ["Lexmark",["MS621","MS421"]],
                          ["Canon",["MF264","MF112","MF445"]], ["Brother",["HL1202","HL1302"]],
                          ["HP",["Laser 107w","InkTank 115"]],["Xerox",["Phaser 3020","Phaser 3052"]]]

    def create_eq_rnd(self, type_eq: str, storage_eq):
        """
        Метод создает запрашиваемый тип OfficeEquip с рандоными характеристиками
        :param type_eq:
        :return:
        """
        rnd = randint(0,len(self._model_eq)-1)
        manuf = self._model_eq[rnd][0]
        model = self._model_eq[rnd][1]
        model = model[randint(0,len(self._model_eq[rnd])-1)]
        equip = 0
        if type_eq == "printer":
            equip = PrinterOE({"manuf": manuf ,"model":model})
        elif type_eq == "scaner":
            equip = ScanerOE({"manuf": manuf ,"model":model})
        elif type_eq == "copyer":
            equip = CopyMachineOE({"manuf": manuf ,"model":model})

        storage_eq.append_eq(equip)

    def create_eq(self,config_dict,storage_eq):
        if config_dict["type"] == "printer":
            equip = PrinterOE({"manuf":config_dict["manuf"],"model":config_dict["model"]})
        elif config_dict["type"] == "scaner":
            equip = ScanerOE({"manuf":config_dict["manuf"],"model":config_dict["model"]})
        elif config_dict["type"] == "copyer":
            equip = CopyMachineOE({"manuf":config_dict["manuf"],"model":config_dict["model"]})
        else:
            return False

        storage_eq.append_eq(equip)
        return True

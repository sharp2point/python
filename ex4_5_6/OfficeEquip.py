from abc import ABC, abstractmethod
from datetime import datetime


class OfficeEquip(ABC):
    """
    класс Оргтехника
    """

    def __init__(self, config_dict={"manuf": "epson", "model": "l800"}):
        self._config_dict = config_dict
        self._config_dict["data"] = datetime.now()

    @property
    def get_eq_data(self):
        return self._config_dict

    @abstractmethod
    def button_go(self):
        pass

    @property
    def get_id(self):
        pass

    def __str__(self):
        cd = self._config_dict
        return f"id:{cd['id']}.{cd['type']}:\t{cd['manuf']} model: {cd['model']}\t\tdata:{cd['data']}"


class PrinterOE(OfficeEquip):
    """
    класс Принтер
    """
    _id = 0

    def __init__(self, config_dict):
        super().__init__(config_dict)
        PrinterOE._id += 1
        self._config_dict["type"] = "printer"
        self._config_dict["id"] = PrinterOE._id

    @property
    def get_id(self):
        return self._config_dict["id"]

    def _printed(self):
        return "Printed"

    def button_go(self):
        print(f"Printer {self._printed()} id:{self._config_dict['id']}, model:{self._config_dict['manuf']}- PRESSED button GO")


class ScanerOE(OfficeEquip):
    """
    класс Сканер
    """
    _id = 2000

    def __init__(self, config_dict):
        super().__init__(config_dict)
        ScanerOE._id += 1
        self._config_dict["type"] = "scaner"
        self._config_dict["id"] = ScanerOE._id

    @property
    def get_id(self):
        return self._config_dict["id"]

    def _scaned(self):
        return "Scaned"

    def button_go(self):
        print(f"Scaner {self._scaned()} id:{self._config_dict['id']}, model:{self._config_dict['manuf']}- PRESSED button GO")


class CopyMachineOE(OfficeEquip):
    """
    класс Копировальный аппарат
    """
    _id = 1000

    def __init__(self, config_dict):
        super().__init__(config_dict)
        CopyMachineOE._id += 1
        self._scaner = ScanerOE(config_dict)
        self._printer = PrinterOE(config_dict)
        self._config_dict["type"] = "copyer"
        self._config_dict["id"] = CopyMachineOE._id

    @property
    def get_id(self):
        return self._config_dict["id"]

    def _copyed(self):
        return "Copyed"

    def button_go(self):
        print("\033[34m")
        print(f"Copyer {self._copyed()} id:{self._config_dict['id']}, model:{self._config_dict['manuf']} - PRESSED button GO")
        self._scaner.button_go()
        self._printer.button_go()
        print("\033[30m")

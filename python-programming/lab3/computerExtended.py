import time as t
import typing

def performanceLog(func: typing.Callable) -> typing.Callable:
    def wrapper(self, component: str, value: str | int) -> None:
        currentTime: str = t.strftime("%d-%m-%Y %H:%M:%S", t.gmtime())
        oldValue: str | int = 0
        component = component.lower()
        match component:
            case "cpu":
                oldValue = self.cpu
            case "gpu":
                oldValue = self.gpu
            case "ram":
                oldValue = self.ram
            case "storage":
                oldValue = self.storage
            case _:
                raise ValueError("component не определен")
        try:
            func(self, component, value)
        except Exception as e:
            print(f"Exception: {e}")
        else:
            condStr: str = "GB ->" if isinstance(value, int) == True else " ->"
            print(f"{currentTime} Функция: {func.__name__}, Изменение {component}: {oldValue}{condStr} {value}")
    return wrapper

class ComputerExtended:
    __slots__: list[str] = ["_cpu", "_ram", "_storage", "_gpu", "_vram", "_totalMemory", "id"]
    computerCount: int = 0

    def __init__(self, cpu: str, ram: int, storage: int, gpu: str, vram: int) -> None:
        self._cpu: str = cpu
        self._ram: int = ram
        self._storage: int = storage
        self._gpu: str = gpu
        self._vram: int = vram
        self._totalMemory: int = ram + vram
        ComputerExtended.computerCount += 1
        self.id: str = f"PC_{ComputerExtended.computerCount}"

    @property
    def cpu(self) -> str:
        return self._cpu
    
    @cpu.setter
    def cpu(self, value: int) -> None:
        if not isinstance(value, str):
            raise ValueError("CPU должен быть строкой")
        self._cpu = value

    @property
    def ram(self) -> int:
        return self._ram
    
    @ram.setter
    def ram(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("RAM должен быть положительным целым числом")
        self._ram = value
    
    @property
    def storage(self) -> int:
        return self._storage

    @storage.setter
    def storage(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Объем хранилища должен быть положительным целым числом")
        self._storage = value

    @property
    def gpu(self) -> str:
        return self._gpu
    
    @gpu.setter
    def gpu(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("GPU должен быть строкой")
        self._gpu

    @property
    def vram(self) -> int:
        return self._vram
    
    @vram.setter
    def vram(self, value: int) -> None:
        if not isinstance(value, int) and value <= 0:
            raise ValueError("VRAM должен быть положительным целым числом")
        self._vram = value
    
    def totalMemory(self) -> int:
        return self._totalMemory

    @performanceLog
    def upgradeComponent(self, component: str, value: str | int) -> None:
        if not isinstance(component, str):
            raise TypeError("component должен быть строкой")
        match component.lower():
            case "cpu":
                self.cpu = value
            case "gpu":
                self.gpu = value
            case "ram":
                self.ram = value
            case "storage":
                self.storage = value
            case _:
                raise ValueError("component не является ни одной из частей данного компьютера ")
    
    @staticmethod
    def isHighPerformance(computer) -> bool:
        if not isinstance(computer, ComputerExtended):
            raise TypeError("computer должен быть типом класса ComputerExtended")
        return computer.ram > 32 and computer.storage > 1024 and computer.vram > 8
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ComputerExtended):
            raise TypeError("other должен быть типом класса ComputerExtended")
        return self.cpu == other.cpu \
          and self.gpu == other.gpu \
          and self.ram == other.ram \
          and self.storage == other.storage
    
    def __str__(self) -> str:
        return f"Computer {self.id}: CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB, GPU: {self.gpu}"

def main() -> None:
    computer1: ComputerExtended = ComputerExtended("AMD Ryzen 7 7840HS", 16, 1024, "AMD Radeon 780 M", 1040)
    computer1.upgradeComponent("cpu", "Intel I9-12900K")

if __name__ == "__main__":
    main()
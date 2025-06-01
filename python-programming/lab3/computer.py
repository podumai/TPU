class Computer:
    computerCount: int = 0

    def __init__(self, cpu: str, ram: int, gpu: int, storage: int) -> None:
        self.cpu: str = cpu
        self.ram: int = ram
        self.gpu: int = gpu
        self.storage:int = storage
        Computer.computerCount += 1
        self.id: str = f"PC_{Computer.computerCount}"
        setattr(self, f"comp_{Computer.computerCount}", self.id)

    def __str__(self) -> str:
        return f"Computer {self.id}: CPU: {self.cpu}, RAM: {self.ram}GB, GPU RAM: {self.gpu}GB, Storage: {self.storage}GB"
    
    def __lt__(self, other) -> bool:
        return self.ram < other.ram and self.gpu < other.gpu
    
    def __eq__(self, other) -> bool:
        return self.ram == other.ram and self.storage == other.storage
    
    def __mul__(self, value: int):
        return Computer(self.cpu, self.ram * value, self.gpu, self.storage * value)
    
    def __rmul__(self, value: int):
        return self.__mul__(value)

    def __add__(self, other):
        return Computer(
            self.cpu,
            self.ram + other.ram,
            self.gpu + other.gpu,
            self.storage + other.storage
    )
    
    def __getitem__(self, index: int) -> str | int:
        specs: list[str, int] = [self.cpu, self.ram, self.storage, self.id]
        return specs[index]
    
    def __bool__(self) -> bool:
        return self.ram > 0 and self.storage > 0
    
    def __del__(self) -> None:
        Computer.computerCount -= 1
        print(f"Computer {self.id} has been deleted. Remaining computers: {Computer.computerCount}")

    def upgradeRam(self, additionalRam: int) -> None:
        self.ram += additionalRam

def main() -> None:
    computer: Computer = Computer("AMD Ryzen 7 7840HS", 16, 2, 1024)
    print(computer)

if __name__ == "__main__":
    main()
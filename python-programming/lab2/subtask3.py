from timeit import timeit
from typing import Dict

TEST_SIZE: int = 1_000_000
TEST_ITERATIONS: int = 1_000

BASE_TEST_SETUP: str = "from typing import List"
RAND_TEST_SETUP: str = "from typing import List\n" \
                       "from random import randrange"

BASE_TEST_ENV: Dict[str, int] = {"TEST_SIZE": TEST_SIZE}

def subtask3_1() -> None:
    executionTime: float = timeit("testList1: List[int] = []\n"
                                  "for i in range(TEST_SIZE):\n"
                                  "\ttestList1.append(i)",
                                  setup=BASE_TEST_SETUP,
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Creating List[int] with for loop using append: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def subtask3_2() -> None:
    executionTime: float = timeit("testList1 : List[int] = []\n"
                                  "for _ in range(TEST_SIZE):\n"
                                  "\ttestList1.append(randrange(10))",
                                  setup=RAND_TEST_SETUP,
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Creating List[int] with for loop using append(rand): iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def subtask3_3() -> None:
    exectuionTime: float = timeit("testList: List[int] = [i for i in range(TEST_SIZE)]",
                                  setup=BASE_TEST_SETUP,
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print("Creating List[int] using list comprehension [i for i in range(TEST_SIZE)]:\n"
          f"iterations = {TEST_ITERATIONS}; Time: {exectuionTime}")

def subtask3_4() -> None:
    executionTime: float = timeit("testList1: List[int] = [randrange(10) for _ in range(TEST_SIZE)]",
                                  setup=RAND_TEST_SETUP,
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print("Creating List[int] using list comprehension [randrange(10) for _ in range(TEST_SIZE)]"
          f"iterations = {TEST_ITERATIONS}; Time: {executionTime}")

if __name__ == "__main__":
    subtask3_1()
    subtask3_2()
    subtask3_3()
    subtask3_4()
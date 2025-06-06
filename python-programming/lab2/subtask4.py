from typing import Dict
import sys
from timeit import timeit

TEST_SIZE: int = 1_000_000
TEST_ITERATIONS: int = 1_000
BASE_TEST_ENV: Dict[str, int] = {"TEST_SIZE": TEST_SIZE}

def subtask4_1() -> None:
    executionTime: float = timeit("testDict: Dict[Tuple[str, int], int] = dict()\n"
                                  "for i in range(TEST_SIZE):\n"
                                  "\ttestDict[('secret-key', i)] = i",
                                  setup="from typing import Dict, Tuple",
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Creating dict[tuple[str, int], int] using for loop: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def subtask4_2() -> None:
    executionTime: float = timeit("testDict: Dict[Tuple[str, int], int] = {('secret-key', i): i for i in range(TEST_SIZE)}",
                                  setup="from typing import Dict, Tuple",
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Creating dict[tuple[str, int], int] using dict comprehension: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

if __name__ == "__main__":
    subtask4_1()
    subtask4_2()
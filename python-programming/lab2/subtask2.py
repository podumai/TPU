from typing import List
from timeit import timeit

TEST_SIZE: int = 1_000_000
TEST_ITERATIONS: int = 1_000

def subtest2_1() -> None:
    testList1: List[int] = [0 for _ in range(TEST_SIZE)]
    testList2: List[int] = [0 for _ in range(TEST_SIZE)]
    executionTime: float = timeit("for i in range(TEST_SIZE):\n"
                                  "\ttestList1[i] += testList2[i]",
                                  number=TEST_ITERATIONS,
                                  globals={"TEST_SIZE": TEST_SIZE, "testList1": testList1, "testList2": testList2})
    print(f"Indexing for loop: iterations = {TEST_SIZE}; Time: {executionTime}")

def subtest2_2() -> None:
    testList1: List[int] = [0 for _ in range(TEST_SIZE)]
    testList2: List[int] = [0 for _ in range(TEST_SIZE)]
    executionTime: float = timeit("for v1, v2 in zip(testList1, testList2):\n"
                                  "\tv1 += v2",
                                  number=TEST_ITERATIONS,
                                  globals={"TEST_SIZE": TEST_SIZE, "testList1": testList1, "testList2": testList2})
    print(f"Indexing zip loop: iterations = {TEST_SIZE}; Time: {executionTime}")

def subtest2_3() -> None:
    testList1: List[int] = [0 for _ in range(TEST_SIZE)]
    testList2: List[int] = [0 for _ in range(TEST_SIZE)]
    executionTime: float = timeit("for i, testValue2 in enumerate(testList2):\n"
                                  "\ttestList1[i] += testValue2",
                                  number=TEST_ITERATIONS,
                                  globals={"TEST_SIZE": TEST_SIZE, "testList1": testList1, "testList2": testList2})
    print(f"Indexing enumerate loop: iterations = {TEST_SIZE}; Time: {executionTime}")

if __name__ == "__main__":
    subtest2_1()
    subtest2_2()
    subtest2_3()
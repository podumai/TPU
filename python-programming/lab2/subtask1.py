from timeit import timeit
from typing import List, Set, Tuple, Dict
from dataclasses import dataclass
import sys

TEST_SIZE: int = 10_000
TEST_ITERATIONS: int = 1_000
BASE_TEST_ENV: Dict[str, int] = {"TEST_SIZE": TEST_SIZE}

def appendTest1_1() -> None:
    executionTime: float = timeit("for i in range(TEST_SIZE):\n"
                                  "\ttestList.append(i)",
                                  setup="from typing import List\n"
                                         "testList: List[int] = []",
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Append method test for list[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def appendTest1_2() -> None:
    executionTime: float = timeit("testSet: Set[int] = set()\n"
                                  "for i in range(TEST_SIZE):\n"
                                  "\ttestSet.add(i)",
                                  setup="from typing import Set",
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Add method test for set[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def appendTest1_3() -> None:
    executionTime: float = timeit("testDict: Dict[int, int] = dict()\n"
                                  "for i in range(TEST_SIZE):\n"
                                  "\ttestDict[i] = i",
                                  setup="from typing import Dict",
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Insert method test for dict[int, int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def deletionTest2_1() -> None:
    executionTime: float = timeit("testList: List[int] = [i for i in range(TEST_SIZE)]\n"
                                  "for i in range(TEST_SIZE):\n"
                                  "\ttestList.pop()",
                                  setup="from typing import List",
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Pop method test for list[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def deletionTest2_2() -> None:
    executionTime: float = timeit("testSet: Set[int] = {i for i in range(TEST_SIZE)}\n"
                                  "for i in range(TEST_SIZE):\n"
                                 "\ttestSet.remove(i)",
                                 setup="from typing import Set",
                                 number=TEST_ITERATIONS,
                                 globals=BASE_TEST_ENV)
    print(f"Remove method test for set[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def deletionTest2_3() -> None:
    executionTime: float = timeit("testDict: Dict[int, int] = {i: i for i in range(TEST_SIZE)}\n"
                                  "for i in range(TEST_SIZE):\n"
                                  "\tdel testDict[i]",
                                  setup="from typing import Dict",
                                  number=TEST_ITERATIONS,
                                  globals=BASE_TEST_ENV)
    print(f"Removing elements test for dict[int, int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

@dataclass
class Collections:
    list_: List[int]
    tuple_: Tuple[int]
    set_: Set[int]
    dict_: Dict[int, int]

collections: Collections = Collections(
    [i for i in range(TEST_SIZE)],
    tuple(i for i in range(TEST_SIZE)),
    {i for i in range(TEST_SIZE)},
    {i: i for i in range(TEST_SIZE)}
)

TEST_MID_VALUE: int = TEST_SIZE // 2

def searchTest3_1() -> None:
    executionTime: float = timeit(f"temp: bool = {TEST_MID_VALUE} in testList",
                                  number=TEST_ITERATIONS,
                                  globals={"testList": collections.list_})
    print(f"Search in list[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def searchTest3_2() -> None:
    executionTime: float = timeit(f"temp: bool = {TEST_MID_VALUE} in testSet",
                                  number=TEST_ITERATIONS,
                                  globals={"testSet": collections.set_})
    print(f"Search in set[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def searchTest3_3() -> None:
    executionTime: float = timeit(f"temp: bool = {TEST_MID_VALUE} in testDict",
                                  number=TEST_ITERATIONS,
                                  globals={"testDict": collections.dict_})
    print(f"Search in dict[int, int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")
  
def searchTest3_4() -> None:
    executionTime: float = timeit(f"temp: bool = {TEST_MID_VALUE} in testTuple",
                                  number=TEST_ITERATIONS,
                                  globals={"testTuple": collections.tuple_})
    print(f"Search in tuple[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def iterationTest4_1() -> None:
    executionTime: float = timeit("for i in testList:\n"
                                  "\tpass",
                                  number=TEST_ITERATIONS,
                                  globals={"testList": collections.list_})
    print(f"For loop in list[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def iterationTest4_2() -> None:
    executionTime: float = timeit("for i in testSet:\n"
                                  "\tpass",
                                  number=TEST_ITERATIONS,
                                  globals={"testSet": collections.set_})
    print(f"For loop in set[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def iterationTest4_3() -> None:
    executionTime: float = timeit("for i in testTuple:\n"
                                  "\tpass",
                                  number=TEST_ITERATIONS,
                                  globals={"testTuple": collections.tuple_})
    print(f"For loop tuple[int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def iterationTest4_4() -> None:
    executionTime: float = timeit("for i in testDict:\n"
                                  "\tpass",
                                  number=TEST_ITERATIONS,
                                  globals={"testDict": collections.dict_})
    print(f"For loop in dict[int, int]: iterations = {TEST_ITERATIONS}; Time: {executionTime}")

def sizeTest(collection: List[int] | Set[int] | Dict[int, int] | Tuple[int]) -> None:
    collectionMemorySize: int = sys.getsizeof(collection)
    collectionSize: int = len(collection)
    print(f"Information for {type(collection)}{"[int, int]" if isinstance(collection, Dict) else "[int]"}:\n"
          f"\tMemory Size: {collectionMemorySize}\n"
          f"\tSize: {collectionSize}")

if __name__ == "__main__":
    appendTest1_1()
    appendTest1_2()
    appendTest1_3()

    deletionTest2_1()
    deletionTest2_2()
    deletionTest2_3()

    searchTest3_1()
    searchTest3_2()
    searchTest3_3()
    searchTest3_4()

    iterationTest4_1()
    iterationTest4_2()
    iterationTest4_3()
    iterationTest4_4()

    sizeTest(collections.list_)
    sizeTest(collections.set_)
    sizeTest(collections.tuple_)
    sizeTest(collections.dict_)
# Extra works needed to figure out how it works

from typing import TypeVar, Generic, List

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    print(f"A: {tower_a}", end=" ")
    print(f"B: {tower_b}", end=" ")
    print(f"C: {tower_c}")
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)
        print(i)
        print(f"A: {tower_a}", end=" ")
        print(f"B: {tower_b}", end=" ")
        print(f"C: {tower_c}")


if __name__ == "__main__":
    hanoi(tower_a, tower_b, tower_c, num_discs)
    print(f"A: {tower_a}")
    print(f"B: {tower_b}")
    print(f"C: {tower_c}")

# hanoi([1, 2, 3], [], [], 3)
# n != 1 (n == 3)
# hanoi([1, 2, 3], [], [], 2) => hanoi([1, 2, 3], [], [], 1) => [1, 2], [3], []
# hanoi([1, 2], [3], [], 1) => [1], [3, 2], []
# hanoi([], [3, 2], [], 2) =>


# Credit from Real Python
# https://realpython.com/python-thinking-recursively/

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]


# Each function call represents an elf doing his work
def delivery_presents_recursively(houses):
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        delivery_presents_recursively(first_half)
        delivery_presents_recursively(second_half)


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        print(f"{n} x ({n} - 1) = {n * (n - 1)}")
        return n * factorial_recursive(n - 1)


def sum_recursive(current_number, accumulated_sum):
    # Final case for return
    if current_number == 11:
        return accumulated_sum
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)


if __name__ == "__main__":
    # delivery_presents_recursively(houses)
    # print(factorial_recursive(5))
    print(sum_recursive(1, 0))


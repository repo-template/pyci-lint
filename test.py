from random import choices
from string import ascii_letters, digits


def random_string(s: str, n: int) -> str:
    return "".join(choices(s, k=n))


if __name__ == "__main__":
    print(random_string(ascii_letters + digits, 10))

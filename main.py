"""Command-line demo for the Week 7 Gitflow project."""
from src.calculator import add, subtract, multiply, divide


def main() -> None:
    print("=== Week 7: Gitflow Calculator ===")
    a, b = 12, 4
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")


if __name__ == "__main__":
    main()

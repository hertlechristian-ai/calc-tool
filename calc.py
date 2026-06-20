"""Ein kleines Taschenrechner-Modul für erste Schritte."""


def add(a, b):
    """Addiert zwei Zahlen."""
    return a + b


def subtract(a, b):
    """Subtrahiert b von a."""
    return a - b


def multiply(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b


if __name__ == "__main__":
    print("3 + 4 =", add(3, 4))
    print("10 - 6 =", subtract(10, 6))
    print("5 * 5 =", multiply(5, 5))

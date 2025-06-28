def add(x, y):
    return x + y

def divide(x, y):
    return x / y  # Warning: division by zero not handled!

if __name__ == "__main__":
    print(add(5, 3))
    print(divide(10, 0))
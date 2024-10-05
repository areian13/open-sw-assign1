def add(a, b):
    return a + b
def sub(a, b):
    return a - b

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(add(a, b))
    print(sub(a, b))
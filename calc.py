def add(a,b):
    print(__name__)
    return a+b

def sub(a,b):
    print("I am subtracting")
print(__name__)


def main():
    add(3,4)
    sub(3,4)

if __name__ == "__main__":    
    main()
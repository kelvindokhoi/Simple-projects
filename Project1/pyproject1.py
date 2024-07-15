import sys
def calc(a,b):
    c = a*b
    if c<=1000:
        return c
    else:
        return a+b
a = int(input("Input first number:\t"))
b = int(input("Input second number:\t"))
print(f"Your result is: {calc(a,b)}")
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(f"{len(sys.argv)-1} arguments: {sys.argv[1:]}")
    else:
        print("No arguments provided.")
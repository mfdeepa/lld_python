
class Args:
    def __init__(self, *args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)


if __name__ =="__main__":
    ls = ["deepa",35 ,40,50]
    ls1 = {"name": "deepa", "age": 25}
    p = Args(*ls,**ls1)
    print(p)
    print()

def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Alice", age=30)
print(example_function())
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}

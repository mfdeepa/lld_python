try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero")

def write_to_db():
    raise FileExistsError("File error occured")

def create_user(password):
    try:
        print()
        write_to_db()
    except FileExistsError:
        print("File already exists")


def divide10By(num):
    try:
        return 10/num
    except ZeroDivisionError:
        print("Division by zero")

# we should not raise error in any critical section.
def debitAmount(amount):
    try:
        raise RuntimeError
        print("amount debited")
    except RuntimeError:
        print("amount not debited")

def creditAmount(amount):
    print("amount credited")

def start():
    print("diving number by...")
    debitAmount(1)
    creditAmount(1)
    print("payment debited")
    print("payment credited...")

start()

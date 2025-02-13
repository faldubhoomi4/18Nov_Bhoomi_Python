
try:
    a = int(input("Enter First integer value for divison: "))
    b = int(input("Enter second integer value for divison: "))
    c = a / b
    print(f"Divison value is {c}")
except Exception as e:
    print(e)
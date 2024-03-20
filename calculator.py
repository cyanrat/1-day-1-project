def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y == 0:
        return "Don't use zero"
    else:
        return x / y
print("Pilih operasi slur")
print("1.+")
print("2.-")
print("3.-")
print("4./")


while True:
choice = input(":")

if choice in("1", "2", "3", "4"):
     num1 = float(input("Angka Pertama: "))
     num2 = float(input("Angka Kedua: "))
     if choice == '1':
         print(add(num1, num2))
     if choice == '2':
         print(sub(num1, num2))
     if choice == '3':
         print(mul(num1, num2))
     if choice == '4':
         print(div(num1, num2))

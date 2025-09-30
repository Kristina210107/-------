
my_dict = {
    "key" : "value",
    "apple" : "яблоко",
    1 : "один",
}

if my_dict.get("apple", None):
    print(my_dict["apple"])
else:
    print("Ключ не найден")    
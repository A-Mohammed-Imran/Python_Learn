# Dictionary

dic = {"name": "Alice", "age": 30, "city": "New York"}
print(dic["name"])  # Output: Alice
print(dic.get("age"))  # Output: 30
print(dic.get("country", "USA"))  # Output: USA (default value)
print(f"Name: {dic['name']}, Age: {dic['age']}, City: {dic['city']}")
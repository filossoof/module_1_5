immutable_var = tuple(["тип", 0.4, 6.3, "напряжение", "ток"])
print(immutable_var)
immutable_var += (" номер",) # если не ставить запятую, то получится строка а не кортеж
print(immutable_var)

print(immutable_var[2])
# print(immutable_var[2]) = 10  можно получить элемент по индексу, но изменить его нельзя.
# кортеж относится к неизменяемым типам.

mutable_list = ["тип", "напряжение", "ток"]
print(mutable_list)
mutable_list.append(" номер")
print(mutable_list)
print(mutable_list[::-1])
mutable_list.remove("ток")
print(mutable_list)

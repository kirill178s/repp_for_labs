users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

size = len(users)
d = {"Общее количество" : 0, "Уникальные посещения" : 0}
d["Общее количество"] = size

s = set(users)
size2 = len(s)
d["Уникальные посещения"] = size2

print(d)

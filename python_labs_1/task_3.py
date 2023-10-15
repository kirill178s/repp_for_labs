list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

size = len(list_players)
size_for_team = size // 2

first_team = list_players[0:size_for_team:1]
second_team = list_players[size_for_team:size:1]

print(first_team)
print(second_team)

"""
2 способ 
size = len(list_players)

first_team = list_players[0:size:2]
second_team = list_players[1:size:2]

print(first_team)
print(second_team)
"""

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_of_players = len(list_players)

list_first_team = list_players[:int(count_of_players // 2)]
list_second_team = list_players[int(count_of_players // 2):]

# TODO Разделите участников на две команды
print(list_first_team)
print(list_second_team)

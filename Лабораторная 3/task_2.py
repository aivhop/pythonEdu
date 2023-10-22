def find_common_participants(first, second, sep=','):
    first = first.split(sep)
    second = second.split(sep)
    common = list(set(first).intersection(set(second)))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants_common = find_common_participants(participants_first_group, participants_second_group, "|")
print("Common: ", participants_common)

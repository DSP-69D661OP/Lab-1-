# TODO Напишите функцию find_common_participants


def find_common_participants(fist_group, second_group, separator = ','):
    group_one = fist_group.split(separator)
    group_two = second_group.split(separator)

    common_participants = []
    for i in group_one:
        if i in group_two and i not in common_participants:
            common_participants.append(i)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой

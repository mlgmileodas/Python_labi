# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, separator=','):

  first_group_list = participants_first_group.split(separator)
  second_group_list = participants_second_group.split(separator)

  set_first_group = set(first_group_list)
  set_second_group = set(second_group_list)

  common_participants = set_first_group.intersection(set_second_group)
  return list(common_participants)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, ';')
print("Общие участники:", common_participants)
# TODO Провеьте работу функции с разделителем отличным от запятой

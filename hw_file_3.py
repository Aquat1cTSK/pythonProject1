my_dict = {}


def check_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        my_list = []
        i = 0
        for line in file:
            i += 1
            my_list.append(line)
        my_dict[i] = my_list
    return my_dict


def add_at_file(file_name):
    list_keys = list(my_dict.keys())
    list_keys.sort()
    new_dict = {}
    for i in list_keys:
        new_dict[i] = my_dict[i]
    f = open(file_name, 'w', encoding='utf-8')
    for key, values in new_dict.items():
        f.write(str(key))
        f.write('\n')
        for res in values:
            f.write(res)
        f.write('\n')


result_one = check_file('one.txt')
result_two = check_file('two.txt')
result_three = check_file('three.txt')

add_at_file('final.txt')
# print(my_dict)



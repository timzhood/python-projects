# coding=utf-8
"""
Analyse a set of enumerations.
"""
import csv


def main(file_name):
    """
    Read in enums from file.
    :param file_name: the file
    """

    # make a dictionary of lists by enum name
    enums = dict()

    type_prefix = 'TYPE='

    with open(file_name) as in_file:
        lines = in_file.readlines()
        enum_name = None
        for line in lines:
            if line.startswith(type_prefix):
                enum_name = line.split(type_prefix, 1)[1].strip()
                enums[enum_name] = list()
            else:
                enums[enum_name].append(line.strip())

    # make complete master list
    total_set = set()
    for enum in enums.values():
        total_set.update(enum)
    print(total_set)

    # make a sorted list
    total_list = list(total_set)
    total_list.sort()
    print(total_list)

    # expand each of the enum lists
    expanded_enums = dict()

    for enum_name in enums.keys():
        expanded_enums[enum_name] = list()
        for value in enums[enum_name]:
            index = total_list.index(value)
            while index >= len(expanded_enums[enum_name]):
                expanded_enums[enum_name].append('')
            expanded_enums[enum_name][index] = value
        print(expanded_enums[enum_name])

    for enum_name in expanded_enums.keys():
        while len(expanded_enums[enum_name]) < len(total_list):
            expanded_enums[enum_name].append('')

    with open('some.csv', 'wb') as f:
        writer = csv.writer(f)
        header_row = list()
        header_row.append('all')
        for enum_name in sorted(expanded_enums.keys()):
            header_row.append(enum_name)
        writer.writerow(header_row)
        for index in range(len(total_list)):
            row = list()
            row.append(total_list[index])
            for enum_name in sorted(expanded_enums.keys()):
                row.append(expanded_enums[enum_name][index])
            writer.writerow(row)


if __name__ == '__main__':
    main('jim.txt')

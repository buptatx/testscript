#!/usr/bin/env python
#! coding=utf-8


def load_data(filename):
    data_list = []

    with open(filename, "r") as mfilehandle:
        for line in mfilehandle:
            data_list.append(line.strip())

    return data_list


def do_list_compare(firstlist, secondlist):
    common_item_list = []
    first_special_list = []

    for item in firstlist:
        if item in secondlist:
            common_item_list.append(item)
            secondlist.remove(item)
        else:
            first_special_list.append(item)

    second_special_list = secondlist[:]

    print "[common items count]{}".format(len(common_item_list))
    for item in common_item_list:
        print "[in both]{}".format(item)

    print "[first only items count]{}".format(len(first_special_list))
    for item in first_special_list:
        print "[only in first]{}".format(item)

    print "[second only items count]{}".format(len(second_special_list))
    for item in second_special_list:
        print "[only in second]{}".format(item)


def compare(firstfile, secondfile):
    first_content = load_data(firstfile)
    second_content = load_data(secondfile)

    do_list_compare(first_content, second_content)


if __name__ == "__main__":
    compare("./data/zp.txt", "./data/jn.txt")

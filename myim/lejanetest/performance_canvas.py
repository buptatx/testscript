#!/usr/bin/env python
#! coding=utf-8


import numpy as np
import matplotlib.pyplot as plt


def get_content():
    mcontent = []

    with open("./data/popstar.txt", "r") as mhandle:
        for line in mhandle:
            if "popstar" not in line:
                continue
            else:
                mcontent.append(line.strip())

    return mcontent


def draw_performance_canvas(mcontent):
    cpu_perf = []
    vss_perf = []
    rss_perf = []

    for item in mcontent:
        temp_list = item.split(" ")
        while "" in temp_list:
            temp_list.remove("")

        cpu_perf.append(temp_list[2].strip("%"))
        vss_perf.append(temp_list[5].strip("K"))
        rss_perf.append(temp_list[6].strip("K"))

    print vss_perf

    col_num = len(cpu_perf)
    print "column:{}".format(col_num)

    fig, ax = plt.subplots()
    index = np.arange(col_num)
    bar_width = 0.4
    opacity = 0.5

    mem_list = []
    for i in range(col_num):
        mem_list.append("2908464")

    #rect_vss = plt.bar(index, vss_perf, bar_width, alpha=opacity, color='b', label="VSS")
    #rect_rss = plt.bar(index+bar_width, rss_perf, bar_width, alpha=opacity, color='r', label="RSS")
    #rect_mem = plt.bar(index+bar_width*2, mem_list, bar_width, alpha=opacity, color='g', label="mem")
    rect_mem = plt.bar(index, cpu_perf, bar_width, alpha=opacity, color='g', label="mem")
    plt.xlabel("Times")
    #plt.ylabel("KBytes")
    plt.ylabel("%")
    #plt.title("VSS and RSS with time")
    plt.title("CPU with time")
    plt.xticks(index+bar_width, (i for i in range(col_num)))

    #plt.ylim()
    #plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    mcontent = get_content()
    draw_performance_canvas(mcontent)
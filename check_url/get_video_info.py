#! -*- coding:utf-8 -*-


import xlrd


def load_data_from_xlsx(xlsx_name):
    info_list = []
    wb = xlrd.open_workbook(xlsx_name)
    sheet = wb.sheet_by_index(0)
    for idx in range(0, sheet.nrows):
        temp = {}
        temp["id"] = int(sheet.row(idx)[0].value)
        temp["title"] = sheet.row(idx)[1].value.encode('utf-8')
        temp["url"] = sheet.row(idx)[2].value.encode('utf-8')
        info_list.append(temp)

    return info_list


def load_data_from_check_result(result_name):
    result_list = []
    with open(result_name, "rb") as mf:
        for line in mf:
            result_list.append(line.strip())

    return result_list


def get_video_info(xlsx_name, result_name):
    check_result_list = load_data_from_check_result(result_name)
    xlsx_list = load_data_from_xlsx(xlsx_name)

    for item in check_result_list:
        for srow in xlsx_list:
            if item == srow["url"]:
                print("{} {} {}".format(srow["id"], srow["title"], srow["url"]))
                break


if __name__ == "__main__":
    get_video_info("./data/myzj.xlsx", "./data/check_result.txt")

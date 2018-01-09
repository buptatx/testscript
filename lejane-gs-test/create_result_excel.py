#! -*- coding:utf-8 -*-

import os
import xlwt


class createResultExcel():
    def __init__(self, path):
        self.result_path = path

    def getRelativeLogs(self):
        return os.listdir(self.result_path)

    def getServiceName(self, logname):
        if "da" in logname:
            service_name = u"档案"
        elif "dhys" in logname:
            service_name = u"电话医生"
        elif "gh" in logname:
            service_name = u"挂号"
        elif "jh" in logname:
            service_name = u"急症救护"
        elif "jy" in logname:
            service_name = u"境外就医"
        elif "pg" in logname:
            service_name = u"健康风险评估"
        elif "wz" in logname:
            service_name = u"电话轻问诊"
        elif "zc" in logname:
            service_name = u"健康自测"
        elif "zj" in logname:
            service_name = u"找专家"
        elif "jlcx" in logname:
            service_name = u"服务历史查询"
        else:
            service_name = u"其他"

        return service_name

    def createExcel(self):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("result", cell_overwrite_ok=True)
        sheet.write(0, 0, u"ServiceName")
        sheet.write(0, 1, u"验证服务开通状态平均耗时（ms）")
        sheet.write(0, 2, u"获取服务URL平均耗时（ms）")
        sheet.write(0, 3, u"加载URL平均耗时（ms）")
        sheet.write(0, 4, u"总耗时平均值（ms")

        current_row = 1

        for log in self.getRelativeLogs():
            with open("./result/" + log, "r") as mResult:
                service_name = self.getServiceName(log)
                sheet.write(current_row, 0, service_name)

                current_line = 1
                for line in mResult:
                    sheet.write(current_row, current_line, line.split("] ")[1])
                    current_line += 1

            current_row += 1

        workbook.save('./result.xlsx')

if __name__ == "__main__":
    creator = createResultExcel("./result")
    creator.createExcel()
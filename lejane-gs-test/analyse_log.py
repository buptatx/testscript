#! -*- coding=utf-8 -*-

import sys


class AnalyseLog():
    def __init__(self, path):
        self.checkServiceStatusCost = []
        self.getServiceUrlCost = []
        self.loadUrlCost = []
        self.logpath = path

    def getContent(self):
        log_data_list = []
        with open(self.logpath, "rb") as myfile:
            for line in myfile:
                if "PRETTYLOGGER-GsService:" in line and "--timecost" in line:
                    log_data_list.append(line.strip())

        return log_data_list

    def outputResult(self, avgCSSC, avgGSUC, avgLUC):
        content_list = []
        content_list.append("[avgCSSC] {}\r\n".format(avgCSSC))
        content_list.append("[avgGSUC] {}\r\n".format(avgGSUC))
        content_list.append("[avgLUC] {}\r\n".format(avgLUC))
        content_list.append("[totalC] {}\r\n".format(avgCSSC + avgGSUC + avgLUC))

        print self.logpath
        output_filename = "./result/" + self.logpath.split("/")[2]
        print output_filename
        with open(output_filename, "wb+") as mResult:
            mResult.write("".join(content_list))

    def data_fliter(self):
        log_data_list = self.getContent()

        for item in log_data_list:
            if "loadUrl" in item:
                print "[LU]" + item
                self.loadUrlCost.append(int(item.split("timecost ")[1]))
            elif "getServiceUrl" in item:
                print "[GSU]" + item
                self.getServiceUrlCost.append(int(item.split("timecost ")[1]))
            else:
                print "[CSSC]" + item
                self.checkServiceStatusCost.append(int(item.split("timecost ")[1]))

    def cel_timecost(self):
        self.data_fliter()

        if len(self.checkServiceStatusCost) != 0:
            tolCSSC = sum(self.checkServiceStatusCost)
            avgCSSC = float(tolCSSC) / len(self.checkServiceStatusCost)
            print "[avgCSSC] {}".format(avgCSSC)
        else:
            avgCSSC = 0

        if len(self.getServiceUrlCost) != 0:
            tolGSUC = sum(self.getServiceUrlCost)
            avgGSUC = float(tolGSUC) / len(self.getServiceUrlCost)
            print "[avgGSUC] {}".format(avgGSUC)

        if len(self.loadUrlCost) != 0:
            tolLUC = sum(self.loadUrlCost)
            avgLUC = float(tolLUC) / len(self.loadUrlCost)
            print "[avgLUC] {}".format(avgLUC)

        print "[totalC] {}".format(avgCSSC + avgGSUC + avgLUC)
        self.outputResult(avgCSSC, avgGSUC, avgLUC)

if __name__ == "__main__":
    test = AnalyseLog(sys.argv[1])
    test.cel_timecost()

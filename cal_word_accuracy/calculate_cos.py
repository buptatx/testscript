import math
import time

from jieba import posseg


def simicos(str1, str2):
    cut_str1 = [w for w, t in posseg.lcut(str1) if t != 'x']
    cut_str2 = [w for w, t in posseg.lcut(str2) if t != 'x']
    if cut_str1 != [] and cut_str2 != []:
        all_words = set(cut_str1 + cut_str2)
        freq_str1 = [cut_str1.count(x) for x in all_words]
        freq_str2 = [cut_str2.count(x) for x in all_words]
        sum_all = sum(map(lambda z, y: z * y, freq_str1, freq_str2))
        sqrt_str1 = math.sqrt(sum(x ** 2 for x in freq_str1))
        sqrt_str2 = math.sqrt(sum(x ** 2 for x in freq_str2))
        return sum_all / (sqrt_str1 * sqrt_str2)
    else:
        return 0


def main():
    with open("test.txt", "r") as f:
        f = [ele.strip() for ele in f.readlines() if ele.split()]
    rows = len(f)
    start = time.time()
    for n in range(0,rows):
        sentence = f[n].strip()
        for line in f:
            if line != sentence:
                similarity = simicos(sentence, line)
                if similarity > 0.6:
                    print("{}#{}#{}".format(sentence,line,similarity))
            else:
                pass
    end = time.time()
    print("耗时: %.3fs" % (end - start))


if __name__ == '__main__':
    main()
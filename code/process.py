import re
'''
判断字符串是否含有数字
'''
pun = '[,.—!\']'

def check_contain_digit(check_str):
    for ch in check_str:
        if ch.isdigit():
            return True
    return False
'''
现将停用词读取到列表中
'''
def readStop():
    '''
    :return: list
    '''
    f = open("../data/stop.txt",encoding = 'utf-8')
    stopWords = []
    line = f.readline()
    while line:
        stopWords = stopWords + line.split(" ")
        line = f.readline()
    f.close()

    return stopWords

def processData():
    '''
    :return:
    '''
    f = open("../data/news.txt",encoding = 'utf-8')

    stopWords = readStop()
    line = f.readline()
    resWords = []
    N = 0
    while line:
        N = N+1
        print("--"+str(N))
        line = line.replace("\n","") #去掉换行符
        line = re.sub(pun,'',line) #去掉敏感字符
        lineWords = line.split(" ")
        #删除列表中的空值
        while '' in lineWords:
            lineWords.remove('')

        #去除这一行的停用词
        bug = []
        for i in range(len(lineWords)):

            lineWords[i] = lineWords[i].lower()
            lineWords[i] = re.sub("[“”?;:()]", "", lineWords[i])

            if lineWords[i] in stopWords:
                bug.append(lineWords[i])
            if check_contain_digit(lineWords[i]):
                bug.append(lineWords[i])

        for b in bug:
            lineWords.remove(b)

        #将去除后的停用词写到文件里
        words = " ".join(str(word) for word in lineWords)
        resWords.append(words)
        line = f.readline()
        print("--")
    f.close()
    p = open("../data/process.txt", "w+",encoding='utf-8')
    n= 0
    for line in resWords:
        n=n+1
        print("=="+str(n))
        if line != '\n':
          p.write(line+"\n")
    p.close()

#从处理好的新闻数据集中抽取数据字典
def getDict():
    dict = []
    p = open("../data/process.txt",encoding='utf-8')
    line = p.readline()
    N = 0
    while line:
        N=N+1
        print("=="+str(N))
        line = line.replace("\n","")
        words = line.split(" ")
        for w in words:
            if w not in dict:
                dict.append(w)
        line = p.readline()

    p = open("../data/dict.txt","w+", encoding='utf-8')
    words = "\n".join(str(d) for d in dict)
    print(words)
    p.write(words)
    p.close()

if __name__ == '__main__':
   processData()
   getDict()




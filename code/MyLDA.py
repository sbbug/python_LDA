import numpy as np
import random as rand
#统计文档个数,以及每个文档中所含单词个数
def countDocs():
    file_path= "../data/process.txt"
    f = open(file_path,"r+",encoding="utf-8")
    n = 0;

    doc_n = []

    line = f.readline()
    while line:
        n=n+1
        words = line.split(" ")
        doc_n.append(len(words))
        line = f.readline()

    return n,doc_n

#生成一个文档矩阵
def getDocMat():
    '''
    :param k:
    :return:
    '''
    N,doc_n = countDocs()
    doc_mat = []

    for i in range(len(doc_n)):
           temp = []
           for j in range(doc_n[i]):
               #初始值是1
               temp.append(1)
           doc_mat.append(temp)

    return doc_mat

def sampling(i,j):

    pass
#建立单词数据字典
def getDict():
    file_path = "../data/dict.txt"

    f = open(file_path, "r+", encoding="utf-8")

    line = f.readline()
    dicts = []
    while line:
        word = line.split("\n")[0]
        dicts.append(word)
        line = f.readline()

    return dicts

#寻找某个单词在字典中位置
def getIndex(value,dict):
    n = -1
    for i in range(len(dict)):
        if value==dict[i]:
            n = i
            break

    return n

def getDocVec():

    docs_word_mat = getDocMat()
    dicts = getDict()

    file_path = "../data/process.txt"
    f = open(file_path, "r+", encoding="utf-8")
    i=0
    j=0

    line = f.readline()
    while line:
        words = line.split(" ")
        for w in words:
            index = getIndex(w,dicts)
            docs_word_mat[i][j] = index
            j = j+1
        j=0
        i=i+1
        line = f.readline()

    return docs_word_mat

#为文档单词随机分配主题，初始化主题分布
def initDocK(doc_mat,k):
    '''
    :param doc_mat:
    :param k:
    :return:
    '''
    for i in range(len(doc_mat)):
        for j in range(len(doc_mat[i])):
            doc_mat[i][j] = rand.randint(0,k)

    return doc_mat

if __name__ == "__main__":

    print(getDocMat()[0])


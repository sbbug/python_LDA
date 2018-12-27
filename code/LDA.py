from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

#读取新闻数据到列表
def readNews():

    new_lists = []
    news_path = "../data/news.txt"

    f = open(news_path,'r',encoding='utf-8')
    line = f.readline()
    N = 0
    while line:
        N = N+1
        if line!='\n':
            new_lists.append(line)
        print("===="+str(N))
        line = f.readline()

    return new_lists

#获取停用词
def readStop():
    stop_path = "../data/stop.txt"

    sf = open(stop_path, 'r',encoding='utf-8')
    sc = sf.readline()
    # 将停用词表转换为list
    stpwrdlst = sc.split(" ")
    sf.close()

    return stpwrdlst

def roundMat(matrix):

    row,col = matrix.shape
    for i in range(row):
        for j in range(col):
            matrix[i][j] = round(matrix[i][j],2)

    return matrix

if __name__ == "__main__":

    #读取新闻到列表中
    new_list = readNews()

    #将停用词读到列表中
    stop_list = readStop()

    #获取停用词向量
    stopVec = CountVectorizer(stop_words=stop_list)

    new_tf = stopVec.fit_transform(new_list)

    print(new_tf)

    print("LDA模型开始------")
    LDA = LatentDirichletAllocation(n_components=10,
                                    learning_offset=50.,
                                    random_state=0)
    docres = LDA.fit_transform(new_tf)

    #对小数点截取
    ress = roundMat(docres)
    print(ress)
    print("-----------------------------")
    resss = LDA.components_
    resss = roundMat(resss)
    print(resss)
    #print(LDA.components_)
    # print(readStop())

    #CountVectorizer(stop_words=stpwrdlst)

    # corpus = [res1, res2, res3]
    # cntVector = CountVectorizer(stop_words=stpwrdlst)
    # cntTf = cntVector.fit_transform(corpus)




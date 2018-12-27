# f = open("../data/news.txt",encoding = 'utf-8')
#
#
# lines = f.readlines(10)
#
# for line in lines:
#     res = line.split(" ")
#     print(res)
#
#
# f.close()
# def check_contain_digit(check_str):
#     for ch in check_str:
#         if ch.isdigit():
#             return True
#     return False
#
# print(check_contain_digit("afsf"))
import numpy as np
# a = [
#     [0.1223,0.35456],
#     [0.354,0.2325,1323424],
#     [0.354,0.2325]
# ]
# print(len(a))
# import re
# def getDocVec():
#
#     file_path = "../data/test1.txt"
#     f = open(file_path, "r+", encoding="utf-8")
#     lists = []
#     i=0
#     j=0
#
#     line = f.readline()
#     while line:
#         words = line.split("\n")
#         w = words[0]
#         if w!='':
#             w = re.sub("[’s“”?;:()]", "",w)
#             w = w.replace("’s","")
#             # w = w.replace("“","")
#             # w = w.replace("”", "")
#             # w = w.replace("?","")
#             # w = w.replace(";","")
#             # w = w.replace(":","")
#             # w = w.replace("(", "")
#             # w = w.replace(")", "")
#             lists.append(w)
#         line = f.readline()
#
#     print(lists)
#
# if __name__ =="__main__":
#     getDocVec()
# import random
# def rowAddb(row, b):
#     res = []
#     for r in row:
#         res.append(r + b)
#
#     return res
# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# a=[1,2,3]
# # print(random.sample(1,2,0.6))
# print(type(a))
# print(isinstance(a,list))
f = open("../data/test2.txt","r+",encoding="utf-8")

line = f.readline()

while line:
    line = line.replace('\n','')
    words = line.split(" ")
    print(words)
    line = f.readline()
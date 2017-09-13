# Author:Mr

# 最好自己
result=["one","two",'three',['1',2,3,4],2,3,4,5]
# list.append(result,6)
# result.pop()
# print(result)
def eat(testt):
    for i in range(0,8):
        testt.pop(0)
        i-=1
        print(testt)

eat(result)
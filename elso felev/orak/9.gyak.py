# import random as r
#
# s=set()
# s2=set()
#
# n=int(input())
#
# while len(s)!=n:
#     x=r.randint(1,10)
#     s.add(x)
#
# while len(s2)!=n:
#     x = r.randint(1, 10)
#     s2.add(x)
#
# print("s={0}, s2={1}".format(s,s2))
# print(s|s2)
# print(s&s2)
# print(s-s2)
# print(s^s2)

# eloford={}
#
# while True:
#     s=input("Add meg a szót: ")
#     if s=="":
#         break
#     if s in eloford.keys():
#         eloford[s]+=1
#     else:
#         eloford[s]=1
#         #eloford.update[(s : 1)]
# for kulcs, ertek in eloford.items():
#     print("{0} : {1}".format(kulcs, ertek))

def ossz_pontok(x:tuple, y:tuple):
    return (x[0]+y[0], x[1]+y[1])

def ossz_szamok(x,y):
    return x+y

def ossz(fgv, x,y):
    return fgv(x,y)

def main():
    print(ossz(ossz_pontok,(1,2),(2,5)))
    print(ossz(ossz_szamok(2,5)))

if __name__=="__main__":
    main()
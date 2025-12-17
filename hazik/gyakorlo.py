import sys


# 1. ppt
# def faktorialis(n:int)->int:
#     if n==1:
#         return 1
#     else:
#         return n*faktorialis(n-1)
#
# def main():
#     n=int(input())
#     fakt=faktorialis(n)
#     print(fakt)
#
# if __name__=="__main__":
#     main()

# import math
# def hatvany(n:int,x:int)->int:
#     if n==1:
#         return x
#     else:
#         return x*hatvany(x,n-1)
# def main():
#     x=int(input("x= "))
#     n=int(input("n= "))
#     print(hatvany(n,x))
#
# if __name__=="__main__":
#     main()

# def osszeg(n:int)->int:
#     if n==1:
#         return 1
#     else:
#         return n+osszeg(n-1)
#
# def main():
#     n=int(input("n= "))
#     print(osszeg(n))
#
# if __name__=="__main__":
#     main()

# def negyzetosszeg(n=int)->int:
#     if n==1:
#         return 1
#     else:
#         return n*n+negyzetosszeg(n-1)
#
# def main():
#     n=int(input("n= "))
#     print(negyzetosszeg(n))
#
# if __name__=="__main__":
#     main()

# def x(n:int, i:int)->int:
#     if i==n:
#         return n*n-2
#     else:
#         return i*i-2+x(n,i+1)
#
# def main():
#     n=int(input("n= "))
#     print(x(n,1))
#
# if __name__=="__main__":
#     main()
# ures={}
# ures["kaposzta"]=2
# print(ures)
# bevasarlolista = {
#     "alma": 2,
#     "körte": 1,
#     "barack": 5,
#     }
# print(bevasarlolista)
#
# for i in bevasarlolista:
#     ertek = bevasarlolista[i]
#     print(i, ertek)
#
# for ertek in bevasarlolista.values():
#     print(ertek)
# print("Összesen:", sum(bevasarlolista.values()))
#
# for kulcs, ertek in bevasarlolista.items():
#     print(f"{kulcs}: {ertek} kg")

# d={}
# szo=input()
# while szo!="":
#     if szo in d:
#         d[szo]=d[szo]+1
#     else:
#         d[szo]=1
#     szo=input()
#
# for kulcs, ertek in d.items():
#     print("{0} : {1}".format(kulcs,ertek))

# import sys
# majmok={}
# for line in sys.stdin:
#     sor=line
#     s=sor.split(";")
#     if s[0] in majmok:
#         majmok[s[0]]=majmok[s[0]]+int(s[1])
#     else:
#         majmok[s[0]]=int(s[1])
#
# for kulcs, ertek in sorted(majmok.items()):
#     print("{0} : {1}".format(kulcs,ertek))

# import sys
# def main():
#     egyuttesek={}
#     for line in sys.stdin:
#         sor=line
#         s=sor.split(":")
#         eloadok=s[1].strip().split(",")
#         k=len(eloadok)
#         for i in range(k):
#             if eloadok[i] in egyuttesek:
#                 egyuttesek[eloadok[i]]+=1
#             else:
#                 egyuttesek[eloadok[i]] =1
#
#     for kulcs, ertek in sorted(egyuttesek.items()):
#         print("{0} : {1}".format(kulcs,ertek))
# if __name__=="__main__":
#     main()

# import sys
# sportolok={}
# def main():
#     n=int(input("n= "))
#     for line in sys.stdin:
#         s=line.split(":")
#         nevek=s[1].strip().split(",")
#         for i in range(len(nevek)):
#             if nevek[i] in sportolok:
#                 sportolok[nevek[i]]+=1
#             else:
#                 sportolok[nevek[i]]= 1
#     for kulcs, ertek in sorted(sportolok.items(), key=lambda rend:(-rend[1], rend[0])):
#         if ertek>n:
#             print("{0}: {1}".format(kulcs, ertek))
# if __name__=="__main__":
#     main()

# import sys
# gyerekek={}
# for line in sys.stdin:
#     s=line.split(":")
#     gyumolcsok=s[1].strip().split(",")
#     for i in range(len(gyumolcsok)):
#         if gyumolcsok[i] in gyerekek:
#             gyerekek[gyumolcsok[i]]+=1
#         else:
#             gyerekek[gyumolcsok[i]] = 1
#
# for kulcs, ertek in sorted(gyerekek.items(), key=lambda rend:(rend[0])):
#     print("{0}: {1}".format(kulcs,ertek))


# varosok={}
#
# def main():
#     n=int(input("n= "))
#     for i in range(n):
#         s=input().split(":")
#         varosok[s[0]]=int(s[1])
#
#     m=int(input())
#     for i in range(m):
#         b=input().split(":")
#         if varosok[b[0]]> int(b[2]):
#             varosok[b[0]]-=int(b[2])
#             varosok[b[1]]+=int(b[2])
#     for kulcs,ertek in sorted(varosok.items(),key=(lambda rend:(rend[0]))):
#         print("{0}: {1}".format(kulcs,ertek))
#
# if __name__=="__main__":
#     main()

# import sys
#
# n=len(sys.argv)
# szorzat=1
# for i in range(1,n):
#     szorzat=int(sys.argv[i])*szorzat
# print(szorzat)

# import sys
# def count_of_odds()->int:
#     paratlan=0
#     for i in sys.argv[1:]:
#         if int(i)%2!=0:
#             paratlan+=1
#     return paratlan
# def main():
#     print(count_of_odds())
# if __name__=="__main__":
#     main()

# import sys
# def count_of_prime()->int:
#     prim=0
#     for i in sys.argv[1:]:
#         if i>0:
#             osztok = 0
#             for k in range(1, int(i) + 1):
#                 if int(i) % k == 0:
#                     osztok += 1
#             if osztok == 2:
#                 prim += 1
#             osztok = 0
#     return prim
#
# def main():
#     print(count_of_prime())
#
# if __name__=="__main__":
#     main()

# import sys
# def lnko(a:int,b:int)->int:
#     while a!=b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
# def main():
#     with open(sys.argv[1]) as file:
#         lista=[]
#         for line in file:
#             s=line.strip("\n").split(" ")
#             if len(s)<2:
#                 lista.append(int(s[0]))
#             else:
#                 oszto=int(s[0])
#                 for i in range(len(s)-1):
#                     oszto=lnko(oszto,int(s[i+1]))
#                 lista.append(oszto)
#     for i in lista:
#         print("{0}".format(i))
#
# if __name__=="__main__":
#     main()

# import sys
#
# def main():
#     varosok={}
#     with open(sys.argv[1]) as file:
#         for line in file:
#             s=line.strip("\n").split(";")
#             if s[0] in varosok:
#                 varosok[s[0]]+=float(s[2])
#             else:
#                 varosok[s[0]] = float(s[2])
#     for kulcs,ertek in sorted(varosok.items(), key=lambda rendezes:(-rendezes[1], rendezes[0])):
#         print(kulcs)
#
# if __name__=="__main__":
#     main()

# import sys
# def count_of_local_maximums()->None:
#     with open(sys.argv[1]) as file:
#         nagyobb=0
#         for line in file:
#             s=line.strip("\n").split(",")
#             if len(s)<3:
#                 print("0")
#             else:
#                 for i in range(1,len(s)-1):
#                     if int(s[i])>int(s[i-1]) and int(s[i])>int(s[i+1]):
#                         nagyobb+=1
#     print(nagyobb)
#
# def main():
#     count_of_local_maximums()
#
# if __name__=="__main__":
#     main()

# import sys
#
# def main():
#     versenyzok={}
#     with open(sys.argv[1]) as file:
#         for line in file:
#             s=line.strip("\n").split(";")
#             if s[0] in versenyzok:
#                 versenyzok[s[0]]+=int(s[2])
#             else:
#                 versenyzok[s[0]] = int(s[2])
#     for kulcs,ertek in sorted(versenyzok.items(),key=lambda rendezes:(-rendezes[1],rendezes[0])):
#         print("{0}".format(kulcs))
#
#
# if __name__=="__main__":
#     main()

# import sys
#
# def prim(x:list):
#     for i in range(len(x)):
#         osztok=0
#         s=set()
#         for k in range(len(x(i))):
#             if x(i) not in s:
#                 if x(i) % k == 2:
#                     s.add(x(i))
#         print(prim,end=" ")
#
# def main():
#     with open(sys.argv[1]) as file:
#         for line in file:
#             primek=[]
#             s=line.strip("\n").split(" ")
#             for i in range(len(s)):
#                 primek.append(int(s[i]))
#     prim(primek)
# if __name__=="__main__":
#     main()

from typing import NamedTuple
import sys
Minion=NamedTuple("Minion",[("name",str), ("hunger", int),("motivation", int),("size",str)])

def spl(line:str)->Minion:
    

    return 1


def main():
    lista=[]
    with open(sys.argv[1]) as file:
        for line in file:
            lista.append(spl(line))
# import math
#
# def pythagorean(a:int, b:int)->int:
#     c=math.sqrt(a**2+b**2)
#     return c
#
# lista=[]
# def main():
#     while True:
#         try:
#             s=input().split()
#             a = float(s[0])
#             b = float(s[1])
#             c=pythagorean(a,b)
#             lista.append(c)
#
#         except EOFError:
#             break
#     for i in lista:
#         print(i)
#
#
# if __name__=="__main__":
#     main()

# import math
# lista=[]
# def pythagorean(a:int, b:int)->int:
#       c=math.sqrt(a**2+b**2)
#       return c
# def main():
#     n=int(input())
#     for i in range(0,n):
#         s = input().split()
#         a = float(s[0])
#         b = float(s[1])
#         c=pythagorean(a,b)
#         lista.append(c)
#     for i in lista:
#         print(i)
#
# if __name__=="__main__":
#     main()


# import math
# lista=[]
# def pythagorean(a:int, b:int)->int:
#       c=math.sqrt(a**2+b**2)
#       return c
# def main():
#     while True:
#         s = input()
#         if s == "0":
#             break
#         else:
#             x=s.split()
#             a = float(x[0])
#             b = float(x[1])
#             c = pythagorean(a, b)
#             lista.append(c)
#     for i in lista:
#         print(i)
#
# if __name__=="__main__":
#     main()

def apply_float_division(szamok:list, oszto:int)->list:
    veg = []
    for i in range(len(szamok)):
        veg.append(round(szamok[i]/oszto,3))
    return veg
szamok=[]

def main():
    while True:
        try:
            s = input().split()
            oszto = int(input())
            for i in range(0, len(s)):
                szamok.append(int(s[i]))
            e=apply_float_division(szamok, oszto)
            print(e)
        except EOFError:
            break

if __name__=="__main__":
     main()
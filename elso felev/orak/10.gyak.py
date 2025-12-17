# import sys
# argc =len(sys.argv)
# print("parancssori arg. hossza", argc)
#
# for i in range(1,argc):
#     print("elem: ",sys.argv[i])
#
# print("Elérési útv.",sys.argv[0])

# import sys
# szorzat=1
# argc=len(sys.argv)
# for i in range(1,argc):
#     szorzat=szorzat*int(sys.argv[i])
# print("A szorzat: {0}".format(szorzat))
# print("Elérési útv.",sys.argv[0])

import sys
fajlneve=sys.argv[1]
def lnko(a:int,b:int)->int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


with open(fajlneve) as file:
    for line in file:
        szamok=line.strip("\n").split(" ")
        lnk=int(szamok[0])

        for i in range(1, len(szamok)):
            lnk=lnko(lnk,int(szamok[i]))

        print(lnk)


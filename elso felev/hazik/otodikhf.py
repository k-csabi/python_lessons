#elso
# n=int(input())
# pozitivp=0
#
# for i in range(0,n):
#     a=int(input())
#     if(a!=0 and a%2==0 and a>0):
#         pozitivp+=1
#
#
# print(pozitivp)

#masodik
# import sys
# maganhangzok="aáeéiíoóöőuúüű"
# while True:
#     try:
#         szo = input()
#         nelkuli=""
#         for i in range(0,len(szo)):
#             if szo[i] not in maganhangzok:
#                 nelkuli=nelkuli+szo[i]
#         print(nelkuli)
#     except EOFError:
#         break

#harmadik
# szo=""
#
# while (szo!="END"):
#     szo=input()
#     nagy=szo.upper()
#     ujszo=""
#     for i in range(0,len(szo)):
#         if szo[i]==nagy[i]:
#             ujszo+=2*szo[i]
#         else:
#             ujszo+=szo[i]
#     print(ujszo)
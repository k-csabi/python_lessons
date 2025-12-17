szam=0
a=[]

while szam>=0:
    szam=int(input())
    if szam>0 :
        a.append(szam)

hossz=len(a)
for i in range(hossz):
    if a[i]>=80:
        print("jeles")
    elif a[i]>=70:
        print("jo")
    elif a[i]>=60:
        print("kozepes")
    elif a[i]>=50:
        print("elegseges")
    else: print("elegtelen")
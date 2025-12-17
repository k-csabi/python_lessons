szam=int(input())
eredeti=szam
seged=0

def palindrom(szam, seged):
    seged=seged*10+(szam%10)
    szam=szam//10

    if eredeti==seged:
        return True
    else:
        return False

if palindrom(szam,seged):
    print("palindrom")
else:
    print("nem palindrom")
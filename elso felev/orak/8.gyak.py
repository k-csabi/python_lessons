#faktorialis

# def faktorialis(alap):
#     if alap==1:
#         return 1
#     return alap * faktorialis(alap-1)
#
# def main():
#     print(faktorialis(5))
#
# if __name__=="__main__":
#     main()

#fibonacci

# def fibonacci(n:int) -> int:
#     if n==1 or n==2:
#         return 1
#     if n==0:
#         return 0
#     return fibonacci(n-1)+fibonacci(n-2)

# def main():
#     print(fibonacci(40))
#
# if __name__=="__main__":
#     main()

n=int(input())
def osszeg(n:int) ->int:
    if n==1:
        return 1
    return n+osszeg(n-1)
def main():
    print(osszeg(n))

if __name__=="__main__":
    main()
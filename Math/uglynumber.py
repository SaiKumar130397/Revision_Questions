def remove_prime(n,pr):
    while n%pr==0 and n>1:
        n=n/pr
    return n
def isUgly(n: int) -> bool:
    n= remove_prime(n,2)
    n= remove_prime(n,3)
    n= remove_prime(n,5)
    return n==1
        
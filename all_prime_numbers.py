# Time Complexity=O(n*log log n)
#Space Complexity=O(n+1)~=O(n)

#function to check  the nos. which are prime and less or equal to givrn no.

def prime_numbers(n):
    is_prime=[True]*(n+1)
    is_prime[0]=is_prime[1]=False
    for i in range(2,n+1):
        if is_prime[i] and i*i<=n:
            for j in range(i*i,n+1,i):
                is_prime[j]=False

    Print_primes(is_prime)


# function to print the prime nos.
def Print_primes(a):
    for i in range(len(a)):
        if  a[i]:
            print(i)


prime_numbers(100)  
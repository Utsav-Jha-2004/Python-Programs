def isPrime(n):
    for d in range(2, n):
        if (n % d == 0):
            break
        else:
            return True
    
    return False

def primefrom1toN(n):
    for k in range(2, n + 1):
        is_k_prime = isPrime(k)
        if (is_k_prime):
            print(k)
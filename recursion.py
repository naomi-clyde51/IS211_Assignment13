def fibonnaci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)
print("Here is a sample answer: " + str(fibonnaci(10)))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print("Here is a sample answer: " + str(gcd(48, 18)))


def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    
    if not s1:
        return -1
    
    if not s2:
        return 1
    
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    
    return compareTo(s1[1:], s2[1:])
print("Here is a sample answer: " + str(compareTo("1", "2")))

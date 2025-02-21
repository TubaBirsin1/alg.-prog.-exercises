a=3
def sumTen(a):
    if a<1:
        return 0
    return a + sumTen(a-1)
print(sumTen(10))





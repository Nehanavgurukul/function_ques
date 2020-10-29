def test(a):
    c=5**a
    a=c
    def add(b):
        d=c//b
        return d   
    print(add(4))
    return a
print(test(7))
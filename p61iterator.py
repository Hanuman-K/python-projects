no=[7,4,5,6]
it =iter(no)
print(it.__next__())
print(next(it))
for i in no:
    print(i)

class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=topten()
print(next(values))
for i in values:
    print(i)

#generator it gives iterator
def topen():
    yield 1
    yield 2
    yield 3
    yield 4
values = topen()
print(values.__next__())
for i in values:
    print(i)

def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
values=topten()
for i in values:
    print(i,1)



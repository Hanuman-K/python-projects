

def div(a,b):
    print(a/b)
div(2,4)
def smart_dev(h):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return h(a,b)
    return inner

div=smart_dev(div)   #if we write div inplace of div1 then we are changing it
div(2,4)
div(4,2)



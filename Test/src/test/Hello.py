x = 'abc'  

def fetcher(obj, index):  
    return obj[index]  
  
def catcher():  
    try:  
        fetcher(x,1)  
    except Exception as e:  
        print e
        return 0
    else:
        print 'else'
        return -2
    finally:
        print 'fi'
        return -3
        
    print "continuing"
    return -1
    
def fun1(*keys):
    print "keys type=%s" % type(keys)
    print "keys=%s" % str(keys)
    for i in range(0, len(keys)):
        print "keys[" + str(i) + "]=%s" % str(keys[i])


from functools import wraps
def memo(fn):
    cache = {}
    miss = object()
    @wraps(fn)
    def wrapper(a):
        print a
        result = cache.get(a, miss)
        if result is miss:
            result = fn(a)
            cache[a] = result
        else:
            print 'aa'
        return result
    return wrapper
@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def test(a,*args,**kargs):
    print a,args,kargs
test(1,2,3,c=1,b=2)
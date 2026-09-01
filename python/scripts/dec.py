def memoized(func):
    cache = {}

    def wrapper(*args, **kwargs):
        print(f'a: {args}, k: {kwargs}')
        key = str(args)

        if cache.get(key):
            print('[hit]')
            return cache.get(key)

        print(f'[miss]: key:{key} type:{type(key)}')

        ret = func(*args, **kwargs)
        cache[key] = ret

        return ret

    return wrapper

@memoized
def calculate(a,b,c, **kwargs):
    return a + b + c


def fn():
    print('this is a testing...\n\n')

    print(f'--test 01 {calculate(1,2,3)} \n')
    print(f'--test 02 {calculate(2,2,3)} \n')
    print(f'--test 03 {calculate(1,2,3)} \n')
    print(f'--test 04 {calculate(2,2,3)} \n')

def fn2():
    self_identity = False

    if self_identity:
        policies = []
    else:
        print('no policies available')
    

    for policy in policies:
        print(f'policy: {policy}')


fn2()
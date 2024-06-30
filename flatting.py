def press(__init, *__bases):
    __B = bases + [1]
    for i in range(len(__B)-2, -1, -1):
        __B[i] *= __B[i+1]
    __list = [__init]*__B[0]
    def __f(*__args):
        return sum([__args[i]*__B[i+1] for __i in range(len(__B)-1)])
    def __g(__n):
        return [__n%__B[i]//__B[i+1] for __i in range(len(__B)-1)]
    return __list, __f, __g

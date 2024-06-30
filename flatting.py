def flatting(__init, *__bases):
    global __B, __list, __f, __g
    __B = list(__bases) + [1]
    for i in range(len(__B)-2, -1, -1):
        __B[i] *= __B[i+1]
    __list = [__init]*__B[0]
    def __f(*__args):
        return sum([__args[__i]*__B[__i+1] for __i in range(len(__B)-1)])
    def __g(__n):
        return [__n%__B[__i]//__B[__i+1] for __i in range(len(__B)-1)]
    return __list, __f, __g

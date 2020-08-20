import time, functools

def TimedProcess(name):
    def _outer(fn):
        @functools.wraps(fn)
        def _inner(*args, **kwargs):
            t_start = time.perf_counter()
            fn(*args, **kwargs)
            t_end = time.perf_counter()
            print (f"Completed {name} in {str(round(t_end - t_start, 2))} seconds")
        return _inner
    return _outer

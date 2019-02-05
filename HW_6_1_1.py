from sys import getsizeof


def summarizing(args):
    summ = 0

    for i in args:
        el = args.get(i)
        if i.startswith('__'):
            continue
        elif hasattr(i, '__call__'):
            continue
        elif hasattr(i, '__loader__'):
            continue
        else:
            if hasattr(el, '__iter__'):
                if hasattr(el, 'items'):
                    for k, v in el.items():
                        summ += getsizeof(k)
                        summ += getsizeof(v)
                elif type(el) != str:
                    for j in el:
                        summ += getsizeof(j)
            summ += getsizeof(el)

    return f'Размер памяти, выделяемый под переменные = {summ}.'

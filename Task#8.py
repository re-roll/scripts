def first_with_given_key(iterable, key = repr):
    new_key = lambda x: key(x)
    array = {}
    for i in iterable:
        klic = new_key(i)
        if not klic in array.keys(): 
            array[klic] = repr(i)
            yield i

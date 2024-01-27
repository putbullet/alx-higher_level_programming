#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result_tuple = ()
    lenght = min(len(tuple_a), len(tuple_b))
    for i in range(lenght):
        result_tuple += (tuple_a[i] + tuple_b[i],)
    return result_tuple

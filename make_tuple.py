def make_tuple(a,b,c=3,d=4):
    my_tuple = (a,b,c,d)
    # return my_tuple
    # Pokus o pouziti list comprehension
    return tuple([i for i in my_tuple])


a = make_tuple("ja", "ty","on", )
print(a)
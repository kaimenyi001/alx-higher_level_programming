def complex_delete(a_dictionary, value):
    n_keys = list(a_dictionary.keys())

    for i in n_keys:
        if value == a_dictionary.get(i):
            del a_dictionary[i]

    return (a_dictionary)

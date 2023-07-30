dict_first = {"사과": 30, "배": 15, "감": 10, "포도": 10}
dict_second = {"사과": 5, "감": 25, "배": 15, "귤": 25}

def merge_dict(dict_first, dict_second):
    for x in dict_second:
        if dict_first.get(x):
            dict_first[x] += dict_second[x]
        else:
            dict_first[x] = dict_second[x]
    return dict_first

merge_dict(dict_first, dict_second)
from itertools import count

def follow_pattern(pattern,s):
    """_this function compaares the two arguments
    pattern and s, and outputs a boolean statement to
    show whether the string s follows the pattern_

    Args:
        pattern (_str_): _a representation of the format_
        s (_str_): _the string to be tested for the pattern_

    Returns:
        _bool_: _returns True or False depending on the outcome 
        of the comparism_
    """    
    pattern_list = list(pattern)
    string_list = s.split(" ")

    res = list(map({}.setdefault, pattern_list, count()))
    res2 = list(map({}.setdefault, string_list, count()))
    return res == res2


if __name__ == "__main__":
    result=follow_pattern("abba","cat dog dog cat")
    print(result)
# True

#JEK __python__
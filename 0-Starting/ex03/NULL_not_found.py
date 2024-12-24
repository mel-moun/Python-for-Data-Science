def NULL_not_found(object: any) -> int:
    if (object is None):
        print("Nothing:", object, type(object))
    elif (object != object and type(object) == float): 
        print("Cheese:", object, type(object))
    elif (type(object) is int and object == 0):
        print("Zero:", object, type(object))
    elif (type(object) is str and not object):
        print("Empty:", object, type(object))
    elif (type(object) is bool and object is False):
        print("Fake:", object, type(object))
    else:
        print("Type not Found")
        return 1
    return 0

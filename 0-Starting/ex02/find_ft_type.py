def all_thing_is_obj(object: any) -> int:
    x = type(object)
    if (x is list):
        print("List :", x)
    elif (x is tuple):
        print("Tuple :", x)
    elif (x is set):
        print("Set :", x)
    elif (x is dict):
        print("Dict :", x)
    elif (x is str):
        print(object, "is in the kitchen :", x)
    else:
        print("Type not found")
    return 42

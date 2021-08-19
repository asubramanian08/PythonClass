def HelloX(x):
    if x <= 0:  # Base Case
        return
    print("Hello")
    HelloX(x-1)


def AddList(num_list):
    if len(num_list) <= 1:
        return num_list[0]
    else:
        return num_list[0] + AddList(num_list[1:])

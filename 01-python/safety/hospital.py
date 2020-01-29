def draw_hospital(width):
    string = "hospitals"
    for i in range(width):
        print("-",end="")
    print()
    x = ""
    for i in range(width):
        if i == 0 or i == width-1:
            x += "|"
        elif i == width//2:
            x += "+"
        else:
            x += " "
    print(x)
    for i in range(width):
        print("-",end="")
    print()
    y = ""
    for i in range(width):
        if i == 0 or i == (width-1):
                y += "|"
        else:
                y += " "
    print(y)
    k = ""
    newwidth = width - len(string)
    for i in range(newwidth):
        if i == 0 or i == newwidth-1:
            k += "|"
        else:
            k += " "
    k1 = k[0:newwidth//2] + string + k[newwidth//2:]
    print(k1)
    print(y)
    for i in range(width):
        print("-",end="")
    print()
    return

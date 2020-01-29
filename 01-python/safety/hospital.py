def draw_hospital():
    """ please modify the width, it should be an odd number """
    width = 13
    draw_line(width)
    draw_hospital_sign(width)
    draw_line(width)
    draw_hospital_body(width)
    draw_hospital_name(width)
    draw_hospital_body(width)
    draw_line(width)
    return

def draw_line(width):
    for index in range(width):
        print("-",end="")
    print()
    return

def draw_hospital_body(width):
    body_line = ""
    for index in range(width):
        if index == 0 or index == (width-1):
                body_line += "|"
        else:
                body_line += " "
    print(body_line)

def draw_hospital_sign(width):
    sign_line = ""
    for index in range(width):
        if index == 0 or index == width-1:
            sign_line += "|"
        elif index == width//2:
            sign_line += "+"
        else:
            sign_line += " "
    print(sign_line)

def draw_hospital_name(width):
    name = "hospitals"
    name_line1 = ""
    newwidth = width - len(name)
    for index in range(newwidth):
        if index == 0 or index == newwidth-1:
            name_line1 += "|"
        else:
            name_line1 += " "
    hospital_name = name_line1[0:newwidth//2] + name + name_line1[newwidth//2:]
    print(hospital_name)

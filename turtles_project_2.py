import turtle

#def the function
def theshape(r):
    turtle.screensize(canvwidth=400, canvheight=400, bg="#336633")
    turtle.pen(pencolor="#FFFFCC", pensize=1.5)
    turtle.turtlesize(0.1, 0.1, 0.1)

    point_a = [-r, 0]
    point_b = [-r / (2 ** .5), r / (2 ** .5)]
    point_c = [0, r]
    point_d = [r / (2 ** .5), r / (2 ** .5)]
    point_e = [r, 0]
    point_f = [r / (2 ** .5), -r / (2 ** .5)]
    point_g = [0, -r]
    point_h = [-r / (2 ** .5), -r / (2 ** .5)]

    lst_8 = [point_a, point_b, point_c, point_d, point_e, point_f, point_g, point_h]

    for i in lst_8:
        for x in range(len(lst_8)):
            if i in lst_8[:x]:
                pass
            else:
                turtle.goto(i[0],i[1])
                y = lst_8[x]
                turtle.goto(y[0], y[1])
    turtle.goto(0,-r)
    turtle.circle(r)

for i in range(5):
    theshape(20*i)

end = input('end?')
import colorgram
import turtle as t
import random

# colors = colorgram.extract("Day_18_Turtle/CU_LOGO.jpg", 30)

# tuple_colors =[]


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     tuple_colors.append(new_color)

# print(tuple_colors)

rgb_colors  = [(252, 252, 250), (109, 77, 123), (8, 145, 67), (89, 88, 105), (230, 237, 227), (43, 37, 44), (27, 26, 25), (156, 158, 168), (241, 233, 240), (44, 42, 51), (176, 154, 148), (169, 152, 162), (15, 40, 22), (222, 223, 227), (110, 93, 90), (163, 171, 164), (62, 59, 75), (73, 56, 71), (152, 109, 126), (122, 123, 140), (186, 88, 81), (28, 87, 52), (204, 181, 197), (189, 189, 200), (212, 181, 177), (186, 195, 185), (192, 193, 187), (93, 141, 113), (97, 48, 45), (65, 64, 60)]

t.colormode(255)
tim = t.Turtle()

tim.penup() # so that line will not be drawn when turtle moves
tim.hideturtle() #to hide turtle
tim.speed("fastest")

tim.setheading(225) #to move it to a better position to start
tim.forward(300)
tim.setheading(0)

dots = 100

for dot in range(1, dots + 1):
    tim.dot(20, random.choice(rgb_colors)) # draw dot with random color from the list
    tim.forward(50)
    
    if dot % 10 == 0: # after every 10 dots, move the turtle to the next line
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()

screen.exitonclick()

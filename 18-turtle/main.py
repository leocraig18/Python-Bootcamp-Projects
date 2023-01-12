import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed("fastest")
dots = 0
tim.hideturtle()
rgb_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
              (254, 194, 0)]
tim.penup()
tim.setheading(200)
tim.forward(260)
tim.setheading(0)


def back_home():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)


while dots < 100:
    for _ in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)
        dots += 1
    back_home()

screen = t.Screen()
screen.exitonclick()

# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rbg_tuple = (r, g, b)
#     return rbg_tuple
#
#
# tim.color("green")
# tim.shape("turtle")
#
# colours = ["light sky blue", "red", "green", "light green", "slate blue", "rosy brown", "black", "yellow", "hot pink"]
# tim.width(1)
# tim.speed("fastest")
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(360 / size_of_gap):
#         tim.pencolor(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(size_of_gap=6)

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 84)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

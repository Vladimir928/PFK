#!/usr/bin/env python3
################################################################################
#   sample.py
#
#   chapter 4: Turtle
#
#   09.07.2019  Created by:  vo958
################################################################################
import turtle

main_window = turtle.Screen()
t = turtle.Pen()

t.forward(100)
t.left(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.forward(250)
t.left(60)
t.forward(250)
t.left(60)
t.forward(250)
t.left(60)

main_window.mainloop()


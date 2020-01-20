import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

#Main game loop
while True:
    wn.update()
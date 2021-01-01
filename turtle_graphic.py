def hit_the_target():
    import turtle
    import math

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    MAX_DISTANCE = int(math.sqrt((SCREEN_WIDTH / 2)**2 + (SCREEN_HEIGHT / 2)**2))

    TARGET_LOW_LEFT_X = 100
    TARGET_LOW_LEFT_Y = 250
    TARGET_WIDTH = 25

    PEN_SPEED = 0

    #1 open a 600 by 600 pixel window
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    pen = turtle.Pen()

    #2 draw a square 25px on all sides
    pen.hideturtle()
    pen.speed(PEN_SPEED)
    pen.penup()
    pen.goto(TARGET_LOW_LEFT_X, TARGET_LOW_LEFT_Y)
    pen.pendown()
    def draw_square(width):
        EAST = 0
        NORTH = 90
        WEST = 180
        SOUTH = 270
        
        headings = [EAST, NORTH, WEST, SOUTH]
        for heading in headings:
            pen.setheading(heading)
            pen.forward(width)
    draw_square(TARGET_WIDTH)
    
    #3 return the pen to origin
    pen.penup()
    pen.home()
    pen.showturtle()

    #4 prompt user for angle and distance
    angle = int(input("Enter the projectile's angle (0-359): "))
    distance = int(input(f"Enter the launch distance (1-{MAX_DISTANCE}): "))
    
    #5 move the pen per the angle and distance provided
    pen.speed(PEN_SPEED + 1)
    pen.pendown()
    def move_pen(angle, distance):
        pen.setheading(angle)
        pen.forward(distance)
    move_pen(angle, distance)

    #6 determine if it hit
    #6.1 hit is if the pen position is within the square
    x_pos = pen.xcor()
    y_pos = pen.ycor()

    hit = False
    if x_pos >= TARGET_LOW_LEFT_X and x_pos <= TARGET_LOW_LEFT_X + TARGET_WIDTH:
        if y_pos >= TARGET_LOW_LEFT_Y and y_pos <= TARGET_LOW_LEFT_Y + TARGET_WIDTH:
            hit = True
        else:
            hit = False
    
    #7 show a hit / miss message to the user
    if hit:
        print('Hit!')
    else:
        print('Miss!')
    
    turtle.done()

hit_the_target()
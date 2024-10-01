""" Welcome to the RoboCats' intro to pybricks! """

"""
Blocks of text like this (surrounded by triple-quotes) are called comments.
They do not affect how the program behaves.  In this file, they wil contain
instructions, explanations, and other useful info.

The lines below are also comments, because they start with a # sign.
When you see these, un-comment them to try out the example code.
"""

# Remove both the # and the space to un-comment a line

""" 
The code below calls a built-in python function named print.
Try it - uncomment the line and press play.

The quotes tell python to create a "string" of text and pass it to print. The
arguments must be in parenthesis to show that they belong to the function call.
"""

# print("Hello, world!")

"""
The placement of quotes and parenthesis are important.  Try the following
to see what can happen when there is a 'syntax error'.  Try them one at 
a time and re-comment them afterwards.
"""

# print("What happens if a quote is missing)

# print("What if the parens are wrong?)"

"""
Programs can store information in named variables, and then pass those
variables to functions, do math on those variables, and other cool things.

You can create a variable using the equals symbol.  Try it:
"""
# my_variable = "Hello again"
# print(my_variable)

"""
Variables can hold more than just strings.  They can hold numbers,
True/False values, lists of values, and lots of other cool things.

We can pass variables to functions, do operations on them, and
update them with new values.

Do the four experiments below one at a time, because some will
generate errors.   Comment them out again afterwards.
"""

# numbers_arent_quoted = 5
# another_number = numbers_arent_quoted + 1
# print(f"this is another number: {another_number}")

# another_number = another_number * 2
# print(f"we updated the variable, and now it is: {another_number}")

# print(another_number / 3)


"""
OK, now it's time to make the bot move.

The lines below tell python to load the pybricks code our program needs.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

"""
Next, this code initializes our hub, create motor objects, and creates a
DriveBase object.   We will make calls on these objects to control the bot.

To create a Motor, we need to provide the port it is plugged into, and 
which direction the motor's positive direction is.  The drive base needs 
to know the wheel diameter and distance between the wheels, so that it 
knows how to drive and turn a specific amount.
"""

PrimeHub()
right_wheel = Motor(port=Port.A)
left_wheel = Motor(port=Port.B,
                   positive_direction=Direction.COUNTERCLOCKWISE)
base = DriveBase(left_motor=left_wheel,
                 right_motor=right_wheel,
                 wheel_diameter=57,
                 axle_track=82)

"""
With our setup out of the way, driving the bot is easy.  Methods
on the DriveBase object can make the bot move and turn.
"""

# base.straight(distance=200)

# base.turn(angle=90)

# base.curve(radius=150, angle=90)

"""
Can you make the bot move in a square path, back to where
it started?  Try it.
"""

"""
What if you wanted it to drive in a hexagon or octagon shape?
Hint: You'll need a for loop to iterate a certain number of times.
      The code examples below should be enough to get you started.
"""

# start_at = 0
# stop_before = 9
# print(range(start_at, stop_before))

# numbers = [1, 2,3]
# for i in numbers:
#    print(i)


"""
Now let's control an arm motor.
"""

# arm = Motor(port=Port.C)

# angle = arm.angle()
# print(f"initial value from arm.angle: {angle}")

# arm.run_angle(speed=100, rotation_angle=60)

# print(f"new value from arm.angle: {arm.angle()}")


"""
What is the difference between run_target and run_angle? 

Check out this page: https://docs.pybricks.com/en/stable/pupdevices/motor.html

"""
# arm.run_target(speed=100, target_angle=0)


"""
What if Motor.run_target didn't exist?  Can you write 
code using Motor.angle and Motor.run_angle that will
do the same thing as Motor.run_target?
"""


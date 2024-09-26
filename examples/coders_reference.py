"""
printing
"""

message = my_str
print(message)
print("multiple", " different", "arguments and ", message)
print(f"Use an f-string with braces around variables or function calls: {message}")


"""
Basic data types
"""

my_none = None
my_str = "Hello, world!"
my_int = 3
my_float = 3.1415926
my_bool = True                  # or False
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)         # same as a list, but can't be modified
my_set = {1, 2, 3, 4}           # No order, can only contain 1 of each item
my_dictionary = {"Shark": "Grey",
                 "Bear": "Brown"}


"""
Boolean expressions
"""
# these conditionals always evaluate to True!
if my_none is None or my_none is not None:
    pass
if my_str == "Hello, world!" or my_str != "Hello, world!":
    pass
if my_int == 3 or my_int != 3 or my_int < 3 or my_int > 3:
    pass
if my_bool is True or my_bool is not True or my_bool is False:
    pass
if 2 in my_list:                    # Is this value anywhere in the list?
    pass
if "Shark" in my_dictionary:        # Is this key anywhere in the dictionary?
    pass
if (my_int == 3 or my_bool is True) and my_none is None:   # You can group conditions with parenthesis
    pass

"""
List methods
"""

first_item = my_list[0]                 # Lists start with index 0
second_item = my_list[1]
my_list.append("an item")               # adds an item to the end
my_list.extend([1, 2, 3])               # To combine two lists, use extend, not append
my_list.pop()                           # removes the item from the end
my_list.remove(2)                       # Removes first occurrence of item.  Raises an exception if item is not present
my_list.copy()                          # returns a copy of the list (in case you want one to modify)
my_list.sort()                          # sorts the list in place
my_list.reverse()                       # reverses the order of the list in place
l = filter(lambda x: x != 2, my_list)   # Only keep items that are != 2.
l2 = [x for x in my_list if x != 2]     # Same as the above filter.

"""
dictionary methods
"""

the_sharks_color = my_dictionary["Shark"]       # Grab the value corresponding to a given key
just_the_keys = my_dictionary.keys()            # Returns an iterable - to get a regular list, do list(just_the_keys)
just_the_values = my_dictionary.values()        # values() and items() also return iterables
key_value_tuples = my_dictionary.items()        # e.g. [("Shark", "grey"), ("Bear", Brown)]
del my_dictionary["Shark"]                      # Remove an item from the dictionary


"""
Flow Control
"""

sky = "blue"
sea = "green"

if sky == "blue":           # If the expression is true, the contained block of code is executed
    pass

if sky == "yellow":         # elif is optional, and will only be executed if the if block did not execute.
    pass
elif sea == "green":        # we can have multiple elif blocks; Only the first True on will execute.
    pass
else:                       # else is also optional, and is executed only if nothing else was executed.
    pass

"""
while loops
"""
i = 1
while i < 6:
    i = i + 1               # Will do this until i == 6

numbers_to_add = [1, 2, 3, 4]
total = 0
for i in numbers_to_add:           # For each item in the list, sets i equal to that item and runs the block
    total = total + i      # We could also have just used sum(to_add)


start_at = 1
end_before = 11
for i in range(start_at, end_before):   # If you want to do something 10 times
    pass

"""
functions
"""


def takes_no_inputs():
    return "some return value"


return_val = takes_no_inputs()


def takes_one_input(required_arg):
    return f"You passed {required_arg}"


return_val = takes_one_input(3)


def takes_multiple_inputs(required_arg, optional_arg=None, optional_arg2=0):
    return(f"required_arg = {required_arg}, optional_arg = {optional_arg}, optional_arg2 = {optional_arg2}")


return_val = takes_multiple_inputs(1)
return_val = takes_multiple_inputs(1, optional_arg2=5)

"""
Robotics
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop, Direction

PrimeHub()
right_wheel = Motor(port=Port.A)
left_wheel = Motor(port=Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
base = DriveBase(left_motor=left_wheel,
                 right_motor=right_wheel,
                 wheel_diameter=TODO,
                 axle_track=TODO)


base.straight(distance=200)
base.turn(angle=35)
base.curve(radius=100, angle=35)

arm = Motor(port=Port.C)
angle = arm.angle()
arm.run_angle(speed=100, rotation_angle=25)
arm.run_target(speed=100, target_angle=0)
stalled_angle = arm.run_until_stalled(300, duty_limit=10)

stop_constants = [Stop.HOLD, Stop.BRAKE, Stop.COAST, Stop.COAST_SMART]

# https://docs.pybricks.com
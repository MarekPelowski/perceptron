training_data = [
    [23, 4, 'ring'],
    [18, 3, 'ring'],
    [8, 2, 'ring'],
    [200, 300, 'ring'],
    [8, 150, 'pen'],
    [30, 350, 'pen'],
    [5, 100, 'pen'],
    [10, 200, 'pen']
]


input_a = 23 # diameter
input_b = 4 # length
name = "ring"
good = False
weight_a = -2
weight_b = 1/10
constant_speed = 0.2

output_a = input_a * weight_a
output_b = input_b * weight_b

addition = 6

summed_output = output_a + output_b + addition

# interpretation
if summed_output >= 0:
    print("ring")
    if name == "ring":
        good = True
    else:
        good = False
else:
    print("pen")
    if name == "pen":
        good = True
    else:
        good = False

print(name, good)

if not good:
    if name == "ring":
        add = 1
    else:
        add = -1

    print(weight_a, add, input_a, constant_speed)

    weight_a += add * input_a * constant_speed
    weight_b += add * input_b * constant_speed

    addition += add * constant_speed

    print(weight_a)
    print(weight_b)
    print(addition)

    output_a = input_a * weight_a
    output_b = input_b * weight_b

    addition = 6

    summed_output = output_a + output_b + addition

    # interpretation
    if summed_output >= 0:
        print("ring")
        if name == "ring":
            good = True
        else:
            good = False
    else:
        print("pen")
        if name == "pen":
            good = True
        else:
            good = False

    print(name, good)

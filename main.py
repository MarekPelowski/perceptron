import time

training_data = [
    [23, 4, 'ring'],
    [18, 3, 'ring'],
    [8, 2, 'ring'],
    [200, 30, 'ring'],
    [8, 150, 'pen'],
    [30, 350, 'pen'],
    [5, 100, 'pen'],
    [10, 200, 'pen']
]

# input_a = training_data[0][0]  # diameter
# input_b = training_data[0][1]  # length
# name = training_data[0][2]

weight_a = -2
weight_b = 1 / 10
constant_speed = 0.2
addition = 6

everyGood = True
i = 0
while everyGood == False or i == 0:
    everyGood = True

    print()
    print('weight a: ', weight_a)
    print('weight b: ', weight_b)
    print()

    for data in training_data:

        input_a = data[0]  # diameter
        input_b = data[1]  # length
        name = data[2]

        output_a = input_a * weight_a
        output_b = input_b * weight_b

        summed_output = output_a + output_b + addition

        # interpretation
        if summed_output >= 0:
            if name == "ring":
                if len(data) == 3:
                    data.append(True)
                else:
                    data[3] = True

            else:
                if len(data) == 3:
                    data.append(False)
                else:
                    data[3] = False
                everyGood = False
        else:
            if name == "pen":
                if len(data) == 3:
                    data.append(True)
                else:
                    data[3] = True
            else:
                if len(data) == 3:
                    data.append(False)
                else:
                    data[3] = False
                everyGood = False
        print(data)


    for data in training_data:
        if not data[3]:
            if data[2] == 'ring':
                add = 1
            else:
                add = -1

            weight_a += add * data[0] * constant_speed
            weight_b += add * data[1] * constant_speed

            addition += add * constant_speed



            break


    time.sleep(1)
    i+=1

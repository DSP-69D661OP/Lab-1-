numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
lenght = len(numbers)
sm = 0
for i in range(lenght):
    if (numbers[i] != None):
        sm += numbers[i]
sm = sm / lenght
for i in range(lenght):
    if (numbers[i] == None):
        numbers[i] = sm

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)

import math

while True:
    try:
        text = input('>>:')
        if text == "q":
            break
        x = int(text)
        y = math.log10(x)
        print('log10({}) = {}'.format(x, y))
    except ValueError:
        print("the value must be greater then 0 !")

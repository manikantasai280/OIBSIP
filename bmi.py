
def bmifun(height,weight):
    bmi=(weight/height**2)
    print("your bmi value is:" + str(bmi))
    if(bmi<18.5):
        print("you are underweight...eat dry fruits regularly")
    elif(bmi>= 18.5 and bmi<24.9):
        print("you are normal weight")
    elif(bmi>=24.9 and bmi<29.9):
        print("you are overweight do some exercises")
    else:
        print("you have obesity... try to go gym")


height=float(input("please enter your height in meters"))
if(height <= 2.5 and height >= 1.2):
    weight=float(input("now enter your weight in kgs"))
    if(weight < 250 and weight > 30):
        bmifun(height,weight)
    else:
        print("please enter valid weight")
else:
    print("please enter valid height")
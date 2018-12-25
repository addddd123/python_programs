import math
def bmi_(height,weight):

        height*=height

        bmi=weight/height
        return round(bmi,1)
height=float(input(" Enter height in meter: "))     
weight=float(input(" Enter weight in kg's: "))  
bmi=bmi_(height,weight)
if bmi<18.5:
    print(" u r Underweight: ")
elif 18.5<bmi<24.9:
    print(" Healthy weight: ")
elif 25<bmi>29.9:
    print(" Overweight: ")
else:
    print(" Obese: ")
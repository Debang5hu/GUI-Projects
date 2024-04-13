#!/usr/bin/python3

# _*_ coding:utf-8 _*_ 

# it will calculate Body Mass Index(BMI) using kg and m
# formula weight / height * height

# it requires no dependency


# displaying catergories wise
def display(BMI):

    #conditions
    if BMI <= 18.5:
        print(f'[+] BMI = {round(BMI,2)}\n[+] Category = Under Weight')
    elif BMI >= 18.5 and BMI <= 24.9:
        print(f'[+] BMI = {round(BMI,2)}\n[+] Category = Healthy Weight')
    elif BMI >= 25.0 and BMI <= 29.9:
        print(f'[+] BMI = {round(BMI,2)}\n[+] Category = Over Weight')
    elif BMI >= 30.0:
        print(f'[+] BMI = {round(BMI,2)}\n[+] Category = Obesity')
    else:
        print('[+] Check the value correctly')


# it calculates the bmi
def calculate(height,weight) -> float:
    BMI = weight / (height ** 2)
    return BMI

# main
if __name__ == '__main__':

    # cli inputs
    height = float(input('[+] Enter your Height [metre]: '))
    weight = float(input('[+] Enter your Weight [kilogram]: '))

    BMI = calculate(height,weight)  # calculate

    display(BMI) # result

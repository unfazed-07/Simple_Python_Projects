try:
    name=input('Enter your name:')
    weight=int(input('Enter you weight in kg:'))
    height=float(input('Enter your height in meter :'))
except:
    raise ValueError("INVALID INPUT! PLease enter numeric values for weight and height.")
bmi= weight/(height**2)

if bmi<18.5: print( f'Your BMI is {bmi:.2f}\n', name, 'You are UNDERWEIGHT! Needs to increase your calorie intake.' )
elif bmi<24.9: print(f'Your BMI is {bmi:.2f}\n',name, 'You are Fit and have normal weight., ' )
elif bmi<29.9: print(f'Your BMI is {bmi:.2f}\n',name, 'You are OVERWEIGHT and require to give some time to health along with carrer goals.')
elif bmi<34.9: print(f'Your BMI is {bmi:.2f}\n',name, 'You are OBESED and need a strong focus on health.' )
elif bmi<39.9: print(f'Your BMI is {bmi:.2f}\n',name, 'You are OBESED at an intense level. No words for you!' )
else: print("Hey",name, 'Enter some valid input' )

#Suggesting Calorie intake based on Mifflin-ST Jeor Equation which is browse through Web
go_on=input("\nWe can recommend you daily calorie intake.\n press (y):\n")
if go_on.lower()=='y':
    
    try:
        age=int(input('Enter your age in years:'))
        sex=(input('Enter your Gender: "Male" or "female"'))
    except:
        raise ValueError('Please Enter numeric value for age')
    
    if sex.lower()=='male':
        BMR = (10*weight) + (6.25*(height*100)) -(5*age) + 5
    if sex.lower()=='female':
        BMR = (10*weight) + (6.25*(height*100)) -(5*age) -161

#After calculating BMR

    print("\nChoose your activity level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise 1–3 days/week)")
    print("3. Moderately active (moderate exercise 3–5 days/week)")
    print("4. Very active (hard exercise 6–7 days/week)")
    print("5. Super active (very hard exercise or physical job)")

    activity_factor={
                    '1':1.2,
                    '2':1.375,
                    '3':1.55,
                    '4':1.725,
                    '5':1.9,
                    }
    
    activity_choice=input('ENter the number corrosponding to your activity:')
    while True:
        if activity_choice in activity_factor:
            multiplier =activity_factor[activity_choice]
            break
        else:
            print("INvalid Choice. Please enter a number betweeen 1 and 5")

    est_cal=multiplier*BMR
    print(f"Hey {name}! Based on provided data and activity level, Your estimated  daily calorie need is {est_cal}")

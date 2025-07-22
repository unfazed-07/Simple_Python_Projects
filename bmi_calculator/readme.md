# BMI CALCULATOR

# OVERVIEW
This project is a simple python-based tool designed to calulate Body Mass Index 

## Features
- Accepts user input for weight and height with error handling for non-numeric values.
- Calculates BMI using the formula: `weight / (height^2)`.
- Provides a basic user interface with personalized output using the entered name.
- Includes exception handling to ensure robust input validation.

## Additional feature
- Can also suggest you  very precise daily calorie need by using "Mifflin-ST Jeor Equation" which I found on web
  - For men: `BMR = 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) + 5`
  - For women: `BMR = 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) - 161`
- To calculate daily calorie needs, BMR can be multiplied by an activity factor (e.g., 1.2 for sedentary, 1.375 for lightly active)


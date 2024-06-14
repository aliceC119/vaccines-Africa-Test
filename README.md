![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

## Purpose of this project

- Vaccines-Africa want this Python program to show how many lives are saved by each vaccine (diphtheria ,hepatitis B, measles , polio, rubella, tetanus, tuberculosis, yellow fever) on average in Africa between 2020 and 2024.
- We want to use these averages to help to decide how many vaccines to produce for the next year.
- We also want to know the total number of lives saved by each of the vaccine from year 2020 to 2024.

## How this program works

1. Collect lives saved data from user
2. Check that the lives saved data input from the user is valid
3. Add lives saved data into lives saved worksheet
4. Calculate surplus numbers (the number of vaccine produce minus the number of lives saved)
5. Add surplus data to surplus worksheet
6. Calculate averages lives saved for the last 5 years
7. Add calculated vaccine produce numbers (if the numbers < 10000 then the same number of vaccines will be produced for the next year, if the numbers > 10000 then less vaccines will be produced in next year according to the calculated numbers)
8. Print vaccine produce amount for recommendations
9. Calculate the total number of lives saved for each vaccine between the year 2020 to 2024 ( sum up the numbers of lives saved for each vaccine)
10. Print the total lives saved numbers for each vaccine



![Blank diagram](https://github.com/aliceC119/vaccines-Africa-Test/assets/162838985/d90cb69f-d3fc-4c26-af6b-3291366bafe3)


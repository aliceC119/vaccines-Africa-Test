import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Vaccines - Africa (2020-2024)')

def get_livessaved_data():
    """
    Get lives saved figures input from the user.
    Run a while loop to collecz a valid string of data from the user
    via the terminal, which must be a string of 8 numbers separated
    by commas. The loop will repeated request data, until it is valid.
    """
    while True:
        print("Please enter lives saved data from last year.")
        print("Data should be eight numbers, separated by commas.")
        print("Example: 100,200,300,400,500,600,700,800\n")

        data_str = input("Enter your data here: ")
    
        livessaved_data = data_str.split(",")

        if validate_data(livessaved_data):
            print("Data is valid!")
            break
    
    return livessaved_data

        



def validate_data(values):
    """ 
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 8 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 8:
            raise ValueError(
                f"Exactly 8 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

def update_livessaved_worksheet(data):
    """ 
    Update livessaved worksheet, add new row with the list data provided.
    """
    print("Updating livessaved worksheet...\n")
    livessaved_worksheet = SHEET.worksheet("livessaved")
    livessaved_worksheet.append_row(data)
    print("livessaved worksheet updated successfully.\n")

def calculate_surplus_data(livessaved_row):
    """ 
    Compare lives saved number with vaccine produce number and calculate the surplus for each vaccine type.

    The surplus is defined as the lives saved figure subtracted from the vaccine produce number.
    """
    print("Calculating surplus data...\n")
    vaccineproduce = SHEET.worksheet("vaccineproduce").get_all_values()
    vaccineproduce_row = vaccineproduce[-1]
    print(vaccineproduce_row)

def main():
    """ 
    Run all program functions
    """
    data = get_livessaved_data()
    livessaved_data = [int(num) for num in data]
    update_livessaved_worksheet(livessaved_data)
    calculate_surplus_data(livessaved_data)

print("Welcome to Lives Saved Data Automation")
main()


# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

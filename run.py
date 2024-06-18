import gspread
from google.oauth2.service_account import Credentials

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
    Get livessaved figures input from the user.
    """
    while True:
        print("Please enter the numbers of lives saved by the following \n\
        vaccines in the last year in this order: \n\
        Diphtheria, Hepatitis B, Measles, Polio, Rubella,Tetanus, \n\
        Tuberculosis, Yellow fever.")
        print("Data should be eight numbers, separated by commas")
        print("Example: 1000,2000,3000,4000,5000,6000,7000,8000\n")

        data_str = input("Enter your data here:\n")
        livessaved_data = data_str.split(",")

        if validate_data(livessaved_data):
            print("Data is valid!")
            print(f"The data provided is {data_str}")
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


def update_worksheet(data, worksheet):
    """
    - Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided.

    -The data refer to the numbers of lives saved, and the
    calculated numbers of surplus, vaccine production, and the
    total lives saved.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_surplus_data(livessaved_row):
    """
    - Compare lives saved number with vaccine produce number.
    Calculate the surplus for each vaccine type.

    - The surplus is defined as the lives saved figure subtracted
    from the vaccine produce number.
    """
    print("Calculating surplus data...\n")
    vaccineproduce = SHEET.worksheet("vaccineproduce").get_all_values()
    vaccineproduce_row = vaccineproduce[-1]

    surplus_data = []
    for vaccineproduce, livessaved in zip(vaccineproduce_row, livessaved_row):
        surplus = int(vaccineproduce) - livessaved
        surplus_data.append(surplus)
    print(surplus_data)

    return surplus_data


def get_last_5_entries_livessaved():
    """
    Collects collumns of data from lives saved worksheet,
    collecting the last 5 entries for each vaccine
    and returns the data as a list of lists.
    """
    livessaved = SHEET.worksheet("livessaved")

    columns = []
    for ind in range(1, 9):
        column = livessaved.col_values(ind)
        columns.append(column[-5:])

    return columns


def calculate_vaccineproduce_data(data):
    """
    Calculate the average vaccine produce number for each type of vaccine,
    then adding 20%.
    """
    print("Calculating new vaccince production data for next year...\n")
    new_vaccineproduce_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        vaccineproduce_num = average * 2.2
        new_vaccineproduce_data.append(round(vaccineproduce_num))
    print(new_vaccineproduce_data)

    return new_vaccineproduce_data


def calculate_totallivessaved_data(data):
    """
    Calculate the lump sum number for each vaccine tape from the last 5 years
    """
    print("Calculating total lives saved data from the last 5 years...\n")
    new_totallivessaved_data = []

    for column in data:
        int_column = [int(num) for num in column]
        total = sum(int_column)
        totallivessaved_num = total
        new_totallivessaved_data.append(totallivessaved_num)
    print(new_totallivessaved_data)
    return new_totallivessaved_data


def main():
    """
    Run all program functions
    """
    data = get_livessaved_data()
    livessaved_data = [int(num) for num in data]
    update_worksheet(livessaved_data, "livessaved")
    new_surplus_data = calculate_surplus_data(livessaved_data)
    update_worksheet(new_surplus_data, "surplus")
    livessaved_columns = get_last_5_entries_livessaved()
    vaccineproduce_data = calculate_vaccineproduce_data(livessaved_columns)
    update_worksheet(vaccineproduce_data, "vaccineproduce")
    totallivessaved_data = calculate_totallivessaved_data(livessaved_columns)
    update_worksheet(totallivessaved_data, "totallivessaved")


print("Welcome to Vaccines Africa Data Automation")
main()
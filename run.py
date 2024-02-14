import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('ironworks-414114-a4b4bfe9cf94.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('The Ironworks')

def get_sales_data():
    """ sales data input from user """
    print("Please enter sales data.")
    print("Data should be nine numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60,70,80,90\n")
    
    data_str = input("Enter data here:")
    
    sales_data = data_str.split(",")
    
    if validate_data(sales_data):
        print("Data is Valid")
        breakpoint
        
    return sales_data
    

def validate_data(values):
    """ create value error if not enough numbers """
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(f"9 values needed, you entered {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, Please re-enter.\n")
        return False
    
    return True

def update_sales_worksheet(data):
    """ update sales worksheet with new row data """
    print("Updating sales...\n")
    sales_worksheet = SHEET.worksheet("Weekly_Sales")
    sales_worksheet.append_row(data)
    print("Sales updated successfully.\n")

def update_surplus_worksheet(data):
    """ update surplus worksheet with new row data """
    print("Updating surplus...\n")
    surplus_worksheet = SHEET.worksheet("Daily_Surplus")
    surplus_worksheet.append_row(data)
    print("Surplus updated successfully.\n")
        
def calculate_surplus_data(sales_row):
    """ compare sales and stock to define surplusb """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("Stock_View").get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
        
    return surplus_data
    
def main():
    """ program functions """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)
    
print("Welcome to Eddies Ironworks automation suite")
main()

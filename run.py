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
SHEET = GSPREAD_CLIENT.open('The Ironworks')

def get_sales_data():
    """ sales data input from user """
    while True:
        print("Please enter sales data.")
        print("Data should be nine numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60,70,80,90\n")
        data_str = input("Enter data here:\n")
        sales_data = data_str.split(",")
    
        if validate_data(sales_data):
            print("Data is Valid!")
            break
        
    return sales_data
    
def validate_data(values):
    """ create value error if not enough numbers """
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(
                f"Exactly 9 values needed, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, Please ReEnter.\n")
        return False
    
    return True

def update_worksheet(data, worksheet):
    """ function to update the correct worksheet """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n") 
           
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

def get_last_5_entries_sales():
    """ merge sales data into stock data function """
    sales = SHEET.worksheet("Weekly_Sales")
    
    columns = []
    for ind in range(1, 10):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns
    
def calculate_stock_data(data):
    """ calculate stock average, adding 30% """
    print("Calculating stock data...\n")
    new_stock_data = []
    
    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 3.3
        new_stock_data.append(round(stock_num))
        
    return new_stock_data
    
def main():
    """ program functions """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "Weekly_Sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "Daily_Surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "Stock_View")
    
    
print("Welcome to Eddies Ironworks automation suite")
main()

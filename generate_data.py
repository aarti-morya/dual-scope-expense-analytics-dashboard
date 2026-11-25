# Import basic modules required for handling CSV files and generating random data
import csv
import random
from datetime import datetime, timedelta

print("Starting to create expense data...")


# 1. PERSONAL EXPENSES DATA (500 Rows)

# Define categories and payment modes that we will use randomly
categories_personal = ['Food', 'Rent', 'Utilities', 'Shopping', 'Entertainment', 'Healthcare']
payment_modes = ['UPI', 'Credit Card', 'Debit Card', 'Cash']

# Create an empty list to store all the rows
personal_rows = []

# Add the header row (column names)
personal_rows.append(['Transaction_ID', 'Transaction_Date', 'Category', 'Amount', 'Payment_Mode', 'Scope'])

# Simple for loop to generate 500 records
for i in range(1, 501):
    # Create transaction ID like PER-1, PER-2...
    trans_id = "PER-" + str(i)
    
    # Generate a random date from the past few days
    days_ago = random.randint(1, 180)
    date_obj = datetime.now() - timedelta(days=days_ago)
    trans_date = date_obj.strftime('%Y-%m-%d')
    
    # Select a random category, amount, and payment mode
    category = random.choice(categories_personal)
    amount = round(random.uniform(200, 15000), 2)
    mode = random.choice(payment_modes)
    scope = 'Personal'
    
    # Put values into a list and add it to the main list
    row = [trans_id, trans_date, category, amount, mode, scope]
    personal_rows.append(row)

# Save the data into 'personal_expenses_cleaned.csv' file
with open('personal_expenses_cleaned.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(personal_rows)

print("Personal expenses CSV file is ready!")



# 2. CORPORATE EXPENSES DATA (500 Rows)

departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Operations']
categories_corp = ['Travel', 'Software', 'Office Supplies', 'Client Dinner']
statuses = ['Approved', 'Pending', 'Rejected']

corp_rows = []
corp_rows.append(['Transaction_ID', 'Transaction_Date', 'Department', 'Category', 'Amount', 'Approval_Status', 'Scope'])

for i in range(1, 501):
    trans_id = "CORP-" + str(i)
    
    days_ago = random.randint(1, 180)
    date_obj = datetime.now() - timedelta(days=days_ago)
    trans_date = date_obj.strftime('%Y-%m-%d')
    
    dept = random.choice(departments)
    category = random.choice(categories_corp)
    amount = round(random.uniform(1500, 75000), 2) # Larger amounts for corporate expenses
    status = random.choice(statuses)
    scope = 'Corporate'
    
    row = [trans_id, trans_date, dept, category, amount, status, scope]
    corp_rows.append(row)

# Save the data into 'corporate_expenses_cleaned.csv' file
with open('corporate_expenses_cleaned.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(corp_rows)

print("Corporate expenses CSV file is ready!")
print("Both files created successfully!")
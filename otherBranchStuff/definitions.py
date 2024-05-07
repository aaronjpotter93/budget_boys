import csv

# Define month names
def get_month_name(month_as_digit):
    month_names = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    }
    return month_names.get(month_as_digit, 'Invalid Month')

# Define expected categories and their order
expected_categories = [
    'Gas',
    'Healthcare',
    'Bills',
    'Rent',
    'Car Maintenance',
    'Groceries',
    'Restaurants & Drinks',
    'Recreation',
    'Dates',
    'Personal',
    'Gifts',
]

# Define your category mapping for ICCU CSV
category_mapping = {
    'Clothing': 'Personal',
    'Telephone Services': 'Bills',
    'Utilities': 'Bills',
    'Insurance': 'Bills',
    'Cable & Satellite': 'Bills',
    'Printing': 'Gifts',
    'Hobbies': 'Gifts',
    'Gasoline/Fuel': 'Gas',
    'Entertainment': 'Recreation',
    'Govt-services-parking': 'Parking',
    'Grocery': 'Groceries',
    'Restaurants & Dining': 'Restaurants & Drinks',
    'Restaurants': 'Restaurants & Drinks',
    'Personal Care & Fitness': 'Healthcare',
    'Healthcare & Pharmacy': 'Healthcare',
    # Add more mappings as needed
}

# Define your merchant mapping for Apple CSV
merchant_mapping = {
    'SP Kinjaz Store Us': 'Personal',
    'SP Ensorings': 'Personal',
    'Apple Services': 'Bills',
    'Walgreens': 'Healthcare',
    'Rps*Cortland At Ten': 'Rent',
    'Steamgames.com 4259522': 'Personal',
    'Nintendo Ca925360032': 'Personal',
    'Cortland At Ten Mil': 'Rent',
    'Amazon Payments': 'Personal',
    'Vioc 090138': 'Car Maintenance',
    'Campus Stre (Paypal)': 'School',
    'Target': 'Shopping',
    'R.c. Willey': 'Furnishing',
    # Add more mappings as needed
}

# Define description mapping for ICCU CSV
description_mapping = {
    'ACH Deposit 1x123-SILVER CRE XX54 - DIRDEP': 'Income'
}

memo_mapping = {
    'Date Night': 'Dates',
    'Pixie Haircut and Paste': 'Healthcare',
    'Gifts': 'Gifts',
    'Gift': 'Gifts',
    'Date': 'Dates',
    'Dates': 'Dates',
    'Food': 'Restaurants & Drinks',
}

# Define the categories to exclude
excluded_categories = {'Deposits', 'Credit Card Payments', 'Transfers', 'Payment', 'Paychecks/Salary'}

def get_income_from_csv(file_path):
    income = 0  # Initialize income as 0
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            if row['Transaction Category'] == 'Paychecks/Salary':
                income += float(row['Amount'])  # Add to income if necessary

            if row['Transaction Category'] == 'Deposits':
                description = row['Description']
                mapped_category = description_mapping.get(description)
                if mapped_category == 'Income':
                    income += float(row['Amount'])  # Add to income if necessary

    return income  # Return income after going through all rows

    return 0  # Return 0 if no income is found

# Define a function to process ICCU CSV
def process_iccu_csv(file_path, summary):
    with open(file_path, 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            date = row['Posting Date']
            amount = float(row['Amount'])
            original_category = row['Transaction Category']
            memo = row['Memo']
            if memo:
                category = memo_mapping.get(memo, category_mapping.get(original_category, original_category))
            else:
                category = category_mapping.get(original_category, original_category)
            if category in excluded_categories:
                continue
            summary['Total'] += amount
            if category not in summary['Categories']:
                summary['Categories'][category] = 0
            summary['Categories'][category] += amount

# Define a function to process Apple CSV
def process_apple_csv(file_path, summary):
    with open(file_path, 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            if 'Transaction Date' in row:
                date = row['Transaction Date']
                amount = -float(row['Amount (USD)'])
                original_merchant = row['Merchant']
                original_category = row['Category']
                if original_category == 'Other' or original_category == 'Shopping':
                    category = merchant_mapping.get(original_merchant, original_merchant)
                else:
                    category = category_mapping.get(original_category, original_category)
                if category in excluded_categories:
                    continue
                summary['Total'] += amount
                if category not in summary['Categories']:
                    summary['Categories'][category] = 0
                summary['Categories'][category] += amount

    # Round the total spendings per category to the nearest cent
    summary['Total'] = round(summary['Total'], 2)
    for category in summary['Categories']:
        summary['Categories'][category] = round(summary['Categories'][category], 2)


# Write to CSV file
def write_summary_to_csv(output_csv_path, month, income, summary, expected_categories):
    with open(output_csv_path, 'w', newline='') as output_csv_file:
        csv_writer = csv.writer(output_csv_file)

        # Write Month of transactions
        csv_writer.writerow(['Month', month])

        # Write income
        csv_writer.writerow(['Income', f'{income:.2f}'])

        # Write total spendings
        csv_writer.writerow(['Total Spendings', summary['Total']])

        # Write surplus/deficit
        csv_writer.writerow(['Surplus/Deficit', f'{income + summary["Total"]:.2f}'])

        # Write empty row
        csv_writer.writerow([])

        # Write header
        csv_writer.writerow(['Category', 'Total'])

        # Write data for all categories
        for category in expected_categories:
            csv_writer.writerow([category, summary['Categories'][category]])

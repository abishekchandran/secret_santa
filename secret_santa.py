import pandas as pd
import random

"""
Function: secret_santa

Description:
    This function simulates a Secret Santa game assigning each employee from the provided list to another employee randomly, ensuring that no one is assigned to themselves or to the same person as the previous year. It takes two pandas DataFrames as input: employee_list, which contains information about employees including their email IDs, and prev_year_santa, which contains the results of the previous year's Secret Santa game. It then returns a modified DataFrame with new columns indicating the assigned Secret Santa for each employee.

Parameters:
    - employee_list: pandas DataFrame
        DataFrame containing employee information including their email IDs.
    
    - prev_year_santa: pandas DataFrame
        DataFrame containing the results of the previous year's Secret Santa game.
        
Returns:
    - output_santa: pandas DataFrame
        DataFrame with new columns indicating the assigned Secret Santa for each employee.
        
Error Handling:
    - If an employee from the current year's list is not found in the previous year's Santa list, it prints an error message and continues.
    
    - If there are no available employees for a particular individual, it prints an error message and skips the assignment for that employee.
    
    - Handles file-not-found errors for input files.

Imports:
    - pandas as pd: Library for data manipulation and analysis.
    - random: Library for generating random numbers.
"""

class SecretSantaGame:
    def __init__(self, employee_list_file, prev_year_santa_file):
        self.employee_list = self.read_excel(employee_list_file)
        self.prev_year_santa = self.read_excel(prev_year_santa_file)
        
    def read_excel(self, filename):
        return pd.read_excel(filename)
    
    def secret_santa(self):
        output_santa = self.employee_list.copy()
        new_columns = ['Secret_Child_Name', 'Secret_Child_EmailID', 'Assigned']
        for col in new_columns:
            if col == 'Assigned':
                output_santa[col] = False
            else:
                output_santa[col] = ''
        
        for i in range(0, len(output_santa)):
            available_employees = output_santa.loc[~output_santa['Assigned'], 'Employee_EmailID'].tolist()
            self_email = output_santa.iloc[i]['Employee_EmailID']
            
            try:
                previous_year_santa_email = self.prev_year_santa.loc[self.prev_year_santa['Employee_EmailID'] == self_email, 'Secret_Child_EmailID'].iloc[0]
                available_employees = [x for x in available_employees if x not in (self_email, previous_year_santa_email)]
            except IndexError:
                print(f"Error: Employee with email '{self_email}' not found in previous year's Santa list.")
                continue
        
            if not available_employees:
                print(f"Error: No available employees for {self_email}. Skipping.")
                continue
            
            secret_santa = random.choice(available_employees)
            output_santa.loc[output_santa['Employee_EmailID'] == secret_santa, 'Assigned'] = True
            output_santa.at[i, 'Secret_Child_EmailID'] = secret_santa
            output_santa.at[i, 'Secret_Child_Name'] = self.employee_list.loc[self.employee_list['Employee_EmailID'] == secret_santa, 'Employee_Name'].iloc[0]
        
        output_santa = output_santa.drop(columns='Assigned')
        return output_santa

try:
    secret_santa_game = SecretSantaGame('Employee-list.xlsx', 'Secret-Santa-Game-Result-2023.xlsx')
    output_santa = secret_santa_game.secret_santa()
    
    output_filename = 'output_secret_santa.csv'
    output_santa.to_csv(output_filename, index=False)
    print(f"Secret Santa assignments saved to {output_filename}.")
    
except FileNotFoundError:
    print("Error: Input file not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

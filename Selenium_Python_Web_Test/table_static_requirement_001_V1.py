"""
Go to
https://testautomationpractice.blogspot.com/
page
"""
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#waiting for target element presence
WebDriverWait(driver, 9).until(EC.presence_of_element_located((By.XPATH, "//table[@name='BookTable']")))
driver.set_window_rect( 25,29,808,960)

#getting webelement and scrolling down to it
table = driver.find_element(By.XPATH, "//table[@name='BookTable']")
action = ActionChains(driver)
action.move_to_element(table).perform()

# //table[@name='BookTable']//tr/th  ----------all headeres
# //table[@name='BookTable']//tr"    ----------- all rows
# //table[@name='BookTable']//tr//td[col_index]---------- specific column

# //table[@name='BookTable']//tr/th[col_index]  -------through headers
# //table[@name='BookTable']//tr[row_index]/td[col_index] --------through cell value

col_elemnts = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
col_cnt = len(col_elemnts)      #4
print(col_cnt)

#below code is getting row_cint including header need to minus one row
row_elemnts = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
row_cnt = len(row_elemnts)-1
print(row_cnt)

columns_elemnts = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
columns_names = [i.text for i in columns_elemnts]
print(columns_names)

search_col = 'Author'
search_val = 'Mukesh'
def get_table_rows_by_column_and_value_in_it(search_col:str, search_val:str):
    for col_index in range(1,col_cnt+1):                #search through col header by increasing col_index
        if search_col == driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr/th[{col_index}]").text :
            temp_row = []                               #creating empty list to catch row data
            for row_index in range(2,row_cnt+2):        #search through column data by increasing row_index and constant col_index
                if search_val == driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{row_index}]/td[{col_index}]").text :
                    if len(temp_row) != 0:              #deleting row_data before loading it with new row_data
                        temp_row.clear()
                    for cel in range(1,col_cnt+1):      #Search through row for selected row by increasing cell value
                        row_element = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{row_index}]/td[{cel}]")
                        cel_value = row_element.text
                        temp_row.append(cel_value)      #Appending cell value to row_data list
                    #creating
                    result_data = dict(zip(columns_names,temp_row))
                    print(result_data)


get_table_rows_by_column_and_value_in_it('Author','Mukesh')
# {'BookName': 'Learn Java', 'Author': 'Mukesh', 'Subject': 'Java', 'Price': '500'}
# {'BookName': 'Master In Selenium', 'Author': 'Mukesh', 'Subject': 'Selenium', 'Price': '3000'}

get_table_rows_by_column_and_value_in_it('Subject','Selenium')
# {'BookName': 'Learn Selenium', 'Author': 'Amit', 'Subject': 'Selenium', 'Price': '300'}
# {'BookName': 'Master In Selenium', 'Author': 'Mukesh', 'Subject': 'Selenium', 'Price': '3000'}


#getting higest priced book details
#step One finding higest value from Price column
# //table[@name='BookTable']//tr//td[4]     ------- search through price columns
price_col_values = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr//td[4]")
price_col_values = [int(i.text) for i in price_col_values]
max_price = str(max(price_col_values))
print(max_price)

get_table_rows_by_column_and_value_in_it('Price',max_price)
# {'BookName': 'Master In Selenium', 'Author': 'Mukesh', 'Subject': 'Selenium', 'Price': '3000'}
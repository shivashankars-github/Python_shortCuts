
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

url = 'https://testautomationpractice.blogspot.com/'
table_locator = "//table[@name='BookTable']"

driver = webdriver.Chrome()
driver.get(url)

#waiting for target element presence
WebDriverWait(driver, 9).until(EC.presence_of_element_located((By.XPATH, "//table[@name='BookTable']")))
# driver.get_window_position()
# driver.set_window_rect({'x': 4, 'y': 4, 'width': 1292, 'height': 978})
# driver.get_window_size()
# driver.set_window_rect( -5,0,970,1085)
driver.set_window_rect( 25,29,808,960)


#getting webelement and scrolling down to it
table = driver.find_element(By.XPATH, "//table[@name='BookTable']")
action = ActionChains(driver)
action.move_to_element(table).perform()


#get table header values as list
columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th")
columns = [i.text for i in columns]
print(columns)  # ['BookName', 'Author', 'Subject', 'Price']

#get columns count
col_cnt = len(columns) #4


#get all rows and find total rows in table
all_rows = "//table[@name='BookTable']/tbody//tr"
all_rows = driver.find_elements(By.XPATH, all_rows)
all_rows = [i.text for i in all_rows]
print("total records in table including header row : ", len(all_rows))
print(all_rows)


#Find specific row and get it'ts data as list
#And create dictionary as {col:value, ....}
first_row = "//table[@name='BookTable']/tbody//tr[2]/td"
first_row = driver.find_elements(By.XPATH, first_row)
first_row = [i.text for i in first_row]
print(first_row)
# ['Learn Selenium', 'Amit', 'Selenium', '300']
first_row_with_col_names = [i for i in zip(columns,first_row)]
print(first_row_with_col_names)


#Iterate through all cell values and create a dict
all_cells = "//table[@name='BookTable']/tbody//tr/td"
all_cell_values = driver.find_elements(By.XPATH, all_cells)
all_cell_values = [i.text for i in all_cell_values]
print(all_cell_values)


#get all rows with column names
#step one : getting every row as list values
data_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody//tr/following-sibling::tr")
data_row_count = len(data_rows)
data_rows = []
for j in range(2,data_row_count+2):
    data_row = driver.find_elements(By.XPATH, f"//table[@name='BookTable']/tbody//tr[{j}]//td")
    data_row = [i.text for i in data_row]
    data_rows.append(data_row)


#step two : binding all rows with column values
table_data = []
for i,row in enumerate(data_rows):
    for col in columns:
        rows = [i for i in zip(columns,row)]
        table_data.append(rows)
        break

print(table_data)
        # [('BookName', 'Learn Selenium'), ('Author', 'Amit'), ('Subject', 'Selenium'), ('Price', '300')]
        # [('BookName', 'Learn Java'), ('Author', 'Mukesh'), ('Subject', 'Java'), ('Price', '500')]
        # [('BookName', 'Learn JS'), ('Author', 'Animesh'), ('Subject', 'Javascript'), ('Price', '300')]
        # [('BookName', 'Master In Selenium'), ('Author', 'Mukesh'), ('Subject', 'Selenium'), ('Price', '3000')]
        # [('BookName', 'Master In Java'), ('Author', 'Amod'), ('Subject', 'JAVA'), ('Price', '2000')]
        # [('BookName', 'Master In JS'), ('Author', 'Amit'), ('Subject', 'Javascript'), ('Price', '1000')]


# Creating a fucntion which gives entire row data depending on given col and val
def find_entire_row_using_given_col_vale(col,val,data):
    for i in range(len(data)):
        for j in range(len(table_data[i])):
            if (data[i][j]) == (col,val):
                return(data[i])


# result2 = find_entire_row_using_given_col_vale('Price','300',table_data)
# print(result2)

expected = [('BookName', 'Learn JS'), ('Author', 'Animesh'), ('Subject', 'Javascript'), ('Price', '300')]
result = find_entire_row_using_given_col_vale('Author','Animesh',table_data)
assert result == expected

driver.quit()

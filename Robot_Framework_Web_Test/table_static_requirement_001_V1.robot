*** Settings ***
Documentation    This test suite identifies gieven table from a webpag and verifies given column/ cell value existance
Library     SeleniumLibrary
Library    Collections


*** Variables ***
# Having variables in YML files and importing them into test suite file is a good practice
# here we are hardcoding inside this suite
${browser}    chrome
${url}        https://testautomationpractice.blogspot.com/
${table}      xpath://table[@name='BookTable']
${column}    BookName
${search_value}    Learn JS


*** Test Cases ***
Get table data from a given table
    [Documentation]    Get's table data and verifies column name and a given cell value
    Open browser and login page    ${url}    ${browser}
    page should contain talbe   ${table}
    table should contain given column     ${column}
    table should contain book    ${search_value}


*** Keywords ***
Open browser and login page
    [Arguments]    ${url}    ${browser}
    SeleniumLibrary.Open Browser    ${url}    ${browser}

page should contain talbe
    [Arguments]    ${table}
    SeleniumLibrary.Scroll Element Into View    ${table}
    ${cnt}    SeleniumLibrary.Get Element Count    ${table}
    BuiltIn.Should Be Equal    ${cnt}    ${1}


table should contain given column
    [Arguments]    ${column}
    SeleniumLibrary.Table Header Should Contain    ${table}    ${column}

table should contain book
    [Arguments]    ${search_value}
    SeleniumLibrary.Table Should Contain    ${table}     ${search_value}


get columns values as list
    [Documentation]    this keyword takes table header locator and returns column names list
    [Arguments]    ${header_locator}
    @{header_web_elements}=    SeleniumLibrary.Get WebElements  ${header_locator}
    @{headers_list}=     BuiltIn.Create List
    FOR    ${Index}    ${ele}    IN ENUMERATE     @{header_web_elements}    start=1
        ${cel_value}    SeleniumLibrary.Get Table Cell    ${table}    row=${1}    column=${Index}
        Collections.Append To List    ${headers_list}    ${cel_value}
    END
    RETURN  ${headers_list}


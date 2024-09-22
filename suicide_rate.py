#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Noah Burra
Suicide Rates in Countries
Use repository data to visualize and interpret suicide rates from 2000-2016
in various countries. Show how the rates vary from third-world and 
modern/western countires as well as their respective sex comparisons.
"""
import matplotlib.pyplot as plt

def read_suicide_data(filename, header=0, delimiter=","):
    """
    Read the suicide data CSV file into a list of lists.
    filename: CSV file
    header: first line
    delimiter: seperator in data
    return: table of all countries
    """
    table = []

    with open(filename, "r") as file:
        
        for i in range(header):
            file.readline()
            
        lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            values = line.split(delimiter)
            row = []
            
            for value in values:
                try:
                    convert_value = float(value)
                except ValueError:  
                    convert_value = value  
                    
                row.append(convert_value)
                
            table.append(row)
            
    return table

def select_country(table, country_name):
    """
    Select specific country to compare across countries in table.
    table: output of read_suicide_data
    country_name: specific country chosen
    return: rate data of chosen country
    """
    both_sex = []
    male = []
    female = []
   
    for row in table:
        if row[0].strip() == country_name:
            sex = row[1].strip()
            if sex == "Both sexes":
                both_sex = row
            elif sex == "Male":
                male = row
            elif sex == "Female":
                female = row
   
    return both_sex, male, female
    
def main():
    table = read_suicide_data("suicide_data.csv", header=1, delimiter=",")
    
    afg_both, afg_male, afg_female = select_country(table, "Afghanistan")
    usa_both, usa_male, usa_female = select_country(table, 
                                                    "United States of America")
    
    
    years = ["2000", "2005", "2010", "2015"]
    
    afg_both = afg_both[2:] 
    afg_male = afg_male[2:] 
    afg_female = afg_female[2:]

    usa_both = usa_both[2:] 
    usa_male = usa_male[2:]
    usa_female = usa_female[2:] 
        
    plt.figure(figsize=(12, 6))
    plt.plot(years, usa_both, marker="x", linestyle=":", label="USA(Both sexes)")
    plt.plot(years, usa_male, marker="x", linestyle=":", label="USA(Male)")
    plt.plot(years, usa_female, marker="x", linestyle=":", label="USA(Female)")
    
    plt.plot(years, afg_both, marker="o", label="Afghanistan(Both sexes)")
    plt.plot(years, afg_male, marker="o", 
             label="Afghanistan(Male)")
    plt.plot(years, afg_female, marker="o", 
             label="Afghanistan(Female)")
    
    plt.title("Suicide Rates in Afghanistan vs America")
    plt.xlabel("Years")
    plt.ylabel("Suicide Rates")
    plt.grid(True)
    plt.legend()
    plt.savefig("suicide_rate.png")
    plt.show()
    
    print("Interpretation: The graph compares the suicide rates of Afghanistan (a developing country) and the United States (a developed country). This data is crucial because it highlights significant differences in suicide rates between these two countries. Specifically, the trend for both sexes in the United States shows a clear decrease from 2000 to 2015, whereas Afghanistan exhibits an increase. This disparity may be due to differences in healthcare systems. Afghanistan's healthcare system is less developed and lacks resources for mental health care, while the United States has a more advanced healthcare infrastructure with greater access to mental health services. Additionally, the comparison between male and female suicide rates reveals that, in the United States, both genders show a decreasing trend, aligning with the overall decline in suicide rates for both sexes. Conversely, Afghanistan shows a notable increase in the male suicide rate, while the female rate remains relatively stable with a minor decrease.")

main()

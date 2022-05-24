import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change my working directory to where the data is. Just like cd in Unix.
os.chdir("E:\semester 2\cygwin\home\86180\IBI1\IBI1_2021-22\Practical7")
#use panda module to read csv documentation as covid_data.
covid_data = pd.read_csv("full_data.csv")

#Use iloc to use numeric order to choose, and [10:21,[0,2]] to choose what is need
covid_data.iloc[10:21,[0,2]]
print('the first and third columns from rows 10-20: ', covid_data.iloc[10:21, [0, 2]])

#Use Boolean to select the total cases in Afghanistan
print('total cases in Afghanistan:\n', covid_data.loc[covid_data['location'] == "Afghanistan", "total_cases"])

china_new_data = covid_data.loc[covid_data['location'] == 'China', ['date', 'new_cases', 'new_deaths']]
# calculate the mean number of new cases and new deaths in China.
mean_cases = np.mean(china_new_data['new_cases'])
mean_deaths = np.mean(china_new_data['new_deaths'])
print('Mean value of new cases in China is', mean_cases)
print('Mean value of new deaths in China is', mean_deaths)
china_dates = china_new_data['date']
china_new_cases = china_new_data['new_cases']
china_new_deaths = china_new_data['new_deaths']


# a boxplot to describe new cases and new deaths in China
plt.boxplot([china_new_cases, china_new_deaths], labels=['new cases', 'new deaths'])
plt.title('China new cases and deaths')
plt.ylabel('scaled number')
plt.yscale('log')
plt.show()

# a plot of both new cases and new deaths in China over time
plt.plot(china_dates, china_new_cases, 'r-')
plt.plot(china_dates, china_new_deaths, 'b-')
plt.xlabel('dates')
plt.ylabel('numbers')
plt.title('China new cases and deaths over time')
plt.xticks(china_dates.iloc[0:len(china_dates):3], rotation=-45) #note the date at the length of 3 days
plt.legend(['new cases', 'new deaths']) #give the annotation of the line
plt.show()


#answer for question
#Use Boolean variable to select the data of Canada
Canada_covid_data=covid_data.loc[covid_data['location'] == "Canada",]
Canada_dates = Canada_covid_data['date']
Canada_total_cases = Canada_covid_data['total_cases']
Canada_total_deaths = Canada_covid_data['total_deaths']
plt.plot(Canada_dates, Canada_total_cases, 'r*')
plt.plot(Canada_dates, Canada_total_deaths, 'b*')
plt.ylabel('number')
plt.xlabel('date')
plt.title('Canada total cases and deaths over time')
plt.xticks(Canada_dates.iloc[0:len(Canada_dates):3], rotation=-90) 
plt.legend(['total cases', 'total deaths'])
plt.show()

import pandas as pd
#Reading File
df = pd.read_csv('adult.data.csv')

#Finding how many of each race in the dataset
race = pd.Series(df['race']).value_counts()
#print(race)

#Calculating the average age of males
males = df[df['sex'] == 'Male']
age_list = males['age']
average_age_males = age_list.mean()
#print('The average age of males is ', average_age_males)

#Calculating % of people that have a Bachelors Degree (dec_num)
degrees = pd.Series(df['education']).value_counts()
total_edu = degrees.sum()
bach = degrees.loc['Bachelors']
percent = bach / total_edu
dec_num = percent * 100
#print(f"There are {round(dec_num,1)}% of people that have a Bachelor's Degree")

#Calculating % of people with advanced degrees (B.S, M.S, & PhD) make more than 50k
adv_deg = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
salary = adv_deg['salary']
salary_counts = salary.value_counts()
total_salary = salary_counts[0] + salary_counts[1]
over_fifty = salary_counts[1] / total_salary
over_fifty_percent = over_fifty * 100
#print(f"There are {round(over_fifty_percent,1)}% of advanced degree holders that make over 50k in salary")

#Finding minimum number of hours that someone works a week
hours = df['hours-per-week'].min()
#print(f"The minimum number of hours worked by someone is {hours}")

#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
#print(adv_deg)
min_workers = df[df['hours-per-week'] == 1]
min_workers_sal = min_workers['salary']
min_sal_count = min_workers_sal.value_counts()
total_min_workers = min_sal_count[0] + min_sal_count[1]
min_workers_rich_percent = (min_sal_count[1] / total_min_workers) * 100
#print(f"The proportion of workers that work {hours} hour per week that make more than 50K is {min_workers_rich_percent}%")

#What country has the highest percentage of people that earn >50K and what is that percentage?

countries = df['native-country']
#United States %
USA = df[df['native-country'] == 'United-States']
USA_salary = USA['salary']
USA_salary_count = USA_salary.value_counts()
USA_tot = USA_salary_count[0] + [1]
USA_perc = (USA_salary_count[1] / USA_tot) * 100

#print(countries.value_counts())

df2 = df[['native-country', 'salary']]
country_list = df2['native-country'].value_counts()


#Identify the most popular occupation for those who earn >50K in India.
india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
india_job = india[['native-country', 'occupation']]
india_job_count = india_job['occupation'].value_counts()

maxnum = india_job_count.index[0]
print(maxnum)












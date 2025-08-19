import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    
    race_count = df['race'].value_counts()
    #print(race_count)

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', ['age']].mean()['age'].round(1)
    #print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'].value_counts()['Bachelors']/df['education'].count()*100).round(1)

    #print(percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    high_edu = ['Bachelors', 'Masters','Doctorate']

    #total number of rows that satisfies "high_edu"
    total_high_edu = df.loc[df['education'].isin(high_edu)].count()['education']

    total_low_edu = df.loc[~df['education'].isin(high_edu)].count()['education']

    total_rows = df.count()['education']

    higher_education = total_high_edu/total_rows*100
    lower_education = total_low_edu/total_rows*100

    #print("higher_education:", higher_education)
    #print("lower_education:", lower_education)

    # percentage with salary >50K

    #number of rows that satisfies "high_edu" and has salary >50K
    total_high_edu_rich = df.loc[df['education'].isin(high_edu), 'salary'].value_counts()['>50K']
    higher_education_rich = (total_high_edu_rich/total_high_edu*100).round(1)

    total_low_edu_rich = df.loc[~df['education'].isin(high_edu), 'salary'].value_counts()['>50K']
    lower_education_rich = (total_low_edu_rich/total_low_edu*100).round(1)

    #print("higher_education_rich", higher_education_rich)
    #print("lower_education_rich", lower_education_rich)

    


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    #print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    #minimum hours worked per week
    min_hours = df['hours-per-week'].min()
    #number of workers that work min hours 
    num_min_workers = df['hours-per-week'].value_counts()[min_hours]
    #table of these minimum workers
    min_workers = df.loc[df['hours-per-week'] == min_hours]
    #number of these workers that earn more than 50K
    num_min_rich_workers = min_workers['salary'].value_counts()['>50K']
    #percentage of the people that work minimum hours and earn > 50K         
    rich_percentage = num_min_rich_workers/num_min_workers*100

    #print(num_min_workers)
    #print(min_workers)
    #print(num_min_rich_workers)
    #print(rich_percentage)

    # What country has the highest percentage of people that earn >50K?

    #counts the number of people in each country
    num_people_countries = df['native-country'].value_counts()
    #print(num_people_countries)

    #counts how many people in each country earn more than 50K
    rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    #print(rich_counts)

    #the percentage of rich people in each country
    rich_pct_by_country = (rich_counts / num_people_countries * 100).fillna(0)


    #takes the country in the previous series (rich_pct_by_country) that has the highest percentage
    highest_earning_country = rich_pct_by_country.idxmax()
    #print("highest_earning_country", highest_earning_country)

    #takes the percentage from the highest paying country
    highest_earning_country_percentage = rich_pct_by_country.max().round(1)
    #print("highest_earning_country_percentage", highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.

    #finds occupations from those who have a salary higher than 50K and are indian
    indian_rich = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts()
    #print(indian_rich)

    #shows the title of the highest value (occupation with most people)
    top_IN_occupation = indian_rich.idxmax()
    #print(top_IN_occupation)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()

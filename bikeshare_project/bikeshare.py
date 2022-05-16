import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH = pd.Series({'january': 1, 'february': 2, 'march': 3, 
                   'april': 4, 'may':5, 'june': 6})

WEEKDAY = pd.Series({'monday': 0, 'tuesday':1, 'wednesday':2, 'thursday':3,
                    'friday': 4, 'saturday': 5, 'sunday': 6})

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    print('NOTE: if you want to exit at any time press(ctrl + c).\n')
    
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input("Enter the city to explore(Chicago, New York, Washington): ").strip().lower()
        if city not in CITY_DATA:
            print('\nPlease enter one of the cities from the list.')
            print("your input should be one of the following:", end=' ')
            print(*CITY_DATA, sep=', ')
            continue
        break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month(full name of the month january:june) or (all): ").strip().lower()
        if month not in MONTH and month != 'all':
            print("\nMake sure you wrote the name of the month correctly: ")
            print("your input should be one of the following:", end=' ')
            print('all', *MONTH.index, sep=', ')
            continue
        break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day (full name of the day) or (all): ").strip().lower()
        if day not in WEEKDAY and day != 'all':
            print("\nMake sure you wrote the name of the day correctly.")
            print("your input should be one of the following:", end=' ')
            print('all', *WEEKDAY.index, sep=', ')
            continue
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # generate month and day_of_week columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    
    try:
        df['Age'] = df['Start Time'].dt.year - df['Birth Year']
    except KeyError:
        pass

    # filter by month
    if month != 'all':
        df = df.loc[df['month'] == MONTH[month]]

    # filter by weak
    if day != 'all':
        df = df.loc[df['day_of_week'] == WEEKDAY[day]]
    
    return df


def tabular_print(*to_disp):
    """Displays the arguments in a table like format."""
    n = len(to_disp)
    st = "{:35} "*n
    print(st.format(*to_disp))

def readable_time(t: float) -> str:
        """Returns time in a human-readable format"""
        t = round(t)
        return str(datetime.timedelta(seconds=t)) 
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    freq_month = df['month'].value_counts().index[0]
    freq_month = MONTH.index[freq_month - 1].title()
    tabular_print(" - The most common month:", freq_month)

    # display the most common day of week
    freq_day = df['day_of_week'].value_counts().index[0]
    freq_day = WEEKDAY.index[freq_day].title()
    tabular_print(" - The most common day:", freq_day)

    # display the most common start hour
    freq_hour = df['Start Time'].dt.hour.value_counts().index[0]
    freq_hour = datetime.time(freq_hour).strftime("%I:00 %p")
    tabular_print(" - The most common hour:", freq_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    comm_start = df['Start Station'].value_counts().index[0]
    tabular_print(" - The most common start station:", comm_start)

    # display most commonly used end station
    comm_end = df['End Station'].value_counts().index[0]
    tabular_print(" - The most common end station:", comm_end)

    # display most frequent combination of start station and end station trip
    comm_trip = df[['Start Station', 'End Station']].value_counts().index[0]
    tabular_print(" - The most common trip:", f"{comm_trip[0]}  -->  {comm_trip[-1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tt_total = readable_time(df['Trip Duration'].sum())
    tabular_print(" - The total travel time:", tt_total)
    
    # display mean travel time
    tt_mean = readable_time(df['Trip Duration'].mean())
    tabular_print(" - The mean travel time:", tt_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User type counts...")
    type_counts = df['User Type'].value_counts()
    tabular_print(" - Number of customers:", type_counts['Customer'])
    tabular_print(" - Number of subscribers:", type_counts['Subscriber'])
    # Display counts of gender
    
    try:
        print("\nGender counts...")
        gender_counts = df['Gender'].value_counts()
        tabular_print(" - Number of males:", gender_counts['Male'])
        tabular_print(" - Number of females:", gender_counts['Female'])
        # Display earliest, most recent, and most common year of birth
        print("\nBirth Year stats...")
        earliest = int(df['Birth Year'].min())
        tabular_print(" - The earliest year of birth:", earliest)
        recent = int(df['Birth Year'].max())
        tabular_print(" - The most recent year of birth:", recent)
        comm_year = int(df['Birth Year'].mode())
        tabular_print(" - The most common year of birth:", comm_year)
      
    except KeyError:
        print("\nno gender nor birth data available for the specified dataset.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def extra_stats(df):
    """Displays statistics on bikeshare user's ages."""
    
    print('\nCalculating extra User Stats...\n')
    start_time = time.time()
    # male and female average travel time
    mean_d = df.groupby(['Gender'])['Trip Duration'].mean().map(readable_time)
    print("\nGender average travel time comparison...\n")
    tabular_print("Gender", "Average Travel Time")
    tabular_print("Female", mean_d['Female'])
    tabular_print("Male", mean_d['Male'])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # the most frequent person
    start_time = time.time()
    print("The Most Frequent User Stats...")
    best_person= df[['Gender', 'Age']].value_counts().index[0]
    best_persons = df['Trip Duration'][(df['Gender'] == best_person[0]) & (df['Age'] == best_person[1])]
    bp_avg_tt, bp_max_tt, bp_min_tt = list(map(readable_time, [best_persons.mean(), best_persons.max(), best_persons.min()]))
    to_print = [(" - Gender:", best_person[0]),
                (" - Age:", int(best_person[-1])),
                (" - Average Travel Time:", bp_avg_tt),
                (" - Maximum Travel Time:", bp_max_tt),
                (" - Minimum Travel Time:", bp_min_tt)]
    
    for line in to_print:
        tabular_print(*line)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """Prompt the user if he want to disply 5 rows of the raw data and displays if he want"""
    i = 0
    pd.set_option("display.max_columns", 200)
    pd.set_option("display.max_rows", 20)
    while True:
        resp = input("Do you want to disply rows from the dataset: ").strip().lower()
        
        
        if resp == 'yes':
            # get the number of rows to be displayed
            while True:
                try:
                    n = int(input("How many rows you want to display [0:20]: ").strip())
                    if 20 < n < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("invalid input please enter a number in [0:20].")
            # there is at least n rows to disply
            if (i + n) <= df.shape[0]:
                print(df.iloc[i: i + n])
                i += n
                continue
            # exit the loop after displying the remaining < n rows or if no more rows
            elif (i + 1) < df.shape[0]:
                print(df.iloc[i:])
            print('No more rows to disply.')
            break
            
        elif resp == 'no':
            break
        else:
            print("invalid input your input should be either 'yes' or 'no'.")
        

def main():
    try:
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            if city != 'washington':
                extra_stats(df)
            
            show_data(df)
                
            while True:
                restart = input('\nWould you like to restart? Enter yes or no: ').strip().lower()
                print()
                
                if restart == 'yes':
                    break
                elif restart == 'no':
                    raise KeyboardInterrupt
                else:
                    print("invalid input your input should be either 'yes' or 'no'.")
                    
    except KeyboardInterrupt:
        print('\n','-'*40)
        print("\nGoodbye!\n")


if __name__ == "__main__":
	main()

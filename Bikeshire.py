import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?").lower()
        print("Looks like you want to hear about {}! If this is not true, restart the programme now!".format(city).title())
        if city not in ['chicago', 'new york city', 'washington']:
            print('No data has been found. Please try again.')
        else:
            break
    
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? all, January, February, March, April, May, or June?').lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('No data has been found. Please try again.')
            continue
        else:
            break
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday').lower()
        if day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            print('No data has been found. Please try again.')
            continue
        else:
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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    # filter by month to create the new dataframe    
        df = df[df['month'] == month]

    
    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is: ',popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most commonly used end station is: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['popular_trip'] = df['Start Station'] + '--' + df['End Station']
    print('The most popular trip is: ', df['popular_trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration']/60)
    print('Total travel time of your selection in minutes: ', round(total_travel_time, 1) )

    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()/60
    print('Average travel time of your selection in minutes: ', round(avg_travel_time, 1) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())
    print()

    # Display counts of gender
    try:
        print('Counts of gender:\n', df['Gender'].value_counts())
        print()
        # Display earliest, most recent, and most common year of birth
        print('User birth year stats:\n')
        print('Earliest year of birth: ', int(df['Birth Year'].min()))
        print('Youngest year of birth: ', int(df['Birth Year'].max()))
        print('Most common year of birth: ', int(df['Birth Year'].mode()[0]))
    except KeyError:
        print('Gender and birth year information is only available for New York City and Chicago.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    """Display raw data as requested"""
    f=0
    while True:
        if_raw = input('Would you like to see the raw data? Yes or No?')
        if if_raw.lower() == 'yes':
            print(df[f: f+5])
            f += 5
        else:
            break
        
            

def main():
    """Bind all functions together"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    


if __name__ == "__main__":
	main()

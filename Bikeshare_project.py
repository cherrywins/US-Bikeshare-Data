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
    # We get user's input for city (chicago, new york city, washington) using a while loop to handle invalid inputs
    while True:
        city = input("Please enter the city you want to know about. Right now we have statistics for Chicago, New York City and Washigton (DC)\n").lower().strip()
        if city in CITY_DATA.keys():
            break
        else:
            print('Please type the full name of the city. In case of Washington DC, you should type it without "DC" part\n')

    print(city.title() + ' is chosen!\n')    
    

    #  We get user's input for month (all, january, february, ... , june)
    while True:
        month = input("Now let's choose the month. The data is available for the first 6 months of 2017 year. You also can type 'all' if you don't want to filter the data by month \n").lower().strip()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print('Please type a full month\'s name. We have data available for the months from january till june\n')

    print(month.title() + ' is chosen!\n') 

    # We get user's input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Last but not the least. You can filter the data by day of the week! If you want to see data for all days, just type 'all'  \n").lower().strip()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        else:
            print('Please type a day\'s name without any abbreviation. Also, don\'t forget that we have data only for the first 6 months (january - june) \n')

    print(day.title() + ' is chosen!\n') 



    print('(^･ｪ･^)'*20)
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # We display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    popular_month_2 = months[popular_month -1]
    
    print('Most Popular Month:', popular_month_2.title())
    
    # We display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    
    print('Most Popular Day Of Week:', popular_day_of_week)


    # We display the most common start hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour, "h")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n','(^･ｪ･^)'*20)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().index[0]

    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().index[0]

    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination_of_start_and_end = df.groupby(["Start Station", "End Station"]).size().nlargest(1)

    print('Most Popular Combination of Start and End Station:', popular_combination_of_start_and_end.index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n','(^･ｪ･^)'*20)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_sec = df['Trip Duration'].sum()
    total_travel_time_min = total_travel_time_sec/60
    days = int(total_travel_time_min/(60*24))
    hours = int((total_travel_time_min - days*24*60)/60)
    minutes = int(total_travel_time_min - days*24*60 - hours*60)

    print('Total travel time: ' + str(days) + ' days ' + str(hours) + ' hours, ' + str(minutes) + " minutes")
    # TO DO: display mean travel time
    mean_travel_time_sec = df['Trip Duration'].mean()
    mean_travel_time_min = mean_travel_time_sec/60
    m_hours = str(int(mean_travel_time_min % (60 * 24) // 60))
    m_minutes = str(int(mean_travel_time_min % 60))

    print('Mean Travel Time: ' + m_hours + ' hours, ' + m_minutes + " minutes\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n','(^･ｪ･^)'*20)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('Number of Subscribers: ', counts_of_user_types[0], '\nNumber of Customers: ', counts_of_user_types[1])

    # TO DO: Display counts of gender
    while True:
        try:
            gender_counts = df['Gender'].value_counts()
            print('\nCounts of gender:', '\nFemale: ', gender_counts[0], '\nMale: ', gender_counts[1])
            break
        except KeyError: 
            print('\nUnfortunately, we don\'t have the data about gender for chosen city.')
            break

      

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try: 
            earliest_year_of_birth = int(df['Birth Year'].min())
            most_recent_year_of_birth = int(df['Birth Year'].max())
            most_common_year_of_birth = int(df['Birth Year'].mode())
            print('\nEarliest Year Of Birth: ', earliest_year_of_birth, '\nMost Recent Year Of Birth: ', most_recent_year_of_birth, '\nMost Common Year of Birth: ', most_common_year_of_birth )
            break
        except KeyError: 
            print('Unfortunately, we don\'t have the data about year of birth for chosen city.')
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\nThat\'s all for now!')

def raw_data(df):
    print('\nWould you like to see raw data first?')
    while True:
        user_input = input('Please type "yes" if you want to see raw data and "no" if you don\'t: \n')
        if user_input == 'yes':
            rows = int(input('How much rows would you like to see? Please enter a number: \n'))
            print(df.head(rows))
            print('Do you want to see more rows of the data?\n')
        else:
            break
    
    print('Okay, let\'s see some statistics then')   


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
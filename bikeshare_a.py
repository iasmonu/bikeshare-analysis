import time
import pandas as pd
import numpy as np

city_ka_data = {'chicago': 'chicago.csv',
                'new york city': 'new_york_city.csv',
                'washington': 'washington.csv'}


def get_filters():

    """
    print('hello, we are going to explore the bikeshare data')
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
         or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
         or "all" to apply no day filter
    """
    print('Hello! guys we aill be exploring some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    print('enter the city for analayzing->chicago, new york city, washington :')
    city = input("city name ")
    city = city.lower()
    # HINT: Use a while loop to handle invalid inputs
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('wrong entry is made, recheck the data ').lower()
    else:
        month = input('enter the month for the analysis ').lower()
# TO DO: get user input for month (all, january, february, ... , june)
        day = input('enter th day of week for analysis ').lower()
# TO DO: get user input for day of week (all, monday, tuesday...sunday)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by
    month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
        or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
        or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    file_name = city_ka_data[city]
    df = pd.read_csv(file_name)
    df = pd.read_csv(city_ka_data[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month = month.index(month) + 1
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

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print(" most common month  :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print(" most common day of week is :", most_common_day_of_week)
    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print(" most common start hour is :", most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station : {} ".format(
        df['Start Station'].mode().values[0])
    )
    # TO DO: display most commonly used end station
    print(" most common end station : {}".format(
        df['End Station'].mode().values[0])
    )
    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station'] + " " + df['End Station']
    print("The most common start and end station combo is: {}".format(
        df['routes'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    max_travel = df['Trip Duration'].max()
    print("Max travel time :", max_travel)

    print("Travel time for each user type:\n")
    # display the total trip duration for each user type
    group_by_user_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print("  {}: {}".format(group_by_user_trip.index[index], user_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here are the counts of various user types:")
    print(df['User Type'].value_counts())
    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    except KeyError:
            print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
            print("\nEarliest Year:\nNo data available for this month.")

    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    """

    Display contents of the CSV file to the display as requested by

    the user.

    """
    start_loc = 0

    end_loc = 5
    display_active = input("Do you want to see the raw data?: ").lower()
    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc, :])
            start_loc += 5
            end_loc += 5
            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':

                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

""" some sources I used :
     https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.T.html
     https://stackoverflow.com/
"""
     
import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv' }

def get_filters():
    """ get_filters is a function used to check the different inputs
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""
    #---------------------------------------------------------------------------------------------------------------#
     #while loop to check the input of city and raise TypeError if the input dosn't meet the condition
    while True:
        try:
            city=str(input("which city do you want to display data for? (Chicago, New York City , or Washington) \n")).lower()
            print('-'*80)
            if (city in['chicago','new york city','washington']):
                break
            else:
                raise TypeError
        except TypeError:
                print("That\'s not a valid input , please check your input data...")
                continue 
        except EOFError:
                print("Please input something....")
                continue 
    #---------------------------------------------------------------------------------------------------------------#            
      #while loop to check the input of month and raise TypeError if the input dosn't meet the condition   
    while True:
        try:
            month=input("Which month do you want to filter with? (January, February,March,April,May,or June): \n or insert 'all' if you do not want to filter by month:\n ").title()     
            print('-'*80)
            if (month in['January','February','March','April','May','June','All']):
                break
            else:
                raise TypeError
        except TypeError:
                print("That\'s not a valid input , please check your input data...")
                continue 
        except EOFError:
                print("Please input something....")
                continue
     #---------------------------------------------------------------------------------------------------------------#           
    #while loop to check the input of day and raise TypeError if the input dosn't meet the condition 
    while True:
        try:
            day=input("Which day do you want to filter with? (Monday,Tuesday,Wednesday,Thursday ,Friday,Saturday,or Sunday): \n or insert 'all' if you do not want to filter by day of week: \n ").title()
            print('-'*80)
            if (day in['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']):
                break
            else:
                raise TypeError
        except TypeError:
                print("That\'s not a valid input , please check your input data...")
                continue 
        except EOFError:
                print("Please input something....")
                continue 
    
    print('Hello! Let\'s explore some US bikeshare data!')
   
    print('-'*45)
     # return user input for city (city, month, day).
    return city, month, day

  #---------------------------------------------------------------------------------------------------------------#
  #---------------------------------------------------------------------------------------------------------------#
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
    #load the csv file of the selected city
    df=pd.read_csv(CITY_DATA[city])
    
    
    
    #convert Start Time col to datatime type
    df['Start Time'] = pd.to_datetime(df['Start Time']) 

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
        
    return df
 #---------------------------------------------------------------------------------------------------------------#
 #---------------------------------------------------------------------------------------------------------------#
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # ==> display the most common month
    popular_month=df['month'].mode()[0]        
    print("The most common month is ==>> ",calendar.month_name[popular_month])
    
    # ==> display the most common day of week
    popular_day=df['day_of_week'].mode()[0]     
    print("The most common day is ==>> ",popular_day)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    #==> # display the most common start hour
    popular_hour = df['hour'].mode()[0]    
    print("The most common hour is ==>> ",popular_hour)
    
    # calculate time to execute these calculations
    print("\nThis took %s seconds." % (time.time() - start_time))      
    print('-'*40)
   #---------------------------------------------------------------------------------------------------------------#
  #---------------------------------------------------------------------------------------------------------------#  
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print("The most common start station is ==>> ",common_start_station)
    
    # display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print("The most common end station is ==>> ",common_end_station)
    
    # display most frequent combination of start station and end station trip
    df['common trip']="Start: "+ df['Start Station']+"/"+ "End: "+ df['End Station']
    
    # display most commonly used trip
    common_trip=df['common trip'].mode()[0]
    print("The most common trip is ==>> ",common_trip)
    
    # calculate time to execute these calculations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   #---------------------------------------------------------------------------------------------------------------#
  #---------------------------------------------------------------------------------------------------------------#  
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total trip duration is ==> {} seconds ".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("The Average of trip duration is ==> {} seconds ".format(df['Trip Duration'].mean()))
    
    # calculate time to execute these calculations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
   #---------------------------------------------------------------------------------------------------------------#
  #---------------------------------------------------------------------------------------------------------------#  
def user_stats(city,df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
        
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of User type:\n", user_types)
    print('-'*40)
    
    if city != 'washington':
                
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print("Count of gender:\n ", gender)
        print('-'*40) 
        
        # Display earliest, most recent, and most common year of birth
        earliest_yearofbirth = df['Birth Year'].min()     
        recent_yearofbirth = df['Birth Year'].max()     
        popular_yearofbirth = df['Birth Year'].mode()[0]   
        print("The earliest year of birth is ==> ",earliest_yearofbirth)
        print("The most recent year of birth is ==> ",recent_yearofbirth)
        print("The most common year of birth is ==> ",popular_yearofbirth)
    
        # calculate time to execute these calculations
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        
        print("\n no statistics available for 'Gender' as it isn't provided for washington\n")
        print("\n no statistics available for 'Birth Year' as it isn't provided for washington\n")
        print('-'*40)

   #---------------------------------------------------------------------------------------------------------------#
  #---------------------------------------------------------------------------------------------------------------# 
def print_individual_data(city,df):
    
    df=df.fillna("' '")
    
    # view some individual trip data if the user type 'yes'#
    #Dealing with NAN values to clean data
    
    """ while loop to print individual trip data upon the request of user
        first check if user type 'yes'
        then check if the city is washington to print individual trip data
        if the user type 'new york city' or 'chicago' it will execute the else statement 
    """
    while True:
        view_df = input('\n Would you like to view some individual trip data? type YES or NO...\n' )
        if view_df.lower() == 'yes':
            if city == "washington":
                summary_df=df[df.columns[0:7]].sample(n=5)
                summary_df=summary_df.to_dict('records')
                print("some individual trip data: \n")
                print("-"*40)
                for row in (summary_df):
                    for k, v in row.items():
                        print (k, '==>', v)
                        
                    print("-"*40)
                continue
            elif city in ['new york city', 'chicago']:
                summary_df=df[df.columns[0:9]].sample(n=5)
                summary_df=summary_df.to_dict('records')
                print("some individual trip data: \n")
                print("-"*40)
                for row in (summary_df):
                    for k, v in row.items():
                        print (k, '==>', v)
                    print("-"*40)
                continue
              
        elif view_df.lower() not in['yes','no']:
            print("That\'s not a valid input , please type YES or NO...\n")
            continue
        elif view_df.lower()== 'no':
            break 
def restart():
    
    while True:
        """ While loop to check the user input:
        ==> if the user typed  'Yes', it would restart the whole program
        ==> if the user typed 'No'. it would stop executing of the program
        ==> if the user typed any other input except 'yes' or 'no' it would rise error and ask him to retype his input again
        """
        try:
                
            restart = input("\n Would you like to restart? type YES or NO...\n")
            if restart.lower() == 'no':
                
                break
            
            elif restart.lower() == 'yes':
                main()
               
            elif restart.lower() not in ['yes','no']:
                raise TypeError
            
        except TypeError:
            print("That\'s not a valid input , please type YES or NO...\n")
            continue
          
            
def main():
    """main function used to call above functions till the user choose "no", it would stop""" 
    
    city, month, day = get_filters()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(city,df)
    print_individual_data(city,df)
    restart()
        
         
        
#Calling of main function#
if __name__ == "__main__":
	main()

import datetime as dt
import time


def calculate_age(born, date=''):
    """Calculate age in years.
    
    Args:
        born: (datetime): Datetime object for date of birth (yyyy-mm-dd)
        date: (datetime): Optional date to calculate from. If no date is
        passed, today's date is used.
        
    Returns:
        age (int): Age in years.
    
    Source:
        https://stackoverflow.com/questions/2217488/age-from-birthdate-in-
        python
    """
    if date not in (None, ''):
        return date.year - born.year - ((date.month, date.day) <
                                     (born.month, born.day))
    else:
        today = dt.datetime.today()
        return today.year - born.year - ((today.month, today.day) <
                                     (born.month, born.day))


def calculate_days(first_date, second_date, in_sep='/', out_sep='/'):
    """Return the number of days passed between two dates.
    
    Subtracts the first date from second date to return the number of days that
    have passed between the provided dates. Works on strings.
    
    Args:
        first_date (str): Date in the format dd/mm/yyyy.
        second_date (str): Date in the format dd/mm/yyyy.
        in_sep (str): Seperator in supplied date. Defaults to '/' if none
        provided.
        out_sep (str): Separator to be used in output. Defaults to '/' in none
        provided.
        
    Returns:
        days (int): Number of days passed.
    """
    # print('First Date: {}'.format(first_date))
    # print('Second Date: {}'.format(second_date))
    # Check first date is valid
    if not validate_date(first_date):
        # print('Date: {}'.format(first_date))
        return False
    else:
        cleaned_first_date = clean_date(first_date, in_sep, out_sep, '')
        # print('Cleaned_date: {}'.format(cleaned_date))
    # Check second date is valid
    if not validate_date(second_date):
        # print('Date: {}'.format(second_date))
        return False
    else:
        cleaned_second_date = clean_date(second_date, in_sep, out_sep, '')
        # print('Cleaned_date: {}'.format(cleaned_date))
    # Check cleaned dates are valid
    if cleaned_first_date and cleaned_second_date:
        # Make sure that first date is before second date
        if check_first_second_dates(cleaned_first_date, cleaned_second_date):
            # print('Converted date: {}'.format(date))
            # Convert provided date to a datetime object
            f_date = dt.datetime.strptime(cleaned_first_date,"%d/%m/%Y")
            s_today = dt.datetime.strptime(cleaned_second_date,"%d/%m/%Y")
            # print('Converted date: {}'.format(p_date))
            # print('Converted today date: {}'.format(up_today))
            return abs((f_date-s_today).days)
        else:
            return False
    else:
        return False


def calculate_days_dt(first, second):
    """Return number of days between date a and date b.
    
    Args:
        first (datetime): First date (earliest)
        second (datetime): Second date (latest).
        
    Returns:
        days (int): Number of days between first and second.    
    """
    return abs((first-second).days)


def check_date_digits(day, month, year):
    """Check that date only contains digits.

    Checks that the input for Days, Months and Years are digits and not
    letters or special characters.

    Args:
        day (str): String for the day values.
        month (str): String for the month values.
        year (str): String for the year values.

    Returns:
        True if only digits are found, False otherwise.
    """
    if not day.isdigit():
        return False
    elif not month.isdigit():
        return False
    elif not year.isdigit():
        return False
    else:
        return True


def check_date_digits_whole(input_date, sep):
    """Check that the days, months and years are all digits.
    
    Extracts the Days, Months and Years from a date and checks that each
    consists only of digits. Calls check_date_digits to check the extracted
    days, months and years.
    
    Args:
        input_date (str): String of the date to check.
        sep (str): Separator to use.

    Returns:
        True if date is in correct format, False otherwise.
    """
    if not check_date_dmy(input_date, sep):
        return False
    # Separate into days, months, year and then check if digits
    # Process Days
    first_sep = input_date.index(sep)
    days = input_date[:first_sep]
    # Process Months
    remaining = input_date[first_sep + 1:]
    second_sep = remaining.index(sep)
    months = remaining[:second_sep]
    # Process Years
    years = remaining[second_sep + 1:]
    if not check_date_digits(days, months, years):
        return False
    return True


def check_date_dmy(input_date, sep='/'):
    """Returns True or False for date being valid.

    Checks that the date is in the correct format: dd/mm/yyyy. Uses the
    separator provided or deaults to "/" if none provided. Days and Months can
    be either one or two digits, Years must be 4.

    Args:
        input_date (str): String of the date to check.
        sep (str): Separator to use.

    Returns:
        True if date is in correct format, False otherwise.
    """
    # Make sure there are two '/' in the date
    if input_date.count(sep) != 2:
        return False
    # Check if there are one or two day digits
    first_sep = input_date.index(sep)
    days = input_date[0:first_sep]
    if len(days) not in (1, 2):
        return False
    # Check if there are one or two month digits
    remaining = input_date[first_sep + 1:]
    second_sep = remaining.index(sep)
    months = remaining[0:second_sep]
    if len(months) not in (1, 2):
        return False
    # Check there are four year digits
    years = remaining[second_sep + 1:]
    if len(years) != 4:
        return False
    # Check that each character is a digit
    if not check_date_digits(days, months, years):
        return False
    return True


def check_date_ymd(input_date, sep='/'):
    """Returns True or False for date being valid.

    Checks that the date is in the correct format: yyyy/mm/dd. Uses the
    separator provided or deaults to "/" if none provided. Days and Months can
    be either one or two digits, Years must be 4.

    Args:
        input_date (str): String of the date to check.
        sep (str): Separator to use.

    Returns:
        True if date is in correct format, False otherwise.
    """
    # Make sure there are two '/' in the date
    if input_date.count(sep) != 2:
        return False
    # Check if there are four year digits
    first_sep = input_date.index(sep)
    years = input_date[0:first_sep]
    if len(years) != 4:
        return False
    # Check if there are one or two month digits
    remaining = input_date[first_sep + 1:]
    second_sep = remaining.index(sep)
    months = remaining[0:second_sep]
    if len(months) not in (1, 2):
        return False
    # Check there are two days digits
    days = remaining[second_sep + 1:]
    if len(days) not in (1, 2):
        return False
    # Check that each character is a digit
    if check_date_digits(days, months, years):
        return True
    else:
        return False


def check_first_second_dates(first_date, second_date):
    """Checks that the first date is before the second date.

    Converts each date to a timestamp and then compares to make sure the first
    date is before the second.

    Args:
        first_date (str): First date to compare.
        second_date (str): Second date to compare.

    Returns:
        True if first date is before the second date, False otherwise.
    """
    # Convert dates to timestamps
    first = convert_to_timestamp(first_date)
    second = convert_to_timestamp(second_date)
    # Compare timestamps
    if first < second:
        return True
    else:
        return False


def check_leap_year(year):
    """Check if a year is a leap year.

    Args:
        year (str): Four-digit year to be checked.

    Returns:
        True if the year is a leap year, False otherwise.
    """
    # Make sure the input year is an int
    if len(year) != 4:
        return False
    if not check_date_digits('01', '01', year):
        # Valid Day and Month provided so only year is checked
        return False  
    try:
        check_year = int(year)
    except ValueError:
        return False
    if check_year % 400 == 0:
        return True
    elif check_year % 100 == 0:
        return False
    elif check_year % 4 == 0:
        return True
    return False


def clean_date(input_date, in_sep='/', out_sep='/', output=''):
    """Return date in format DD/MM/YYYY.

    Strips additional timestamp information or other characters and returns
    date in the format DD/MM/YYYY. If the supplied date cannot be converted, 
    is in the incorrect format, or contains non-digit characters, it returns
    False.
    A separator can be specified for the output string.

    Args:
        date (str): The timestamp information.
        in_sep (str): Seperator in supplied date. Defaults to '/' if none
        provided.
        out_sep (str): Separator to be used in output. Defaults to '/' in none
        provided.
        output (str): 'd' returns DD/MM/YYYY. 'y' returns YY/MM/DDDD.
        
    Returns:
        cleaned_date (str): Date in format DD/MM/YYYY
    """
    # Return empty strings
    if input_date in (None, ''):
        return input_date
    # Find position of separators
    try:
        first_sep = input_date.index(in_sep)
    except ValueError:
        print('Cannot find {} for first_sep'.format(in_sep))
        return False
    remaining = input_date[first_sep + 1:]
    try:
        second_sep = remaining.index(in_sep)
    except ValueError:
        print('Cannot find {} for second_sep'.format(in_sep))
        return False
    if len(input_date[:first_sep]) == 4:
        years = input_date[:first_sep]
        months = remaining[:second_sep]
        # Find end of date
        try:
            ending = remaining.index(' ')
            days = remaining[second_sep + 1:ending]
        except ValueError:
            # If no ' ' then assume it is just a date with no further data
            days = remaining[second_sep + 1:]
    elif len(input_date[:first_sep]) in (1, 2):
        days = input_date[:first_sep]
        months = remaining[:second_sep]
        # Find end of date
        try:
            ending = remaining.index(' ')
            years = remaining[second_sep + 1:ending]
        except ValueError:
            # If no ' ' then assume it is just a date with no further data
            years = remaining[second_sep + 1:]
    else:
        return False
    # Check that days and months are two digits
    if len(days) == 1:
        days = '0{}'.format(days)
    if len(months) == 1:
        months = '0{}'.format(months)
    # Generate correct output
    if output != 'y': # Anything that is not y'' output as DD/MM/YYYY
        cleaned_date = '{}{}{}{}{}'.format(days, out_sep, months, out_sep,
                        years)
        # Check it is a valid date
        if check_date_dmy(cleaned_date, out_sep):
            return cleaned_date
        else:
            print('Failed check_date_dmy!')
            return False
    else:
        cleaned_date = '{}{}{}{}{}'.format(years, out_sep, months, out_sep,
                        days)
        if check_date_ymd(cleaned_date, out_sep):
            return cleaned_date
        else:
            print('Failed check_date_ymd!')
            return False


def convert_datetime(date, date_format):
    """Convert a datetime object to desired format.
    
    Takes a datetime object and converts it to the desired format. The format
    is determined by date_format.
    
    Args:
        date (datetime): Date to be converted.
        date_format(str): Format of the date (e.g. %Y-%m-%d)
        
    Returns:
        converted_date (str): Converted datetime object in desired format.
    """
    return dt.datetime.strftime(date, date_format)


def convert_to_datetime(date, date_format):
    """Convert to a datetime object.
    
    Takes a string and converts it to a datetime object. The format of the date
    is determined by date_format.
    
    Args:
        date (str): Date to be converted.
        date_format(str): Format of the date (e.g. %d/%m/%Y)
        
    Returns:
        converted_date (datetime): Converted date as a datetime object.
    """
    return dt.datetime.strptime(date, date_format)


def convert_to_mmm_yy(date):
    """Return date string in format Mmm-YY.
    
    Extracts the first three letters of the date and the last two digits and
    returns the date string in the format Mmm_YY.
    
    Args:
        date (str): String of date in format Month Year e.g. October 2018.
        
    Returns:
        extracted_date (str): Extracted date in form Mmm-YY e.g. Oct-18.
        If an invalid date is passed, prints the invalid date and returns an
        empty string.
    """
    allowed_months = ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November',
                     'December']
    # Extract month
    month = date[:-5]
    # Extract year
    year = date[-4:]
    # Check that a valid month and year is passed
    if month in allowed_months:
        try:
            int(year)
        except ValueError:
            print('Invalid year: {}'.format(year))
            return ''
        else:
            # Return Month and Year in required format
            return(month[:3] + '-' + year[2:])
    else:
        print('Invalid month: {}'.format(month))
        return ''


def convert_to_timestamp(date):
    # print('Date: {}'.format(date))
    return time.mktime(dt.datetime.strptime(str(date), "%d/%m/%Y")
                       .timetuple())


def date_correct(date_to_check):
    """Check that date is in the correct format.

    Checks that the date is in the format DD/MM/YYYY.

    Args:
        date_to_check (str): Date to be checked.

    Returns:
        True if date is in correct format, False otherwise.
    """
    try:
        dt.datetime.strptime(date_to_check, "%d/%m/%Y")
    except ValueError:
        return False
    return True


def extract_dates(input_date, in_sep='/', out_sep='/'):
    """Extract day, month and year from a date.

    Extracts the day, month and year from a date in the format
    dd/mm/yyyy. Returns False if the date is not valid or cannot be extracted.

    Args:
        input_date (str): Date in the format dd/mm/yyyy.
        in_sep (str): Seperator in supplied date. Defaults to '/' if none
        provided.
        out_sep (str): Separator to be used in output. Defaults to '/' in none
        provided.

    Returns:
        day (str): Day component as two digits.
        month (str): Month component as two digits.
        year (str): Year component as four digits.
    """
    old_date = input_date.strip()
    cleaned_date = clean_date(old_date, in_sep, out_sep, '')
    # Catch returns of False from clean_date()
    if cleaned_date:
        day = cleaned_date[:2]
        month = cleaned_date[3:5]
        year = cleaned_date[6:] 
        return day, month, year
    else:
        return False, False, False


def get_days_past(input_date, in_sep='/', out_sep='/'):
    """Return the number of days passed.
    
    Subtracts the date from today to return the number of days that have passed
    since the provided date.
    
    Args:
        input_date (str): Date in the format dd/mm/yyyy.
        in_sep (str): Seperator in supplied date. Defaults to '/' if none
        provided.
        out_sep (str): Separator to be used in output. Defaults to '/' in none
        provided.
        
    Returns:
        days (int): Number of days passed.
    """
    # print('Provided date: {}'.format(input_date))
    # Get todays date in the format "DD/MM/YYYY"
    today = (dt.datetime.today())
    # print('Today start: {}'.format(today))
    # Convert to DD/MM/YYYY
    cleaned_today = clean_date(str(today), '-', '/')
    # print('Today: {}'.format(cleaned_today))
    # Find out the format of the passed date
    if validate_date(input_date):
        cleaned_date = clean_date(input_date, in_sep, out_sep, '')
        # print('Cleaned_date: {}'.format(cleaned_date))
        if cleaned_date:
            # Make sure that provided date is before today's date
            # If not, return the incorrect value
            if check_first_second_dates(cleaned_date, cleaned_today):
                # print('Converted date: {}'.format(date))
                # Convert provided date to a datetime object
                p_date = dt.datetime.strptime(cleaned_date,"%d/%m/%Y")
                up_today = dt.datetime.strptime(cleaned_today,"%d/%m/%Y")
                # print('Converted date: {}'.format(p_date))
                # print('Converted today date: {}'.format(up_today))
                return abs((p_date-up_today).days)
    else:
        return False


def get_todays_date():
    """Return today's date.
    
    Returns:
        today (datetime): Today's date as a datetime object.
    """
    return dt.datetime.today()


def replace_nil_date(date):
    """Return processed date.
    
    Checks if the date is a nil date ('01-01-1970' or '1970-01-01') and returns
    an empty string if it is.
    
    Args:
        date (str): Date to be checked.
    
    Returns:
        '' if date is '01-01-1970', passed date otherwise.
    """
    nil_dates = ['01-01-1970', '01/01/1970', '1970-01-01', '1970/01/01']
    if date in nil_dates:
        return ''
    else:
        return date
    

def replace_unwanted_date(provided_date, unwanted_dates):
    """Replace a given date with an empty string.

    Args:
        provided_date (str): The date that is to be checked.
        unwanted_date (list): List of dates to be replaced with an empty
                             string if one of them found.
    Returns:
        str with the returned date.
    """
    if provided_date in unwanted_dates:
        return ''
    else:
        return provided_date


def validate_date(input_date):
    """Check date is valid.

    Checks that date is a vaild date that exists. Cleans date so that it
    is in the format DD/MM/YYYY and then checks that this is a valid
    date.

    Args:
        input_date (str): The date to be checked.

    Returns:
        True if date is valid, False otherwise.
    """
    # Check that the date is in the correct format
    if not check_date_dmy(input_date):
        if not check_date_ymd(input_date):
            return False
        else:
            input_date = clean_date(input_date)
    day, month, year = extract_dates(input_date)
    # Check month is valid
    if int(month) < 1 or int(month) > 12:
        return False
    # Check if February
    if int(month) == 2:
        # Check if it is a leapyear
        if check_leap_year(year):
            if int(day) < 1 or int(day) > 29:
                return False
        else:
            if int(day) < 1 or int(day) > 28:
                return False
    # Check for months that have 31 days
    thirty_one = (1, 3, 5, 7, 8, 10, 12)
    if int(month) in thirty_one:
        if int(day) < 1 or int(day) > 31:
            return False
    # Check months that have 30 days
    else:
        if int(day) < 1 or int(day) > 30:
            return False
    # Otherwise must be valid
    return True
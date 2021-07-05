import os
import sys
import datetime as dt
import yfinance as yf

import pandas as pd
from pandas_datareader import data


##################################
# Global variables and constants #
##################################

JOB_NAME = None

YEAR_PERIODS = [
    {"year": 2012, "year_start": pd.Timestamp(2012,1,3), "year_end": pd.Timestamp(2012,12,28)},
    {"year": 2013, "year_start": pd.Timestamp(2013,1,2), "year_end": pd.Timestamp(2013,12,30)},
    {"year": 2014, "year_start": pd.Timestamp(2014,1,2), "year_end": pd.Timestamp(2014,12,30)},
    {"year": 2015, "year_start": pd.Timestamp(2015,1,2), "year_end": pd.Timestamp(2015,12,30)},
    {"year": 2016, "year_start": pd.Timestamp(2016,1,4), "year_end": pd.Timestamp(2016,12,30)},
    {"year": 2017, "year_start": pd.Timestamp(2017,1,3), "year_end": pd.Timestamp(2017,12,29)},
    {"year": 2018, "year_start": pd.Timestamp(2018,1,2), "year_end": pd.Timestamp(2018,12,28)},
    {"year": 2019, "year_start": pd.Timestamp(2019,1,2), "year_end": pd.Timestamp(2019,12,30)},
    {"year": 2020, "year_start": pd.Timestamp(2020,1,2), "year_end": pd.Timestamp(2020,12,30)},
    {"year": 2021, "year_start": pd.Timestamp(2021,1,4), "year_end": pd.Timestamp(2021,12,28)}
]

TRAILING_RETURNS = []
# {"year": 2012, "year_start": pd.Timestamp(2012, 1, 3), "year_start_price": 233.25,
#  "year_end": pd.Timestamp(2012, 12, 28) "year_end_price": 400.15 }


#---------------------------------------------------------------------------------------#
def log_msg(catg,msg):

    cur = dt.datetime.now()
    cur_str = cur.strftime("%Y-%m-%d %H:%M:%S")
    print("%s %s: %s" % (cur_str,catg,msg))

#---------------------------------------------------------------------------------------#
def show_obj(obj):
    t = type(obj)
    p = dir(obj)
    print("***************")
    print("* Object Type *")
    print("***************")
    print(t)
    print("*********************")
    print("* Object Properties *")
    print("*********************")
    print(p)
    print("")

# ---------------------------------------------------------------------------------------#
def current_year():

    return int(str(dt.date.today())[:4])

#---------------------------------------------------------------------------------------#
def current_week():

    now_dt = dt.datetime.combine(dt.date.today(), dt.datetime.min.time())
    start_dt = now_dt - dt.timedelta(days=now_dt.weekday()+1)
    end_dt = start_dt + dt.timedelta(days=6)

#    mon_start_dt = start_dt + dt.timedelta(days=1)
#    fri_end_dt = end_dt - dt.timedelta(days=1)
#    log_msg("DEBG","current_week() start_dt = %s end_dt = %s" % (start_dt,end_dt))
#    log_msg("DEBG","current_week() mon_start_dt = %s fri_end_dt = %s" % (mon_start_dt,fri_end_dt))

    return start_dt, end_dt

#---------------------------------------------------------------------------------------#
def print_dataframe_columns(df):

    cur = dt.datetime.now()
    cur_str = cur.strftime("%Y-%m-%d %H:%M:%S")
    print("%s %s: Column names: " % (cur_str,"DEBG"),end="")

    for col in df.columns:
        print(col + " ",end = "")

    print("")

#---------------------------------------------------------------------------------------#
# df = dataframe
# idx = dataframe index where 0 = top and -1 = bottom
def print_dataframe(df,idx):

    cur = dt.datetime.now()
    cur_str = cur.strftime("%Y-%m-%d %H:%M:%S")

    print("%s %s: Column names: " % (cur_str,"DEBG"),end="")

    for col in df.columns:
        print(col + " ",end = "")
    print("")

    print("%s %s: Column values: " % (cur_str,"DEBG"),end="")

    for data in df.values[idx]:
        print("%f " % (data), end="")
    print("")

#---------------------------------------------------------------------------------------#
"""
Validate the YEAR_PERIODS dictionary list by using the year_start and year_end pandas timestamps to 
query yfinance. yfinance will return a pandas dataframe.  If a dataframe is not returned or if the YEAR_PERIODS
year_start element does not match the actual dataframe year start date, YEAR_PERIODS will be invalid and the job
will abort.  

The Microsoft MSFT ticker is used because the company stock has been around since 
the 1980s which guarantees that it can be used in the analysis 10 year range.
 
The current year is a special case because its stock end date changes every time the job runs, so YEAR_PERIODS
is updated with the current end date. 
 
Input: global YEAR_PERIODS
Output: valid and updated global YEAR_PERIODS
"""
def validate_year_periods():

    global YEAR_PERIODS

    log_msg("INFO","Validating year periods")

    current_yr = current_year()

    for p in YEAR_PERIODS:

        year = p["year"]
        year_start = p["year_start"]
        year_end = p["year_end"]
#        log_msg("INFO","Validating %d start=%s end=%s" % (year,year_start,year_end))

        # MSFT spans almost 40 years so it is a good stock to validate with.
        tick_obj = yf.Ticker("MSFT")

        ###########################
        # Capture year_start data #
        ###########################

        # Actual year_start must be between 1/1 and 1/7
        start_ts = pd.Timestamp(year, 1, 1)
        end_ts = pd.Timestamp(year, 1, 7)
        tick_hist = tick_obj.history(start=start_ts, end=end_ts)
        if tick_hist.empty:
            log_msg("EROR","Period start dataframe is empty")
            raise SystemExit(1)

        # Trade date is the index to this dataframe. Extract the real year_start.
        data_top = tick_hist.head()
        df_year_start = data_top.index[0]
        if df_year_start != year_start:
            log_msg("EROR","Validating YEAR_PERIODS year = %d year_start = %s YFINANCE year_start = %s" % (year,year_start,df_year_start))
            raise SystemExit(1)

        #########################
        # Capture year_end data #
        #########################

        if year == current_yr:
            start_ts, end_ts = current_week()
        else:
            start_ts = pd.Timestamp(year, 12, 24)
            end_ts = pd.Timestamp(year, 12, 31)

        tick_hist = tick_obj.history(start=start_ts, end=end_ts)
        if tick_hist.empty:
            log_msg("EROR","Period end dataframe is empty")
            raise SystemExit(1)

        data_bot = tick_hist.tail()
        df_year_end = data_bot.index[-1]

        if year != current_yr:
            if df_year_end != year_end:
                log_msg("EROR","Validating YEAR_PERIODS year = %d year_end = %s YFINANCE year_end = %s" % (year,year_end,df_year_end))
                raise SystemExit(1)
        else:
            log_msg("INFO","Updating current year %d year_end to %s" % (year,df_year_end))
            # Update 2021 YEAR_PERIODS dictionary
            p.update({"year_end": df_year_end})

"""
TRAILING_RETURNS{
"ticker": "MSFT", "year": 2012, 
"year_start": ts, "year_start_price": 233.25,
"year_end": ts    "year_end_price": 400.15,
"year_return": 210.22, "year_perc": -.05 }
"""
#---------------------------------------------------------------------------------------#
def create_trailing_data(ticker_list):

    global YEAR_PERIODS
    global TRAILING_RETURNS

    log_msg("INFO","Creating yearly trailing return data")

    for ticker in ticker_list:

        log_msg("INFO","Processing ticker %s data" % (ticker))

        d_ticker = ticker

        # Loop through YEAR_PERIODS

        for yp_dict in YEAR_PERIODS:

            d_year = yp_dict["year"]
            d_year_start = yp_dict["year_start"]
            d_year_start_price = 0.0
            d_year_end = yp_dict["year_end"]
            d_year_end_price = 0.0
            d_year_return = 0.0
            d_year_perc = 0.0

            # Get yfinance history dataframe
            tick_obj = yf.Ticker(d_ticker)
            # history(end=) is non-inclusive so add one to the end date to ensure it will be included in the dataframe
            year_end_adj = d_year_end + dt.timedelta(days=1)
            tick_hist = tick_obj.history(start=d_year_start, end=year_end_adj)

            if tick_hist.empty:

                log_msg("WARN","Ticker %s: missing or incomplete data for %d" % (d_ticker,d_year))

            else:

                # Validate dataframe year_start and year_end rows

                data_top = tick_hist.head()
                df_year_start = data_top.index[0]
                # If we have a partial dataframe
                if df_year_start != d_year_start:
                    log_msg("WARN", "Partial year %s dataframe year start %s does not match period year start %s" % \
                            (d_ticker, df_year_start, d_year_start))
                else:

                    d_year_start_price = tick_hist.iloc[0, 3]

                    data_bot = tick_hist.tail()
                    df_year_end = data_bot.index[-1]
                    if df_year_end != d_year_end:
                        log_msg("EROR", "%s dataframe year end %s does not match period year end %s" % (
                        d_ticker, df_year_end, d_year_end))
                        raise SystemExit(1)

                    d_year_end_price = tick_hist.iloc[-1, 3]

                    # Calculate trailing year return and gain/loss percentage
                    d_year_return = d_year_end_price - d_year_start_price
                    d_year_perc = d_year_return / d_year_start_price

                # else full dataframe

            # dataframe returned else if tick_hist.empty:

            # Add to TRAILING_RETURNS list of dictionaries
            TRAILING_RETURNS.append({"ticker": d_ticker, "year": d_year, "year_start": d_year_start, "year_start_price": d_year_start_price, \
                                     "year_end": d_year_end, "year_end_price": d_year_end_price, "year_return": d_year_return, "year_perc": d_year_perc})

            log_msg("INFO","%d start: %s %f end: %s %f return: %f percent: %f" % (d_year,d_year_start,d_year_start_price,d_year_end, d_year_end_price,d_year_return,d_year_perc))

        # end: for yp_dict in YEAR_PERIODS:

    # end: for ticker in ticker_list:

#---------------------------------------------------------------------------------------#
def print_trailing_data():

    log_msg("INFO","print_trailing_data()")
    years = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    perc = []

    # Print report title
    print("Ticker     %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d" % \
          (years[0],years[1],years[2],years[3],years[4],years[5],years[6],years[7],years[8],years[9]))
    print("---------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------")

    row_count = 0
    ticker_key = None

    for i, td in enumerate(TRAILING_RETURNS):

        row_count += 1

        if row_count == 1:
            ticker_key = td["ticker"]

        d_year_perc = td["year_perc"]

#        log_msg("INFO","start_price: %f end_price: %f return: %f percent: %f" % (d_year_start_price, d_year_end_price, d_year_return, d_year_perc))
        r_year_perc = round( (d_year_perc * 100.0 ),2)
        perc.append(r_year_perc)

        # If control break
        if td["ticker"] != ticker_key:
            print("%-10.10s %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f" % \
                  (ticker_key, perc[0], perc[1], perc[2], perc[3], perc[4], perc[5], perc[6], perc[7], perc[8], perc[9]))
            perc = []
            ticker_key = td["ticker"]
            row_count = 0

    # for td in TRAILING_RETURNS:

    # Last ticker control break
    print("out of loop: ticker=%s" % (ticker_key))
    print(perc)
    print("Last td")
    print(td)
#    old_print_trailing_data()
#    print("%-10.10s %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f" % \
#          (ticker_key, perc[0], perc[1], perc[2], perc[3], perc[4], perc[5], perc[6], perc[7], perc[8], perc[9]))


#---------------------------------------------------------------------------------------#
def old_print_trailing_data():

    cur = dt.datetime.now()
    cur_str = cur.strftime("%Y-%m-%d %H:%M:%S")

    print("")
    print("Generated at %s" % (cur_str))
    print("")
    print("%s|%s|%s|%s|%s|%s|%s|%s|" % \
          ("Ticker","Year","Year_Start","Start_Price","Year_End","End_Price","Return","Percentage"))

    for td in TRAILING_RETURNS:
        print("%s|%s|%s|%s|%s|%s|%s|%s|" % \
              (td["ticker"],td["year"],td["year_start"],td["year_start_price"],\
               td["year_end"],td["year_end_price"],td["year_return"],td["year_perc"]))
    print("")

########
# main #
########

# Get program name

tmp_list = sys.argv[0].split("/")
JOB_NAME = tmp_list[len(tmp_list) - 1]

log_msg("INFO","%s starting" % (JOB_NAME))

# Activate yfinance workaround for performance by hijacking pandas_datareader.data.get_data_yahoo() method
yf.pdr_override()

validate_year_periods()

#create_trailing_data(["MSFT","AAPL","TSLA"])
create_trailing_data(["AAPL","TSLA","ROKU","TDOC","ARKK"])

print_trailing_data()

# Exit gracefully

log_msg("INFO","%s completed successfully" % (JOB_NAME))

raise SystemExit(0)
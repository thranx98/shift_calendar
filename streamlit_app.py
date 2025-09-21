import datetime
from datetime import date
import calendar
from itertools import cycle
import pytz
import streamlit as st
from streamlit_autorefresh import st_autorefresh
count = st_autorefresh(interval=5000, limit=None, key="my_autorefresh_key")
klTz = pytz.timezone("Asia/Kuala_Lumpur")
timeInKL = datetime.datetime.now(klTz)
day_of_week = calendar.day_name[timeInKL.weekday()]
print(day_of_week)

year = timeInKL.year
month = timeInKL.month
day = timeInKL.day
#day_of_week = timeInKL.dayofweek
date_val = date(year, month, day)

if date_val.year==2023:

    twelveam_7am = ['A','A','A','A','B','B','B','B','C','C','C','C'] # 2023
    sevenam_7pm =  ['B','B','C','C','C','C','A','A','A','A','B','B']
    sevenpm_12am = ['A','A','A','B','B','B','B','C','C','C','C','A']

elif date_val.year==2024:

    twelveam_7am = ['B','B','B','C','C','C','C','A','A','A','A','B'] # 2024
    sevenam_7pm =  ['C','A','A','A','A','B','B','B','B','C','C','C']
    sevenpm_12am = ['B','B','C','C','C','C','A','A','A','A','B','B']

elif date_val.year==2025:

    twelveam_7am = ['C','A','A','A','A','B','B','B','B','C','C','C'] # 2025
    sevenam_7pm =  ['B','B','B','C','C','C','C','A','A','A','A','B']
    sevenpm_12am = ['A','A','A','A','B','B','B','B','C','C','C','C']

base=date(date_val.year, 1, 1)

year=date_val.year
numdays=366 if calendar.isleap(year) else 365

date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
my_list = date_list
#date_val = date.today()
#date_val = datetime.date(2024,1,31)

day_of_year = date_val.toordinal() - date(date_val.year, 1, 1).toordinal()
day_week = calendar.day_name[date_val.weekday()]

cyc1 = cycle(twelveam_7am)
twelveam_7am_list = [[i, next(cyc1)] for i in my_list]

cyc2 = cycle(sevenam_7pm)
sevenam_7pm_list = [[i, next(cyc2)] for i in my_list]

cyc3 = cycle(sevenpm_12am)
sevenpm_12am_list = [[i, next(cyc3)] for i in my_list]

midnight_shift = twelveam_7am_list[day_of_year]
day_shift = sevenam_7pm_list[day_of_year]
night_shift = sevenpm_12am_list[day_of_year]

shift_one = midnight_shift[1]
shift_two = day_shift[1]
shift_three = night_shift[1]
message_tele = str(date_val) + " (" + day_week + ")\n\n12am --> 7am   : " + shift_one + "\n7am   --> 7pm   : " + shift_two + "\n7pm   --> 12am : " + shift_three + "\n"
spaces = r" " * 4

st.title("🕝 Today\'s Shift")
st.header(f"Date: {date_val} ({day_of_week})")
st.warning(f"💤 12am ➔ 7am | {shift_one}")
st.success(f"☀️ 7am ➔ 7pm | {shift_two}")
st.info(f"🌙 7pm ➔ 12am | {shift_three}")
st.write(f"Last refresh: {timeInKL:%Y, %d-%b %H:%M:%S}")
st.write(f"In case the webapp freezes, click refresh button below:")
st.button("Refresh")

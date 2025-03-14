# Import required libraries
import streamlit as st
from datetime import datetime
import pytz

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Create app title
st.title("Time Zone App")

# Create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    try:
        # Get and format current time for each selected timezone with AM/PM
        current_time = datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        # Display timezone and its current time
        st.write(f"**{tz}**: {current_time}")
    except Exception as e:
        st.error(f"Error getting time for {tz}: {str(e)}")

# Create section for time conversion
st.subheader("Convert Time Between Timezones")
# Create time input field with current time as default
current_time = st.time_input("Current Time", value=datetime.now().time())
# Dropdown to select source timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
# Dropdown to select target timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Create convert button and handle conversion
if st.button("Convert Time"):
    try:
        # Combine today's date with input time and source timezone
        dt = datetime.combine(datetime.today(), current_time)
        dt = pytz.timezone(from_tz).localize(dt)
        # Convert time to target timezone and format it with AM/PM
        converted_time = dt.astimezone(pytz.timezone(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        # Display the converted time with success message
        st.success(f"Converted Time in {to_tz}: {converted_time}")
    except Exception as e:
        st.error(f"Error converting time: {str(e)}")

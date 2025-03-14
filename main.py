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

def get_time_in_timezone(timezone):
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        return current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    except Exception as e:
        return f"Error: {str(e)}"

# Create app title
st.title("Time Zone App")

# Create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    time_str = get_time_in_timezone(tz)
    st.write(f"**{tz}**: {time_str}")

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
        # Create datetime object with current date and selected time
        dt = datetime.combine(datetime.today(), current_time)
        # Localize the datetime to source timezone
        source_tz = pytz.timezone(from_tz)
        dt = source_tz.localize(dt)
        # Convert to target timezone
        target_tz = pytz.timezone(to_tz)
        converted_dt = dt.astimezone(target_tz)
        # Format and display the result
        converted_time = converted_dt.strftime("%Y-%m-%d %I:%M:%S %p")
        st.success(f"Converted Time in {to_tz}: {converted_time}")
    except Exception as e:
        st.error(f"Error converting time: {str(e)}")

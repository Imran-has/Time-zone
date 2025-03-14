# Import required libraries
import streamlit as st
from datetime import datetime
import pytz

# Enable debug mode
st.set_option('deprecation.showPyplotGlobalUse', False)

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

# Debug information
st.sidebar.write("Debug Information:")
st.sidebar.write(f"Python Version: {st.__version__}")
st.sidebar.write(f"Pytz Version: {pytz.__version__}")

try:
    # Create a multi-select dropdown for choosing time zones
    selected_timezone = st.multiselect(
        "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
    )

    # Display current time for selected time zones
    st.subheader("Selected Timezones")
    for tz in selected_timezone:
        try:
            tz_obj = pytz.timezone(tz)
            current_time = datetime.now(tz_obj)
            time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
            st.write(f"**{tz}**: {time_str}")
        except Exception as e:
            st.error(f"Error with timezone {tz}: {str(e)}")

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
            # Create datetime object
            dt = datetime.combine(datetime.today(), current_time)
            
            # Convert time
            source_tz = pytz.timezone(from_tz)
            target_tz = pytz.timezone(to_tz)
            
            # Localize and convert
            dt = source_tz.localize(dt)
            converted_dt = dt.astimezone(target_tz)
            
            # Display result
            converted_time = converted_dt.strftime("%Y-%m-%d %I:%M:%S %p")
            st.success(f"Converted Time in {to_tz}: {converted_time}")
            
        except Exception as e:
            st.error(f"Conversion Error: {str(e)}")
            st.error("Please try again with different time zones")

except Exception as e:
    st.error(f"Application Error: {str(e)}")
    st.error("Please refresh the page and try again")

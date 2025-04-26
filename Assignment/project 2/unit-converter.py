import streamlit as st

st.title("🌎Unit Converter App")
st.markdown("### converts Length, Weight and  Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

category = st.selectbox("choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):

     if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.6213711
     elif category == "Weight":
          if unit == "Kilograms to Pounds":
             return value * 2.20462
          elif unit == "Pounds to Kilograms":
             return value / 2.20462
     elif category == "Time":
          if unit == "Seconds to Minutes":
             return value / 60
          elif unit == "Minutes to Seconds":
             return value * 60
          elif unit == "Minutes to Hours":
             return value / 60
          elif unit == "Hours to Minutes":
             return value * 60
          elif unit == "Hours to Days":
             return value / 24
          elif unit == "Days to Hours":
              return value * 24
      

if category == "Length":
    unit = st.selectbox("📏select Conversation", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
   unit = st.selectbox(" ⚖ select Conversation", ["Kilograms to Pounds", "Pounds to Kilograms"]) 

elif category == "Time":
    unit = st.selectbox(" ⌛ select Conversation", ["Seconds to Minutes",  "Minutes to Seconds"]) 

value = st.number_input("Enter the value to convert")  

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"the result is {result:.2f}")
                        
          


# streamlit run unit-converter.py
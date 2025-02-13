import streamlit as st
import requests

# OpenWeatherMap API key
API_KEY = '3c1622cc143e619c59c04d3ce45c33b4'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def main():
    st.title('Weather App')
    
    city = st.text_input('Enter city name:')
    
    if city:
        weather_data = get_weather(city)
        
        if weather_data.get('cod') != 200:
            st.error('City not found!')
        else:
            st.subheader(f"Weather in {city}")
            st.write(f"Temperature: {weather_data['main']['temp']} °C")
            st.write(f"Weather: {weather_data['weather'][0]['description']}")
            st.write(f"Humidity: {weather_data['main']['humidity']} %")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")

if __name__ == '__main__':
    main()
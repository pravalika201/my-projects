import requests

def get_weather(city_name, API_key):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
    
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}\n")
    else:
        print(f"\nCity '{city_name}' not found or API request failed.\n")

if __name__ == "__main__":
    API_key = "fd910cf6d6bab19db9f287a9d11f0679"  
    city = input("Enter city name: ")
    get_weather(city, API_key)





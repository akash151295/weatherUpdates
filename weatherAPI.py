import json, requests

API_Key = "a856f37654e904929fcb858c09499991"
i = 0

while(i<3):

  City = str(input("Please Enter City.."))

  getGeoCode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={City}&limit=5&appid={API_Key}"
  getGeoCode_response = requests.get(getGeoCode_url)
  getGeoCode_response = getGeoCode_response.json()

  if getGeoCode_response:
    # print(getGeoCode_response)
    # print(getGeoCode_response[0]['lat'])
    # print(getGeoCode_response[0]['lon'])
    City_lat = getGeoCode_response[0]['lat']
    City_Long = getGeoCode_response[0]['lon']

    getWeather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={City_lat}&lon={City_Long}&appid={API_Key}"
    getWeather_response = requests.get(getWeather_url)
    getWeather_response = getWeather_response.json()

    # print(getWeather_response)
    temperature = getWeather_response['main']['temp']
    temperature = temperature - 273.15
    feelsLike_temperature = getWeather_response['main']['feels_like']
    feelsLike_temperature = feelsLike_temperature - 273.15
    humidity = getWeather_response['main']['humidity']
    grnd_level = getWeather_response['main']['grnd_level']

    print(f"Hey Buddy {City} status is {'%.f' % temperature} degree C but it feels like {'%.f' % feelsLike_temperature} degree C.")
    print(f"{City} humidity is {humidity} g.m-3.")
    print(f"{City} groud level is {grnd_level} MD.")
    i=i+1
  else:
    print("City not found !!")
    i=i+1

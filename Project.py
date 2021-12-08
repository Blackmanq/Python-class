import requests,json
Main_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_Key = "fe3b5a322005921d3177ffa0a88722d6"
City = "San Antonio"
URL = Main_URL = "q=" + City + "&appid=" + API_key + "&units=imperial"
response = requests.get(URL)
if response.status_code ==  200:
    data = response.json()
    main = data["main"]
    temperature = main["temp"]
    humidity = main["humidity"]
    pressure = main["pressure"]
    report = data["weather"]
    print(f"{City:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
else:
    print("Error in the HTTP request")

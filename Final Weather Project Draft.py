import requests, json

welcome = input("Press enter to Request Weather Report")

#Main function
def main():
    while True:
        choice = input('Weather Report options: Type Zip for zip code or City for city name(case sensitive):')
        if choice == 'Zip':
            try:
                print("Connection Established.")
                by_zip()

            except Exception:
                print("Invalid City, Try Again.")
                by_zip()

        if choice == 'City':
            try:
                print("Connection Established.")
                by_city()
            except Exception:
                print('Inavalid Zip, Try Again.')
                by_city()

        else:
            print('Well, that is not a choice try again')

#Pull data function
def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Humidity : {}%'.format(humidity))
    print('Description : {}'.format(description))
    
    

# Request city function
def by_city():
    city = input('Enter City:')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=fe3b5a322005921d3177ffa0a88722d6&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)
#make continuous
    question = input('Would you like to do another search? Type Yes or No:')
    if question == 'Yes':
        main()
    if question == 'No':
        print('Thank You, Bye!')
        exit()


#request zip function
def by_zip():
    zip_code = int(input('Enter Zip Code:'))
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=fe3b5a322005921d3177ffa0a88722d6&units=imperial'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    show_data(data)
                   
    question = input('Would you like to do another search? Type Yes or No:')
    if question == 'Yes':
        main()
    if question == 'No':
        print('Thank you, Bye!')
        exit()

main()
                   

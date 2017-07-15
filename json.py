import requests

def get_menulist():
    my_request = requests.get('http://go.codeschool.com/spamvanmenu')

    #this will return a list of dictionary items
    menu_list = my_request.json()

    for item in menu_list:
        print('name=', item['name'], ' desc=', item['desc'], ' price=', item['price'], sep='')

    #print(menu_list)

def get_weather():
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=2de143494c0b295cca9337e1e96b00e0"
        request = requests.get(url)
        weather_json = request.json()
        print(weather_json)
        weather_main = weather_json.get('main')
        temp = weather_main.get('temp')
        print("The Circus's current temperature is ", temp)
    except Exception as err:
        print("Uh oh..", err)


def main():
    #get_weather()
    get_menulist()

main()

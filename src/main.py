import requests
from creds import api_key



def get_weather():
    user_input = input()
    weather_data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}'
    )
    if weather_data.json()['cod'] == '404':
        print(f"No city found, check {user_input} is a real city")
    else:
        try:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])

        except ValueError:
            print("please input a valid value")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            print(f"The weather in {user_input} is: {weather}")
            print(f"The temp in {user_input} is: {temp}")


if __name__ == '__main__':
    get_weather()


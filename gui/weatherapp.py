import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt
# api key is wrong 
str_api_key = '75a30e16008082ceebfc1f5a57c0312'
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        # label and text box to enter city
        self.label_city = QLabel("Enter city name: ",self)
        self.textbox_city = QLineEdit(self)
        # button to get weather of city
        self.btn_get_weather = QPushButton("Get weather",self)
        # labels for temp,emoji,description
        self.label_temperature = QLabel(self)
        self.label_emoji = QLabel(self)
        self.label_description = QLabel(self)
        
        self.initUI()
        
    def initUI(self):
        
        # set title
        self.setWindowTitle("Weather App")
        # self.setGeometry(0,0,100,100)
        # vertical layout
        vbox = QVBoxLayout()
        # add widgets to vertical Layout
        vbox.addWidget(self.label_city)
        vbox.addWidget(self.textbox_city)
        vbox.addWidget(self.btn_get_weather)
        vbox.addWidget(self.label_temperature)
        vbox.addWidget(self.label_emoji)
        vbox.addWidget(self.label_description)
        
        self.setLayout(vbox)
        
        # align all to center
        self.label_city.setAlignment(Qt.AlignCenter)
        self.textbox_city.setAlignment(Qt.AlignCenter)
        self.label_temperature.setAlignment(Qt.AlignCenter)
        self.label_emoji.setAlignment(Qt.AlignCenter)
        self.label_description.setAlignment(Qt.AlignCenter)
        
        # add name to widgets for adding styles
        self.label_city.setObjectName("label_city")
        self.textbox_city.setObjectName("textbox_city")
        self.label_temperature.setObjectName("label_temperature")
        self.label_emoji.setObjectName("label_emoji")
        self.label_description.setObjectName("label_description")
        self.btn_get_weather.setObjectName("btn_get_weather")
        
        # adding style
        self.setStyleSheet("""
                           QLabel,QPushButton{
                               font-family: calibri;
                           }
                           QLabel#label_city{
                               font-size: 40px;
                               font-style: italic;
                           }
                           QLineEdit#textbox_city{
                               font-size: 40px;
                           }
                           QPushButton#btn_get_weather{
                               font-size: 30px;
                               font-weight: bold;
                           }
                           QLabel#label_temperature{
                               font-size: 75px
                           }
                           QLabel#label_emoji{
                               font-size: 100px;
                               font-family: segoe UI emoji;
                           }
                           QLabel#label_description{
                               font-size:50px;
                           }
                           """)
        
        # add get weather method to get btn 
        self.btn_get_weather.clicked.connect(self.get_weather)
        
        
        
        
        
        
        
        
        
        
        
        
    '''
    fetch the weather data
    '''    
    def get_weather(self):
        str_city_name = self.textbox_city.text()
        print(str_city_name)
        str_url = f"https://api.openweathermap.org/data/2.5/weather?q={str_city_name}&appid={str_api_key}"
        try:
            res = requests.get(str_url)
            # in case the statuscode is in between 400 - 500 raise an exception
            res.raise_for_status()
            print(res)
            if res.status_code == 200:
                obj_res = res.json()
            else:
                # incase of invalid key
                obj_res = self.get_temp_json() 
            
            
            if obj_res["cod"] == 200:
                self.display_weather(obj_res)
        # in case the response is in between 400 - 500 HTTPError is raised 
        except requests.exceptions.HTTPError as http_err:
            match res.status_code:
                case 400:
                    self.display_error("Bad Request \n Please Check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid api key")
                case 403:
                    self.display_error("Forbidden\n Access denied")
                case 404:
                    self.display_error("Not Found\nCity not found")
                case 500:
                    self.display_error("Internal Server Error \n Please try again later")
                case 502:
                    self.display_error("Bad Gateway\nInvalid response from server")
                case 503:
                    self.display_error("Bad Gateway\n Server is down")
                case 504:
                    self.display_error("Gateway Timeout\nServer is down")
                case _:
                    self.display_error(f"Http error occured \n{http_err}")
        #to handle any connection error 
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck Your internet Connection")
        # to handle connection timeout error
        except requests.exceptions.Timeout:
            self.display_error("TimeOut Error:\nThe request Timeout")
        # in case of many redirects
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        # in case any unhandled error from Request
        except requests.exceptions.RequestException as req_err:
            self.display_error(f"Request Error\n{req_err }")
        
            
    '''
    to displaly weather from response
    '''
    def display_weather(self,obj_data):
        print(obj_data)
        dbl_temp_k = obj_data["main"]["temp"]
        dbl_temp_c = dbl_temp_k - 273.15
        dbl_temp_f = (dbl_temp_k * 9/5) - 459.67
        
        print(dbl_temp_c)
        # resetting the style to default
        self.label_temperature.setStyleSheet("font-size: 75px;")
        self.label_temperature.setText(f"{dbl_temp_c:.2f}°c")
        # handling description
        self.label_description.setText(obj_data["weather"][0]["description"] or "")
        # handling icon
        int_weather_id = obj_data["weather"][0]["id"]
        self.label_emoji.setText( self.get_weather_emoji(int_weather_id))
        
    '''
    to handle error
    '''
    def display_error(self,str_message:str):
        print(str_message)
        # set style for showing err
        self.label_temperature.setStyleSheet("color:red;font-size:20px")
        self.label_emoji.clear()
        self.label_description.clear()
        self.label_temperature.setText(str_message)
        
        
    '''
    To get Emoji based on weather id
    there an detailed description about id related sky in api docs
    '''
    @staticmethod
    def get_weather_emoji(int_weather_id:int):
        print(int_weather_id)
        
        # if int_weather_id >= 200 and int_weather_id <=232:
        if 200 <= int_weather_id <= 232:
            return "⛈️"
        elif 300<= int_weather_id <= 321:
            return "🌥️"
        elif 500 <= int_weather_id <=531:
            return "⛆"
        elif 600 <= int_weather_id <= 622:
            return "⛄"
        elif 701 <= int_weather_id <= 741:
            return "🌫️"
        elif int_weather_id == 762:
            return "🌫️"
        elif int_weather_id == 711:
            return "🌪️"
        elif int_weather_id == 771:
            return "💨"
        elif int_weather_id == 800:
            return "🌞"
        elif 801 <= int_weather_id <= 804:
            return "☁️"
        else:
            return ""
        
        
        
    '''
    sample json
    '''
    def get_temp_json(self):
        return {
     "coord": {
       "lon": -0.13,
       "lat": 51.51
     },
     "weather": [
       {
         "id": 300,
         "main": "Drizzle",
         "description": "light intensity drizzle",
         "icon": "09d"
       }
     ],
     "base": "stations",
     "main": {
       "temp": 280.32,
       "pressure": 1012,
       "humidity": 81,
       "temp_min": 279.15,
       "temp_max": 281.15
     },
     "visibility": 10000,
     "wind": {
       "speed": 4.1,
       "deg": 80
     },
     "clouds": {
       "all": 90
     },
     "dt": 1485789600,
     "sys": {
       "type": 1,
       "id": 5091,
       "message": 0.0103,
       "country": "GB",
       "sunrise": 1485762037,
       "sunset": 1485794875
     },
     "id": 2643743,
     "name": "London",
     "cod": 200
     }
              
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    
    sys.exit(app.exec_())
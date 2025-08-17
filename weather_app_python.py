import sys
from typing import Self
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton,QLineEdit
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter City Name:",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""QLabel,QPushButton {
            font-family:calibri;
        }
        QLabel#city_label{
            font-size:40px;
            font-style:italic;
        }
        QPushButton#get_weather_button{
            font-size:40px;
            font-weight:bold;
        }
        QLineEdit#city_input{
            background-color: #0056a1;
            font-size:40px;
        }
        QLabel#temperature_label{
            font-size:75px;
            font-weight:bold;
        }
        QLabel#emoji_label{
            font-size:100px;
            font-family:Segoe UI Emoji;
        }
        QLabel#description_label{
            font-size:50px;
        }
        """)
        
        self.get_weather_button.clicked.connect(self.get_weather)




    def get_weather(self):
        api_key="ff47232e7dca42e56be07a5dc6a8c61e"
        city_name = self.city_input.text().strip()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(data)
            if str(data.get("cod")) == "200":
                    self.display_weather(data)
            else:
                self.display_error(data.get("message", "City not found."))

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 404:
                    self.display_error("City not found.")
                case 401:
                    self.display_error("Invalid API key.")

                case 400:
                    self.display_error("Bad request.")
                case 403:
                    self.display_error("Forbidden.")
                case 500:
                    self.display_error("Internal Server Error.")
                case 502:
                    self.display_error("Bad Gateway.")
                case 503:
                    self.display_error("Service Unavailable.")
                case 504:
                    self.display_error("Gateway Timeout.")
                case _:
                    self.display_error(f"Unexpected error: {http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Network error. Please check your connection.")
        except requests.exceptions.Timeout:
            self.display_error("Request timed out. Please try again later.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects. Please check the URL.")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Error fetching weather data: {req_error}")

    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message)

    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size:75px;")
        temperature_k=data["main"]["temp"]
        temperature_c=temperature_k -273.15
        temperature_f=(temperature_c * 9/5) +32
        weather_ID = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_emoji(weather_ID))
        self.description_label.setText(weather_description.capitalize())

    @staticmethod
    def get_emoji(weather_ID):
        if 200 <= weather_ID < 300:
            return "⛈️"
        elif 300 <= weather_ID < 400:
            return "🌧️"
        elif 500 <= weather_ID < 600:
            return "🌧️"
        elif 600 <= weather_ID < 700:
            return "❄️"
        elif 700 <= weather_ID < 800:
            return "🌫️"
        elif weather_ID == 800:
            return "☀️"
        elif weather_ID == 801:
            return "🌤️"
        elif 802 <= weather_ID < 900:
            return "☁️"
        return "🌍"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

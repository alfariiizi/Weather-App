from PySide6.QtCore import *
import requests
import json

class APIWeather( QThread ):
    responseSignal = Signal( dict )
    def __init__( self, parent, city ) -> None:
        super().__init__(parent)
        # self.responseSignal = Signal( dict )
        self.apiKey = "1ef2f22817563af358d2b227e4e65537"
        self.city = city
    
    def run( self ) -> None:
        self.getData()
    
    def getData( self ):
        response = requests.get( f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.apiKey}' )
        json_response = json.loads(response.text)
        self.responseSignal.emit( json_response )
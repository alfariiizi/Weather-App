from PySide6.QtWidgets import *
from PySide6.QtCore import *

from resource.main_window import Ui_MainWindow
from about_version import AboutVersion
from helper.api_weather import APIWeather


class MainWindow( QMainWindow, Ui_MainWindow ):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.abtVer = AboutVersion( '0.1' )

        self.setupUi(self)
        self.setWindowTitle('Weather App')
        self.searchBtn.clicked.connect( self.changeCity )           # if search button is clicked
        self.aboutBtn.clicked.connect( self.showAboutVersion )      # if 'about version' is clicked
    
    def changeCity( self ):
        city = self.searchBar.text()
        city = city.capitalize()
        weatherApi = APIWeather( self, city )
        weatherApi.responseSignal.connect( self.doneGetData )
        weatherApi.start()

    def doneGetData( self, response ):
        self.cityLbl.setText( response['name'] )
        temp = response['main']['temp']
        temp -= 273.15      # kelvin to celcius
        temp = float("{:.2f}".format(temp))
        self.temperatureLbl.setText( f'{temp}° Celcius' )
        self.descLbl.setText( response['weather'][0]['description'].capitalize() )

    def showAboutVersion( self ):
        self.abtVer.show()


if __name__ == "__main__":
    import os, sys
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit( app.exec() )
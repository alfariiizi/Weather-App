from PySide6.QtWidgets import *
from PySide6.QtCore import *
from resource.about_version import Ui_Form

class AboutVersion( QDialog, Ui_Form ):
    def __init__( self, version: str=None ) -> None:
        super().__init__()
        self.setupUi( self )

        if version != None:
            self.setVersion( version )
        self.closeBtn.clicked.connect( self.closeAboutVersion )

    def closeAboutVersion( self ):
        self.close()
    
    def setVersion( self, version ):
        text = self.versionLbl.text()
        text = text[ 0:text.find('v1')+1 ]
        newText = f'{text}{version}'
        self.versionLbl.setText( newText )

if __name__ == '__main__':
    import os, sys

    app = QApplication( sys.argv )
    abtVer = AboutVersion( version='1.1' )
    abtVer.show()
    sys.exit( app.exec() )
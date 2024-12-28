'''
Digital clock PyQt5
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFont,QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        # label for timer
        self.timer_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUi()
        
    def initUi(self):
        # title of app
        self.setWindowTitle("Digital Clock")
        # height and width for app
        self.setGeometry(600,700,300,100)
        # layout for timer
        vbox = QVBoxLayout()
        # add timer widget
        vbox.addWidget(self.timer_label)
        self.setLayout(vbox)
        
        # align it to center
        self.timer_label.setAlignment(Qt.AlignCenter)
        # adding style timer 
        self.timer_label.setStyleSheet("font-size: 150px;"
                                       "color: hsl(111,100%,50%)"
                                       )
        # adding style to windoe
        self.setStyleSheet("background-color: black;")
        # changing font
        
        font_id = QFontDatabase.addApplicationFont("gui/DS-DIGIT.TTF")
        print(font_id)
        # creating font families
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        print(font_family)
        # creating font and passing it to 
        myFont = QFont(font_family,150)
        self.timer_label.setFont(myFont)
        # connecting update_time method to timer when it's timeout
        self.timer.timeout.connect(self.update_time)
        # starting timer with 1000ms as timeout
        self.timer.start(1000)
        # self.update_time() 
        
    def update_time(self):
        str_current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.timer_label.setText(str_current_time)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt,QTime,QTimer

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        # self.setGeometry(700,500,500,500)
        self.time = QTime(0,0,0,0)
        self.time_label =  QLabel("00:00:00.00",self)
        self.btn_start = QPushButton("Start",self)
        self.btn_stop = QPushButton("Stop",self)
        self.btn_reset = QPushButton("Reset",self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Stop watch")
        
        # create an vertical layout
        vbox = QVBoxLayout()
        # add widgets
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        # align center timer
        self.time_label.setAlignment(Qt.AlignCenter)
        # horizontally align buttons
        hbox = QHBoxLayout()
        #add buttone
        hbox.addWidget(self.btn_start) 
        hbox.addWidget(self.btn_stop) 
        hbox.addWidget(self.btn_reset)
        # add them to the layout
        vbox.addLayout(hbox) 
        
        # add styling
        self.setStyleSheet("""
                           QPushButton, QLabel {
                               padding: 20px;
                               font-weight: bold;
                               font-family: calbiri
                           }
                           QPushButton{
                               font-size:50px;
                           }
                           QLabel{
                               font-size: 80px;
                               background-color:hsl(200,100%,85%);
                               border-radius:20px;
                           }
                           """)
        
        # connect btn's to metheods
        self.btn_start.clicked.connect(self.start)
        self.btn_stop.clicked.connect(self.stop)
        self.btn_reset.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_ui)

    def start(self):
        print("CLICKED START")
        self.timer.start(10)
        self.btn_start.setDisabled(True)
    
    def stop(self):
        print("CLICKED stop")
        self.timer.stop()
        self.btn_start.setDisabled(False)
        
        
    
    def reset(self):
        print("CLICKED reset")
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText("00:00:00.00")
        self.btn_start.setDisabled(False)
        
    
    def format_time(self,time):
        str_hour = time.hour()
        str_minute = time.minute()
        str_second = time.second()
        str_millisecond = time.msec()//10 # interger division (//2) to 2 digit number
        return f"{str_hour:02}:{str_minute:02}:{str_second:02}.{str_millisecond:02}"
    
    def update_ui(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StopWatch()
    window.show()
    sys.exit(app.exec_())
    
'''Radio Button'''
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(700,500,500,500)
        # inint buttons
        self.btn1 = QPushButton("#1",self)
        self.btn2= QPushButton("#2",self)
        self.btn3 = QPushButton("#3",self)
        
        self.initUI()
        
        
        
    def initUI(self):
        # creating an central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        # create a layout
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)
        
        central_widget.setLayout(hbox)
        
        # object name
        self.btn1.setObjectName("btn1")
        self.btn2.setObjectName("btn2")
        self.btn3.setObjectName("btn3")
        
        #styling
        self.setStyleSheet("""
                           QPushButton{
                               font-size:40px;
                               font-family: Arial;
                               padding: 25px 75px;
                               margin: 25px;
                               border: 3px solid;
                               border-radius: 15px
                           }
                           QPushButton#btn1{
                               background-color:red;
                           }
                           QPushButton#btn2{
                               background-color:green;
                           }
                           QPushButton#btn3{
                               background-color:blue;
                           }
                           QPushButton#btn1:hover{
                               background-color:yellow;
                           }
                           QPushButton#btn2:hover{
                               background-color:tan
                           }
                           QPushButton#btn3:hover{
                               background-color:purple;
                           }
                           """) 
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
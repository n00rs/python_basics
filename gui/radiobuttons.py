'''Radio Button'''
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QRadioButton,QButtonGroup
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,500,500,500)
        # inint checbox
        self.radio1 = QRadioButton("Visa",self)
        self.radio2 = QRadioButton("Master Card",self)
        self.radio3 = QRadioButton("Gift Card",self)
        self.radio4 = QRadioButton("In-store",self)
        self.radio5 = QRadioButton("Online",self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        
        self.initUI()
        
        
        
    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,30,300,50)
        self.radio3.setGeometry(0,60,300,50)
        self.radio4.setGeometry(0,90,300,50)
        self.radio5.setGeometry(0,120,300,50)
        '''
        to apply style to group of buttons add class name inside {add style property}
        '''
        self.setStyleSheet("QRadioButton{"
                                "font-size:20px;"
                                "font-family:Arial;"
                                "padding:10px;"
                           "}")
        '''
        add payment option to one group 
        and payment type to another group
        '''
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
       
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        
    '''
    method to connect
    ''' 
    def radio_button_changed(self):
        '''
        to get which radio was clicked use sender method
        '''
        obj_radio_btn = self.sender()
        if obj_radio_btn.isChecked():
            print(f"{obj_radio_btn.text()} is selected")
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
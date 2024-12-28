import sys

from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,500,500,500)
        self.button = QPushButton("Click Me ..!",self)
        self.label = QLabel("Hello",self)
        self.initUI()
        
    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        
        
        self.label.setStyleSheet('color:blue; font-size:30px')
        self.label.setGeometry(0,0,100,100)
        
    '''
    method to be called when button is clicked
    '''
    def on_click(self):
        print("Clicked Me . . . . !")
        self.button.setText("Clicked")
        self.label.setStyleSheet('color:black; font-size:30px')
        self.button.setDisabled(True)
    

    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
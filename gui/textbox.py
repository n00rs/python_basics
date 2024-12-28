'''Radio Button'''
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,500,500,500)
        # inint text boxes
        self.textbox = QLineEdit(self)
        self.btn = QPushButton("Submit",self)
        self.initUI()
        
        
        
    def initUI(self):
        self.textbox.setGeometry(10,10,200,40)
        self.textbox.setStyleSheet("font-size:25px;" "Font-family:Arial")
        self.textbox.setPlaceholderText("Enter anything")
        # for buttons
        self.btn.setGeometry(215,10,200,40)
        self.btn.setStyleSheet("font-size:25px;" "Font-family:Arial")
        self.btn.clicked.connect(self.on_submit)
        
        
    def on_submit(self):
        # get value edited
        str_text = self.textbox.text()
        print("Btn clicked",str_text)
        # clear text
        self.textbox.clear()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
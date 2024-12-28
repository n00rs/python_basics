import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,500,500,500)
        # inint checbox
        self.checkbox = QCheckBox("Do you like apple ? : ",self)
        self.initUI()
        
    def initUI(self):
        # setting style
        self.checkbox.setStyleSheet("font-size: 30px;" "font-family:Arial;")
        # setting height and width
        self.checkbox.setGeometry(10,0,500,100)
        self.bln_checked = False
        # setting default value
        self.checkbox.setChecked(self.bln_checked)
        self.checkbox.stateChanged.connect(self.checkbox_clicked)
    
    '''
    method to be called when check box status is changed
    '''
    def checkbox_clicked(self,state):
        # Qt.Checked is 2 when clicked it state will be two
        if state == Qt.Checked:
            print("You like apple")
        else:
            print("You hate apple")
            
        self.checkbox.setChecked(not self.bln_checked)
        
        
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
    
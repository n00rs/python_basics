import sys 
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                            QWidget,QBoxLayout,QGridLayout,QHBoxLayout,QVBoxLayout)

from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first Gui")
        # setting x,y ,width,height
        self.setGeometry(700,500,500,500)
        self.setWindowIcon(QIcon("abcd.jpg"))
        
        label = QLabel("Name",self)
        label.setFont(QFont("Arial",30))
        # setting width and height for label
        label.setGeometry(0,0,500,100)
        # adding style
        label.setStyleSheet("color: blue;"
                            "background-color: lime;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            )
        # setting alignments
        
        # label.setAlignment(Qt.AlignTop) #Vertically Top
        # label.setAlignment(Qt.AlignBottom) #Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) #Vertically Center
        
        # label.setAlignment(Qt.AlignRight) #Horizontally Right
        # label.setAlignment(Qt.AlignHCenter) #Horizontally Center
        # label.setAlignment(Qt.AlignLeft) #Vertically Left
        
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Bottom & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Center & Center
        label.setAlignment(Qt.AlignCenter) #Center & Center
        '''
        adding image
        '''
        img_label = QLabel(self)
        img_label.setGeometry(100,100,250,250)
        
        obj_pixmap = QPixmap("abcd.jpg") #create ab pix map object
        img_label.setPixmap(obj_pixmap) #set image to label
        img_label.setScaledContents(True) #the image will automatically adjust
        img_label.setGeometry((self.width()-img_label.width()) //2,
                              (self.height()-img_label.height())//2,
                              img_label.width(),
                              img_label.height()
                              )
        self.initUI() #inintilizing layout
        '''
        LAYOUTS
        '''
    def initUI(self):
        '''
        create an generic widget inside that we can create or use Layout
        '''
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1",self)
        label2 = QLabel("#2",self)
        label3 = QLabel("#3",self)
        label4 = QLabel("#4",self)
        label5 = QLabel("#5",self)
        
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: green;")
        label3.setStyleSheet("background-color: yellow;")
        label4.setStyleSheet("background-color: purple;")
        label5.setStyleSheet("background-color: blue;")
        
        '''
        creating veritcal layout
        '''
        vbox = QVBoxLayout()
        
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        
        # central_widget.setLayout(vbox)
        
        '''
        creating Horizontal layout
        '''
        hbox = QHBoxLayout()
        
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)
        
        # central_widget.setLayout(hbox)
        
        '''
        creating Grid layout (need to pass row and column as different arg )
        addWidget(QWidget,row,column)
        '''
        grid = QGridLayout()
        
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,1,0)
        grid.addWidget(label4,1,1)
        grid.addWidget(label5,1,2)
        
        central_widget.setLayout(grid)
    
     
def main():
    # creating app and passing args ie is typed in terminal
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    















if __name__=="__main__":
    main()
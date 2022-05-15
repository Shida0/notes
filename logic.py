from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from text_window import Ui_MainWindow
from PyQt5.QtGui import QFont



class logic(QMainWindow):
    def __init__(self):
        super(logic, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file = open("data.txt", "r", encoding="utf-8")
        self.src = self.file.read()                

        self.add_func()

    def add_func(self):
        self.ui.btn_save.clicked.connect(self.save_text)
        self.ui.btn_view.clicked.connect(self.view_text)
        self.ui.btn_back.clicked.connect(self.back)
        self.ui.redact_btn.clicked.connect(self.redact)
        self.ui.btn_change.clicked.connect(self.save_redacts)
        self.ui.btn_back_change.clicked.connect(self.back_change)
        

    def save_text(self):        
        text = self.ui.text_input.toPlainText()        
        with open("data.txt", "a", encoding="utf-8") as file:
            file.write(f"{text}\n")
        self.ui.text_input.setPlainText("")           

    def view_text(self):   
        self.ui.tabWidget.setCurrentIndex(1)
        with open("data.txt", "r", encoding="utf-8") as file:
            src = file.read()
        self.ui.text_label_.setText(src)    

    def back(self):   
        self.ui.tabWidget.setCurrentIndex(0)   

    def save_redacts(self):        
        total_text = ""
        text = self.ui.save_input.toPlainText() 
        #print(text)
        self.file = text
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write(self.file)       

    def back_change(self):
        self.ui.tabWidget.setCurrentIndex(1)
        with open("data.txt", "r", encoding="utf-8") as file:
            src = file.read()
        self.ui.text_label_.setText(src) 

    def redact(self):   
        self.ui.tabWidget.setCurrentIndex(2)
        with open("data.txt", "r", encoding="utf-8") as file:
            src = file.read()
        self.ui.save_input.setPlainText(f"{src}")       


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    log = logic()
    log.show()
    sys.exit(app.exec_())
      
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class BMI_Window(object):
    def setupUi(self, bmi_window):
        bmi_window.setObjectName("bmi_window")
        bmi_window.resize(400, 229)
        bmi_window.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.centralwidget = QtWidgets.QWidget(bmi_window)
        self.centralwidget.setObjectName("centralwidget")
        self.weigth_label = QtWidgets.QLabel(self.centralwidget)
        self.weigth_label.setGeometry(QtCore.QRect(40, 80, 91, 17))
        self.weigth_label.setObjectName("weigth_label")
        self.heigth_label = QtWidgets.QLabel(self.centralwidget)
        self.heigth_label.setGeometry(QtCore.QRect(40, 30, 91, 17))
        self.heigth_label.setObjectName("heigth_label")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(210, 140, 191, 31))
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")
        self.heigth_input = QtWidgets.QLineEdit(self.centralwidget)
        self.heigth_input.setGeometry(QtCore.QRect(210, 30, 113, 20))
        self.heigth_input.setObjectName("heigth_input")
        self.weigth_input = QtWidgets.QLineEdit(self.centralwidget)
        self.weigth_input.setGeometry(QtCore.QRect(210, 80, 113, 20))
        self.weigth_input.setObjectName("weigth_input")
        self.bmi_button = QtWidgets.QPushButton(self.centralwidget)
        self.bmi_button.setGeometry(QtCore.QRect(40, 140, 99, 27))
        self.bmi_button.setObjectName("bmi_button")
        self.bmi_button.clicked.connect(self.calculate_bmi)
        bmi_window.setCentralWidget(self.centralwidget)
        self.retranslateUi(bmi_window)
        QtCore.QMetaObject.connectSlotsByName(bmi_window)

    def retranslateUi(self, bmi_window):
        _translate = QtCore.QCoreApplication.translate
        bmi_window.setWindowTitle(_translate("bmi_window", "BMI Calculator"))
        self.weigth_label.setText(_translate("bmi_window", "Gewicht (kg)"))
        self.heigth_label.setText(_translate("bmi_window", "Größe (cm)"))
        self.bmi_button.setText(_translate("bmi_window", "Berechne"))

    def calculate_bmi(self):
        try:
            weigth = float(self.weigth_input.text())
            heigth = float(self.heigth_input.text())
       
            if weigth > 140 or heigth > 200:
                self.output_label.setText("Netter Versuch =)")
            else:
                self.output_label.setText('Ihr BMI: {:.2f}'.format(weigth / (heigth ** 2) * 10000))
        except (ValueError, ZeroDivisionError):
            self.weigth_input.setText("")
            self.heigth_input.setText("")
            self.output_label.setText("")
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bmi_window = QtWidgets.QMainWindow()
    ui = BMI_Window()
    ui.setupUi(bmi_window)
    bmi_window.show()
    sys.exit(app.exec_())


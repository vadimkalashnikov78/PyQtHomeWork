"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from b_systeminfo_widget import SystemInfoForm
from c_weatherapi_widget import WindowWeather


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Объединенное окно")
        self.setMinimumSize(1200, 600)
        self.window_s = SystemInfoForm()
        self.window_s.setMinimumSize(500, 300)
        self.window_w = WindowWeather()
        self.initUI()

    def initUI(self):
        layout_s = QtWidgets.QVBoxLayout()
        layout_s.addWidget(self.window_s)
        layout_w = QtWidgets.QVBoxLayout()
        layout_w.addWidget(self.window_w)

        groupbox1 = QtWidgets.QGroupBox()
        groupbox2 = QtWidgets.QGroupBox()

        groupbox1.setTitle("System Information")
        groupbox2.setTitle("Weather")

        groupbox1.setLayout(layout_s)
        groupbox2.setLayout(layout_w)

        layout1 = QtWidgets.QVBoxLayout()
        layout1.addWidget(groupbox1)
        spacer1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        layout1.addItem(spacer1)

        layout2 = QtWidgets.QVBoxLayout()
        layout2.addWidget(groupbox2)

        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

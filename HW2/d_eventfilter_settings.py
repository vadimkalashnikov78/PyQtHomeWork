"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

import time

from PySide6 import QtWidgets, QtCore
from form_ui import Ui_Form


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.installEventFilter(self)
        self.initSignals()

        self.dial.setSliderPosition(0)
        self.horizontalSlider.setSliderPosition(0)
        self.comboBox.setItemData(0, "dec")

        self.__load()

    def __load(self):
        settings = QtCore.QSettings("MyFormSettings")
        setts = settings.value("settings")
        print(setts)
        self.lcdNumber.display(setts[0])
        self.comboBox.setCurrentText(setts[1])

    def __save(self):
        settings = QtCore.QSettings("MyFormSettings")
        settings.setValue("settings", [self.lcdNumber.value(), self.comboBox.currentText()])

    def eventFilter(self, watched: QtWidgets.QWidget, event: QtCore.QEvent) -> bool:
        print(time.ctime(), ">>>", event, ">>>", watched.objectName())

        return super().eventFilter(watched, event)

    def initSignals(self):
        self.dial.sliderReleased.connect(self.onDialSliderReleased)
        self.horizontalSlider.sliderReleased.connect(self.onHorizontalSliderReleased)
        self.comboBox.currentTextChanged.connect(self.onComboBoxCurrentTextChanged)

    def onDialSliderReleased(self):
        """

        :return:
        """
        self.horizontalSlider.setSliderPosition(self.dial.sliderPosition())
        self.lcdNumber.display(self.dial.sliderPosition())

    def onHorizontalSliderReleased(self):
        """

        :return:
        """
        self.dial.setSliderPosition(self.horizontalSlider.sliderPosition())
        self.lcdNumber.display(self.horizontalSlider.value())

    def onComboBoxCurrentTextChanged(self):
        """

        :return:
        """
        if self.comboBox.currentText() == "bin":
            self.lcdNumber.setBinMode()
        if self.comboBox.currentText() == "oct":
            self.lcdNumber.setOctMode()
        if self.comboBox.currentText() == "dec":
            self.lcdNumber.setDecMode()
        if self.comboBox.currentText() == "hex":
            self.lcdNumber.setHexMode()

    def keyPressEvent(self, event):
        if event.text() == "+":
            n1 = self.horizontalSlider.sliderPosition()
            n1 += 1
            self.horizontalSlider.setSliderPosition(n1)
            self.lcdNumber.display(n1)
            self.dial.setSliderPosition(n1)
        if event.text() == "-":
            n2 = self.horizontalSlider.sliderPosition()
            n2 -= 1
            self.horizontalSlider.setSliderPosition(n2)
            self.lcdNumber.display(n2)
            self.dial.setSliderPosition(n2)

    def closeEvent(self, event):
        self.__save()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

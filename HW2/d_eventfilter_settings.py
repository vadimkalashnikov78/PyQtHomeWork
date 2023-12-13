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

        self.settings = QtCore.QSettings("Settings")

        self.setupUi(self)
        self.installEventFilter(self)
        self.initSignals()

        self.dial.setSliderPosition(0)
        self.horizontalSlider.setSliderPosition(0)
        self.comboBox.setItemData(0, "dec")


        settings1 = self.settings.value("settings", [])
        print(settings1)

    def eventFilter(self, watched: QtWidgets.QWidget, event: QtCore.QEvent) -> bool:
        print(time.ctime(), ">>>", event, ">>>", watched.objectName())

        return super().eventFilter(watched, event)

    def initSignals(self):
        self.dial.rangeChanged.connect(self.onDialRangeChanged)
        self.horizontalSlider.rangeChanged.connect(self.onHorizontalSliderRangeChanged)
        self.comboBox.currentTextChanged.connect(self.onComboBoxTextChanged)

    def onDialRangeChanged(self):
        """

        :return:
        """
        self.lcdNumber.setText(self.dial.value())

    def onHorizontalSliderRangeChanged(self):
        """

        :return:
        """
        self.lcdNumber.setValue(self.horizontalSlider.value())

    def onComboBoxTextChanged(self):
        """

        :return:
        """
        self.lcdNumber.setDecMode()

    # def event_key(self, event):
    #     if event.type() == QtCore.QEvent.Type.KeyPress:
    #         if event.key() == "+":
    #             self.lcdNumber.text += event.delta()
    #         elif event.key() == "-":
    #             horizontalSlider.value() -= event.delta()


    def closeEvent(self, event):
        self.settings.setValue("settings", [self.comboBox.windowModality(), self.lcdNumber.value()]
                               )



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

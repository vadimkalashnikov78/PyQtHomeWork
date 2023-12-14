"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import psutil
from PySide6 import QtWidgets
from form1 import Ui_Form
from a_threads import SystemInfo


class SystemInfoForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initSignals()


    def initSignals(self):
        """

        :return:
        """
        self.lineEdit.textChanged.connect(self.onTextChanged)
        self.progress()




    def onTextChanged(self):
        """

        :return:
        """

    def progress(self):
        """

        :return:
        """
            self.lcdNumber.display(psutil.cpu_percent(1, False))
            self.lcdNumber_2.display(psutil.virtual_memory().percent)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoForm()
    window.show()

    app.exec()

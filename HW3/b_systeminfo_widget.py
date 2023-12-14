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
from PySide6 import QtWidgets, QtCore
from form2 import Ui_Form
from a_threads import SystemInfo


class SystemInfoForm(QtWidgets.QWidget, Ui_Form, SystemInfo):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.setupUi(self)
        self.initSignals()
        print(self.systemInfoReceived)

    def initThreads(self) -> None:
        """

        :return:
        """
        self.thread = QtCore.QThread()
        self.worker = SystemInfo()
        self.worker.moveToThread(self.thread)
        self.worker.start()




    def initSignals(self):
        """

        :return:
        """
        self.worker.started.connect(self.onProgress)

        # self.lineEdit.textChanged.connect(self.onTextChanged)


    # слоты

    def onTextChanged(self):
        """

        :return:
        """

    def onProgress(self):
        """

        :return:
        """
        print("Информация получена")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoForm()
    window.show()

    app.exec()

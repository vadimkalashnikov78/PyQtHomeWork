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
from PySide6 import QtWidgets, QtCore
from form2 import Ui_Form
from a_threads import SystemInfo




class SystemInfoForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.setupUi(self)
        self.initSignals()

    def initThreads(self) -> None:
        """

        :return:
        """
        self.thread = SystemInfo()
        self.thread.start()


    def initSignals(self):
        """

        :return:
        """
        self.thread.systemInfoReceived.connect(self.onProgress)
        self.lineEdit.textChanged.connect(self.onTextChanged)


    # слоты

    def onTextChanged(self) -> None:
        """

        :return:
        """
        if self.lineEdit.text() == "":
            self.thread.delay = None
            print("Время задержки >>> ", 1)
            return

        delay_new = float(self.lineEdit.text())
        if isinstance(delay_new, float):
            self.thread.delay = float(delay_new)
        else:
            self.thread.delay = 1
        print("Время задержки изменено на >>> ", self.thread.delay)
        pass

    def onProgress(self) -> None:
        """

        :return:
        """
        # print("Информация получена", self.thread.cpu, self.thread.ram)
        self.plainTextEdit.setPlainText(str(self.thread.cpu))
        self.plainTextEdit_2.setPlainText(str(self.thread.ram))

        self.progressBar.setValue(self.thread.cpu)
        self.progressBar_2.setValue(self.thread.ram)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoForm()
    window.show()

    app.exec()

# ### Задача.
#
# Разработать клиент для работы с базой данных, разработка которой велась на курсе DevDB.
#
# Обязательные функции в приложении:
#
# * Должна присутствовать авторизация в БД
# * Функционал должен обеспечивать полный набор CRUD операции с БД.
# * Обеспечить возможность работы с клиентом (отображение данных в графических элементах).
#
from PySide6 import QtCore, QtGui, QtWidgets




class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initSignals()
        self.initUi()


    def initThreads(self) -> None:

    def initUi(self) -> None:
        self.setWindowIcon(QtGui.QIcon(""))
        self.setWindowTitle("Работа с базой данных")

    def initSignals(self) -> None:



        #  Запуск основного приложения

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

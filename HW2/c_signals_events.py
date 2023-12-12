"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtCore, QtGui
from Ui_Form import Ui_Form
import time


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.installEventFilter(self)
        self.initSignals()

    def eventFilter(self, watched: QtWidgets.QWidget, event: QtCore.QEvent) -> bool:
        # print (time.ctime(), ">>>", event, ">>>", watched.objectName())

        return super().eventFilter(watched, event)

    def initSignals(self):
        self.pushButtonCenter.clicked.connect(self.on_pushButtonCenter_clicked)
        self.pushButtonLB.clicked.connect(self.on_pushButtonLB_clicked)
        self.pushButtonRB.clicked.connect(self.on_pushButtonRB_clicked)
        self.pushButtonLT.clicked.connect(self.on_pushButtonLT_clicked)
        self.pushButtonRT.clicked.connect(self.on_pushButtonRT_clicked)
        self.pushButtonMoveCoords.clicked.connect(self.on_pushButtonMoveCoords_clicked)
        self.pushButtonGetData.clicked.connect(self.Screen_Params)


    def on_pushButtonCenter_clicked(self):
        self.setupUi()


    def on_pushButtonLB_clicked(self):
        self.setupUi()

    def on_pushButtonRB_clicked(self):
        self.setupUi()


    def on_pushButtonLT_clicked(self):
        self.setupUi()

    def on_pushButtonRT_clicked(self):
        self.setupUi()

    def on_pushButtonMoveCoords_clicked(self):
        self.setupUi()

    def Screen_Params(self):
        text = ''
        # Количество экранов
        app = QtCore.QCoreApplication.instance()
        screens = app.screens()
        text += 'Количество экранов равно >>>  ' + str(len(screens)) + '\n'
        # * Текущее основное окно
        current_win = '1'

        text += 'Текущее основное окно >>>  ' + current_win + '\n'


        # * Разрешение экрана




        # * На каком экране окно находится

        # * Размеры окна
        current_size = self.size()
        text += 'Размеры окна >>>  ' + str(current_size) + '\n'
        # * Минимальные размеры окна
        min_size = self.minimumSize()
        text += 'Минимальные размеры окна >>>  ' + str(min_size) + '\n'

        # * Текущее положение (координаты) окна
        coords = self.geometry()
        text += 'Текущее положение (координаты) окна >>> ' + str(coords) + '\n'

        # * Координаты центра приложения

        # * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)"
        status = self.window().statusTip()
        text += 'Текущее состояние окна >>> ' + str(status) + '\n'


        self.plainTextEdit.setPlainText(text)


    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """
        print(time.ctime(), ' >>> ', str(event.size()))

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        :param event: QtGui
        :param event:
        :return:
        """
        old = event.oldPos()
        new = event.pos()
        print(time.ctime(), ' >>> ', 'Старая позиция >>> ' + str(old) + ' Новая позиция >>> ' + str(new))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

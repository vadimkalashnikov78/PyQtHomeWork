# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form2YvCfhJ.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(522, 496)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 459, 425))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(100, 20))
        self.lineEdit.setMaximumSize(QSize(50, 50))
        self.lineEdit.setBaseSize(QSize(100, 0))
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(25, 10))

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 10))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 10))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.plainTextEdit_2)

        self.progressBar_2 = QProgressBar(self.widget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)

        self.horizontalLayout_3.addWidget(self.progressBar_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM", None))
    # retranslateUi


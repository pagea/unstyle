# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stylproj.ui'
#
# Created: Tue Mar 31 16:43:10 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_6.addWidget(self.textEdit, 1, 0, 1, 1)
        self.saveDoc = QtWidgets.QPushButton(self.frame_2)
        self.saveDoc.setObjectName("saveDoc")
        self.gridLayout_6.addWidget(self.saveDoc, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.yourdoc = QtWidgets.QLineEdit(self.frame)
        self.yourdoc.setEnabled(True)
        self.yourdoc.setText("")
        self.yourdoc.setReadOnly(True)
        self.yourdoc.setObjectName("yourdoc")
        self.gridLayout_2.addWidget(self.yourdoc, 0, 0, 1, 1)
        self.browseYourDoc = QtWidgets.QPushButton(self.frame)
        self.browseYourDoc.setObjectName("browseYourDoc")
        self.gridLayout_2.addWidget(self.browseYourDoc, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame_4.setEnabled(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.frame_4)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_6 = QtWidgets.QLabel(self.splitter)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.otherdocslist = QtWidgets.QListWidget(self.layoutWidget)
        self.otherdocslist.setDragDropMode(
            QtWidgets.QAbstractItemView.DragOnly)
        self.otherdocslist.setResizeMode(QtWidgets.QListView.Fixed)
        self.otherdocslist.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.otherdocslist.setObjectName("otherdocslist")
        self.horizontalLayout.addWidget(self.otherdocslist)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.browseYourDocs = QtWidgets.QPushButton(self.layoutWidget)
        self.browseYourDocs.setObjectName("browseYourDocs")
        self.verticalLayout_5.addWidget(self.browseYourDocs)
        self.deleteYourDocs = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteYourDocs.setObjectName("deleteYourDocs")
        self.verticalLayout_5.addWidget(self.deleteYourDocs)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.stackedNext = QtWidgets.QPushButton(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stackedNext.setFont(font)
        self.stackedNext.setObjectName("stackedNext")
        self.verticalLayout.addWidget(self.stackedNext)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.stackedWidgetPage2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_3 = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.stackedWidgetPage2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setObjectName("formLayout")
        self.anonIcon = QtWidgets.QLabel(self.frame_3)
        self.anonIcon.setText("")
        self.anonIcon.setPixmap(QtGui.QPixmap(":/icons/img/x.png"))
        self.anonIcon.setObjectName("anonIcon")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.anonIcon)
        self.anonStatus = QtWidgets.QLabel(self.frame_3)
        self.anonStatus.setScaledContents(True)
        self.anonStatus.setWordWrap(True)
        self.anonStatus.setObjectName("anonStatus")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.anonStatus)
        self.gridLayout_7.addWidget(self.frame_3, 3, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.stackedWidgetPage2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rankTable = QtWidgets.QTableWidget(self.frame_5)
        self.rankTable.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.rankTable.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.rankTable.setRowCount(9)
        self.rankTable.setColumnCount(3)
        self.rankTable.setObjectName("rankTable")
        self.rankTable.horizontalHeader().setSortIndicatorShown(False)
        self.verticalLayout_2.addWidget(self.rankTable)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.featureDescription = QtWidgets.QLabel(self.frame_5)
        self.featureDescription.setWordWrap(True)
        self.featureDescription.setObjectName("featureDescription")
        self.verticalLayout_2.addWidget(self.featureDescription)
        self.gridLayout_7.addWidget(self.frame_5, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(False)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1209, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave_session = QtWidgets.QAction(MainWindow)
        self.actionSave_session.setObjectName("actionSave_session")
        self.actionLoad_session = QtWidgets.QAction(MainWindow)
        self.actionLoad_session.setObjectName("actionLoad_session")
        self.actionNew_session = QtWidgets.QAction(MainWindow)
        self.actionNew_session.setObjectName("actionNew_session")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen_documentation_in_browser = QtWidgets.QAction(
            MainWindow)
        self.actionOpen_documentation_in_browser.setObjectName(
            "actionOpen_documentation_in_browser")
        self.menuFile.addAction(self.actionNew_session)
        self.menuFile.addAction(self.actionLoad_session)
        self.menuFile.addAction(self.actionSave_session)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionOpen_documentation_in_browser)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Your document:"))
        self.textEdit.setHtml(
            _translate(
                "MainWindow",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Select a document to anonymize.</span></p></body></html>"))
        self.saveDoc.setText(_translate("MainWindow", "Save As..."))
        self.label.setText(_translate("MainWindow", "Document to anonymize:"))
        self.yourdoc.setToolTip(
            _translate(
                "MainWindow",
                "Click the \'Browse\' button to the right to select the document you would like to anonymize."))
        self.browseYourDoc.setText(_translate("MainWindow", "Browse"))
        self.label_6.setText(
            _translate("MainWindow", "Other documents written by you:"))
        self.otherdocslist.setToolTip(
            _translate(
                "MainWindow",
                "Click the \'browse\' button and select other documents you have written. Hint: Holding the Ctrl button allows you to select multiple documents.<br><br>It is strongly recommended that the combined word count of your documents is at least 6500."))
        self.browseYourDocs.setText(_translate("MainWindow", "Browse"))
        self.deleteYourDocs.setText(_translate("MainWindow", "Delete"))
        self.stackedNext.setText(_translate("MainWindow", "Next"))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "Your documents were successfully analyzed. Your top writing style traits (in order of importance) are listed on the left; suggestions on improving your anonymity are on the right. "))
        self.anonStatus.setText(
            _translate(
                "MainWindow",
                "It is still possible to identify you as the author. Continue changing your document."))
        self.label_2.setText(_translate("MainWindow", "Description:"))
        self.featureDescription.setText(
            _translate(
                "MainWindow",
                "Click on a feature to receive a description of the feature."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave_session.setText(
            _translate("MainWindow", "Save session"))
        self.actionLoad_session.setText(
            _translate("MainWindow", "Load session"))
        self.actionNew_session.setText(_translate("MainWindow", "New session"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen_documentation_in_browser.setText(
            _translate("MainWindow", "Open documentation in browser"))

import resources_rc

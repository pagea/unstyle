from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from stylproj.gui.stylproj_auto import Ui_MainWindow
import stylproj.controller

class StylProj(QMainWindow):
    def __init__(self, parent=None):
        # Initialized the generated interface code.
        super(StylProj, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signal connections
        self.ui.stackedNext.clicked.connect(self.stackNext_clicked)
        self.ui.browseYourDoc.clicked.connect(self.browseYourDoc_clicked)
        self.ui.browseYourDocs.clicked.connect(self.browseYourDocs_clicked)
        self.ui.deleteYourDocs.clicked.connect(self.deleteYourDocs_clicked)

    # stackedWidget buttons
    def stackNext_clicked(self):
        # Go to the next screen.
        self.ui.stackedWidget.setCurrentIndex(1)
        # Tell the controller to train its classifier.
        stylproj.controller.readyToClassify()

    def browseYourDoc_clicked(self):
        filename = QFileDialog.getOpenFileName()
        stylproj.controller.document_to_anonymize_path = filename[0]
        self.ui.yourdoc.setText(filename[0])
        stylproj.controller.document_to_anonymize = stylproj.controller.load_document(filename[0])
        # Show the text of the document in the text editor and enable it.
        self.ui.textEdit.setText(stylproj.controller.document_to_anonymize)
        self.ui.textEdit.setEnabled(True)

    def browseYourDocs_clicked(self):
        filenames = QFileDialog.getOpenFileNames()
        for path in filenames[0]:
            stylproj.controller.other_user_documents_paths.append(path)
            self.ui.otherdocslist.addItem(path)

    def deleteYourDocs_clicked(self):
        selected = self.ui.otherdocslist.currentItem()
        # Make sure the user selected a document before trying to delete
        # anything
        if selected is not None:
            row = self.ui.otherdocslist.currentRow()
            stylproj.controller.other_user_documents_paths.remove(selected.text())
            self.ui.otherdocslist.takeItem(row)
        else:
            pass

    # Controller messages
    def updateStats(self):
        # Set up rank table dimensions
        self.ui.rankTable.setRowCount(len(stylproj.controller.feature_ranks))
        # Name the headers of the table
        headers = "Text Features", "Target"
        self.ui.rankTable.setHorizontalHeaderLabels(headers)
        headerObj = self.ui.rankTable.horizontalHeader()
        headerObj.setSectionResizeMode(0, QHeaderView.ResizeToContents)

        print("Rank table size: " + str(len(stylproj.controller.feature_ranks)))
        # Populate rank table
        for idx, pair in enumerate(stylproj.controller.feature_ranks):
            currItem = self.ui.rankTable.item(idx, 0)
            # If we are setting up the table for the first time, currItem will
            # not exist.
            if currItem is None:
                currItem = QTableWidgetItem(1)
                currItem.setText(pair[0])
                self.ui.rankTable.setItem(idx, 0, currItem)
            else:
                currItem.setText(feature_ranks[pair[0]])

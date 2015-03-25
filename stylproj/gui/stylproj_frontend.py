from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
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
        stylproj.controller.document_to_anonymize_path = filename
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
        row = self.ui.otherdocslist.currentRow()
        stylproj.controller.other_user_documents_paths.remove(selected.text())
        self.ui.otherdocslist.takeItem(row)

#if __name__ == "__main__":
#    import sys
#
#    app = QApplication(sys.argv)
#    window = StylProj()
#    window.show()
#    sys.exit(app.exec_())

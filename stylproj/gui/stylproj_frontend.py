from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from stylproj_auto import Ui_MainWindow

# Nasty-ass hack to get around python's rigid import rules and import our
# controller module
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"),
os.path.pardir)))
import controller

class StylProj(QMainWindow):
    def __init__(self, parent=None):
        # Initialized the generated interface code.
        super(StylProj, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signal connections
        self.ui.stackedNext.clicked.connect(self.stackNext_clicked)
        self.ui.browseYourDoc.clicked.connect(self.browseYourDoc_clicked)

    # stackedWidget buttons
    def stackNext_clicked(self):
        # Go to the next screen.
        self.ui.stackedWidget.setCurrentIndex(1)

    def browseYourDoc_clicked(self):
        filename = QFileDialog.getOpenFileName()
        controller.document_to_anonymize_path = filename
        self.ui.yourdoc.setText(filename[0])

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = StylProj()
    window.show()
    sys.exit(app.exec_())

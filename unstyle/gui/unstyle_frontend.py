from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5 import QtGui
from unstyle.gui.unstyle_auto import Ui_Unstyle
import unstyle.controller


class Unstyle(QMainWindow):

    def __init__(self, parent=None):
        # Initialized the generated interface code.
        super(Unstyle, self).__init__(parent)
        self.ui = Ui_Unstyle()
        self.ui.setupUi(self)
        self.featureRows = {}
        self.setWindowTitle("Unstyle")
        # Signal connections
        self.ui.stackedNext.clicked.connect(self.stackNext_clicked)
        self.ui.browseYourDoc.clicked.connect(self.browseYourDoc_clicked)
        self.ui.browseYourDocs.clicked.connect(self.browseYourDocs_clicked)
        self.ui.deleteYourDocs.clicked.connect(self.deleteYourDocs_clicked)
        self.ui.textEdit.textChanged.connect(self.refreshAnonymity)
        self.ui.rankTable.selectionModel().selectionChanged.connect(
            self.row_highlighted)
        self.ui.saveDoc.clicked.connect(self.saveDoc_clicked)

    def getFeatureDesc(self, functionName):
        """Translate feature extractor names into something that the end user
        can understand.
        :param functionName: A feature extracting function.
        :returns: A typle containing ("Feature Name", "Description of feature").
        """
        names = {
            "letterSpace": (
                "Letter Space",
                ("The total number of letters appearing in your "
                 "document.")),
            "gunningFog": (
                "Gunning-Fog readability",
                ("A function related to "
                 "the ratio of words/sentences and complex word/total words.")),
            "avgSyllablesPerWord": (
                "Average syllables per word",
                ("The total "
                 "number of syllables/the total number of words.")),
            "unique_words": (
                "Unique words",
                ("The number of words that appear "
                 "only once in your document.")),
            "sentenceCount": (
                "Sentence count",
                ("The number of sentences in your document.")),
            "characterSpace": (
                "Character space",
                ("The total number of "
                 "characters (letters and numbers) appearing in your document.")),
            "avgSentenceLength": (
                "Average sentence length",
                ("The average "
                 "length of sentences in your document.")),
            "complexity": (
                "Complexity",
                ("The ratio of unique words to total"
                 "words in your document.")),
            "fleschReadingEase": (
                "Flesch readability",
                ("A function related to"
                 " the ratio of words/sentences and syllables/words."))}
        return names[functionName]

    # stackedWidget buttons
    def stackNext_clicked(self):
        # Go to the next screen.
        self.ui.stackedWidget.setCurrentIndex(1)
        # Tell the controller to train its classifier.
        unstyle.controller.readyToClassify()

    def browseYourDoc_clicked(self):
        filename = QFileDialog.getOpenFileName()
        unstyle.controller.document_to_anonymize_path = filename[0]
        self.ui.yourdoc.setText(filename[0])
        unstyle.controller.document_to_anonymize = unstyle.controller.load_document(
            filename[0])
        # Show the text of the document in the text editor and enable it.
        self.ui.textEdit.setText(unstyle.controller.document_to_anonymize)
        self.ui.textEdit.setEnabled(True)

    def browseYourDocs_clicked(self):
        filenames = QFileDialog.getOpenFileNames()
        if filenames is not '':
            for path in filenames[0]:
                unstyle.controller.other_user_documents_paths.append(path)
                self.ui.otherdocslist.addItem(path)

    def deleteYourDocs_clicked(self):
        selected = self.ui.otherdocslist.currentItem()
        # Make sure the user selected a document before trying to delete
        # anything
        if selected is not None:
            row = self.ui.otherdocslist.currentRow()
            unstyle.controller.other_user_documents_paths.remove(
                selected.text())
            self.ui.otherdocslist.takeItem(row)
        else:
            pass

    def saveDoc_clicked(self):
        """Save the current state of the text editor to a file defined by the
        user.
        """
        # Open a save dialog
        filename = QFileDialog.getSaveFileName()
        if filename is not None:
            with open(filename, 'w+') as file:
                file.write(str(textEdit.toPlainText()))

    # TODO: Rather than check anonymity every time the user changes the text,
    # have a separate thread check every 5 or 10 seconds. Otherwise, we're going
    # to be constantly locking up the interface when we use large featuresets.
    def refreshAnonymity(self):
        """Called whenever the user changes the text editor.
        """
        # Make sure we've trained the classifier before trying to do any
        # predictions.
        if unstyle.controller.trained_classifier is None:
            return 0

        anonymity = unstyle.controller.checkAnonymity(
            self.ui.textEdit.toPlainText())
        if anonymity is 0:
            self.ui.anonIcon.setPixmap(QtGui.QPixmap(":/icons/img/x.png"))
            self.ui.anonStatus.setText(
                ("It is still possible to identify you as the "
                 "author. Continue changing your document."))
        if anonymity is 1:
            self.ui.anonIcon.setPixmap(QtGui.QPixmap(":/icons/img/w.png"))
            self.ui.anonStatus.setText(
                ("Although you are not the most likely author,"
                 " there is a statistically significant chance"
                 " that you wrote the document. Continue"
                 " changing your document."))
        if anonymity is 2:
            self.ui.anonIcon.setPixmap(QtGui.QPixmap(":/icons/img/check.png"))
            self.ui.anonStatus.setText(
                ("Congratulations! It appears that your"
                 " document is no longer associated with your"
                 " identity."))

    def row_highlighted(self, _, __):
        """Every time someone selects a row from the table, we update our
        description box with the description of the feature.
        """
        selected = self.ui.rankTable.selectionModel().selectedRows()[0].row()
        featureHighlighted = self.featureRows[selected]
        # Display the description of the highlighted feature
        self.ui.featureDescription.setText(
            self.getFeatureDesc(featureHighlighted)[1])

    # Controller messages
    def update_stats(self):
        self.refreshAnonymity()
        # Set up rank table dimensions
        self.ui.rankTable.setRowCount(len(unstyle.controller.feature_ranks))
        # Name the headers of the table
        headers = "Text Features", "Target", "Initial"
        self.ui.rankTable.setHorizontalHeaderLabels(headers)
        headerObj = self.ui.rankTable.horizontalHeader()
        headerObj.setSectionResizeMode(0, QHeaderView.ResizeToContents)

        tableHeight = (len(unstyle.controller.feature_ranks))
        # XXX: Sorting should be handled in the table, not in the
        # rank_features methods. This will allow us to fix this embarrassingly
        # overcomplicated code.

        # Fill in the feature column
        for idx, pair in enumerate(unstyle.controller.feature_ranks):
            currItem = self.ui.rankTable.item(idx, 0)
            # If we are setting up the table for the first time, currItem will
            # not exist.
            if currItem is None:
                currItem = QTableWidgetItem(1)
                currItem.setText(self.getFeatureDesc(pair[0])[0])
                self.ui.rankTable.setItem(idx, 0, currItem)
            else:
                currItem.setText(
                    self.getFeatureDesc(feature_ranks[pair[0]])[0])

        # Initialize target and initial columns
        for idx, target in enumerate(unstyle.controller.targets):
            currItem = self.ui.rankTable.item(idx, 1)
            if currItem is None:
                currItem = QTableWidgetItem(1)
                currItem.setText(str(target))
                self.ui.rankTable.setItem(idx, 1, currItem)
                currItem2 = QTableWidgetItem(1)
                self.ui.rankTable.setItem(idx, 2, currItem2)

        # Populate target and current val columns
        # Track feature table locations
        labelsBeforeSorting = unstyle.controller.featlabels
        for idx, label in enumerate(labelsBeforeSorting):
            for idx2, item in enumerate(range(tableHeight)):
                currItem = self.ui.rankTable.item(item, 0)
                if self.getFeatureDesc(label)[0] == currItem.text():
                    self.featureRows[idx2] = label
                    print(label, " ", currItem.text(), " ", item)
                    currItem = self.ui.rankTable.item(item, 1)
                    currItem.setText(str(unstyle.controller.targets[idx]))
                    currItem = self.ui.rankTable.item(item, 2)
                    currItem.setText(
                        str(unstyle.controller.to_anonymize_features[0][idx]))

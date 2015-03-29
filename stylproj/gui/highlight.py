from PyQt5.QtGui import QTextCharFormat, QTextCursor
from PyQt5.QtCore import Qt

def highlight(begin, end, color, qtextedit):
    form = QTextCharFormat()
    form.setBackground(Qt.red)

    cursor = QTextCursor(qtextedit.document())
    cursor.setPosition(begin, QTextCursor.MoveAnchor)
    cursor.setPosition(end, QTextCursor.KeepAnchor)
    cursor.setCharFormat(form)

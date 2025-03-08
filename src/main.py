from PySide6.QtWidgets import QApplication
from game_gui import BlackjackGUI
import sys
from PySide6.QtGui import QIcon

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(":/icons/game.png"))

window = BlackjackGUI()
window.show()

app.exec()



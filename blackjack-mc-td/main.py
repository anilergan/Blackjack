from PyQt6.QtWidgets import QApplication
from game_gui import BlackjackGUI
import sys

app = QApplication(sys.argv)

window = BlackjackGUI()
window.show()


app.exec()
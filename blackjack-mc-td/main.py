from PyQt6.QtWidgets import QApplication
from game_gui import Blackjack_GUI
import sys

app = QApplication(sys.argv)

window = Blackjack_GUI()
window.show()

app.exec()
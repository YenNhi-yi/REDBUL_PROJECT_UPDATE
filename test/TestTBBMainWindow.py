import sys
from PyQt6.QtWidgets import QApplication
from Project.ui.TBBMainWindowExt import TBBMainWindowExt

app = QApplication(sys.argv)
window = TBBMainWindowExt()
window.show()
sys.exit(app.exec())
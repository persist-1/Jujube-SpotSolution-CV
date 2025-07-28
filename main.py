# 三方库
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QPoint,QFile, QTimer, QEventLoop, QThread, QPropertyAnimation, QEasingCurve, \
    QParallelAnimationGroup, Signal
from matplotlib.backend_bases import MouseEvent
# 本地库
from Refine_window import *
#from Ui_Jujube import Ui_Mainbody
#from custom_grips import CustomGrip


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon(r'images\my_icon\jujube.png'))  # 设置应用程序图标
    apple = MyWindow()
    apple.show()
    app.exec()

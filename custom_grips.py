from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# 拖动窗口 改变窗口大小

class CustomGrip(QWidget):
    def __init__(self, parent, position, disable_color = False):
        # 设置UI
        QWidget.__init__(self)
        self.parent = parent  # 将父窗口对象赋值给self.parent
        self.setParent(parent)  # 设置父窗口
        self.wi = Widgets()  # 创建Widgets类的实例

        # 显示顶部抓手
        if position == Qt.TopEdge:
            self.wi.top(self)  # 调用Widgets类的top方法，设置顶部抓手
            self.setGeometry(0, 0, self.parent.width(), 10)  # 设置该窗口的几何位置和大小
            self.setMaximumHeight(10)  # 设置最大高度

            # 创建大小抓手
            top_left = QSizeGrip(self.wi.top_left)  # 在左上角创建大小抓手
            top_right = QSizeGrip(self.wi.top_right)  # 在右上角创建大小抓手

            # 调整顶部大小的事件处理函数
            def resize_top(event):
                delta = event.pos()  # 获取鼠标位置的变化量
                height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())  # 计算新的高度
                geo = self.parent.geometry()  # 获取父窗口的几何位置
                geo.setTop(geo.bottom() - height)  # 设置父窗口的新顶部位置
                self.parent.setGeometry(geo)  # 应用新的几何位置到父窗口
                event.accept()  # 接收事件，防止事件传递给其他窗口

            self.wi.top.mouseMoveEvent = resize_top  # 将resize_top函数绑定到顶部抓手的mouseMoveEvent

            # 如果禁用颜色，则设置背景为透明
            if disable_color:
                self.wi.top_left.setStyleSheet("background: transparent")  # 设置左上角抓手背景为透明
                self.wi.top_right.setStyleSheet("background: transparent")  # 设置右上角抓手背景为透明
                self.wi.top.setStyleSheet("background: transparent")  # 设置顶部抓手背景为透明


        # 显示底部抓手
        elif position == Qt.BottomEdge:
            self.wi.bottom(self)  # 调用Widgets类的bottom方法，设置底部抓手
            self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)  # 设置该窗口的几何位置和大小
            self.setMaximumHeight(10)  # 设置最大高度

            # 创建大小抓手
            self.bottom_left = QSizeGrip(self.wi.bottom_left)  # 在左下角创建大小抓手
            self.bottom_right = QSizeGrip(self.wi.bottom_right)  # 在右下角创建大小抓手

            # 调整底部大小的事件处理函数
            def resize_bottom(event):
                delta = event.pos()  # 获取鼠标位置的变化量
                height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())  # 计算新的高度
                self.parent.resize(self.parent.width(), height)  # 应用新的大小到父窗口
                event.accept()  # 接收事件，防止事件传递给其他窗口

            self.wi.bottom.mouseMoveEvent = resize_bottom  # 将resize_bottom函数绑定到底部抓手的mouseMoveEvent

            # 如果禁用颜色，则设置背景为透明
            if disable_color:
                self.wi.bottom_left.setStyleSheet("background: transparent")  # 设置左下角抓手背景为透明
                self.wi.bottom_right.setStyleSheet("background: transparent")  # 设置右下角抓手背景为透明
                self.wi.bottom.setStyleSheet("background: transparent")  # 设置底部抓手背景为透明

        # 显示左侧抓手
        elif position == Qt.LeftEdge:
            self.wi.left(self)  # 调用Widgets类的left方法，设置左侧抓手
            self.setGeometry(0, 10, 10, self.parent.height())  # 设置该窗口的几何位置和大小
            self.setMaximumWidth(10)  # 设置最大宽度

            # 调整左侧大小的事件处理函数
            def resize_left(event):
                delta = event.pos()  # 获取鼠标位置的变化量
                width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())  # 计算新的宽度
                geo = self.parent.geometry()  # 获取父窗口的几何位置
                geo.setLeft(geo.right() - width)  # 设置父窗口的新左侧位置
                self.parent.setGeometry(geo)  # 应用新的几何位置到父窗口
                event.accept()  # 接收事件，防止事件传递给其他窗口

            self.wi.leftgrip.mouseMoveEvent = resize_left  # 将resize_left函数绑定到左侧抓手的mouseMoveEvent

            # 如果禁用颜色，则设置背景为透明
            if disable_color:
                self.wi.leftgrip.setStyleSheet("background: transparent")  # 设置左侧抓手背景为透明

        # 当窗口的边缘位置被设置为右侧边缘时
        elif position == Qt.RightEdge:
            # 调用self.wi.right方法，并将self作为参数传递，self指的是当前的窗口或控件
            self.wi.right(self)
            # 设置当前窗口或控件(self)的几何位置和大小。
            # 几何位置是父窗口的宽度减去10，高度为10，大小为宽度10，高度为父窗口的高度。
            # 这样设置后，当前窗口或控件(self)会出现在父窗口的右侧，并且高度与父窗口相同。
            self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
            # 设置当前窗口或控件(self)的最大宽度为10，这样用户就不能将窗口拉得更宽。
            self.setMaximumWidth(10)

            # 定义一个函数resize_right，用于处理鼠标移动事件
            def resize_right(event):
                # 获取鼠标移动的增量值
                delta = event.pos()
                # 计算新的宽度，确保它不小于父窗口的最小宽度
                # 通过将父窗口的当前宽度加上增量x坐标来调整宽度
                width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
                # 调整父窗口的宽度，高度保持不变
                self.parent.resize(width, self.parent.height())
                # 接受事件，这样就不会有其他的事件处理器来处理这个事件
                event.accept()

            # 将resize_right函数设置为右侧边缘调整控件的鼠标移动事件处理函数
            self.wi.rightgrip.mouseMoveEvent = resize_right

            # 如果禁用颜色(disable_color)标志为真
            if disable_color:
                # 设置右侧边缘调整控件的样式表，使背景透明
                # 这样做可能是为了让控件不可见或者让用户界面看起来更加干净
                self.wi.rightgrip.setStyleSheet("background: transparent")

    def mouseReleaseEvent(self, event):
        self.mousePos = None

    def resizeEvent(self, event):
        if hasattr(self.wi, 'container_top'):
            self.wi.container_top.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'container_bottom'):
            self.wi.container_bottom.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'leftgrip'):
            self.wi.leftgrip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, 'rightgrip'):
            self.wi.rightgrip.setGeometry(0, 0, 10, self.height() - 20)
class Widgets(object):
    def top(self, Form): #顶部握手框
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_top = QFrame(Form)
        self.container_top.setObjectName(u"container_top")
        self.container_top.setGeometry(QRect(0, 0, 500, 10))
        self.container_top.setMinimumSize(QSize(0, 10))
        self.container_top.setMaximumSize(QSize(16777215, 10))
        self.container_top.setFrameShape(QFrame.NoFrame)
        self.container_top.setFrameShadow(QFrame.Raised)
        self.top_layout = QHBoxLayout(self.container_top)
        self.top_layout.setSpacing(0)
        self.top_layout.setObjectName(u"top_layout")
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_left = QFrame(self.container_top)
        self.top_left.setObjectName(u"top_left")
        self.top_left.setMinimumSize(QSize(10, 10))
        self.top_left.setMaximumSize(QSize(10, 10))
        self.top_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.top_left.setStyleSheet(u"background-color: rgb(255, 255, 255);") #左上角 rgb(33, 37, 43)
        self.top_left.setFrameShape(QFrame.NoFrame)
        self.top_left.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_left)
        self.top = QFrame(self.container_top)
        self.top.setObjectName(u"top")
        self.top.setCursor(QCursor(Qt.SizeVerCursor))
        self.top.setStyleSheet(u"background-color: rgb(255, 255, 255);") #顶部 rgb(85, 255, 255)
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top)
        self.top_right = QFrame(self.container_top)
        self.top_right.setObjectName(u"top_right")
        self.top_right.setMinimumSize(QSize(10, 10))
        self.top_right.setMaximumSize(QSize(10, 10))
        self.top_right.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.top_right.setStyleSheet(u"background-color: rgb(255, 255, 255);") #右上角 rgb(33, 37, 43)
        self.top_right.setFrameShape(QFrame.NoFrame)
        self.top_right.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_right)

    def bottom(self, Form): #底部握手框
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_bottom = QFrame(Form)
        self.container_bottom.setObjectName(u"container_bottom")
        self.container_bottom.setGeometry(QRect(0, 0, 500, 10))
        self.container_bottom.setMinimumSize(QSize(0, 10))
        self.container_bottom.setMaximumSize(QSize(16777215, 10))
        self.container_bottom.setFrameShape(QFrame.NoFrame)
        self.container_bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout = QHBoxLayout(self.container_bottom)
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_left = QFrame(self.container_bottom)
        self.bottom_left.setObjectName(u"bottom_left")
        self.bottom_left.setMinimumSize(QSize(10, 10))
        self.bottom_left.setMaximumSize(QSize(10, 10))
        self.bottom_left.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.bottom_left.setStyleSheet(u"background-color: rgb(255, 255, 255);") #左下角 rgb(33, 37, 43)
        self.bottom_left.setFrameShape(QFrame.NoFrame)
        self.bottom_left.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_left)
        self.bottom = QFrame(self.container_bottom)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setCursor(QCursor(Qt.SizeVerCursor))
        self.bottom.setStyleSheet(u"background-color: rgb(255, 255, 255);") #底部 rgb(85, 170, 0)
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom)
        self.bottom_right = QFrame(self.container_bottom)
        self.bottom_right.setObjectName(u"bottom_right")
        self.bottom_right.setMinimumSize(QSize(10, 10))
        self.bottom_right.setMaximumSize(QSize(10, 10))
        self.bottom_right.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.bottom_right.setStyleSheet(u"background-color: rgb(255, 255, 255);") #右下角 rgb(33, 37, 43)
        self.bottom_right.setFrameShape(QFrame.NoFrame)
        self.bottom_right.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_right)

    def left(self, Form): # 左侧握手框
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.leftgrip = QFrame(Form)
        self.leftgrip.setObjectName(u"left")
        self.leftgrip.setGeometry(QRect(0, 10, 10, 480))
        self.leftgrip.setMinimumSize(QSize(10, 0))
        self.leftgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.leftgrip.setStyleSheet(u"background-color: rgb(255, 255, 255);") #左侧 rgb(255, 121, 198)
        self.leftgrip.setFrameShape(QFrame.NoFrame)
        self.leftgrip.setFrameShadow(QFrame.Raised)

    def right(self, Form): #右侧握手框
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        self.rightgrip = QFrame(Form)
        self.rightgrip.setObjectName(u"right")
        self.rightgrip.setGeometry(QRect(0, 0, 10, 500))
        self.rightgrip.setMinimumSize(QSize(10, 0))
        self.rightgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.rightgrip.setStyleSheet(u"background-color: rgb(255, 255, 255);") #右侧 rgb(255, 0, 127)
        self.rightgrip.setFrameShape(QFrame.NoFrame)
        self.rightgrip.setFrameShadow(QFrame.Raised)



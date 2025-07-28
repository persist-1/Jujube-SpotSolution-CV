# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jujube.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QSplitter,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Mainbody(object):
    def setupUi(self, Mainbody):
        if not Mainbody.objectName():
            Mainbody.setObjectName(u"Mainbody")
        Mainbody.resize(1344, 756)
        Mainbody.setMinimumSize(QSize(1344, 756))
        Mainbody.setMaximumSize(QSize(65536, 65536))
        Mainbody.setStyleSheet(u"QWidget#Mainbody {\n"
"    background-color: rgb(255, 255, 255); /* \u767d\u8272\u80cc\u666f */\n"
"    border-top: 1px solid rgb(255, 0, 0); /* \u9876\u90e8\u8fb9\u6846\u7ea2\u8272 */\n"
"    border-right: 1px solid rgb(0, 255, 0); /* \u53f3\u4fa7\u8fb9\u6846\u7eff\u8272 */\n"
"    border-bottom: 1px solid rgb(0, 0, 255); /* \u5e95\u90e8\u8fb9\u6846\u84dd\u8272 */\n"
"    border-left: 1px solid rgb(255, 255, 0); /* \u5de6\u4fa7\u8fb9\u6846\u9ec4\u8272 */\n"
"}\n"
"QLabel{\n"
"	background-color: rgb(255, 255, 255); /* \u767d\u8272\u80cc\u666f */\n"
"	border-top: 0px solid rgb(255, 255, 255); \n"
"    border-right: 0px solid rgb(255, 255, 255);\n"
"    border-bottom: 0px solid rgb(255, 255, 255); \n"
"    border-left: 0px solid rgb(255, 255, 255); \n"
"}\n"
"QFrame{\n"
" 	background-color: rgb(255, 255, 255); /* \u767d\u8272\u80cc\u666f */\n"
"	border-top: 0px solid rgb(255, 255, 255); \n"
"    border-right: 0px solid rgb(255, 255, 255);\n"
"    border-bottom: 0px solid rgb(255, 255, 255); \n"
"    border-left:"
                        " 0px solid rgb(255, 255, 255); \n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Mainbody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TotalLayout = QHBoxLayout()
        self.TotalLayout.setObjectName(u"TotalLayout")
        self.leftbox = QFrame(Mainbody)
        self.leftbox.setObjectName(u"leftbox")
        self.leftbox.setMinimumSize(QSize(83, 0))
        self.leftbox.setMaximumSize(QSize(0, 16777215))
        self.leftbox.setStyleSheet(u"QFrame#leftbox{\n"
" 	background-color: rgb(255, 255, 255); /* \u767d\u8272\u80cc\u666f */\n"
"	border-top: 0px solid rgb(255, 255, 255); \n"
"    border-right: 0px solid rgb(0, 85, 0);\n"
"    border-bottom: 0px solid rgb(255, 255, 255); \n"
"    border-left: 0px solid rgb(255, 255, 255); \n"
"}")
        self.leftbox.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftbox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.leftbox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo = QFrame(self.leftbox)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(80, 80))
        self.logo.setMaximumSize(QSize(16777215, 100))
        self.logo.setStyleSheet(u"QFrame#logo {\n"
"	image: url(:/my_icon/images/my_icon/origin.jpg);\n"
"\n"
"}\n"
"")
        self.logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.logo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.logo)

        self.btn_box = QFrame(self.leftbox)
        self.btn_box.setObjectName(u"btn_box")
        self.btn_box.setMinimumSize(QSize(180, 40))
#if QT_CONFIG(accessibility)
        self.btn_box.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.btn_box.setStyleSheet(u"QPushButton{\n"
"    border: none;\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"\n"
"    border-left: 1px solid transparent;\n"
"	border-left-color: rgb(152, 67, 255); \n"
"\n"
"    color: rgb(85, 0, 255);\n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
"	text-align: right;\n"
"    padding-left: 15px;\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"    border:none;\n"
"    background-color: gray; \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272\u4e3a\u7070\u8272 \n"
"    background-repeat: no-repeat;\n"
"    background-position: left 15px center;\n"
"    border-left: 0px solid transparent;\n"
"	color: rgb(0, 255, 127);  \u786e\u4fdd\u9f20\u6807\u60ac\u505c\u65f6\u7684\u5b57\u4f53\u989c\u8272 \n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
"    padding-left: 15px;\n"
" 	text-align: right;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    background-color: rgb(85, 0, 255);\n"
"    background-repeat: no-repeat;\n"
"  "
                        "  background-position: left 15px center;\n"
"    border-left: 0px solid transparent;\n"
"	color: rgb(0, 255, 127);  \u786e\u4fdd\u9f20\u6807\u60ac\u505c\u65f6\u7684\u5b57\u4f53\u989c\u8272 \n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
"    padding-left: 15px;\n"
" 	text-align: right;\n"
"}\n"
"QPushButton#menu_btn{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/caidanguanli.png);\n"
"}\n"
"QPushButton#camera_btn{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/a-shexiangtoujiankong.png);\n"
"}\n"
"QPushButton#yolo_btn{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/shenduxuexi.png);\n"
"}\n"
"QPushButton#log_btn{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/kongzhidianshezhi.png);\n"
"}\n"
"QPushButton#info_btn{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/xiangmuxinxi.png);\n"
"}\n"
"")
        self.btn_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.btn_box.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.btn_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_menu = QFrame(self.btn_box)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_menu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menu_btn = QPushButton(self.frame_menu)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMinimumSize(QSize(100, 40))
        self.menu_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.horizontalLayout_2.addWidget(self.menu_btn)


        self.verticalLayout_3.addWidget(self.frame_menu)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_camera = QFrame(self.btn_box)
        self.frame_camera.setObjectName(u"frame_camera")
        self.frame_camera.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_camera.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_camera)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.camera_btn = QPushButton(self.frame_camera)
        self.camera_btn.setObjectName(u"camera_btn")
        self.camera_btn.setMinimumSize(QSize(100, 40))
        self.camera_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_3.addWidget(self.camera_btn)


        self.verticalLayout_3.addWidget(self.frame_camera)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_log = QFrame(self.btn_box)
        self.frame_log.setObjectName(u"frame_log")
        self.frame_log.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_log.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_log)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.log_btn = QPushButton(self.frame_log)
        self.log_btn.setObjectName(u"log_btn")
        self.log_btn.setMinimumSize(QSize(100, 40))
        self.log_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_5.addWidget(self.log_btn)


        self.verticalLayout_3.addWidget(self.frame_log)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.frame_num = QFrame(self.btn_box)
        self.frame_num.setObjectName(u"frame_num")
        self.frame_num.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_num.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_num)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.yolo_btn = QPushButton(self.frame_num)
        self.yolo_btn.setObjectName(u"yolo_btn")
        self.yolo_btn.setMinimumSize(QSize(100, 40))
        self.yolo_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_4.addWidget(self.yolo_btn)


        self.verticalLayout_3.addWidget(self.frame_num)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.frame_info = QFrame(self.btn_box)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_info)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.info_btn = QPushButton(self.frame_info)
        self.info_btn.setObjectName(u"info_btn")
        self.info_btn.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.info_btn)


        self.verticalLayout_3.addWidget(self.frame_info)


        self.verticalLayout.addWidget(self.btn_box)

        self.tail_box = QFrame(self.leftbox)
        self.tail_box.setObjectName(u"tail_box")
        self.tail_box.setMinimumSize(QSize(0, 80))
        self.tail_box.setMaximumSize(QSize(16777215, 80))
        self.tail_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.tail_box.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.tail_box)


        self.TotalLayout.addWidget(self.leftbox)

        self.rightbox = QFrame(Mainbody)
        self.rightbox.setObjectName(u"rightbox")
        self.rightbox.setStyleSheet(u"QFrame#rightbox{\n"
" 	background-color: rgb(255, 255, 255); /* \u767d\u8272\u80cc\u666f */\n"
"	border-top: 0px solid rgb(255, 255, 255); \n"
"    border-right: 0px solid rgb(255, 255, 255);\n"
"    border-bottom: 0px solid rgb(255, 255, 255); \n"
"   	border-right: 0px solid rgb(255, 255, 255);\n"
"}")
        self.rightbox.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightbox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.rightbox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.topinfo = QFrame(self.rightbox)
        self.topinfo.setObjectName(u"topinfo")
        self.topinfo.setMaximumSize(QSize(16777215, 40))
        self.topinfo.setStyleSheet(u"QPushButton#maximizeButton{\n"
" 	background-repeat: no-repeat;\n"
"    background-position: center; /* background-position: left center; */\n"
"	background-image: url(:/v3/images/rescaled_icons_v3/zuidahua.png);\n"
"}\n"
"QPushButton#minimizeButton{\n"
" 	background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	background-image: url(:/v3/images/rescaled_icons_v3/zuixiaohua1.png);\n"
"}\n"
"QPushButton#closeButton{\n"
" 	background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	background-image: url(:/v3/images/rescaled_icons_v3/guanbi.png);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid rgba(148, 148, 148, 253);\n"
"	background-color:rgba(190,190,190, 248) ;/* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272\u4e3ax\u8272 */\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255); /* \u767d\u8272\u80cc\u666f */\n"
"    border-top: 1px solid rgb(255,215,0); /* \u9876\u90e8\u8fb9"
                        "\u6846\u7ea2\u8272 */\n"
"    border-right: 2px solid rgb(154,50,205); /* \u53f3\u4fa7\u8fb9\u6846\u7eff\u8272 */\n"
"    border-bottom: 1px solid rgb(154,50,205); /* \u5e95\u90e8\u8fb9\u6846\u84dd\u8272 */\n"
"    border-left: 2px solid rgb(255,215,0); /* \u5de6\u4fa7\u8fb9\u6846\u9ec4\u8272 */\n"
"}\n"
"")
        self.topinfo.setFrameShape(QFrame.Shape.StyledPanel)
        self.topinfo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.topinfo)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.info_text = QLabel(self.topinfo)
        self.info_text.setObjectName(u"info_text")
        self.info_text.setMinimumSize(QSize(100, 30))
        self.info_text.setStyleSheet(u"QLabel#info_text{\n"
"    background-color: none;\n"
"	font: 19pt \"\u534e\u6587\u4eff\u5b8b\";\n"
"	color: black;\n"
"	font-weight: bold;\n"
"	text-align: right;\n"
"    padding-left: 100px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.info_text)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.maximizeButton = QPushButton(self.topinfo)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(0, 0))
        self.maximizeButton.setMaximumSize(QSize(40, 40))
        self.maximizeButton.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.maximizeButton)

        self.minimizeButton = QPushButton(self.topinfo)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(0, 0))
        self.minimizeButton.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.minimizeButton)

        self.closeButton = QPushButton(self.topinfo)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(0, 0))
        self.closeButton.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.closeButton)


        self.verticalLayout_5.addWidget(self.topinfo)

        self.showbox = QFrame(self.rightbox)
        self.showbox.setObjectName(u"showbox")
        self.showbox.setFrameShape(QFrame.Shape.StyledPanel)
        self.showbox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.showbox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.splitter = QSplitter(self.showbox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.setStyleSheet(u"QSplitter {\n"
"    background-color: gray;\n"
"    border: 1px solid black;\n"
"    border-top: 0px;\n"
"    border-bottom: 0px;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"    background-color: gray; /* \u53ef\u4ee5\u6839\u636e\u9700\u8981\u66f4\u6539\u624b\u67c4\u7684\u989c\u8272 */\n"
"    border: 1px solid black;\n"
"    border-top: 0px;\n"
"    border-bottom: 0px;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: lightgray; /* \u9f20\u6807\u60ac\u505c\u5728\u624b\u67c4\u4e0a\u65f6\u7684\u989c\u8272 */\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background-color: darkgray; /* \u6309\u4e0b\u624b\u67c4\u65f6\u7684\u989c\u8272 */\n"
"}\n"
"")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.showimg = QLabel(self.splitter)
        self.showimg.setObjectName(u"showimg")
        self.showimg.setMinimumSize(QSize(220, 100))
        self.showimg.setPixmap(QPixmap(u":/my_icon/images/my_icon/jujube.png"))
        self.showimg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.showimg)

        self.verticalLayout_8.addWidget(self.splitter)


        self.verticalLayout_5.addWidget(self.showbox)

        self.jujube_status = QLabel(self.rightbox)
        self.jujube_status.setObjectName(u"jujube_status")
        self.jujube_status.setMaximumSize(QSize(16777215, 26))
        self.jujube_status.setStyleSheet(u"QLabel#jujube_status{\n"
"    background-color: none;\n"
"	font: 14pt \"\u65b9\u6b63\u59da\u4f53\";\n"
"	color: rgb(170, 0, 0);\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"    padding-left: 10px;\n"
"	background-color: rgb(255,255,255);\n"
"\n"
"	border-radius:30%;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.jujube_status)

        self.status_info = QLabel(self.rightbox)
        self.status_info.setObjectName(u"status_info")
        self.status_info.setMaximumSize(QSize(16777215, 26))
        self.status_info.setStyleSheet(u"QLabel#status_info{\n"
"    background-color: none;\n"
"	font: 14pt \"\u65b9\u6b63\u59da\u4f53\";\n"
"	color: black;\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"    padding-left: 10px;\n"
"	background-color: rgb(176, 176, 176);\n"
"\n"
"	border-radius:30%;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.status_info)


        self.TotalLayout.addWidget(self.rightbox)

        self.middlebox = QFrame(Mainbody)
        self.middlebox.setObjectName(u"middlebox")
        self.middlebox.setMinimumSize(QSize(0, 0))
        self.middlebox.setMaximumSize(QSize(0, 65536))
        self.middlebox.setStyleSheet(u"")
        self.middlebox.setFrameShape(QFrame.Shape.StyledPanel)
        self.middlebox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.middlebox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cam_settings = QFrame(self.middlebox)
        self.cam_settings.setObjectName(u"cam_settings")
        self.cam_settings.setMinimumSize(QSize(0, 0))
        self.cam_settings.setMaximumSize(QSize(0, 65536))
        self.cam_settings.setStyleSheet(u"QFrame#cam_settings{\n"
"	/*background-color: rgb(139,0,139);*/\n"
"	border-top-color: rgb(139,0,139);\n"
"	border-top-width: 2px;\n"
"	border-bottom-color: rgb(139,0,139);\n"
"	border-bottom-width: 2px;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"    border-left: 3px solid transparent;\n"
"    color: rgb(85, 0, 255);\n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover{\n"
"    border:none;\n"
"    background-color: gray; \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272\u4e3a\u7070\u8272 \n"
"    background-repeat: no-repeat;\n"
"    background-position: left 15px center;\n"
"    border-left: 0px solid transparent;\n"
"	color: rgb(0, 255, 127);  \u786e\u4fdd\u9f20\u6807\u60ac\u505c\u65f6\u7684\u5b57\u4f53\u989c\u8272 \n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
" 	text-align: center;\n"
"}\n"
"QPushButton:pressed{\n"
"    b"
                        "order:none;\n"
"    background-color: rgb(85, 0, 255);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left 15px center;\n"
"    border-left: 0px solid transparent;\n"
"    color: rgb(0, 255, 127); /* \u4fdd\u6301\u9f20\u6807\u60ac\u505c\u65f6\u7684\u5b57\u4f53\u989c\u8272 */\n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"QLabel{\n"
"    background-color: none;\n"
"	font: 12pt \"\u534e\u6587\u4e2d\u5b8b\";\n"
"	color: black;\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"}\n"
"QLabel#cam_logo1{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/shexiangtou.png);\n"
" 	background-repeat: no-repeat;\n"
" 	background-position: left 15px center;\n"
"	text-align: center;\n"
"}\n"
"QLabel#cam_logo2{\n"
"	background-image: url(:/v1/images/rescaled_icons_v1/shexiangtou_re.png);\n"
" 	background-repeat: no-repeat;\n"
" 	background-position: left 15px center;\n"
"	text-align: center;\n"
"}\n"
"QPushButton#cam_set1{\n"
"	background-ima"
                        "ge: url(:/v2/images/rescaled_icons_v2/shenduxuexi1.png);\n"
"}\n"
"QPushButton#cam_set2{background-image: url(:/v2/images/rescaled_icons_v2/bianji_re.png);}\n"
"QPushButton#cam_stop1{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/tubiaozhizuomobanyihuifu-.png);\n"
"}\n"
"QPushButton#cam_stop2{background-image: url(:/v1/images/rescaled_icons_v1/shexiangtou_guanbi_re.png);}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; /* \u9ed8\u8ba4\u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    color: black;            /* \u5b57\u4f53\u989c\u8272\u4e3a\u9ed1\u8272 */\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: lightgray; /* \u9f20\u6807\u60ac\u505c\u65f6\u80cc\u666f\u8272\u4e3a\u6d45\u7070\u8272 */\n"
"    color: black;                /* \u5b57\u4f53\u989c\u8272\u4fdd\u6301\u4e3a\u9ed1\u8272 */\n"
"}\n"
"QRadioButton{\n"
"	background-color: white; /* \u9ed8\u8ba4\u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    color: black;            /* \u5b57\u4f53\u989c\u8272\u4e3a\u9ed1\u8272 */\n"
"}\n"
"QRadi"
                        "oButton:hover {\n"
"    background-color: lightgray; /* \u9f20\u6807\u60ac\u505c\u65f6\u80cc\u666f\u8272\u4e3a\u6d45\u7070\u8272 */\n"
"    color: black;                /* \u5b57\u4f53\u989c\u8272\u4fdd\u6301\u4e3a\u9ed1\u8272 */\n"
"}")
        self.cam_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.cam_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.cam_settings)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_cam1 = QFrame(self.cam_settings)
        self.frame_cam1.setObjectName(u"frame_cam1")
        self.frame_cam1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cam1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_cam1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.cam_logo1 = QLabel(self.frame_cam1)
        self.cam_logo1.setObjectName(u"cam_logo1")
        self.cam_logo1.setMinimumSize(QSize(0, 40))
        self.cam_logo1.setMaximumSize(QSize(65536, 40))
        self.cam_logo1.setStyleSheet(u"")
        self.cam_logo1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.cam_logo1)

        self.IPview1 = QLabel(self.frame_cam1)
        self.IPview1.setObjectName(u"IPview1")
        self.IPview1.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_6.addWidget(self.IPview1)

        self.IPcam = QLineEdit(self.frame_cam1)
        self.IPcam.setObjectName(u"IPcam")

        self.verticalLayout_6.addWidget(self.IPcam)

        self.Portview1 = QLabel(self.frame_cam1)
        self.Portview1.setObjectName(u"Portview1")
        self.Portview1.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.Portview1)

        self.Portcam = QLineEdit(self.frame_cam1)
        self.Portcam.setObjectName(u"Portcam")

        self.verticalLayout_6.addWidget(self.Portcam)

        self.cam_set1 = QPushButton(self.frame_cam1)
        self.cam_set1.setObjectName(u"cam_set1")
        self.cam_set1.setMinimumSize(QSize(0, 40))
        self.cam_set1.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.cam_set1)

        self.cam_stop1 = QPushButton(self.frame_cam1)
        self.cam_stop1.setObjectName(u"cam_stop1")
        self.cam_stop1.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.cam_stop1)


        self.verticalLayout_4.addWidget(self.frame_cam1)


        self.horizontalLayout_9.addWidget(self.cam_settings)

        self.log_show = QFrame(self.middlebox)
        self.log_show.setObjectName(u"log_show")
        self.log_show.setMinimumSize(QSize(0, 0))
        self.log_show.setMaximumSize(QSize(0, 65536))
        self.log_show.setStyleSheet(u"QFrame#log_show{\n"
"	border-top-color: rgb(67,110,238);\n"
"	border-top-width: 2px;\n"
"	border-bottom-color: rgb(67,110,238);\n"
"	border-bottom-width: 2px;\n"
"}\n"
"QFrame#frame_log_info{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border:none;\n"
"}\n"
"QCheckBox{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 13pt \"\u65b9\u6b63\u59da\u4f53\";\n"
"	font-weight: bold;\n"
"}\n"
"QCheckBox:hover{\n"
"	color: rgb(0, 255, 0);\n"
"	background-color: rgb(185, 185, 185);\n"
"	font: 13pt \"\u65b9\u6b63\u59da\u4f53\";\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"    border-left: 3px solid transparent;\n"
"    color: rgb(85, 0, 255);\n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover{\n"
"    border:none;\n"
"    background-color: gray; \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272\u4e3a\u7070\u8272 \n"
"    background-repeat: no-repe"
                        "at;\n"
"    background-position: left 15px center;\n"
"    border-left: 0px solid transparent;\n"
"	color: rgb(0, 255, 127);  \u786e\u4fdd\u9f20\u6807\u60ac\u505c\u65f6\u7684\u5b57\u4f53\u989c\u8272 \n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
" 	text-align: center;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    background-color: rgb(85, 0, 255);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left 15px center;\n"
"    border-left: 0px solid transparent;\n"
"    color: rgb(0, 255, 127); /* \u4fdd\u6301\u9f20\u6807\u60ac\u505c\u65f6\u7684\u5b57\u4f53\u989c\u8272 */\n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"QLabel{\n"
"    background-color: none;\n"
"	font: 12pt \"\u534e\u6587\u4e2d\u5b8b\";\n"
"	color: black;\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"}\n"
"QLabel#cmd_logo{\n"
"	\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/yuanchengkongzhi.png);\n"
" 	background-repeat: n"
                        "o-repeat;\n"
" 	background-position: left 15px center;\n"
"	text-align: center;\n"
"}\n"
"QPushButton#cmd_set{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/shenduxuexi1.png); /* tcp\u76d1\u542c\u6309\u94ae */\n"
"} \n"
"QPushButton#cmd_stop{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/tubiaozhizuomobanyihuifu-.png);  /* \u7ed3\u675f\u76d1\u542c\u6309\u94ae */\n"
"} \n"
"QPushButton#re_counter{\n"
"	background-image: url(:/v2/images/rescaled_icons_v2/qingkong.png);  /* \u8ba1\u6570\u91cd\u7f6e\u6309\u94ae */\n"
"}\n"
"QLineEdit {\n"
"    background-color: white; /* \u9ed8\u8ba4\u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    color: black;            /* \u5b57\u4f53\u989c\u8272\u4e3a\u9ed1\u8272 */\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: lightgray; /* \u9f20\u6807\u60ac\u505c\u65f6\u80cc\u666f\u8272\u4e3a\u6d45\u7070\u8272 */\n"
"    color: black;                /* \u5b57\u4f53\u989c\u8272\u4fdd\u6301\u4e3a\u9ed1\u8272 */\n"
"}\n"
"/*horizontal \uff1a\u6c34\u5e73QSlider*/\n"
""
                        "QSlider::groove:horizontal {\n"
"border: 0px solid #bbb;\n"
"}\n"
"\n"
"/*1.\u6ed1\u52a8\u8fc7\u7684\u69fd\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::sub-page:horizontal {\n"
" /*\u69fd\u989c\u8272*/\n"
"background: rgb(90,49,255);\n"
" /*\u5916\u73af\u533a\u57df\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 2px;\n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:8px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:8px;\n"
"/*width\u5728\u8fd9\u91cc\u65e0\u6548\uff0c\u4e0d\u5199\u5373\u53ef*/\n"
"}\n"
"\n"
"/*2.\u672a\u6ed1\u52a8\u8fc7\u7684\u69fd\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::add-page:horizontal {\n"
"/*\u69fd\u989c\u8272*/\n"
"background: rgb(136, 136, 136);\n"
"/*\u5916\u73af\u5927\u5c0f0px\u5c31\u662f\u4e0d\u663e\u793a\uff0c\u9ed8\u8ba4\u4e5f\u662f0*/\n"
"border: 1px solid #777;\n"
"/*\u5916\u73af\u533a\u57df\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 2px;\n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:9px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df"
                        "\u9ad8\u5ea6*/\n"
"margin-bottom:9px;\n"
"}\n"
" \n"
"/*3.\u5e73\u65f6\u6ed1\u52a8\u7684\u6ed1\u5757\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::handle:horizontal {\n"
"/*\u6ed1\u5757\u989c\u8272*/\n"
"background: rgb(255, 243, 69);\n"
"/*\u6ed1\u5757\u7684\u5bbd\u5ea6*/\n"
"width: 10px;\n"
"/*\u6ed1\u5757\u5916\u73af\u4e3a1px\uff0c\u518d\u52a0\u989c\u8272*/\n"
"border: 1px solid rgb(193,204,208);\n"
" /*\u6ed1\u5757\u5916\u73af\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 5px; \n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:4px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:4px;\n"
"}\n"
"\n"
"/*4.\u624b\u52a8\u62c9\u52a8\u65f6\u663e\u793a\u7684\u6ed1\u5757\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::handle:horizontal:hover {\n"
"/*\u6ed1\u5757\u989c\u8272*/\n"
"background: rgb(85, 85, 255);\n"
"/*\u6ed1\u5757\u7684\u5bbd\u5ea6*/\n"
"width: 10px;\n"
"/*\u6ed1\u5757\u5916\u73af\u4e3a1px\uff0c\u518d\u52a0\u989c\u8272*/\n"
"border: 1px solid rgb(193,204,208);\n"
" /*\u6ed1\u5757"
                        "\u5916\u73af\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 5px; \n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:4px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:4px;\n"
"}\n"
"\n"
"/*5.\u624b\u52a8\u62c9\u52a8\u65f6\u663e\u793a\u7684\u6ed1\u5757\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::handle:horizontal:pressed {\n"
"/*\u6ed1\u5757\u989c\u8272*/\n"
"background: rgb(0, 170, 255);\n"
"/*\u6ed1\u5757\u7684\u5bbd\u5ea6*/\n"
"width: 10px;\n"
"/*\u6ed1\u5757\u5916\u73af\u4e3a1px\uff0c\u518d\u52a0\u989c\u8272*/\n"
"border: 1px solid rgb(193,204,208);\n"
" /*\u6ed1\u5757\u5916\u73af\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 5px; \n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:4px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:4px;\n"
"}")
        self.log_show.setFrameShape(QFrame.Shape.StyledPanel)
        self.log_show.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.log_show)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_cmd = QFrame(self.log_show)
        self.frame_cmd.setObjectName(u"frame_cmd")
        self.frame_cmd.setMinimumSize(QSize(0, 250))
        self.frame_cmd.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cmd.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_cmd)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cmd_logo = QLabel(self.frame_cmd)
        self.cmd_logo.setObjectName(u"cmd_logo")
        self.cmd_logo.setMinimumSize(QSize(0, 40))
        self.cmd_logo.setMaximumSize(QSize(16777215, 40))
        self.cmd_logo.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_12.addWidget(self.cmd_logo)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_20)

        self.IPviewcmd = QLabel(self.frame_cmd)
        self.IPviewcmd.setObjectName(u"IPviewcmd")
        self.IPviewcmd.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_12.addWidget(self.IPviewcmd)

        self.IPcmd = QLineEdit(self.frame_cmd)
        self.IPcmd.setObjectName(u"IPcmd")

        self.verticalLayout_12.addWidget(self.IPcmd)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_16)

        self.Portviewcmd = QLabel(self.frame_cmd)
        self.Portviewcmd.setObjectName(u"Portviewcmd")
        self.Portviewcmd.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_12.addWidget(self.Portviewcmd)

        self.Portcmd = QLineEdit(self.frame_cmd)
        self.Portcmd.setObjectName(u"Portcmd")

        self.verticalLayout_12.addWidget(self.Portcmd)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_21)

        self.cmd_set = QPushButton(self.frame_cmd)
        self.cmd_set.setObjectName(u"cmd_set")
        self.cmd_set.setMinimumSize(QSize(0, 40))
        self.cmd_set.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_12.addWidget(self.cmd_set)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_22)

        self.cmd_stop = QPushButton(self.frame_cmd)
        self.cmd_stop.setObjectName(u"cmd_stop")
        self.cmd_stop.setMinimumSize(QSize(0, 40))
        self.cmd_stop.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_12.addWidget(self.cmd_stop)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_23)


        self.verticalLayout_13.addWidget(self.frame_cmd)

        self.label_8 = QLabel(self.log_show)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 2))
        self.label_8.setMaximumSize(QSize(65536, 0))
        self.label_8.setStyleSheet(u"QLabel{\n"
"	border-top-color: rgb(67,110,238);\n"
"	border-top-width: 2px;\n"
"}")

        self.verticalLayout_13.addWidget(self.label_8)

        self.frame_log_info = QFrame(self.log_show)
        self.frame_log_info.setObjectName(u"frame_log_info")
        self.frame_log_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_log_info.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_log_info)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.yolo_counter = QCheckBox(self.frame_log_info)
        self.yolo_counter.setObjectName(u"yolo_counter")

        self.verticalLayout_16.addWidget(self.yolo_counter)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_27)

        self.jujube_select = QCheckBox(self.frame_log_info)
        self.jujube_select.setObjectName(u"jujube_select")

        self.verticalLayout_16.addWidget(self.jujube_select)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_10)

        self.conveyor_label = QLabel(self.frame_log_info)
        self.conveyor_label.setObjectName(u"conveyor_label")

        self.verticalLayout_16.addWidget(self.conveyor_label)

        self.conveyor_value = QSlider(self.frame_log_info)
        self.conveyor_value.setObjectName(u"conveyor_value")
        self.conveyor_value.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_16.addWidget(self.conveyor_value)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_15)

        self.LED_label = QLabel(self.frame_log_info)
        self.LED_label.setObjectName(u"LED_label")

        self.verticalLayout_16.addWidget(self.LED_label)

        self.LED_value = QSlider(self.frame_log_info)
        self.LED_value.setObjectName(u"LED_value")
        self.LED_value.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_16.addWidget(self.LED_value)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_14)

        self.re_counter = QPushButton(self.frame_log_info)
        self.re_counter.setObjectName(u"re_counter")
        self.re_counter.setMinimumSize(QSize(0, 40))
        self.re_counter.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_16.addWidget(self.re_counter)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_17)


        self.verticalLayout_13.addWidget(self.frame_log_info)


        self.horizontalLayout_9.addWidget(self.log_show)

        self.yolo_settings = QFrame(self.middlebox)
        self.yolo_settings.setObjectName(u"yolo_settings")
        self.yolo_settings.setMinimumSize(QSize(0, 0))
        self.yolo_settings.setMaximumSize(QSize(0, 65536))
        self.yolo_settings.setStyleSheet(u"QFrame#yolo_settings{\n"
"	border-top-color: rgb(78,238,148);\n"
"	border-top-width: 2px;\n"
"	border-bottom-color: rgb(78,238,148);\n"
"	border-bottom-width: 2px;\n"
"}\n"
"QFrame#frame_yolo{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border:none;\n"
"}\n"
"QLabel{\n"
"    background-color: none;\n"
"	font: 18pt \"\u534e\u6587\u4e2d\u5b8b\";\n"
"	color: black;\n"
"	font-weight: bold;\n"
"	text-align: right;\n"
"}\n"
"QLabel#Show_device{\n"
"    background-color: none;\n"
"	font: 11pt \"\u534e\u6587\u4e2d\u5b8b\";\n"
"	color: rgb(170, 0, 255);\n"
"	font-weight: bold;\n"
"	text-align: right;\n"
"}\n"
"QCheckBox{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 11pt \"\u65b9\u6b63\u59da\u4f53\";\n"
"	font-weight: bold;\n"
"}\n"
"/*horizontal \uff1a\u6c34\u5e73QSlider*/\n"
"QSlider::groove:horizontal {\n"
"border: 0px solid #bbb;\n"
"}\n"
"\n"
"/*1.\u6ed1\u52a8\u8fc7\u7684\u69fd\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::sub-page:horizontal {\n"
" /*\u69fd\u989c\u8272*/\n"
"background: rgb(90,49,255);\n"
" /*\u5916\u73af\u533a"
                        "\u57df\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 2px;\n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:8px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:8px;\n"
"/*width\u5728\u8fd9\u91cc\u65e0\u6548\uff0c\u4e0d\u5199\u5373\u53ef*/\n"
"}\n"
"\n"
"/*2.\u672a\u6ed1\u52a8\u8fc7\u7684\u69fd\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::add-page:horizontal {\n"
"/*\u69fd\u989c\u8272*/\n"
"background: rgb(136, 136, 136);\n"
"/*\u5916\u73af\u5927\u5c0f0px\u5c31\u662f\u4e0d\u663e\u793a\uff0c\u9ed8\u8ba4\u4e5f\u662f0*/\n"
"border: 1px solid #777;\n"
"/*\u5916\u73af\u533a\u57df\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 2px;\n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:9px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:9px;\n"
"}\n"
" \n"
"/*3.\u5e73\u65f6\u6ed1\u52a8\u7684\u6ed1\u5757\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::handle:horizontal {\n"
"/*\u6ed1\u5757\u989c\u8272*/\n"
"background: rgb(255, 85, 0);\n"
"/*\u6ed1\u5757\u7684\u5bbd"
                        "\u5ea6*/\n"
"width: 10px;\n"
"/*\u6ed1\u5757\u5916\u73af\u4e3a1px\uff0c\u518d\u52a0\u989c\u8272*/\n"
"border: 1px solid rgb(193,204,208);\n"
" /*\u6ed1\u5757\u5916\u73af\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 5px; \n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:4px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:4px;\n"
"}\n"
"\n"
"/*4.\u624b\u52a8\u62c9\u52a8\u65f6\u663e\u793a\u7684\u6ed1\u5757\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::handle:horizontal:hover {\n"
"/*\u6ed1\u5757\u989c\u8272*/\n"
"background: rgb(85, 85, 255);\n"
"/*\u6ed1\u5757\u7684\u5bbd\u5ea6*/\n"
"width: 10px;\n"
"/*\u6ed1\u5757\u5916\u73af\u4e3a1px\uff0c\u518d\u52a0\u989c\u8272*/\n"
"border: 1px solid rgb(193,204,208);\n"
" /*\u6ed1\u5757\u5916\u73af\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 5px; \n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:4px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:4px;\n"
"}\n"
"\n"
"/*5.\u624b\u52a8\u62c9\u52a8\u65f6"
                        "\u663e\u793a\u7684\u6ed1\u5757\u8bbe\u8ba1\u53c2\u6570*/\n"
"QSlider::handle:horizontal:pressed {\n"
"/*\u6ed1\u5757\u989c\u8272*/\n"
"background: rgb(0, 170, 255);\n"
"/*\u6ed1\u5757\u7684\u5bbd\u5ea6*/\n"
"width: 10px;\n"
"/*\u6ed1\u5757\u5916\u73af\u4e3a1px\uff0c\u518d\u52a0\u989c\u8272*/\n"
"border: 1px solid rgb(193,204,208);\n"
" /*\u6ed1\u5757\u5916\u73af\u5012\u5706\u89d2\u5ea6*/\n"
"border-radius: 5px; \n"
" /*\u4e0a\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-top:4px;\n"
" /*\u4e0b\u906e\u4f4f\u533a\u57df\u9ad8\u5ea6*/\n"
"margin-bottom:4px;\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	width: 8px;\n"
"    height: 8px;\n"
"    border-radius:  4px;\n"
"    background-color:rgb(255,255, 255);\n"
"    border:   1px solid rgb(124, 124, 124);  \n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-radius:  4px;\n"
"    background-color:    rgb(85, 85, 255);   \n"
"    border:  1px solid rgb(124, 124, 124);  \n"
"}\n"
"QRadioButton{\n"
"	background-color: w"
                        "hite; /* \u9ed8\u8ba4\u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    color: black;            /* \u5b57\u4f53\u989c\u8272\u4e3a\u9ed1\u8272 */\n"
"}\n"
"QRadioButton:hover {\n"
"    background-color: lightgray; /* \u9f20\u6807\u60ac\u505c\u65f6\u80cc\u666f\u8272\u4e3a\u6d45\u7070\u8272 */\n"
"    color: black;                /* \u5b57\u4f53\u989c\u8272\u4fdd\u6301\u4e3a\u9ed1\u8272 */\n"
"}")
        self.yolo_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.yolo_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.yolo_settings)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_3 = QFrame(self.yolo_settings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.CPU_shot = QRadioButton(self.frame_3)
        self.CPU_shot.setObjectName(u"CPU_shot")
        font = QFont()
        font.setPointSize(12)
        self.CPU_shot.setFont(font)

        self.verticalLayout_18.addWidget(self.CPU_shot)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_24)

        self.GPU_shot = QRadioButton(self.frame_3)
        self.GPU_shot.setObjectName(u"GPU_shot")
        self.GPU_shot.setFont(font)

        self.verticalLayout_18.addWidget(self.GPU_shot)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_25)

        self.Show_device = QLabel(self.frame_3)
        self.Show_device.setObjectName(u"Show_device")
        self.Show_device.setMinimumSize(QSize(0, 40))
        self.Show_device.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.Show_device)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.frame_yolo = QFrame(self.yolo_settings)
        self.frame_yolo.setObjectName(u"frame_yolo")
        self.frame_yolo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_yolo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_yolo)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_11)

        self.iou_label = QLabel(self.frame_yolo)
        self.iou_label.setObjectName(u"iou_label")

        self.verticalLayout_10.addWidget(self.iou_label)

        self.iou_slider = QSlider(self.frame_yolo)
        self.iou_slider.setObjectName(u"iou_slider")
        self.iou_slider.setMinimum(1)
        self.iou_slider.setMaximum(99)
        self.iou_slider.setValue(50)
        self.iou_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_10.addWidget(self.iou_slider)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)

        self.conf_label = QLabel(self.frame_yolo)
        self.conf_label.setObjectName(u"conf_label")

        self.verticalLayout_10.addWidget(self.conf_label)

        self.conf_slider = QSlider(self.frame_yolo)
        self.conf_slider.setObjectName(u"conf_slider")
        self.conf_slider.setMinimum(1)
        self.conf_slider.setMaximum(99)
        self.conf_slider.setValue(50)
        self.conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_10.addWidget(self.conf_slider)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.line_label = QLabel(self.frame_yolo)
        self.line_label.setObjectName(u"line_label")

        self.verticalLayout_10.addWidget(self.line_label)

        self.line_slider = QSlider(self.frame_yolo)
        self.line_slider.setObjectName(u"line_slider")
        self.line_slider.setMinimum(10)
        self.line_slider.setMaximum(50)
        self.line_slider.setValue(10)
        self.line_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_10.addWidget(self.line_slider)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)


        self.verticalLayout_9.addWidget(self.frame_yolo)

        self.frame_sort = QFrame(self.yolo_settings)
        self.frame_sort.setObjectName(u"frame_sort")
        self.frame_sort.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sort.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_sort)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_12)

        self.sort_label = QLabel(self.frame_sort)
        self.sort_label.setObjectName(u"sort_label")

        self.verticalLayout_11.addWidget(self.sort_label)

        self.sort_slider = QSlider(self.frame_sort)
        self.sort_slider.setObjectName(u"sort_slider")
        self.sort_slider.setMinimum(10)
        self.sort_slider.setMaximum(80)
        self.sort_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_11.addWidget(self.sort_slider)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_13)


        self.verticalLayout_9.addWidget(self.frame_sort)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_9)

        self.show_yolo = QCheckBox(self.yolo_settings)
        self.show_yolo.setObjectName(u"show_yolo")
        self.show_yolo.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.show_yolo)

        self.son_forward = QLabel(self.yolo_settings)
        self.son_forward.setObjectName(u"son_forward")
        self.son_forward.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.son_forward.setStyleSheet(u"QLabel#son_forward{\n"
"	font: 16pt \"\u534e\u6587\u65b0\u9b4f\";\n"
"}")
        self.son_forward.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_9.addWidget(self.son_forward)

        self.show_yolo_re = QCheckBox(self.yolo_settings)
        self.show_yolo_re.setObjectName(u"show_yolo_re")

        self.verticalLayout_9.addWidget(self.show_yolo_re)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)


        self.horizontalLayout_9.addWidget(self.yolo_settings)

        self.our_info = QFrame(self.middlebox)
        self.our_info.setObjectName(u"our_info")
        self.our_info.setMinimumSize(QSize(0, 0))
        self.our_info.setMaximumSize(QSize(0, 65536))
        self.our_info.setStyleSheet(u"QFrame#our_info{\n"
"	border-top-color: rgb(205,16,118);\n"
"	border-top-width: 2px;\n"
"	border-bottom-color: rgb(205,16,118);\n"
"	border-bottom-width: 2px;\n"
"}\n"
"QFrame#frame_our{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border:none;\n"
"}\n"
"QLabel{\n"
"    border:none;\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"    border-left: 3px solid transparent;\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Times New Roman\";\n"
"    font-weight: bold;\n"
"	text-align: center;\n"
"}\n"
"")
        self.our_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.our_info.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.our_info)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_our = QFrame(self.our_info)
        self.frame_our.setObjectName(u"frame_our")
        self.frame_our.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_our.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_our)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_4 = QLabel(self.frame_our)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_15.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame_our)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_3)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_18)

        self.label_2 = QLabel(self.frame_our)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_15.addWidget(self.label_2)

        self.label = QLabel(self.frame_our)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_19)

        self.label_5 = QLabel(self.frame_our)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_15.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_our)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_15.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_our)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_15.addWidget(self.label_7)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_26)


        self.verticalLayout_14.addWidget(self.frame_our)


        self.horizontalLayout_9.addWidget(self.our_info)


        self.TotalLayout.addWidget(self.middlebox)


        self.verticalLayout_2.addLayout(self.TotalLayout)


        self.retranslateUi(Mainbody)

        QMetaObject.connectSlotsByName(Mainbody)
    # setupUi

    def retranslateUi(self, Mainbody):
        Mainbody.setWindowTitle(QCoreApplication.translate("Mainbody", u"\u7ea2\u67a3\u9ed1\u6591\u70b9\u7684\u667a\u80fd\u5316\u8bc6\u522b\u4e0e\u5206\u62e3-GUI", None))
        self.menu_btn.setText(QCoreApplication.translate("Mainbody", u"\u83dc\u5355      ", None))
        self.camera_btn.setText(QCoreApplication.translate("Mainbody", u"\u6444\u50cf\u5934\u8bbe\u7f6e", None))
        self.log_btn.setText(QCoreApplication.translate("Mainbody", u"\u8fd0\u884c\u63a7\u5236    ", None))
        self.yolo_btn.setText(QCoreApplication.translate("Mainbody", u"\u53c2\u6570\u8c03\u6574    ", None))
        self.info_btn.setText(QCoreApplication.translate("Mainbody", u"\u5173\u4e8e\u9879\u76ee    ", None))
        self.info_text.setText(QCoreApplication.translate("Mainbody", u"\u7ea2\u67a3\u9ed1\u6591\u70b9\u7684\u667a\u80fd\u5316\u8bc6\u522b\u4e0e\u5206\u62e3---GUI\u64cd\u7eb5\u754c\u9762", None))
        self.maximizeButton.setText("")
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.showimg.setText("")
        self.jujube_status.setText(QCoreApplication.translate("Mainbody", u"\u7ea2\u67a3\u8ba1\u6570:    \u5065\u5eb7:None    \u9ed1\u6591\u75c5:None", None))
        self.status_info.setText(QCoreApplication.translate("Mainbody", u":\u6b22\u8fce\u4f7f\u7528\uff01", None))
        self.cam_logo1.setText(QCoreApplication.translate("Mainbody", u"\u6444 \u50cf \u6a21 \u5757", None))
        self.IPview1.setText(QCoreApplication.translate("Mainbody", u"IP", None))
        self.IPcam.setText("")
        self.IPcam.setPlaceholderText(QCoreApplication.translate("Mainbody", u"\u5f53\u524dIP: 0.0.0.0", None))
        self.Portview1.setText(QCoreApplication.translate("Mainbody", u"Port", None))
        self.Portcam.setText("")
        self.Portcam.setPlaceholderText(QCoreApplication.translate("Mainbody", u"\u5f53\u524dPort: 53001", None))
        self.cam_set1.setText(QCoreApplication.translate("Mainbody", u"\u542f\u7528TCP\u76d1\u542c", None))
        self.cam_stop1.setText(QCoreApplication.translate("Mainbody", u"\u7ed3\u675f\u76d1\u542c", None))
        self.cmd_logo.setText(QCoreApplication.translate("Mainbody", u"\u547d \u4ee4 \u5355 \u5143", None))
        self.IPviewcmd.setText(QCoreApplication.translate("Mainbody", u"IP", None))
        self.IPcmd.setPlaceholderText(QCoreApplication.translate("Mainbody", u"\u5f53\u524dIP: 0.0.0.0", None))
        self.Portviewcmd.setText(QCoreApplication.translate("Mainbody", u"Port", None))
        self.Portcmd.setPlaceholderText(QCoreApplication.translate("Mainbody", u"\u5f53\u524dPort: 53003", None))
        self.cmd_set.setText(QCoreApplication.translate("Mainbody", u"\u542f\u7528TCP\u76d1\u542c", None))
        self.cmd_stop.setText(QCoreApplication.translate("Mainbody", u"\u7ed3\u675f\u76d1\u542c", None))
        self.label_8.setText("")
        self.yolo_counter.setText(QCoreApplication.translate("Mainbody", u"\u7ea2\u67a3\u8ba1\u6570\u542f\u52a8", None))
        self.jujube_select.setText(QCoreApplication.translate("Mainbody", u"\u7ea2\u67a3\u5206\u62e3\u542f\u52a8", None))
        self.conveyor_label.setText(QCoreApplication.translate("Mainbody", u"\u4f20\u9001\u5e26\u901f\u7387:  None", None))
        self.LED_label.setText(QCoreApplication.translate("Mainbody", u"\u7167\u660eLED\u4eae\u5ea6: None", None))
        self.re_counter.setText(QCoreApplication.translate("Mainbody", u"\u6e05\u7a7a\u7ea2\u67a3\u8ba1\u6570", None))
        self.CPU_shot.setText(QCoreApplication.translate("Mainbody", u"\u9009\u62e9CPU\u63a8\u7406", None))
        self.GPU_shot.setText(QCoreApplication.translate("Mainbody", u"\u9009\u62e9GPU\u63a8\u7406(\u9ed8\u8ba4PCIE\u987a\u5e8fTop1)", None))
        self.Show_device.setText(QCoreApplication.translate("Mainbody", u"\u63a8\u7406\u8bbe\u5907: ", None))
        self.iou_label.setText(QCoreApplication.translate("Mainbody", u"IOU\u9608\u503c: None", None))
        self.conf_label.setText(QCoreApplication.translate("Mainbody", u"\u7f6e\u4fe1\u5ea6\u9608\u503c: None", None))
        self.line_label.setText(QCoreApplication.translate("Mainbody", u"\u8fb9\u6846\u5bbd\u5ea6: None", None))
        self.sort_label.setText(QCoreApplication.translate("Mainbody", u"\u5206\u62e3\u9608\u503c\u7ebf: None", None))
        self.show_yolo.setText(QCoreApplication.translate("Mainbody", u"\u5c55\u793a\u5e76\u5e94\u7528\u68c0\u6d4b\u540e\u7684\u89c6\u9891\u6d41", None))
        self.son_forward.setText(QCoreApplication.translate("Mainbody", u"\u2193", None))
        self.show_yolo_re.setText(QCoreApplication.translate("Mainbody", u"\u5c55\u793a\u8c03\u6574\u53c2\u6570\u4e8e\u89c6\u9891\u6d41", None))
        self.label_4.setText(QCoreApplication.translate("Mainbody", u"<html><head/><body><p><span style=\" color:#aa00ff;\">\u9879\u76ee\u76ee\u7684:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Mainbody", u"\u672c\u9879\u76ee\u5f00\u53d1\u4e86\u4e00\u5957\u7ea2\u67a3\u9ed1\u6591\u70b9\u667a\u80fd\u5316\u8bc6\u522b\u4e0e\u5206\u62e3\u7cfb\u7edf\uff0c\u901a\u8fc7\u96c6\u6210\u9ad8\u5206\u8fa8\u7387\u6444\u50cf\u5934\u4e0e\u9ad8\u6027\u80fd\u5355\u7247\u673a\uff0c\u8fd0\u7528\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5YOLOv11\u5bf9\u7ea2\u67a3\u8868\u9762\u8fdb\u884c\u5b9e\u65f6\u56fe\u50cf\u91c7\u96c6\u4e0e\u5206\u6790\uff0c\u51c6\u786e\u8bc6\u522b\u5e76\u5206\u7c7b\u5e26\u6709\u9ed1\u6591\u70b9\u7684\u7ea2\u67a3\u3002\u7cfb\u7edf\u81ea\u52a8\u5316\u7a0b\u5ea6\u9ad8\uff0c\u5927\u5e45\u63d0\u9ad8\u5206\u62e3\u6548\u7387\u548c\u51c6\u786e\u6027\uff0c\u51cf\u5c11\u4eba\u5de5\u6210\u672c\uff0c\u4fdd\u8bc1\u7ea2\u67a3\u54c1\u8d28\uff0c\u6ee1\u8db3\u5e02\u573a\u9700\u6c42\u3002\u9879\u76ee\u8fd8\u5305\u62ec\u8de8\u5e73\u53f0\u7684APP-GUI\u754c\u9762\uff0c\u63d0\u5347\u7528\u6237\u4ea4\u4e92\u4f53\u9a8c\uff0c\u5b9e\u73b0\u667a\u80fd\u5316\u63a7\u5236\u3002", None))
        self.label_2.setText(QCoreApplication.translate("Mainbody", u"<html><head/><body><p><span style=\" font-weight:700; color:#aa00ff;\">\u9879\u76ee\u610f\u4e49:</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Mainbody", u"\u8be5\u9879\u76ee\u9488\u5bf9\u65b0\u7586\u7ea2\u67a3\u4ea7\u4e1a\u4e2d\u9ed1\u6591\u75c5\u8bc6\u522b\u4e0e\u5206\u62e3\u7684\u96be\u9898\uff0c\u63d0\u4f9b\u4e86\u4e00\u79cd\u9ad8\u6548\u3001\u81ea\u52a8\u5316\u7684\u89e3\u51b3\u65b9\u6848\u3002\u5b83\u4e0d\u4ec5\u63d0\u5347\u4e86\u7ea2\u67a3\u52a0\u5de5\u7684\u6548\u7387\u548c\u4ea7\u54c1\u54c1\u8d28\uff0c\u8fd8\u63a8\u52a8\u4e86\u519c\u4e1a\u73b0\u4ee3\u5316\uff0c\u54cd\u5e94\u4e86\u56fd\u5bb6\u5bf9\u98df\u54c1\u5b89\u5168\u548c\u519c\u4e1a\u79d1\u6280\u521b\u65b0\u7684\u53f7\u53ec\u3002\u901a\u8fc7\u667a\u80fd\u5316\u6280\u672f\u7684\u5e94\u7528\uff0c\u9879\u76ee\u6709\u52a9\u4e8e\u63d0\u5347\u519c\u4e1a\u4ea7\u4e1a\u7684\u56fd\u9645\u7ade\u4e89\u529b\uff0c\u4fc3\u8fdb\u5730\u533a\u7ecf\u6d4e\u53d1\u5c55\uff0c\u4e3a\u519c\u4e1a\u79cd\u690d\u6237\u589e\u52a0\u6536\u5165\uff0c\u5177\u6709\u663e\u8457\u7684\u793e\u4f1a\u548c\u7ecf\u6d4e\u4ef7\u503c\u3002\u540c\u65f6\uff0c\u9879\u76ee\u7684\u5b9e\u65bd\u6709\u52a9\u4e8e\u63a8\u52a8\u667a\u80fd\u519c\u4e1a\u6280"
                        "\u672f\u7684\u53d1\u5c55\uff0c\u4e3a\u672a\u6765\u519c\u4e1a\u4ea7\u4e1a\u7684\u667a\u80fd\u5316\u8f6c\u578b\u63d0\u4f9b\u4e86\u53c2\u8003\u548c\u793a\u8303\u3002", None))
        self.label_5.setText(QCoreApplication.translate("Mainbody", u"<html><head/><body><p><span style=\" font-weight:700; color:#aa00ff;\">\u5f00\u53d1\u8005:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Mainbody", u"persist-1", None))
        self.label_7.setText(QCoreApplication.translate("Mainbody", u"persist1@126.com", None))
    # retranslateUi


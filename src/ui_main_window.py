# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/main_window.ui'
#
# Created: Fri Nov  7 13:55:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 417)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_2 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(22, 22))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(628, 349))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scroll_area_viewer = Viewer(self.centralwidget)
        self.scroll_area_viewer.setAutoFillBackground(True)
        self.scroll_area_viewer.setStyleSheet("background-color: rgb(5, 5, 5);")
        self.scroll_area_viewer.setFrameShape(QtGui.QFrame.NoFrame)
        self.scroll_area_viewer.setFrameShadow(QtGui.QFrame.Plain)
        self.scroll_area_viewer.setLineWidth(0)
        self.scroll_area_viewer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_viewer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_viewer.setWidgetResizable(True)
        self.scroll_area_viewer.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_area_viewer.setObjectName("scroll_area_viewer")
        self.scroll_area_widget_contents = QtGui.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 626, 344))
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scroll_area_widget_contents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.scroll_area_widget_contents)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setLineWidth(0)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_2 1.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.scroll_area_viewer.setWidget(self.scroll_area_widget_contents)
        self.verticalLayout_2.addWidget(self.scroll_area_viewer)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_recent_files = QtGui.QMenu(self.menu_file)
        self.menu_recent_files.setObjectName("menu_recent_files")
        self.menu_view = QtGui.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_navegation = QtGui.QMenu(self.menubar)
        self.menu_navegation.setObjectName("menu_navegation")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Settings = QtGui.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        MainWindow.setMenuBar(self.menubar)
        self.toolbar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolbar.setAcceptDrops(True)
        self.toolbar.setAutoFillBackground(True)
        self.toolbar.setMovable(False)
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolbar.setFloatable(False)
        self.toolbar.setObjectName("toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_18.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon1)
        self.action_open.setMenuRole(QtGui.QAction.TextHeuristicRole)
        self.action_open.setIconVisibleInMenu(True)
        self.action_open.setObjectName("action_open")
        self.action_about = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_31.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon2)
        self.action_about.setObjectName("action_about")
        self.action_about_qt = QtGui.QAction(MainWindow)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_exit = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exit.setIcon(icon3)
        self.action_exit.setObjectName("action_exit")
        self.action_next_page = QtGui.QAction(MainWindow)
        self.action_next_page.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next_page.setIcon(icon4)
        self.action_next_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_next_page.setVisible(True)
        self.action_next_page.setPriority(QtGui.QAction.NormalPriority)
        self.action_next_page.setObjectName("action_next_page")
        self.action_previous_page = QtGui.QAction(MainWindow)
        self.action_previous_page.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_previous_page.setIcon(icon5)
        self.action_previous_page.setObjectName("action_previous_page")
        self.action_first_page = QtGui.QAction(MainWindow)
        self.action_first_page.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_first_page.setIcon(icon6)
        self.action_first_page.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.action_first_page.setObjectName("action_first_page")
        self.action_last_page = QtGui.QAction(MainWindow)
        self.action_last_page.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_last_page.setIcon(icon7)
        self.action_last_page.setObjectName("action_last_page")
        self.action_rotate_left = QtGui.QAction(MainWindow)
        self.action_rotate_left.setCheckable(False)
        self.action_rotate_left.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_rotate_left.setIcon(icon8)
        self.action_rotate_left.setObjectName("action_rotate_left")
        self.action_rotate_right = QtGui.QAction(MainWindow)
        self.action_rotate_right.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_rotate_right.setIcon(icon9)
        self.action_rotate_right.setObjectName("action_rotate_right")
        self.action_vertical_adjust = QtGui.QAction(MainWindow)
        self.action_vertical_adjust.setCheckable(True)
        self.action_vertical_adjust.setChecked(True)
        self.action_vertical_adjust.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_vertical_adjust.setIcon(icon10)
        self.action_vertical_adjust.setAutoRepeat(True)
        self.action_vertical_adjust.setObjectName("action_vertical_adjust")
        self.action_horizontal_adjust = QtGui.QAction(MainWindow)
        self.action_horizontal_adjust.setCheckable(True)
        self.action_horizontal_adjust.setChecked(False)
        self.action_horizontal_adjust.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_horizontal_adjust.setIcon(icon11)
        self.action_horizontal_adjust.setObjectName("action_horizontal_adjust")
        self.action_fullscreen = QtGui.QAction(MainWindow)
        self.action_fullscreen.setCheckable(False)
        self.action_fullscreen.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_fullscreen.setIcon(icon12)
        self.action_fullscreen.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.action_fullscreen.setObjectName("action_fullscreen")
        self.action_go_to_page = QtGui.QAction(MainWindow)
        self.action_go_to_page.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_go_to_page.setIcon(icon13)
        self.action_go_to_page.setObjectName("action_go_to_page")
        self.action_best_fit = QtGui.QAction(MainWindow)
        self.action_best_fit.setCheckable(True)
        self.action_best_fit.setChecked(False)
        self.action_best_fit.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_best_fit.setIcon(icon14)
        self.action_best_fit.setObjectName("action_best_fit")
        self.action_preferences = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/image/document-properties.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_preferences.setIcon(icon15)
        self.action_preferences.setObjectName("action_preferences")
        self.action_original_fit = QtGui.QAction(MainWindow)
        self.action_original_fit.setCheckable(True)
        self.action_original_fit.setChecked(False)
        self.action_original_fit.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_original_fit.setIcon(icon16)
        self.action_original_fit.setObjectName("action_original_fit")
        self.action_show_toolbar = QtGui.QAction(MainWindow)
        self.action_show_toolbar.setCheckable(True)
        self.action_show_toolbar.setChecked(True)
        self.action_show_toolbar.setObjectName("action_show_toolbar")
        self.action_show_statusbar = QtGui.QAction(MainWindow)
        self.action_show_statusbar.setCheckable(True)
        self.action_show_statusbar.setChecked(True)
        self.action_show_statusbar.setObjectName("action_show_statusbar")
        self.action_add_bookmark = QtGui.QAction(MainWindow)
        self.action_add_bookmark.setEnabled(False)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/image/bookmark-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_bookmark.setIcon(icon17)
        self.action_add_bookmark.setVisible(True)
        self.action_add_bookmark.setObjectName("action_add_bookmark")
        self.action_remove_bookmark = QtGui.QAction(MainWindow)
        self.action_remove_bookmark.setEnabled(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/image/edit-delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_remove_bookmark.setIcon(icon18)
        self.action_remove_bookmark.setObjectName("action_remove_bookmark")
        self.action_bookmark_manager = QtGui.QAction(MainWindow)
        self.action_bookmark_manager.setIcon(icon15)
        self.action_bookmark_manager.setObjectName("action_bookmark_manager")
        self.action_open_folder = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_21.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_folder.setIcon(icon19)
        self.action_open_folder.setMenuRole(QtGui.QAction.TextHeuristicRole)
        self.action_open_folder.setIconVisibleInMenu(True)
        self.action_open_folder.setObjectName("action_open_folder")
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_open_folder)
        self.menu_file.addAction(self.menu_recent_files.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_view.addAction(self.action_fullscreen)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_original_fit)
        self.menu_view.addAction(self.action_vertical_adjust)
        self.menu_view.addAction(self.action_horizontal_adjust)
        self.menu_view.addAction(self.action_best_fit)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_rotate_left)
        self.menu_view.addAction(self.action_rotate_right)
        self.menu_navegation.addAction(self.action_next_page)
        self.menu_navegation.addAction(self.action_previous_page)
        self.menu_navegation.addSeparator()
        self.menu_navegation.addAction(self.action_first_page)
        self.menu_navegation.addAction(self.action_last_page)
        self.menu_navegation.addSeparator()
        self.menu_navegation.addAction(self.action_go_to_page)
        self.menu_Help.addAction(self.action_about)
        self.menu_Help.addAction(self.action_about_qt)
        self.menu_Settings.addAction(self.action_show_toolbar)
        self.menu_Settings.addAction(self.action_show_statusbar)
        self.menu_Settings.addSeparator()
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_navegation.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolbar.addAction(self.action_open)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_first_page)
        self.toolbar.addAction(self.action_previous_page)
        self.toolbar.addAction(self.action_next_page)
        self.toolbar.addAction(self.action_last_page)
        self.toolbar.addAction(self.action_go_to_page)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_rotate_left)
        self.toolbar.addAction(self.action_rotate_right)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_original_fit)
        self.toolbar.addAction(self.action_vertical_adjust)
        self.toolbar.addAction(self.action_horizontal_adjust)
        self.toolbar.addAction(self.action_best_fit)
        self.toolbar.addAction(self.action_fullscreen)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pynocchio Comic Reader", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setAccessibleName(QtGui.QApplication.translate("MainWindow", "Pyellow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_recent_files.setTitle(QtGui.QApplication.translate("MainWindow", "&Recent files", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_view.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_navegation.setTitle(QtGui.QApplication.translate("MainWindow", "&Navegation", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Settings.setTitle(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.toolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setText(QtGui.QApplication.translate("MainWindow", "&About Pynocchio", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about_qt.setText(QtGui.QApplication.translate("MainWindow", "&About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_next_page.setText(QtGui.QApplication.translate("MainWindow", "&Next page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_next_page.setShortcut(QtGui.QApplication.translate("MainWindow", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.action_previous_page.setText(QtGui.QApplication.translate("MainWindow", "&Previous page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_previous_page.setShortcut(QtGui.QApplication.translate("MainWindow", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.action_first_page.setText(QtGui.QApplication.translate("MainWindow", "&First page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_first_page.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Left", None, QtGui.QApplication.UnicodeUTF8))
        self.action_last_page.setText(QtGui.QApplication.translate("MainWindow", "&Last page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_last_page.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Right", None, QtGui.QApplication.UnicodeUTF8))
        self.action_rotate_left.setText(QtGui.QApplication.translate("MainWindow", "&Rotate left", None, QtGui.QApplication.UnicodeUTF8))
        self.action_rotate_left.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.action_rotate_right.setText(QtGui.QApplication.translate("MainWindow", "&Rotate right", None, QtGui.QApplication.UnicodeUTF8))
        self.action_rotate_right.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.action_vertical_adjust.setText(QtGui.QApplication.translate("MainWindow", "&Vertical adjust", None, QtGui.QApplication.UnicodeUTF8))
        self.action_vertical_adjust.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+J", None, QtGui.QApplication.UnicodeUTF8))
        self.action_horizontal_adjust.setText(QtGui.QApplication.translate("MainWindow", "&Horizontal adjust", None, QtGui.QApplication.UnicodeUTF8))
        self.action_horizontal_adjust.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.action_fullscreen.setText(QtGui.QApplication.translate("MainWindow", "&Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.action_fullscreen.setShortcut(QtGui.QApplication.translate("MainWindow", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.action_go_to_page.setText(QtGui.QApplication.translate("MainWindow", "&Go to page...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_go_to_page.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.action_best_fit.setText(QtGui.QApplication.translate("MainWindow", "&Whole page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_best_fit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.action_preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.action_original_fit.setText(QtGui.QApplication.translate("MainWindow", "&Original fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_show_toolbar.setText(QtGui.QApplication.translate("MainWindow", "&Show Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_show_statusbar.setText(QtGui.QApplication.translate("MainWindow", "S&how Statusbar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add_bookmark.setText(QtGui.QApplication.translate("MainWindow", "&Add bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove_bookmark.setText(QtGui.QApplication.translate("MainWindow", "&Remove bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.action_bookmark_manager.setText(QtGui.QApplication.translate("MainWindow", "Bookmark &manager", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open_folder.setText(QtGui.QApplication.translate("MainWindow", "Open &Folder", None, QtGui.QApplication.UnicodeUTF8))

from viewer import Viewer
import main_window_rc

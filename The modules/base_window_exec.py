#----------------------------------------------------------------------
#   base_window_exec
#
#   The core module. It controls
#   a) the GUI's display,
#   b) the signals emitted via changes to variables' statuses, and
#   c) basic operations like the scripting process startup.
#----------------------------------------------------------------------

import sys
import os
import subprocess

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
                             QAction, QColorDialog, QTabWidget, QScrollArea,
                             QLabel, QApplication, QMainWindow, QStyleFactory,
                             QMessageBox)
from PyQt5.QtCore import Qt, QFile, QSize
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QMovie, QIcon

import script_init
import base_window_widget
import base_widget_ctrl
import base_low_dict
import db_widget



class CoreWindow(QMainWindow):


    def __init__(self):
        """Initializes a set of external methods.

        Most of the widgets (buttons, boxes, text etc.) and layouts,
        some key variables and subwindows, are set up. Each component
        will be added in the window via appropriate internal methods."""

        super().__init__()

        base_window_widget.menuBarSubSetup(self)
        base_window_widget.tabMainSetup(self)
        base_window_widget.tabEffectSetup(self)
        base_window_widget.tabGroupBoxes(self)
        base_window_widget.tabsTopLayouts(self)
        base_low_dict.dictionariesCateg(self)
        base_widget_ctrl.variablesInit(self)
        db_widget.dbWindowSetup(self)
        db_widget.dbLayouts(self)
        self.startupWindowInit()


    def startupWindowInit(self):
        """Opens a simple starting window instead of the main one.

        It allows a basic and smooth access to the program."""

        self.initscreen = QWidget()
        # <initimage> stores the bg image for the startup screen.
        initimage = QPixmap("sgfiles/startscrn.png")
        self.initscreen.setFixedSize(initimage.width(), initimage.height())
        pal = QPalette()
        # <setBrush()> : a method of the class QPalette that prepares
        # <initimage> to be used as <initscreen>'s bg color/pattern,
        # via the class's object <pal>.
        pal.setBrush(10, QBrush(initimage))
        self.initscreen.setPalette(pal)

        pushok = QPushButton('Enter Program', self)
        pushok.setMinimumSize(QSize(110, 40))
        pushok.setMaximumSize(QSize(110, 40))

        initlayout = QVBoxLayout()
        initlayout.setAlignment(Qt.AlignCenter|Qt.AlignBottom)
        initlayout.addStretch()
        initlayout.addWidget(pushok)

        self.initscreen.setLayout(initlayout)
        self.initscreen.show()
        pushok.clicked.connect(self.mainWindowInit)


    def mainWindowInit(self):
        """Opens the main window and runs its methods."""

        self.menuBarSetup()
        self.tabsSetup()
        self.nonTabWidgetsSetup()
        self.mainWindowSetup()
        self.signalsControl()

        self.posX, self.posY = 400, 200
        self.w, self.h = 500, 600
        self.resize(self.w, self.h)
        self.setWindowTitle("Script Generator YGO")
        self.setWindowIcon(QIcon("sgfiles\logo.png"))

        # The starup screen closes before the main one starts.
        self.initscreen.close()
        self.show()


    def menuBarSetup(self):
        """Creates the menu bar.

        <QAction> is the class used to create instances that
        correspond to the actions of the menu bar's options."""

        self.menubar = self.menuBar()
        filemenu = self.menubar.addMenu('&File')
        dbmenu = self.menubar.addMenu('&Database')
        graphicsmenu = self.menubar.addMenu('&Color')
        helpmenu = self.menubar.addMenu('&Help')

        # <currentpath> stores the directory where base_window_exec
        # is located at.
        currentpath = os.getcwd()

        actionfolder = QAction('&Open folder', self)
        # When "Open folder" is selected, explorer.exe runs.
        actionfolder.triggered.connect(lambda : subprocess.run(['explorer',currentpath]))

        actioneditor = QAction('&Open Notepad2', self)
        actioneditor.triggered.connect(self.editorStart)

        actionexit = QAction('&Exit', self)
        actionexit.setShortcut('Ctrl+Q')
        actionexit.triggered.connect(self.close)

        actiondb = QAction('&Edit database', self)
        actiondb.triggered.connect(lambda : self.dbwindow.show())

        actionbgcolor = QAction('&Set bg color', self)
        actionbgcolor.triggered.connect(self.bgColoring)

        actiontutor = QAction('&Manual - Tutorial', self)
        actiontutor.triggered.connect(self.tutorWindow)

        actionabout = QAction('&About...', self)
        actionabout.triggered.connect(lambda : self.aboutwindow.show())

        filemenu.addAction(actionfolder)
        filemenu.addAction(actioneditor)
        filemenu.addAction(actionexit)
        dbmenu.addAction(actiondb)
        graphicsmenu.addAction(actionbgcolor)
        helpmenu.addAction(actiontutor)
        helpmenu.addAction(actionabout)


    def editorStart(self):
        """Opens an independent editor."""

        editor = ("sgfiles/Notepad2/Notepad2.exe")
        tempeditor = QFile(editor)
        if not tempeditor.exists():
            QMessageBox.about(self, 'Cannot start Notepad2',
        'Program missing or files corrupted. You can extract Notepad2' \
    "\nby unzipping \"notepad2_4.2.25_x86.zip\" in \"sgfiles\", then" \
    "\n\ttry to start it again."
                            )
        else:
            subprocess.Popen(editor)


    def bgColoring(self):
        """Changes the background's color.

        <centralwidget> is the main window's base widget in which
        everything else is added. It is defined later in the program."""

        color = QColorDialog.getColor()
        pal = QPalette()
        pal.setColor(QPalette.Window, color)
        self.centralwidget.setPalette(pal)


    def tutorWindow(self):
        """Opens the Tutorial/Maunal file in a subwindow."""

        if self.tutortmpfile.exists():
            tutorlayout = QVBoxLayout()
            tutorlayout.addWidget(self.tutortxt)
            self.tutor.setLayout(tutorlayout)
            self.tutor.show()
        else:
            QMessageBox.about(self, 'Error',
            "Cannot open Tutorial, missing file or unexpected error.")
            return


    def tabsSetup(self):
        """Creates the tabs & adds the layouts from the
        base_window_widget module."""

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1,"Main")
        self.tabs.addTab(self.tab2,"Effect")
        self.tabs.setTabEnabled(1, False)

        self.tab1.setLayout(self.layouttabmain)
        self.tab2.setLayout(self.layouttabeffect)


    def nonTabWidgetsSetup(self):
        """Creates the widgets that are not included in the tabs."""

        self.btn = QPushButton('Create file', self)
        self.btn.setMinimumSize(QSize(120, 40))
        self.btn.setMaximumSize(QSize(120, 40))
        self.btn.clicked.connect(lambda : script_init.scriptInitialize(self))

        # <gif>: tiny circular animation that indicates the process of
        # creating a file after <btn> is clicked.
        self.labelgif = QLabel()
        self.gif = QMovie('sgfiles\station-loading.gif')
        self.gif.setScaledSize(QSize(30, 30))
        self.gif.start()
        self.labelgif.setMovie(self.gif)
        self.labelgif.hide()


    def mainWindowSetup(self):

        """Creates a few base widgets and layouts, then everything
        created so far is added in <centralwidget>."""

        self.centralwidget = QWidget()
        centrwidglayout = QVBoxLayout(self.centralwidget)

        self.scrollbar = QScrollArea()
        self.scrollbar.setAlignment(Qt.AlignHCenter)
        centrwidglayout.addWidget(self.scrollbar)
        centrwidglayout.setContentsMargins(10, 10, 10, 10)

        pal = QPalette()
        pal.setColor(QPalette.Window, Qt.darkCyan)
        self.centralwidget.setPalette(pal)

        sidegrouplayout = QHBoxLayout()
        sidegrouplayout.setAlignment(Qt.AlignCenter)
        sidegrouplayout.addWidget(self.btn)
        sidegrouplayout.addWidget(self.labelgif)

        mainwincontent = QWidget()
        mainwincontent.resize(450, 550)
        self.scrollbar.setWidget(mainwincontent)

        mainwinlayout = QVBoxLayout()
        mainwincontent.setLayout(mainwinlayout)
        mainwinlayout.setAlignment(Qt.AlignTop)
        mainwinlayout.addWidget(self.tabs)
        mainwinlayout.addLayout(sidegrouplayout)

        self.setCentralWidget(self.centralwidget)


    def signalsControl(self):
        """Calls slots (external methods in this case) based on the
        emitted signals. Not all signals present in base_window_exec
        are here."""

        self.typeofbase.activated[str].connect(lambda : base_widget_ctrl.controlMain(self))
        self.typeofmonster.activated[str].connect(lambda : base_widget_ctrl.controlEffect(self))
        self.summonreq.activated[str].connect(lambda : base_widget_ctrl.controlEffect(self))
        self.monsterlevel.valueChanged.connect(lambda : base_low_dict.dictionariesCateg(self))
        self.typeofeffect.activated[str].connect(lambda : base_widget_ctrl.controlEffect(self))
        self.groupdestroy.buttonClicked.connect(lambda : base_widget_ctrl.controlEffect(self))
        self.checkbtncost.stateChanged.connect(lambda : base_widget_ctrl.controlEffect(self))
        self.menuaffectside.activated[str].connect(lambda : base_widget_ctrl.controlOther(self))
        self.menuaffectcard.activated[str].connect(lambda : base_widget_ctrl.controlOther(self))
        self.menuaffectarea.activated[str].connect(lambda : base_widget_ctrl.controlOther(self))



if __name__ == "__main__":
    app = QApplication([])
    app.setStyle(QStyleFactory.create("Fusion"))
    core = CoreWindow()
    sys.exit(app.exec_())

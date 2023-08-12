#-------------------------------------------------------------------------------
#   base_window_widget
#
#   Most of the main window's widgets, including some variables
#   and subwindows for the menu bar, are created here.
#-------------------------------------------------------------------------------

from PyQt5.QtWidgets import (QTextBrowser, QWidget, QTextEdit, QLabel,
                             QSpinBox, QComboBox, QCheckBox, QLineEdit,
                             QRadioButton, QGroupBox, QVBoxLayout,
                             QGridLayout, QButtonGroup)
from PyQt5.QtCore import QFile, Qt, QSize
from PyQt5.QtGui import QTextImageFormat, QTextCursor



def menuBarSubSetup(self):
    """Creates and prepares the information of "Tutorial" and "About...". """

    self.tutortxt = QTextBrowser()
    self.tutortxt.setReadOnly(True)
    self.tutortxt.setOpenExternalLinks(True)
    self.tutortxt.setFontPointSize(10)

    url1 = \
    "<a href=\"https://www.ygopro.co/Forum/tabid/95/g/posts/t/120/Adding-cards-to-YGOPro--Tutorial----Scripting-video-Added#post381\">" \
    "A fair (but outdated) starting point, about writing scripts and adding cards to the game</a>"
    url2 = \
    "<a href=\"https://www.ygopro.co/Forum/tabid/95/g/posts/t/16781/Scripting-Tutorial--CURRENTLY-INCOMPLETE#post88202\">" \
    "A complementary tutorial to the above, with updated or differently constructed information</a>"
    url3 = \
    "<a href=\"https://www.ygopro.co/Forum/tabid/95/g/posts/t/39580/AlphaKretin-s-Lua-Tutorials#post179635\">" \
    "One way to write your custom cards, explained from a personal point of view</a>"

    self.tutortmpfile = ('sgfiles/tutorial etc.txt')
    self.tutortmpfile = QFile(self.tutortmpfile)
    if self.tutortmpfile.exists():
        tutorfile = open('sgfiles/tutorial etc.txt', 'r').read()
        self.tutortxt.setText(tutorfile)
        self.tutortxt.append(url1)
        self.tutortxt.append(url2)
        self.tutortxt.append(url3)

        self.tutor = QWidget()
        self.tutor.resize(550, 450)
        self.tutor.setWindowTitle('Tutorial etc.')


    self.abouttxt = QTextEdit()
    self.abouttxt.setAlignment(Qt.AlignCenter)
    self.abouttxt.setReadOnly(True)

    aboutlogo = QTextImageFormat()
    aboutlogo.setWidth(57)
    aboutlogo.setHeight(68)
    aboutlogo.setName('sgfiles\logo.png')
    cursor = QTextCursor(self.abouttxt.document())
    cursor.insertImage(aboutlogo)
    self.abouttxt.setFontPointSize(12)
    self.abouttxt.append('\n\n(c) Script Generator YGO\n2018')
    self.abouttxt.setFontPointSize(10)
    self.abouttxt.append('\n\n version 0.3.6.0\n')

    self.aboutwindow = QWidget()
    self.aboutwindow.setFixedSize(400, 400)
    self.aboutwindow.setWindowTitle('About...')

    aboutlayout = QVBoxLayout()
    aboutlayout.addWidget(self.abouttxt)
    self.aboutwindow.setLayout(aboutlayout)


def tabMainSetup(self):
    """Creates the widgets for the Main tab."""

    # <codebox> stores the ID number, a script-related integer.
    self.codelabel = QLabel("    Enter your card's ID:\n     (1000-999999999)")
    self.codebox = QSpinBox()
    self.codebox.setRange(1000, 999999999)

    self.typeofbase = QComboBox()
    self.typeofbase.addItem("Type of card")
    self.typeofbase.addItem("Monster")
    self.typeofbase.addItem("Spell")
    self.typeofbase.addItem("Trap")
    self.typeofbase.setMinimumSize(QSize(110, 40))
    self.typeofbase.setMaximumSize(QSize(110, 40))

    self.typeofspell = QComboBox()
    self.typeofspell.addItem("Type of Spell")
    self.typeofspell.addItem("Normal")
    self.typeofspell.addItem("Continuous")
    self.typeofspell.addItem("Quick-Play")
    self.typeofspell.setEnabled(False)
    self.typeofspell.model().item(2).setEnabled(False)
    self.typeofspell.model().item(3).setEnabled(False)
    self.typeofspell.setMinimumSize(QSize(110, 30))
    self.typeofspell.setMaximumSize(QSize(110, 30))

    self.typeoftrap = QComboBox()
    self.typeoftrap.addItem("Type of Trap")
    self.typeoftrap.addItem("Normal")
    self.typeoftrap.addItem("Continuous")
    self.typeoftrap.addItem("Counter")
    self.typeoftrap.setEnabled(False)
    self.typeoftrap.model().item(2).setEnabled(False)
    self.typeoftrap.model().item(3).setEnabled(False)
    self.typeoftrap.setMinimumSize(QSize(110, 30))
    self.typeoftrap.setMaximumSize(QSize(110, 30))

    self.typeofmonster = QComboBox()
    self.typeofmonster.addItem("Type of Monster")
    self.typeofmonster.addItem("Effect")
    self.typeofmonster.addItem("Synchro")
    self.typeofmonster.addItem("Xyz")
    self.typeofmonster.setEnabled(False)
    self.typeofmonster.setMinimumSize(QSize(110, 30))
    self.typeofmonster.setMaximumSize(QSize(110, 30))

    self.checkcardopt = QCheckBox("Activate card\nonce per turn")
    self.checkcardopt.setEnabled(False)

    self.levellabel = QLabel("Level:")
    self.monsterlevel = QSpinBox()
    self.monsterlevel.setRange(1, 13)

    self.summonreq = QComboBox()
    self.summonreq.addItem("Requirements")
    self.summonreq.addItem("None")
    self.summonreq.setMaximumSize(QSize(100, 20))

    self.description = QLineEdit()
    self.description.setMaxLength(30)
    self.description.setReadOnly(True)

    self.summonhint = QLabel("Required")

    self.tip = QLabel(
    "Tip: If you change the Level, reselect the\nmonster's card type " \
    "to update the text\n\taccordingly"
                    )


def tabEffectSetup(self):
    """Creates the widgets for the Effect tab."""

    self.typeofeffect = QComboBox()
    self.typeofeffect.addItem("Type of effect")
    self.typeofeffect.addItem("Destroy")
    self.typeofeffect.addItem("Back to hand")
    self.typeofeffect.addItem("Banish")
    self.typeofeffect.addItem("Shuffle into Deck")
    self.typeofeffect.addItem("Special Summon")
    self.typeofeffect.setMinimumSize(QSize(100, 25))
    self.typeofeffect.setMaximumSize(QSize(120, 25))

    self.checkbtntarget = QCheckBox("Effect targets")
    self.checkbtntarget.setMinimumSize(QSize(90, 10))
    self.checkbtntarget.setEnabled(False)

    self.checkbtncost = QCheckBox("Effect has a cost")
    self.checkbtncost.setMinimumSize(QSize(90, 10))
    self.checkbtncost.setEnabled(False)

    self.menucardcost = QComboBox()
    self.menucardcost.addItem("Type of cost")
    self.menucardcost.addItem("Discard 1 card")
    self.menucardcost.addItem("Tribute 1 monster")
    self.menucardcost.setEnabled(False)
    self.menucardcost.setMinimumSize(QSize(100, 25))
    self.menucardcost.setMaximumSize(QSize(120, 25))

    self.checkbtnopt = QCheckBox("Use effect once per turn")
    self.checkbtnopt.setEnabled(False)

    self.menuaffectcard = QComboBox()
    self.menuaffectcard.addItem("Card to affect")
    self.menuaffectcard.addItem("Spell/Trap")
    self.menuaffectcard.addItem("Monster")
    self.menuaffectcard.addItem("Any")
    self.menuaffectcard.setMinimumSize(QSize(95, 25))
    self.menuaffectcard.setMaximumSize(QSize(95, 25))

    self.menuaffectside = QComboBox()
    self.menuaffectside.addItem("Side to affect")
    self.menuaffectside.addItem("You")
    self.menuaffectside.addItem("Opponent")
    self.menuaffectside.addItem("Either")
    self.menuaffectside.setMinimumSize(QSize(105, 25))
    self.menuaffectside.setMaximumSize(QSize(105, 25))

    self.menuaffectarea = QComboBox()
    self.menuaffectarea.addItem("Area to affect")
    self.menuaffectarea.addItem("Field")
    self.menuaffectarea.addItem("Graveyard")
    self.menuaffectarea.setMinimumSize(QSize(95, 25))
    self.menuaffectarea.setMaximumSize(QSize(95, 25))

    self.monsterlabel = QLabel("No. of cards to affect:")
    self.radiobtndestnum = QRadioButton("Select number:")
    self.radiobtndestnum.setChecked(True)
    self.radiobtndestnum.setEnabled(False)
    self.radiobtndestall = QRadioButton("all")
    self.radiobtndestall.setEnabled(False)
    self.amountdestroy = QSpinBox()
    self.amountdestroy.setRange(1, 3)
    self.amountdestroy.setEnabled(False)


def tabGroupBoxes(self):
    """Groups the widgets, after including them in layouts."""

    self.tab1layout1 = QGridLayout()
    self.tab1layout1.setVerticalSpacing(40)
    self.tab1layout1.addWidget(self.codelabel, 0, 0)
    self.tab1layout1.addWidget(self.codebox, 0, 2)
    self.tab1layout1.addWidget(self.typeofbase, 1, 1)
    self.tab1layout1.addWidget(self.typeofspell, 2, 0)
    self.tab1layout1.addWidget(self.typeoftrap, 2, 1)
    self.tab1layout1.addWidget(self.typeofmonster, 2, 2)
    self.tab1layout1.addWidget(self.checkcardopt, 3, 0)

    self.grouptab1box1 = QGroupBox()
    self.grouptab1box1.setLayout(self.tab1layout1)

    self.tab1layout2 = QGridLayout()
    self.tab1layout2.addWidget(self.levellabel, 0, 0)
    self.tab1layout2.addWidget(self.monsterlevel, 0, 1)
    self.tab1layout2.addWidget(self.summonreq, 0, 2)
    self.tab1layout2.addWidget(self.description, 0, 3)
    self.tab1layout2.addWidget(self.summonhint, 1, 2, Qt.AlignTop)
    self.tab1layout2.addWidget(self.tip, 1, 3, Qt.AlignTop)

    self.grouptab1box2 = QGroupBox()
    self.grouptab1box2.setLayout(self.tab1layout2)
    self.grouptab1box2.setEnabled(False)

    self.tab2layout1 = QGridLayout()
    self.tab2layout1.addWidget(self.typeofeffect, 0, 0)
    self.tab2layout1.addWidget(self.checkbtncost, 0, 1)
    self.tab2layout1.addWidget(self.checkbtntarget, 1, 0)
    self.tab2layout1.addWidget(self.menucardcost, 1, 1)
    self.tab2layout1.addWidget(self.checkbtnopt, 2, 0)
    self.tab2layout1.setSpacing(40)

    self.grouptab2box1 = QGroupBox()
    self.grouptab2box1.setLayout(self.tab2layout1)

    self.tab2layout2 = QGridLayout()
    self.tab2layout2.setVerticalSpacing(40)
    self.tab2layout2.addWidget(self.menuaffectcard, 0, 0, Qt.AlignRight)
    self.tab2layout2.addWidget(self.menuaffectside, 0, 1)
    self.tab2layout2.addWidget(self.menuaffectarea, 0, 2)
    self.tab2layout2.addWidget(self.monsterlabel, 1, 0)
    self.tab2layout2.addWidget(self.radiobtndestall, 1, 1, Qt.AlignRight)
    self.tab2layout2.addWidget(self.radiobtndestnum, 1, 2)
    self.tab2layout2.addWidget(self.amountdestroy, 1, 3)

    self.grouptab2box2 = QGroupBox()
    self.grouptab2box2.setLayout(self.tab2layout2)
    self.grouptab2box2.setEnabled(False)

    self.groupdestroy = QButtonGroup()
    self.groupdestroy.addButton(self.radiobtndestnum, 1)
    self.groupdestroy.addButton(self.radiobtndestall, 2)


def tabsTopLayouts(self):
    """Adds the groups of widgets in two main layouts, which are then
    added to the main window's tabs."""

    self.layouttabmain = QVBoxLayout()
    self.layouttabmain.setAlignment(Qt.AlignTop)
    self.layouttabmain.addWidget(self.grouptab1box1)
    self.layouttabmain.addWidget(self.grouptab1box2)

    self.layouttabeffect = QVBoxLayout()
    self.layouttabeffect.setAlignment(Qt.AlignTop)
    self.layouttabeffect.addWidget(self.grouptab2box1)
    self.layouttabeffect.addWidget(self.grouptab2box2)

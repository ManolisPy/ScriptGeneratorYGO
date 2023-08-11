#-------------------------------------------------------------------------------
#   db_widget
#
#   All of the database window's widgets are created here.
#-------------------------------------------------------------------------------

from PyQt5.QtWidgets import (QLineEdit, QPushButton, QLabel, QVBoxLayout,
                             QWidget, QSpinBox, QComboBox, QTextEdit,
                             QGridLayout, QGroupBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QIcon

import db_ctrl



def dbWindowSetup(self):
    """Creates the widgets for the database editor window."""

    self.dbnamedisplay = QLineEdit()
    self.dbnamedisplay.setReadOnly(True)

    self.dbinsertbtn = QPushButton('Select database', self)
    self.dbinsertbtn.clicked.connect(lambda : db_ctrl.dbDisplay(self))
    self.dbinsertbtn.setMinimumSize(QSize(100, 25))
    self.dbinsertbtn.setMaximumSize(QSize(100, 25))

    self.dbstart = QPushButton('Start', self)
    self.dbstart.setMinimumSize(QSize(60, 45))
    self.dbstart.setMaximumSize(QSize(60, 45))
    self.dbstart.clicked.connect(lambda : db_ctrl.dbEditStart(self))

    self.textbtn = QPushButton('Text\ncolor', self)
    self.textbtn.setMinimumSize(QSize(60, 35))
    self.textbtn.setMaximumSize(QSize(60, 35))
    self.textbtn.clicked.connect(lambda : db_ctrl.textColorChange(self))

    self.dbeditorinfo = QLabel(
    "The db editor can be used independently. You can add\n" \
    "whichever card you desire in the database, not only\n" \
    "cards strictly made from Script Generator.\n\n\n" \
    "Current limitations:\n\n\n" \
    "1. No Token/Pendulum/Link Monsters support.\n\n" \
    "2. No support for unique cases, like Monster Traps\n" \
    "and Special Summon-only monsters.\n\n" \
    "3. Only individual cards can be added. No\n" \
    "archetypes support.")

    dbinfolayout = QVBoxLayout()
    dbinfolayout.addWidget(self.dbeditorinfo)
    self.dbinfowindow = QWidget()
    self.dbinfowindow.setFixedSize(290, 250)
    self.dbinfowindow.setWindowTitle('Editor information')
    self.dbinfowindow.setLayout(dbinfolayout)
    self.dbinfobtn = QPushButton('Some info\nabout the\neditor', self)
    self.dbinfobtn.setMinimumSize(QSize(60, 45))
    self.dbinfobtn.setMaximumSize(QSize(60, 45))
    self.dbinfobtn.clicked.connect(lambda : self.dbinfowindow.show())


    self.labelidadd = QLabel('Card\'s ID:')
    self.idadd = QSpinBox()
    self.idadd.setRange(1000, 999999999)
    self.idadd.setMinimumSize(QSize(90, 25))
    self.idadd.setMaximumSize(QSize(90, 25))

    self.labelregion = QLabel('(TCG, OCG etc.):')
    self.region = QComboBox()
    self.region.addItem('OCG')
    self.region.addItem('TCG')
    self.region.addItem('TCG/OCG')
    self.region.addItem('Anime')
    self.region.setMinimumSize(QSize(100, 25))
    self.region.setMaximumSize(QSize(100, 25))

    self.labelalias = QLabel('Alias:')
    self.alias = QSpinBox()
    self.alias.setEnabled(False)
    self.alias.setMinimumSize(QSize(100, 25))
    self.alias.setMaximumSize(QSize(100, 25))

    self.labelarch = QLabel('Archetype:')
    self.archetype = QSpinBox()
    self.archetype.setEnabled(False)
    self.archetype.setMinimumSize(QSize(100, 25))
    self.archetype.setMaximumSize(QSize(100, 25))

    self.cardtype = QComboBox()
    self.cardtype.addItem('Type of card:')
    self.cardtype.addItem('Monster')
    self.cardtype.addItem('Spell')
    self.cardtype.addItem('Trap')
    self.cardtype.setMinimumSize(QSize(110, 25))
    self.cardtype.setMaximumSize(QSize(110, 25))
    self.cardtype.activated[str].connect(lambda : db_ctrl.cardTypeChange(self))

    self.monsterMDtype = QComboBox()
    self.monsterMDtype.addItem('MainDeck Monster card type:')
    self.monsterMDtype.addItem('Normal')
    self.monsterMDtype.addItem('Effect')
    self.monsterMDtype.addItem('Ritual')
    self.monsterMDtype.addItem('Ritual Effect')
    self.monsterMDtype.addItem('Spirit')
    self.monsterMDtype.addItem('Union')
    self.monsterMDtype.addItem('Gemini')
    self.monsterMDtype.addItem('Tuner Normal')
    self.monsterMDtype.addItem('Tuner Effect')
    self.monsterMDtype.addItem('Token')
    self.monsterMDtype.addItem('Flip')
    self.monsterMDtype.addItem('Toon')
    self.monsterMDtype.model().item(10).setEnabled(False)
    self.monsterMDtype.setEnabled(False)
    self.monsterMDtype.setMinimumSize(QSize(175, 25))
    self.monsterMDtype.setMaximumSize(QSize(175, 25))

    self.monsterEDtype = QComboBox()
    self.monsterEDtype.addItem('ExtraDeck Monster card type:')
    self.monsterEDtype.addItem('Fusion')
    self.monsterEDtype.addItem('Fusion Effect')
    self.monsterEDtype.addItem('Synchro')
    self.monsterEDtype.addItem('Synchro Effect')
    self.monsterEDtype.addItem('Synchro Tuner Effect')
    self.monsterEDtype.addItem('Xyz')
    self.monsterEDtype.addItem('Xyz Effect')
    self.monsterEDtype.setEnabled(False)
    self.monsterEDtype.setMinimumSize(QSize(175, 25))
    self.monsterEDtype.setMaximumSize(QSize(175, 25))

    self.monsterMDtype.activated[str].connect(lambda : self.monsterEDtype.setCurrentIndex(0))
    self.monsterEDtype.activated[str].connect(lambda : self.monsterMDtype.setCurrentIndex(0))

    self.spelltype = QComboBox()
    self.spelltype.addItem('Spell card type:')
    self.spelltype.addItem('Normal')
    self.spelltype.addItem('Ritual')
    self.spelltype.addItem('Quick')
    self.spelltype.addItem('Continuous')
    self.spelltype.addItem('Equip')
    self.spelltype.addItem('Field')
    self.spelltype.setEnabled(False)
    self.spelltype.setMinimumSize(QSize(110, 25))
    self.spelltype.setMaximumSize(QSize(110, 25))

    self.traptype = QComboBox()
    self.traptype.addItem('Trap card type:')
    self.traptype.addItem('Normal')
    self.traptype.addItem('Continuous')
    self.traptype.addItem('Counter')
    self.traptype.setEnabled(False)
    self.traptype.setMinimumSize(QSize(110, 25))
    self.traptype.setMaximumSize(QSize(110, 25))

    self.labelatk = QLabel('ATK value:')
    self.valueatk = QSpinBox()
    self.valueatk.setRange(0, 5000)
    self.valueatk.setSingleStep(50)
    self.valueatk.setEnabled(False)
    self.valueatk.setMinimumSize(QSize(60, 25))
    self.valueatk.setMaximumSize(QSize(60, 25))

    self.labeldef = QLabel('DEF value:')
    self.valuedef = QSpinBox()
    self.valuedef.setRange(0, 5000)
    self.valuedef.setSingleStep(50)
    self.valuedef.setEnabled(False)
    self.valuedef.setMinimumSize(QSize(60, 25))
    self.valuedef.setMaximumSize(QSize(60, 25))

    self.labellevel = QLabel('Monster\'s Level:')
    self.monsterlvl = QSpinBox()
    self.monsterlvl.setRange(0,13)
    self.monsterlvl.setValue(0)
    self.monsterlvl.setEnabled(False)
    self.monsterlvl.setMinimumSize(QSize(50, 25))
    self.monsterlvl.setMaximumSize(QSize(50, 25))

    self.labelmonsrace1 = QLabel('Monster\'s type (1):')
    self.monsterrace1 = QComboBox()
    self.monsterrace1.addItem('Not a monster')
    self.monsterrace1.addItem('Warrior')
    self.monsterrace1.addItem('Spellcaster')
    self.monsterrace1.addItem('Fairy')
    self.monsterrace1.addItem('Fiend')
    self.monsterrace1.addItem('Zombie')
    self.monsterrace1.addItem('Machine')
    self.monsterrace1.addItem('Aqua')
    self.monsterrace1.addItem('Pyro')
    self.monsterrace1.addItem('Rock')
    self.monsterrace1.addItem('Winged Beast')
    self.monsterrace1.addItem('Plant')
    self.monsterrace1.addItem('Insect')
    self.monsterrace1.setEnabled(False)
    self.monsterrace1.setMinimumSize(QSize(110, 25))
    self.monsterrace1.setMaximumSize(QSize(110, 25))

    self.labelmonsrace2 = QLabel('Monster\'s Type (2):')
    self.monsterrace2 = QComboBox()
    self.monsterrace2.addItem('Not a monster')
    self.monsterrace2.addItem('Thunder')
    self.monsterrace2.addItem('Dragon')
    self.monsterrace2.addItem('Beast')
    self.monsterrace2.addItem('Beast Warrior')
    self.monsterrace2.addItem('Dinosaur')
    self.monsterrace2.addItem('Fish')
    self.monsterrace2.addItem('Sea Serpent')
    self.monsterrace2.addItem('Reptile')
    self.monsterrace2.addItem('Psychic')
    self.monsterrace2.addItem('Divine Beast')
    self.monsterrace2.addItem('Creator God')
    self.monsterrace2.addItem('Wyrm')
    self.monsterrace2.addItem('Cyberse')
    self.monsterrace2.setEnabled(False)
    self.monsterrace2.setMinimumSize(QSize(110, 25))
    self.monsterrace2.setMaximumSize(QSize(110, 25))

    self.monsterrace1.activated[str].connect(lambda : self.monsterrace2.setCurrentIndex(0))
    self.monsterrace2.activated[str].connect(lambda : self.monsterrace1.setCurrentIndex(0))

    self.labelmonsattr = QLabel('Monster\'s Attribute:')
    self.monsterattr = QComboBox()
    self.monsterattr.addItem('Not a monster')
    self.monsterattr.addItem('EARTH')
    self.monsterattr.addItem('WATER')
    self.monsterattr.addItem('FIRE')
    self.monsterattr.addItem('WIND')
    self.monsterattr.addItem('LIGHT')
    self.monsterattr.addItem('DARK')
    self.monsterattr.addItem('DIVINE')
    self.monsterattr.setMinimumSize(QSize(110, 25))
    self.monsterattr.setMaximumSize(QSize(110, 25))

    self.labelcateg = QLabel('Category (optional):')
    self.valuecateg = QSpinBox()
    self.valuecateg.setValue(0)
    self.valuecateg.setEnabled(False)
    self.valuecateg.setMinimumSize(QSize(100, 25))
    self.valuecateg.setMaximumSize(QSize(100, 25))

    self.labelname = QLabel('Card\'s name:')
    self.cardname = QLineEdit()
    self.cardname.setText(" ")

    self.labeldesc = QLabel('Card\'s description:')
    self.carddesc = QTextEdit()
    self.carddesc.setText(" ")

    self.labeliddel = QLabel('Card\'s ID:')
    self.iddel = QSpinBox()
    self.iddel.setRange(1000, 999999999)
    self.iddel.setMinimumSize(QSize(90, 25))
    self.iddel.setMaximumSize(QSize(90, 25))

    self.delnamebtn = QPushButton('Show card\'s name')
    self.delnamebtn.setMinimumSize(110, 25)
    self.delnamebtn.setMaximumSize(110, 25)
    self.delnamebtn.clicked.connect(lambda : db_ctrl.dbNameSearch(self))
    self.delname = QLineEdit()
    self.nametip = QLabel("Tip: If the full name\nis not shown, move or\ndrag the " \
                          "cursor to the\nstart of the word")


def dbLayouts(self):
    """Includes the db widgets in layouts. Also, the db window is
    initiated here."""

    self.dblayoutadd = QGridLayout()
    self.dblayoutadd.addWidget(self.labelidadd, 1, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.idadd, 1, 1)
    self.dblayoutadd.addWidget(self.labelregion, 2, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.region, 2, 1)
    self.dblayoutadd.addWidget(self.labelalias, 3, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.alias, 3, 1)
    self.dblayoutadd.addWidget(self.labelarch, 4, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.archetype, 4, 1)
    self.dblayoutadd.addWidget(self.cardtype, 7, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.monsterMDtype, 5, 1)
    self.dblayoutadd.addWidget(self.monsterEDtype, 6, 1)
    self.dblayoutadd.addWidget(self.spelltype, 7, 1)
    self.dblayoutadd.addWidget(self.traptype, 8, 1)
    self.dblayoutadd.addWidget(self.labelatk, 9, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.valueatk, 9, 1)
    self.dblayoutadd.addWidget(self.labeldef, 10, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.valuedef, 10, 1)
    self.dblayoutadd.addWidget(self.labellevel, 11, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.monsterlvl, 11, 1)
    self.dblayoutadd.addWidget(self.labelmonsrace1, 12, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.monsterrace1, 12, 1)
    self.dblayoutadd.addWidget(self.labelmonsrace2, 13, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.monsterrace2, 13, 1)
    self.dblayoutadd.addWidget(self.labelmonsattr, 14, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.monsterattr, 14, 1)
    self.dblayoutadd.addWidget(self.labelcateg, 15, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.valuecateg, 15, 1)
    self.dblayoutadd.addWidget(self.labelname, 16, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.cardname, 16, 1)
    self.dblayoutadd.addWidget(self.labeldesc, 17, 0, Qt.AlignRight)
    self.dblayoutadd.addWidget(self.carddesc, 17, 1)

    self.dblayoutdel = QVBoxLayout()
    self.dblayoutdel.setAlignment(Qt.AlignTop)
    self.dblayoutdel.addWidget(self.labeliddel)
    self.dblayoutdel.addWidget(self.iddel)
    self.dblayoutdel.addWidget(self.delnamebtn)
    self.dblayoutdel.addWidget(self.delname)
    self.dblayoutdel.addWidget(self.nametip)

    self.groupadd = QGroupBox('Add a card', self)
    self.groupadd.setCheckable(True)
    self.groupadd.setChecked(False)
    self.groupadd.setLayout(self.dblayoutadd)

    self.groupdel = QGroupBox('Delete a card', self)
    self.groupdel.setCheckable(True)
    self.groupdel.setChecked(False)
    self.groupdel.setLayout(self.dblayoutdel)

    self.groupadd.clicked.connect(lambda : self.groupdel.setChecked(False))
    self.groupdel.clicked.connect(lambda : self.groupadd.setChecked(False))

    self.dblayoutmain = QGridLayout()
    self.dblayoutmain.addWidget(self.dbinsertbtn, 0, 0, Qt.AlignRight)
    self.dblayoutmain.addWidget(self.dbnamedisplay, 0, 1, Qt.AlignLeft)
    self.dblayoutmain.addWidget(self.dbstart, 0, 2, Qt.AlignRight)
    self.dblayoutmain.addWidget(self.groupadd, 1, 0)
    self.dblayoutmain.addWidget(self.groupdel, 1, 1)
    self.dblayoutmain.addWidget(self.textbtn, 1, 2, Qt.AlignVCenter)
    self.dblayoutmain.addWidget(self.dbinfobtn, 1, 2, Qt.AlignBottom)

    self.dbwindow = QWidget()
    self.dbwindow.resize(550, 620)
    self.dbwindow.setWindowTitle('Database Editor YGO')
    self.dbwindow.setWindowIcon(QIcon("sgfiles\logo.png"))
    self.dbwindow.setLayout(self.dblayoutmain)

    self.colortext = 'black'
    self.pal = QPalette()
    self.pal.setColor(QPalette.WindowText, Qt.black)
    self.dbwindow.setPalette(self.pal)

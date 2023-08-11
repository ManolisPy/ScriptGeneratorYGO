#-------------------------------------------------------------------------------
#   db_ctrl
#
#   The state of widgets and the functionalities regarding the database
#   (opening, editing etc.) are controlled here.
#-------------------------------------------------------------------------------

import sqlite3

from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QPalette
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import db_dict



def textColorChange(self):

    if self.colortext == 'black':
        self.colortext = 'blue'
        self.pal.setColor(QPalette.WindowText, Qt.blue)
    elif self.colortext == 'blue':
        self.colortext = 'red'
        self.pal.setColor(QPalette.WindowText, Qt.red)
    elif self.colortext == 'red':
        self.colortext = 'black'
        self.pal.setColor(QPalette.WindowText, Qt.black)

    self.dbwindow.setPalette(self.pal)


def dbDisplay(self):
    """Displays an explorer window to select the database."""

    self.dbtempname, _ = QFileDialog.getOpenFileName(self.dbwindow,
                                                    'Save as', "", 'cdb Files (*.cdb)')
    if not self.dbtempname:
        return
    else:
        savedfile = QFileInfo(self.dbtempname)
        self.dbnamedisplay.setText(savedfile.fileName())


def cardTypeChange(self):
    """Changes the state of widgets from the database editor window."""

    if self.cardtype.currentText() == 'Monster':
        self.monsterMDtype.setEnabled(True)
        self.monsterEDtype.setEnabled(True)
        self.valueatk.setEnabled(True)
        self.valuedef.setEnabled(True)
        self.monsterlvl.setEnabled(True)
        self.monsterlvl.setValue(1)
        self.monsterlvl.setRange(1, 13)
        self.monsterrace1.setEnabled(True)
        self.monsterrace2.setEnabled(True)
        self.monsterattr.setEnabled(True)
    else:
        self.monsterMDtype.setCurrentIndex(0)
        self.monsterMDtype.setEnabled(False)
        self.monsterEDtype.setCurrentIndex(0)
        self.monsterEDtype.setEnabled(False)
        self.valueatk.setValue(0)
        self.valueatk.setEnabled(False)
        self.valuedef.setValue(0)
        self.valuedef.setEnabled(False)
        self.monsterlvl.setRange(0, 13)
        self.monsterlvl.setValue(0)
        self.monsterlvl.setEnabled(False)
        self.monsterrace1.setCurrentIndex(0)
        self.monsterrace1.setEnabled(False)
        self.monsterrace2.setCurrentIndex(0)
        self.monsterrace2.setEnabled(False)
        self.monsterattr.model().item(0).setEnabled(True)
        self.monsterattr.setCurrentIndex(0)
        self.monsterattr.setEnabled(False)
    if self.cardtype.currentText() == 'Spell':
        self.spelltype.setEnabled(True)
    else:
        self.spelltype.setCurrentIndex(0)
        self.spelltype.setEnabled(False)
    if self.cardtype.currentText() == 'Trap':
        self.traptype.setEnabled(True)
    else:
        self.traptype.setCurrentIndex(0)
        self.traptype.setEnabled(False)


def dbNameSearch(self):
    """Shows the name of the item in the database which will be deleted."""

    if not self.dbnamedisplay.text():
        dbDisplay(self)
    if self.dbnamedisplay.text():
        id = self.iddel.value()
        db = sqlite3.connect(self.dbtempname)
        cur = db.cursor()
        cur.execute("SELECT name FROM texts WHERE id = ?", (id,))
        data=cur.fetchone()
        if data:
            self.delname.setText(data[0])
        else:
            self.delname.setText("none")


def dbEditStart(self):
    """Calls the appropriate method based on the user's desired action."""

    if not self.dbnamedisplay.text():
        QMessageBox.warning(self.dbwindow, 'No database',
                                "Enter a database first.")
    elif self.groupadd.isChecked():
        dbAddProcess(self)
    elif self.groupdel.isChecked():
        dbDelProcess(self)
    return


def dbAddProcess(self):
    """Adds an item with all the selected characteristics in the database."""

    db_dict.dbDictionaries(self)

    id = self.idadd.value()
    region = self.regioN[self.region.currentIndex()]
    alias = self.alias.value()
    setcode = self.archetype.value()
    if self.monsterMDtype.currentIndex() != 0:
        ctype = self.monsMDtype[self.monsterMDtype.currentIndex()]
    elif self.monsterEDtype.currentIndex() != 0:
        ctype = self.monsEDtype[self.monsterEDtype.currentIndex()]
    elif self.spelltype.currentIndex() != 0:
        ctype = self.spelltypE[self.spelltype.currentIndex()]
    else:
        ctype = self.traptypE[self.traptype.currentIndex()]
    atk = self.valueatk.value()
    deF = self.valuedef.value()
    lvl = self.monsterlvl.value()
    if self.monsterrace1.currentIndex() != 0:
        crace = self.monsrace1[self.monsterrace1.currentIndex()]
    else:
        crace = self.monsrace2[self.monsterrace2.currentIndex()]
    attribute = self.monsattr[self.monsterattr.currentIndex()]
    category = self.valuecateg.value()
    name = self.cardname.text()
    desc = self.carddesc.toPlainText()
    if (self.cardtype.currentText() == 'Type of card:'
        or (self.cardtype.currentText() == 'Monster'
            and (ctype == '0' or crace == '0' or attribute == '0'))
        or (self.cardtype.currentText() == 'Spell'
            and ctype == '0')
        or (self.cardtype.currentText() == 'Trap'
            and ctype == '0')):
        QMessageBox.warning(self.dbwindow, 'Missing details',
        "Make sure that no key detail is missing, then proceed.")
        return

    db = sqlite3.connect(self.dbtempname)
    cur = db.cursor()
    cur.execute("SELECT id FROM datas WHERE id = ?", (id,))
    data=cur.fetchone()
    if data:
        QMessageBox.warning(self.dbwindow, 'Cannot add card',
        "A card with the given ID already exists.\n" \
        "Try with a diffrent ID or delete the existing record.")
        return
    else:
        cur.execute('INSERT INTO datas' \
        '(id, ot, alias, setcode, type, atk, def, level, race, attribute, category)' \
        'VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', \
        (id, region, alias, setcode, ctype, atk, deF, lvl, crace, attribute, category))
        db.commit()
        cur.execute('INSERT INTO texts' \
        '(id, name, desc, str1, str2, str3, str4, str5, str6, str7, str8,' \
        'str9, str10, str11, str12, str13, str14, str15, str16)' \
        'VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', \
        (id, name, desc, " ", " ", " ", " ", " ", " ", " ", " ", \
         " ", " ", " ", " ", " ", " ", " ", " "))
        db.commit()
        db.close()
        QMessageBox.information(self.dbwindow, 'Success',
                                "Card added to the database successfully!")


def dbDelProcess(self):
    """Deletes the selected item from the database."""

    id = self.iddel.value()

    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(self.dbtempname)
    db.open()
    query = QSqlQuery()
    query.exec("DELETE FROM datas WHERE id == {}".format(id))
    query.exec("DELETE FROM texts WHERE id == {}".format(id))
    db.close()
    QMessageBox.information(self.dbwindow, 'Success',
                            "Card deleted from the database successfully!")
#----------------------------------------------------------------------
#   base_widget_ctrl
#
#   The change to the state of most of the widgets happens here.
#   Some dictionary-related edits take place here, too.
#----------------------------------------------------------------------

def variablesInit(self):
    """Initializes a few variables.

    They are supposed to be empty by default due to certain effects
    not requiring any content by the variables."""

    self.listfilter = []
    self.cardtoaffect = ""
    self.chkclocation = ""

def controlMain(self):
    """Changes the state of widgets related to the Main Tab."""

    if self.typeofbase.currentText() in ["Spell", "Trap"]:
        self.checkcardopt.setEnabled(True)
    else:
        self.checkcardopt.setEnabled(False)

    if self.typeofbase.currentText() == "Spell":
        self.typeofspell.setEnabled(True)
    else:
        self.typeofspell.setCurrentIndex(0)
        self.typeofspell.setEnabled(False)

    if self.typeofbase.currentText() == "Trap":
        self.typeoftrap.setEnabled(True)
    else:
        self.typeoftrap.setCurrentIndex(0)
        self.typeoftrap.setEnabled(False)

    if self.typeofbase.currentText() == "Monster":
        self.typeofmonster.setEnabled(True)
    else:
        self.typeofmonster.setCurrentIndex(0)
        self.typeofmonster.setEnabled(False)

    if self.typeofmonster.currentText() in ["Synchro", "Xyz"]:
        self.grouptab1box2.setEnabled(True)
    else:
        self.summonreq.setCurrentIndex(0)
        self.monsterlevel.setValue(2)
        self.grouptab1box2.setEnabled(False)

    #<checkbtnopt> is in the Effect tab but is linked to the Main tab.
    if self.typeofbase.currentText() == "Monster":
        self.checkbtnopt.setEnabled(True)
    else:
        self.checkbtnopt.setChecked(False)
        self.checkbtnopt.setEnabled(False)

    self.typeofspell.currentIndexChanged.connect(lambda : self.tabs.setTabEnabled(1, True))
    self.typeoftrap.currentIndexChanged.connect(lambda : self.tabs.setTabEnabled(1, True))
    self.typeofmonster.currentIndexChanged.connect(lambda : self.tabs.setTabEnabled(1, True))

    self.tabs.setTabEnabled(1, False)


def controlEffect(self):
    """Changes the state of widgets related to the Effect Tab. A handful
    of widgets from the Main tab are included too."""

    if self.typeofmonster.currentText() in ["Synchro", "Xyz"]:
        self.grouptab1box2.setEnabled(True)
    else:
        self.summonreq.setCurrentIndex(0)
        self.monsterlevel.setValue(2)
        self.grouptab1box2.setEnabled(False)

    if self.summonreq.currentText() == "None":
        self.description.setText(self.monscardtypedesc[self.typeofmonster.currentIndex()])
    else:
        self.description.setText("")

    if (self.groupdestroy.checkedId() == 2
        or self.typeofeffect.currentText() == "Type of effect"):
        self.checkbtntarget.setChecked(False)
        self.checkbtntarget.setEnabled(False)
    else:
        self.checkbtntarget.setEnabled(True)
        if self.typeofeffect.currentText() == "Special Summon":
            self.checkbtntarget.setChecked(True)
            self.checkbtntarget.setEnabled(False)
            self.radiobtndestall.setCheckable(False)
        else:
            self.radiobtndestall.setCheckable(True)

    if self.radiobtndestnum.isChecked():
        self.amountdestroy.setEnabled(True)
    else:
        self.amountdestroy.setValue(1)
        self.amountdestroy.setEnabled(False)

    if self.typeofeffect.currentText() != "Type of effect":
        self.checkbtncost.setEnabled(True)
        self.menucardcost.setEnabled(True)
    else:
        self.checkbtncost.setChecked(False)
        self.checkbtncost.setEnabled(False)
        self.menucardcost.setCurrentIndex(0)
        self.menucardcost.setEnabled(False)

    if self.checkbtncost.isChecked():
        self.menucardcost.setEnabled(True)
    else:
        self.menucardcost.setCurrentIndex(0)
        self.menucardcost.setEnabled(False)

    if self.typeofeffect.currentText() == "Special Summon":
        self.menuaffectarea.setCurrentIndex(0)
        self.menuaffectarea.model().item(1).setEnabled(False)
        self.menuaffectarea.model().item(2).setEnabled(True)
        self.menuaffectcard.setCurrentIndex(0)
        self.menuaffectcard.model().item(1).setEnabled(False)
        self.menuaffectcard.model().item(3).setEnabled(False)
    else:
        self.menuaffectarea.setCurrentIndex(0)
        self.menuaffectarea.model().item(1).setEnabled(True)
        self.menuaffectarea.model().item(2).setEnabled(False)
        self.menuaffectcard.setCurrentIndex(0)
        self.menuaffectcard.model().item(1).setEnabled(True)
        self.menuaffectcard.model().item(3).setEnabled(True)

    if self.typeofeffect.currentText() != "Type of effect":
        self.radiobtndestnum.setEnabled(True)
        self.radiobtndestall.setEnabled(True)
        self.grouptab2box2.setEnabled(True)
    else:
        self.radiobtndestnum.setEnabled(False)
        self.radiobtndestall.setEnabled(False)
        self.grouptab2box2.setEnabled(False)



def controlOther(self):
    """Changes the dictionary-related variables' values.

    The variables here are prone to having their values changed
    frequently. When the script generating takes place, the variables
    keep their latest values until the process is done, then change if
    the user tweaks the options."""

    temptext = self.menuaffectcard.currentText()
    if temptext != "Card to affect":
        self.cardtoaffect = self.cardarea[self.menuaffectarea.currentIndex()]
        self.chkclocation = "chkc:IsOnField()"
        if self.typeofeffect.currentText() == "Special Summon":
            self.chkclocation = "chkc:IsLocation(LOCATION_GRAVE)"
        for elem in self.listfilter:
            if elem in self.categspelltrap.values():
                self.listfilter.remove(elem)
                break
        if temptext == "Spell/Trap":
            self.listfilter.append(self.categspelltrap[self.menuaffectcard.currentIndex()])
        if (temptext == "Monster"
            and self.menuaffectarea.currentText() == "Field"):
            self.cardtoaffect = "LOCATION_MZONE"
            self.chkclocation = "chkc:IsLocation(LOCATION_MZONE)"
    else:
        self.cardtoaffect = ""

    if self.menuaffectside.currentText() == "You":
        self.areaofeffect = "{},0".format(self.cardtoaffect)
    elif self.menuaffectside.currentText() == "Opponent":
        self.areaofeffect = "0,{}".format(self.cardtoaffect)
    elif self.menuaffectside.currentText() == "Either":
        self.areaofeffect = "{},{}".format(self.cardtoaffect, self.cardtoaffect)
    else:
        self.areaofeffect = ""

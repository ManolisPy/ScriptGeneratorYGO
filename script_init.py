#-------------------------------------------------------------------------------
#   script_init
#
#   The scripting startup module. It does a few final checks (regarding
#   correct input) before initiazing the scripting process. If there is
#   a wrong input or if the user doesn't want to proceed, they return to
#   the original window.
#-------------------------------------------------------------------------------

import re

from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QFileInfo

import script_product
import base_high_dict



def scriptInitialize(self):

    # <enum> is a script-related integer.
    enum = 1

    if (self.typeofeffect.currentText() == "Type of effect"
        or self.menuaffectcard.currentText() == "Card to affect"
        or self.menuaffectside.currentText() == "Side to affect"
        or (self.typeofmonster.currentText() in ["Synchro", "Xyz"]
            and self.summonreq.currentText() == "Requirements")
        or self.menuaffectarea.currentText() == "Area to affect"):
        QMessageBox.warning(self, 'File Creation Error',
        "Empty or invalid inputs.\nCheck for missing or false key entries and retry.")
        return

    codenum = str(self.codebox.value())
    tempname, _ = QFileDialog.getSaveFileName(self,
                                             'Save as', "c"+ codenum, 'Lua Files (*.lua)')
    if not tempname:
        return
    else:
        savedFile = QFileInfo(tempname)

    if savedFile:
        codenum = savedFile.baseName()
        codenum2 = re.findall('\d+', codenum)
    self.labelgif.show()

    base_high_dict.dictionaries(self, enum, codenum, codenum2)

    file = open(savedFile.absoluteFilePath(), 'w')

    file.write('''
    function '''+ codenum +'''.initial_effect(c)
    	'''+ self.summoncondition +'''
    	local e1=Effect.CreateEffect(c)
    	'''+ self.settype + self.setcode + self.setlimit
            )
    if self.typeofbase.currentText() == "Monster":
        file.write('''
    	'''+ self.setrange
            )
    if self.checkbtntarget.isChecked():
        file.write('''
    	e'''+ str(enum) +''':SetProperty(EFFECT_FLAG_CARD_TARGET)'''
                )
    if (self.typeofbase.currentIndex() == 3
        and self.typeoftrap.currentIndex() == 1):
        file.write('''
        e'''+ str(enum) +''':SetHintTiming(0,0x1e0)'''
                )

    script_product.scriptProduct(self, file, enum, codenum)

    file.close()

    self.labelgif.hide()
    QMessageBox.information(self,'Success','File creation completed!')
    enum = 1
    self.chkconditions.clear()

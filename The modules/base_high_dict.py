#-------------------------------------------------------------------------------
#   base_high_dict
#
#   The sum of dictionaries and lists that are used if the signal to
#   start the scripting process is emitted. The module also has access
#   to base_low_dict.
#-------------------------------------------------------------------------------

def dictionaries(self, enum, codenum, codenum2):
    """Includes dictionaries that correlate with specific sets of options."""

    tempdestno = str(self.amountdestroy.value())
    self.summoncondition = ""

    if self.typeofmonster.currentText() in ["Synchro","Xyz"]:
        if self.summonreq.currentText() == "None":
            self.summoncondition = self.monscardtype[self.typeofmonster.currentIndex()]
        else:
            self.summoncondition = ""
    tempeffvar = self.cardeffvariable[self.typeofeffect.currentIndex()]
    self.tempeffcateg = self.cardeffcategory[self.typeofeffect.currentIndex()]

    if self.typeofeffect.currentText() not in ["Special Summon"]:
        effectvarfiler = "c:{}()".format(tempeffvar)
    else:
        effectvarfiler = "c:{}".format(tempeffvar)
        self.chkconditions.append("Duel.GetLocationCount(tp,LOCATION_MZONE)>0")

    if self.typeofeffect.currentText() not in ["Type of effect", "Destroy"]:
        tempeffvar = "Card." + tempeffvar
    if self.cardeffvarctrl in self.listfilter:
        self.listfilter.remove(self.cardeffvarctrl)
    if self.typeofeffect.currentText() in ["Banish", "Special Summon"]:
        self.listfilter.append(effectvarfiler)
        self.cardeffvarctrl = effectvarfiler

    if self.listfilter:
        tempeffvar = codenum +".filter"

    if self.typeofbase.currentText() == "Monster":
        self.settype = "e"+ str(enum) +":SetType(EFFECT_TYPE_IGNITION)\n"
        self.setcode = ""
        self.setrange = "e"+ str(enum) +":SetRange(LOCATION_MZONE)"
    else:
        self.settype = "e"+ str(enum) +":SetType(EFFECT_TYPE_ACTIVATE)\n"
        self.setcode = "\te"+ str(enum) +":SetCode(EVENT_FREE_CHAIN)"
        self.setrange = ""

    if self.checkbtnopt.isChecked():
        self.setlimit = "	e"+ str(enum) +":SetCountLimit(1)\n"
    elif self.checkcardopt.isChecked():
        self.setlimit = "\n	e"+ str(enum) +":SetCountLimit(1,"+ codenum2[0] \
                        + "+EFFECT_COUNT_CODE_OATH)\n"
    else:
        self.setlimit = ""
#--------------------------------------

    self.dictdestmonsnum = {
    1: tempeffvar +",tp,"+ self.areaofeffect +","+ tempdestno +",nil",
    2: tempeffvar +",tp,"+ self.areaofeffect +",1,nil",
    3: tempeffvar +",tp,"+ self.areaofeffect +",nil",
    4: tempeffvar +",tp,"+ self.areaofeffect +",nil",
    5: "0,"+ self.tempeffcateg +",g,"+ tempdestno +",0,0",
    6: "0,"+ self.tempeffcateg +",g,g:GetCount(),0,0",
    7: "(tp,"+ tempeffvar +",tp,"+ self.areaofeffect +","+ tempdestno +","+ tempdestno +",nil)",
    8: "("+ tempeffvar +",tp,"+ self.areaofeffect +",nil)"
    }

    self.dictfuncname = {
    1: "Duel.IsExistingMatchingCard",
    2: "Duel.IsExistingMatchingCard",
    3: "Duel.GetMatchingGroup",
    4: "Duel.GetMatchingGroup",
    7: "Duel.SelectMatchingCard",
    8: "Duel.GetMatchingGroup"
    }

#--------------------------------------

    self.dictdestmonsnumtrg = {
    1: tempeffvar +",tp,"+ self.areaofeffect +","+ tempdestno +",nil",
    3: "tp,"+ tempeffvar +",tp,"+ self.areaofeffect +","+ tempdestno +","+ tempdestno +",nil",
    5: "0,"+ self.tempeffcateg +",g,"+ tempdestno +",0,0",
    7: ""
    }

    self.dictspecialtrg = {
    1: tempeffvar +",tp,"+ self.areaofeffect +","+ tempdestno +",nil,e,tp",
    3: "tp,"+ tempeffvar +",tp,"+ self.areaofeffect +","+ tempdestno +","+ tempdestno +",nil,e,tp",
    5: "0,"+ self.tempeffcateg +",g,"+ tempdestno +",0,0",
    7: ""
    }

    tempaction = ""
    if tempdestno != "1":
        tempaction = "Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)"
    else:
        tempaction = "Duel.GetFirstTarget()\n		if g:IsRelateToEffect(e) then"
    self.dictfuncnametrg = {
    1: "Duel.IsExistingTarget",
    3: "Duel.SelectTarget",
    7: tempaction
    }

#-------------------------------------

    self.reasoneffect = {
    1: "Duel.Destroy(g,REASON_EFFECT)",
    2: "Duel.SendtoHand(g,nil,REASON_EFFECT)",
    3: "Duel.Remove(g,POS_FACEUP,REASON_EFFECT)",
    4: "Duel.SendtoDeck(g,nil,2,REASON_EFFECT)",
    5: "Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)"
    }

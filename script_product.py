#-------------------------------------------------------------------------------
#   script_product
#
#   The scripting module. It writes the script by using all necessary
#   lists and dictionaries and closes the file.
#-------------------------------------------------------------------------------

def scriptProduct(self, file, enum, codenum):

    finvar = ""
    if self.checkbtntarget.isChecked():
        if self.typeofeffect.currentText() == "Special Summon":
            tempdict = self.dictspecialtrg.copy()
        else:
            tempdict = self.dictdestmonsnumtrg.copy()
        tempfuncdict = self.dictfuncnametrg.copy()
        tempchkc = "	if chkc then return "+ self.chkclocation
        if self.typeofeffect.currentText() == "Back to hand":
            tempchkc += " and chkc:IsAbleToHand()"
        tempchkc += " end\n"

        if self.amountdestroy.value() == 1:
            finvar = "\n\t\tend"
    else:
        tempdict = self.dictdestmonsnum.copy()
        tempfuncdict = self.dictfuncname.copy()
        tempchkc = ""

    x1 = tempdict[self.groupdestroy.checkedId()]
    x2 = tempdict[self.groupdestroy.checkedId()+2]
    x3 = tempdict[self.groupdestroy.checkedId()+4]
    x4 = tempdict[self.groupdestroy.checkedId()+6]
    y1 = tempfuncdict[self.groupdestroy.checkedId()]
    y2 = tempfuncdict[self.groupdestroy.checkedId()+2]
    y4 = tempfuncdict[self.groupdestroy.checkedId()+6]

    z = self.reasoneffect[self.typeofeffect.currentIndex()]

    if self.menucardcost.currentText() == "Discard 1 card":
        setcost = "e{}:SetCost({}.cost)".format(str(enum), codenum)
        costfunc = '''function '''+ codenum +'''.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    	if chk==0 then
    	return Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,1,e:GetHandler()) end
    	Duel.DiscardHand(tp,Card.IsDiscardable,1,1,REASON_COST+REASON_DISCARD)\n	end\n'''
    elif self.menucardcost.currentText() == "Tribute 1 monster":
        setcost = "e{}:SetCost({}.cost)".format(str(enum), codenum)
        costfunc = '''function '''+ codenum +'''.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    	if chk==0 then return Duel.CheckReleaseGroup(tp,nil,1,nil) end
    	local g=Duel.SelectReleaseGroup(tp,nil,1,1,nil)
    	Duel.Release(g,REASON_COST)\n	end\n'''
    else:
        setcost = ""
        costfunc = ""

    if not self.listfilter:
        funcfilter = ""
    else:
        if self.typeofeffect.currentText() == "Special Summon":
            parenth = "(c,e,tp)"
        else:
            parenth = "(c)"
        funcfilter = "function "+ codenum +".filter"+ parenth +"\n		return "+ self.listfilter[0]
        for elem in range(1, len(self.listfilter)):
            funcfilter += " and "+ self.listfilter[elem]
        if self.typeofeffect.currentText() == "Back to hand":
            funcfilter += " and c:IsAbleToHand()"
        funcfilter += "\n\tend"

    chkcond = ""
    if self.chkconditions:
        for cond in range(0, len(self.chkconditions)):
            chkcond += self.chkconditions[cond] + "\nand "

    file.write('''
    	e'''+ str(enum) +''':SetCategory('''+ self.tempeffcateg +''')
    	'''+ setcost +'''
    	e'''+ str(enum) +''':SetTarget('''+ codenum +'''.target)
    	e'''+ str(enum) +''':SetOperation('''+ codenum +'''.activate)
    	c:RegisterEffect(e'''+ str(enum) +''')
    end
    '''+ costfunc +''''''+ funcfilter +'''
    function '''+ codenum +'''.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    	'''+ tempchkc +'''\tif chk==0 then return '''+ chkcond + y1 +'''('''+ x1 +''') end
    	local g='''+ y2 +'''('''+ x2 +''')
    	Duel.SetOperationInfo('''+ x3 +''')
    end
    function '''+ codenum +'''.activate(e,tp,eg,ep,ev,re,r,rp)
    	local g='''+ y4 +''''''+ x4 +'''
    	'''+ z + finvar +'''
    end'''
            )

#-------------------------------------------------------------------------------
#   base_low_dict
#
#   Fixed dictionaries to which the modules have the first access.
#-------------------------------------------------------------------------------

def dictionariesCateg(self):

    level = str(self.monsterlevel.value())

    self.categspelltrap = {
    1: "c:IsType(TYPE_SPELL)",
    2: "c:IsType(TYPE_TRAP)",
    3: "c:IsType(TYPE_SPELL+TYPE_TRAP)"
    }

    self.monstertype = {
    #e.g. Pyro/Dragon/etc.
    }

    self.monsattribute = {
    1: "DARK",
    2: "DIVINE",
    3: "EARTH",
    4: "FIRE",
    5: "LIGHT",
    6: "WATER",
    7: "WIND"
    }

    self.monscardtype = {
    2: "aux.AddSynchroProcedure(c,nil,1,1,aux.NonTuner(nil),1,99)\n	c:EnableReviveLimit()",
    3: "aux.AddXyzProcedure(c,nil,"+ level +",2)\n	c:EnableReviveLimit()"
    }

    self.monscardtypedesc = {
    2: "1 Tuner + 1 or more non-Tuner",
    3: "2 Level "+ level +" monsters"
    }

    self.cardarea = {
    0: "",
    1: "LOCATION_ONFIELD",
    2: "LOCATION_GRAVE"
    }

    self.cardeffcategory = {
    1: "CATEGORY_DESTROY",
    2: "CATEGORY_TOHAND",
    3: "CATEGORY_REMOVE",
    4: "CATEGORY_TODECK",
    5: "CATEGORY_SPECIAL_SUMMON"
    }

    self.cardeffvariable = {
    1: "aux.TRUE",
    2: "IsAbleToHand",
    3: "IsAbleToRemove",
    4: "IsAbleToDeck",
    5: "IsCanBeSpecialSummoned(e,0,tp,false,false)"
    }

    self.chkconditions = []

    self.cardeffvarctrl = "none"
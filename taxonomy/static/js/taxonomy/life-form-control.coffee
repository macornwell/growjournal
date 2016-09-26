root = exports ? this
root.grow_journal = root.grow_journal ? {}

class LifeFormControl

  constructor: ()->
    @selectedLifeForm = ko.observable(-1)
    @displayNameToLifeForm = {}

  addLifeForm:(displayName, lifeForm)=>
    @displayNameToLifeForm[displayName] = lifeForm

  setSelectedLifeForm: (displayName)=>
    @selectedLifeForm(-1)
    if displayName of @displayNameToLifeForm
      @selectedLifeForm(@displayNameToLifeForm[displayName].id)

  clearLifeForms: ()=>
    @selectedLifeForm(-1)
    @displayNameToLifeForm = {}

root.grow_journal.LifeFormControl = LifeFormControl
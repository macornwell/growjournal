root = exports ? this
root.grow_journal = root.grow_journal ? {}

class Kingdom
  constructor: (@id, @name)->

class Genus
  constructor: (@id, @kingdom, @name)->

class Species
  constructor: (@id, @kingdom, @genus, @name)->

class LifeForm
  constructor: (@id, @kingdom, @genus, @name)->

class LifeFormSelector
  constructor: (@__easyData)->
    @kingdomDict = ko.observableArray()
    @selectedKingdom = ko.observable()
    @availableGenus = ko.observableArray()
    @selectedGenus = ko.observable()
    @availableSpecies = ko.observableArray()
    @selectedSpecies = ko.observable()
    @availableVarieties = ko.observableArray()
    @selectedVariety = ko.observable()

    @selectedKingdom.subscribe(_onSelectedKingdom)

  addKingdom: (id, name)=>
    @kingdomChoices.push(new Kingdom(id, name))

  _resetData: (genus, species, variety)=>
    if (genus)
      @availableGenus = ko.observableArray()
      @selectedGenus = ko.observable()
    if (species)
      @availableSpecies = ko.observableArray()
      @selectedSpecies = ko.observable()
    if (variety)
      @availableVarieties = ko.observableArray()
      @selectedVariety = ko.observable()

  _onSelectedKingdom: (kingdomSelected)=>
    id = kingdomSelected.id
    name = kingdomSelected.name
    @_resetData(true, true, true)
    if (id)
      ""




root.grow_journal.LifeFormSelector = LifeFormSelector
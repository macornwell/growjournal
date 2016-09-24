root = exports ? this
root.grow_journal = root.grow_journal ? {}

class Kingdom

  constructor: (@id, @name, @latinName)->
    @genusList = []

class Genus

  constructor: (@kingdom, @id, @name, @latinName)->
    @speciesList = []

class Species

  constructor: (@genus, @id, @name, @latinName)->


class TaxonomyDataAccess

  constructor: ()->
    @kingdomDict = {}
    @genusDict = {}


  addKingdom:(id, name, latinName)=>
    @kingdomDict[id] = new Kingdom(id, name, latinName)


  addGenus:(kingdomID, genusID, name, latinName)=>
    genus = new Genus(@kingdomDict[kingdomID], genusID, name, latinName)
    @kingdomDict[kingdomID].genusList.push(genus)
    @genusDict[genusID] = genus


  addSpecies:(genusID, speciesID, name, latinName)=>
    species = new Species(@genusDict[genusID], speciesID, name, latinName)
    @genusDict[genusID].speciesList.push(species)


  getKingdomList: ()=>
    list = []
    for key in Object.keys(@kingdomDict)
      list.push(@kingdomDict[key])
    return list


  getGenusList: (kingdomID)=>
    list = []
    for key in Object.keys(@kingdomDict)
      kingdom = @kingdomDict[key]
      if kingdom.id == kingdomID
        for genus in kingdom.genusList
          list.push(genus)
    return list


  getSpeciesList: (genusID)=>
    list = []
    for key in Object.keys(@genusDict)
      genus = @genusDict[key]
      if genus.id == genusID
        for species in genus.speciesList
          list.push(species)
    return list



root.grow_journal.TaxonomyDataAccess = TaxonomyDataAccess
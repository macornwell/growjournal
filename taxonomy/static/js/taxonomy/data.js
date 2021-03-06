// Generated by CoffeeScript 1.10.0
(function() {
  var Genus, Kingdom, LifeForm, Species, TaxonomyDataAccess, ref, root,
    bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  root = typeof exports !== "undefined" && exports !== null ? exports : this;

  root.grow_journal = (ref = root.grow_journal) != null ? ref : {};

  Kingdom = (function() {
    function Kingdom(id1, name1, latinName1) {
      this.id = id1;
      this.name = name1;
      this.latinName = latinName1;
      this.genusList = [];
    }

    return Kingdom;

  })();

  Genus = (function() {
    function Genus(kingdom1, id1, name1, latinName1) {
      this.kingdom = kingdom1;
      this.id = id1;
      this.name = name1;
      this.latinName = latinName1;
      this.speciesList = [];
    }

    return Genus;

  })();

  Species = (function() {
    function Species(genus1, id1, name1, latinName1) {
      this.genus = genus1;
      this.id = id1;
      this.name = name1;
      this.latinName = latinName1;
    }

    return Species;

  })();

  LifeForm = (function() {
    function LifeForm(id1, name1, latinName1, species1, cultivar, rootstock) {
      this.id = id1;
      this.name = name1;
      this.latinName = latinName1;
      this.species = species1 != null ? species1 : null;
      this.cultivar = cultivar != null ? cultivar : null;
      this.rootstock = rootstock != null ? rootstock : null;
      '';
    }

    return LifeForm;

  })();

  root.grow_journal.LifeForm = LifeForm;

  TaxonomyDataAccess = (function() {
    function TaxonomyDataAccess() {
      this.getSpeciesList = bind(this.getSpeciesList, this);
      this.getGenusList = bind(this.getGenusList, this);
      this.getKingdomList = bind(this.getKingdomList, this);
      this.addSpecies = bind(this.addSpecies, this);
      this.addGenus = bind(this.addGenus, this);
      this.addKingdom = bind(this.addKingdom, this);
      this.kingdomDict = {};
      this.genusDict = {};
    }

    TaxonomyDataAccess.prototype.addKingdom = function(id, name, latinName) {
      return this.kingdomDict[id] = new Kingdom(id, name, latinName);
    };

    TaxonomyDataAccess.prototype.addGenus = function(kingdomID, genusID, name, latinName) {
      var genus;
      genus = new Genus(this.kingdomDict[kingdomID], genusID, name, latinName);
      this.kingdomDict[kingdomID].genusList.push(genus);
      return this.genusDict[genusID] = genus;
    };

    TaxonomyDataAccess.prototype.addSpecies = function(genusID, speciesID, name, latinName) {
      var species;
      species = new Species(this.genusDict[genusID], speciesID, name, latinName);
      return this.genusDict[genusID].speciesList.push(species);
    };

    TaxonomyDataAccess.prototype.getKingdomList = function() {
      var i, key, len, list, ref1;
      list = [];
      ref1 = Object.keys(this.kingdomDict);
      for (i = 0, len = ref1.length; i < len; i++) {
        key = ref1[i];
        list.push(this.kingdomDict[key]);
      }
      return list;
    };

    TaxonomyDataAccess.prototype.getGenusList = function(kingdomID) {
      var genus, i, j, key, kingdom, len, len1, list, ref1, ref2;
      list = [];
      ref1 = Object.keys(this.kingdomDict);
      for (i = 0, len = ref1.length; i < len; i++) {
        key = ref1[i];
        kingdom = this.kingdomDict[key];
        if (kingdom.id === kingdomID) {
          ref2 = kingdom.genusList;
          for (j = 0, len1 = ref2.length; j < len1; j++) {
            genus = ref2[j];
            list.push(genus);
          }
        }
      }
      return list;
    };

    TaxonomyDataAccess.prototype.getSpeciesList = function(genusID) {
      var genus, i, j, key, len, len1, list, ref1, ref2, species;
      list = [];
      ref1 = Object.keys(this.genusDict);
      for (i = 0, len = ref1.length; i < len; i++) {
        key = ref1[i];
        genus = this.genusDict[key];
        if (genus.id === genusID) {
          ref2 = genus.speciesList;
          for (j = 0, len1 = ref2.length; j < len1; j++) {
            species = ref2[j];
            list.push(species);
          }
        }
      }
      return list;
    };

    return TaxonomyDataAccess;

  })();

  root.grow_journal.TaxonomyDataAccess = TaxonomyDataAccess;

}).call(this);

//# sourceMappingURL=data.js.map

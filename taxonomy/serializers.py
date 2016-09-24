from rest_framework import serializers
from taxonomy.models import Kingdom, Genus, Species, Variety, LifeForm

class KingdomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kingdom
        fields = ('kingdom_id', 'name', 'latin_name')


class GenusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genus
        fields = ('genus_id', 'kingdom', 'name', 'latin_name')


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Species
        fields = ('species_id', 'kingdom', 'genus', 'name', 'latin_name', 'origin_location')


class VarietySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variety
        fields = ('variety_id', 'species', 'name', 'name_denormalized', 'latin_name', 'origin_location')






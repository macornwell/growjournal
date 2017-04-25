from rest_framework import serializers
from taxonomy.models import Kingdom, Genus, Species, Cultivar, LifeForm

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


class CultivarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cultivar
        fields = ('cultivar_id', 'species', 'name', 'name_denormalized', 'latin_name', 'origin_location')


class LifeFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LifeForm
        fields = ('life_form_id', 'species', 'cultivar', 'rootstock', 'name', 'latin_name')




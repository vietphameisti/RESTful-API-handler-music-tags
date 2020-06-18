from rest_framework import serializers
from Music.models import Tag, Track, Album, Artist
from django.forms.models import model_to_dict


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tag
        fields=('id',
                'tag_name')

class TrackSerializer(serializers.ModelSerializer):
    #track_tag=TagSerializer(read_only=True,many=True)
    track_tag=serializers.PrimaryKeyRelatedField(read_only=False, many=True, queryset=Tag.objects.all())
    class Meta:
        model= Track
        fields=('id',
                'track_name',
                'track_tag')
    #Override the to_representation method to get the specified JSON output format 
    def to_representation(self, instance):
        format=  {
            'type':'track',
            'id':instance.id,
            'track name':instance.track_name,
            #'tag':{str(x) for x in instance.track_tag.all()}
            'tag':{x.tag_name for x in instance.track_tag.all()}
            }
        return format

class AlbumSerializer(serializers.ModelSerializer):
    album_tag=serializers.PrimaryKeyRelatedField(read_only=False, many=True,queryset=Tag.objects.all())
    class Meta:
        model= Album
        fields=('id',
                'album_name',
                'album_tag')
    def to_representation(self, instance):
        format=  {
            'type':'album',
            'id':instance.id,
            'track name':instance.album_name,
            'tag':{x.tag_name for x in instance.album_tag.all()}
            }
        return format

class ArtistSerializer(serializers.ModelSerializer):
    artist_tag=serializers.PrimaryKeyRelatedField(read_only=False, many=True, queryset=Tag.objects.all())
    class Meta:
        model= Artist
        fields=('id',
                'artist_name',
                'artist_tag')
    def to_representation(self, instance):
        format=  {
            'type':'artist',
            'id':instance.id,
            'track name':instance.artist_name,
            'tag':{x.tag_name for x in instance.artist_tag.all()}
            }
        return format
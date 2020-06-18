from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import status

from Music.models import Tag,Track,Album,Artist
from Music.serializers import TagSerializer,TrackSerializer,AlbumSerializer,ArtistSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


##TAG
@api_view(['GET','POST'])
def tag_list(request):
    if request.method=='GET':
        tags=Tag.objects.all()
        tag_serializer=TagSerializer(tags,many=True)
        return Response(tag_serializer.data)

    elif request.method=='POST':
        tag_serializer=TagSerializer(data=request.data)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return Response(tag_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def tag_detail(request, pk):
    try:
        tag=Tag.objects.get(id=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        tag_serializer=TagSerializer(tag)
        return Response(tag_serializer.data)

    elif request.metho=='PUT':
        tag_serializer=TagSerializer(tag,data=request.data)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return Response(tag_serializer.data)
        return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##TRACK
'''
This function allows adding tags into tracks via POST method, 
and retrieve tracks' information base on input tags using the GET method (pop, rock..etc) 
Input:  request from user
Output: add tags into a track and display the result return
        or display track information with input tags related 
'''
@api_view(['GET','POST'])
def add_queryTrackTag(request):
    if request.method=='POST':
        track_serializer=TrackSerializer(data=request.data)
        if track_serializer.is_valid():
            track_serializer.save()
            return Response(track_serializer.data, status=status.HTTP_201_CREATED)
        return Response(track_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='GET':
        try:
            tags=request.query_params.get('tags').split(',')
            #tags=request.query_params.getlist('tags','')
            tracks=Track.objects.all()
            for tag in tags:
                id = Tag.objects.get(tag_name=str(tag)).id
                tracks=tracks.filter(track_tag=id)
            track_serializer=TrackSerializer(tracks,many=True)
            return Response(track_serializer.data)
            #track=Track.objects.get(id=pk)
        except Track.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


##ALBUM
'''
This function allows adding tags into albums via POST method, 
and retrieve albums' information base on input tags using the GET method (pop, rock..etc) 
Input:  request from user
Output: add tags into a album and display the result return
        or display album information with input tags related
'''
@api_view(['GET','POST'])
def add_queryAlbumTag(request):
    if request.method=='POST':
        album_serializer=AlbumSerializer(data=request.data)
        if album_serializer.is_valid():
            album_serializer.save()
            return Response(album_serializer.data, status=status.HTTP_201_CREATED)
        return Response(album_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='GET':
        try:
            tags=request.query_params.get('tags').split(',')
            albums=Album.objects.all()
            for tag in tags:
                id = Tag.objects.get(tag_name=str(tag)).id
                albums=albums.filter(album_tag=id)
            album_serializer=AlbumSerializer(albums,many=True)
            return Response(album_serializer.data)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

##ARTIST
'''
This function allows adding tags into artists via POST method, 
and retrieve artists' information base on input tags using the GET method (pop, rock..etc) 
Input:  request from user
Output: add tags into a artist and display the result return
        or display artist information with input tags related
'''

@api_view(['GET','POST'])
def add_queryArtistTag(request):
    if request.method=='POST':
        artist_serializer=ArtistSerializer(data=request.data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return Response(artist_serializer.data, status=status.HTTP_201_CREATED)
        return Response(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='GET':
        try:
            tags=request.query_params.get('tags').split(',')
            artists=Artist.objects.all()
            for tag in tags:
                id = Tag.objects.get(tag_name=str(tag)).id
                artists=artists.filter(artist_tag=id)
            artist_serializer=ArtistSerializer(artists,many=True)
            return Response(artist_serializer.data)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


##EXPORT ALL
'''
This function export all information of tracks, albums, 
and artists tagged and all the related tags
Input:  request from user
Output: information of tracks, albums, and artists tagged in JSON specified format

'''
@api_view(['GET'])
def export(request):
    if request.method=='GET':
        tags=Tag.objects.all()
        tracks=Track.objects.filter(track_tag__in=tags).distinct()
        albums=Album.objects.filter(album_tag__in=tags).distinct()
        artists=Artist.objects.filter(artist_tag__in=tags).distinct()
        track_serializer=TrackSerializer(tracks,many=True)
        album_serializer=AlbumSerializer(albums,many=True)
        artist_serializer=ArtistSerializer(artists,many=True)
        return Response({'tracks':track_serializer.data,
                         'album':album_serializer.data,
                         'artist':artist_serializer.data
                         })
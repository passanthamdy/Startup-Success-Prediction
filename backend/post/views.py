from django.shortcuts import get_object_or_404, render
from .models import Post, Comment
from .serializers import PostSerializer, DatasetSerializer, CreatePostSerializer, CommentSerializer
from profiles.serializer import ProfileSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status as statu
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from profiles.permissions import UserWritePermission
from rest_framework import authentication, permissions
import json
import pandas as pd
import joblib
model = joblib.load('modelPipeline7.pkl')
dataset = pd.read_csv(
    'https://raw.githubusercontent.com/AhmadAmr/start-up-prediction-system/main/companiesfinal.csv')


class CreatePostView(generics.CreateAPIView):
    query_set = Post.objects.all()
    serializer_class = CreatePostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# dont forget to remove allowany permission
class PostDetailView(generics.RetrieveUpdateDestroyAPIView, UserWritePermission):
    permission_classes = [UserWritePermission]
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    lookup_field = 'id'


class AddPostDataset(APIView):
    #permission_classes = [AllowAny]

    def post(self, request, slug=None, format='json', id=id):
        # User data
        data = json.loads(request.body)
        dataF = pd.DataFrame({'x': data}).transpose()
        #print(dataF)
        filt1 = (dataset['country_code'] == data['country_code'])
        filt2 = (dataset['category_list'] == data['category_list'])
        country = dataset.loc[filt1]
        final = country.loc[filt2]
        fail = dataset.loc[filt2]
        status = True

        # compute score
        if final.empty:
            score = model.predict_proba(fail)[:, -1][0]
            status = False
        else:
            score = model.predict_proba(dataF)[:, -1][0]

        # save to Models
        data['user'] = request.user.id
        data['score'] = score
        data['maxfund'] = final['funding_total_usd'].max()
        data['minfund'] = final['funding_total_usd'].median()
        data['post'] = id
        data['status'] = status
        #print(data)
        serializer = DatasetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            json_obj = serializer.data
            return Response(json_obj, status=statu.HTTP_201_CREATED)
        return Response(serializer.errors, status=statu.HTTP_400_BAD_REQUEST)


class PostLike(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None, format=None):
        obj = get_object_or_404(Post, id=id)
        user = self.request.user
        updated = False
        liked = False
        if user:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
            data = {
                "updated": updated,
                "liked": liked
            }

        return Response(data)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostCommentsView(generics.CreateAPIView):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


   


class CommentDetail(generics.RetrieveUpdateDestroyAPIView, UserWritePermission):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [UserWritePermission]
    lookup_field = 'id'

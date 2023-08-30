from django.urls import include, path
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework.routers import DefaultRouter

from api.views import (FollowApiView, ListFollowViewSet, UserViewSet,
                       IngredientsViewSet, RecipeViewSet, TagsViewSet)

router_1 = DefaultRouter()

router_1.register('users', UserViewSet, 'users')
router_1.register('ingredients', IngredientsViewSet, basename='ingredients')
router_1.register('recipes', RecipeViewSet, basename='recipes')
router_1.register('tags', TagsViewSet, basename='tags')

urlpatterns = [
    path('', include(router_1.urls)),
    path('auth/token/login/', TokenCreateView.as_view(), name='login'),
    path('auth/token/logout/', TokenDestroyView.as_view(), name='logout'),
    path('users/<int:id>/subscribe/',
         FollowApiView.as_view(), name='subscribe'),
    path('users/subscriptions/',
         ListFollowViewSet.as_view(), name='subscription'),
    path('', include('djoser.urls')),
]

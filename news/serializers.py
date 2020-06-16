from rest_framework import serializers

from .models import News


class NewsListSerializer(serializers.ModelSerializer):
    """List of news"""

    class Meta:
        model = News
        fields = ('__all__')

class NewsDetailSerializer(serializers.ModelSerializer):
    """Full single news"""

    category = serializers.SlugRelatedField(slug_field='category_title', read_only=True)

    class Meta:
        model = News
        exclude = ('published', )


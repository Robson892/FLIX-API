from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # Campo calculado somente para leitura
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    # Função para campo calculado inicia com get_
    def get_rate(self, obj):

        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]

        if rate:
            return round(rate, 1)

        return None

    # validação de erros, sempre inicar função com validate_
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1990"
            )
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                "O resumo não pode ter mais de 200 caracteres"
            )
        return value


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_movies = serializers.IntegerField()
    average_stars = serializers.FloatField()

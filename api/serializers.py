from rest_framework import serializers
from books.models import Books


class BookSerializer(serializers.ModelSerializer):
    """ Here what information want to show to the outer world/User
    Return from an API doesn't necessariy need to have all fields from model, Because in models we have sometimes sensitive information also calld a internal representation and in api view we have called external representation that client see,
    from product model lets return an id, title and unit_price. 
    """
    # is just like a models fields
    

    class Meta:
        model = Books
        fields = [
            'title',
            'slug',
            'author',
            'genre',
            'isbn'
        ]

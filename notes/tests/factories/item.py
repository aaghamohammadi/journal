import factory

from notes.models import Item
from .user import UserFactory


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    title = factory.Sequence(lambda n: f"title_{n}")
    text = factory.Sequence(lambda n: f"text_{n}")
    user = factory.SubFactory(UserFactory)

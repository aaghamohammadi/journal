import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"username_{n}")
    email = factory.Sequence(lambda n: f"email_{n}@gmail.com")
    password = factory.PostGenerationMethodCall("set_password", "password")

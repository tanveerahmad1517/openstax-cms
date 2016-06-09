from django.core.management import call_command
from django.utils.six import StringIO
from rest_framework import viewsets
from salesforce.models import Adopter
from salesforce.functions import check_if_faculty_pending
from social.apps.django_app.default.models import \
    DjangoStorage as SocialAuthStorage
from wagtail.wagtailimages.models import Image

from .serializers import AdopterSerializer, ImageSerializer, UserSerializer


class AdopterViewSet(viewsets.ModelViewSet):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user

        try:
            social_auth = SocialAuthStorage.user.get_social_auth_for_user(user)
            user.accounts_id = social_auth[0].uid
        except:
            user.accounts_id = None

        try:
            out = StringIO()
            call_command('update_faculty_status', str(user.pk), stdout=out)
        except:
            pass

        # check if there is a record in salesforce for this user - if so, they are pending verification
        user.pending_verification = check_if_faculty_pending(user.pk)

        return [user]


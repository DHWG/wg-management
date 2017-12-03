from persons.models import Inhabitant
from pam import pam

class PAMBackend(object):
    def authenticate(self, request, username=None, password=None):
        if not pam().authenticate(username.lower(), password):
            return None
        try:
            return Inhabitant.objects.get_by_natural_key(username)
        except:
            user = Inhabitant.objects.create(username=username,
                                             password=password,
                                             is_staff=True)
            return user

    def get_user(self, user_id):
        return Inhabitant.objects.get(pk=user_id)
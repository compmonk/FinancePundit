import pyrebase

from django.conf import settings


class FireBase:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
        self.auth = self.firebase.auth()

    def sign_in(self, email, password):
        return self.auth.sign_in_with_email_and_password(email, password)

    def sign_up(self, email, password):
        return self.auth.create_user_with_email_and_password(email, password)

    def get_user_info(self, user):
        return self.auth.get_account_info(user['idToken'])

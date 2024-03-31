import re


class CredentialsModel:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate(self):
        if not self.email:
            return "Missing email."
        if not self.password:
            return "Missing password."
        # In theory valid email can't be shorter than 6 characters.
        # E. g.: a@a.il is 6 characters email.
        if len(self.email) < 6 or len(self.email) > 100:
            return "Email length must be 6 to 100 chars."
        if len(self.password) < 4 or len(self.password) > 100:
            return "Password length must be 4 to 100 characters."
        if not re.match(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", self.email):
            return "Email not valid."
        return None

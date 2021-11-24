import hashlib

from django.db import models

class passcode(models.Model):
    passname_text = models.CharField(max_length=50)
    pass_text = models.CharField(max_length=64)

    def __str__(self):
        return self.passname_text

    def makepasstext(self,x:int):
        self.pass_text=hashlib.sha256(str(x).encode()).hexdigest()
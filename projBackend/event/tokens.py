from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
import random
import string

def GetToken1():
    token = random.randint(1,2147483647)
    return token

def GetToken2():
    token = random.randint(1,2147483647)
    return token

def GetToken3(size=300, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))
# -*- coding: utf-8 -*- 
__author__ = 'ivany'

# import uuid
from app.utils import md5, getUuid

if __name__ == "__main__":
    # u = uuid.uuid4()
    str = md5("he02834894")
    print(str)

    print(getUuid())
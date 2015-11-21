# -*- coding: utf-8 -*-
__author__ = 'ivany'

import os
from app import create_app

app = create_app(os.getenv('IVANY_CONFIG') or 'default')

if __name__ == '__main__':
    app.run()
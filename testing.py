#!/usr/bin/env python
import os

os.environ['FILE_URL'] = 'https://transfer.sh/AQrmt/database.db'

import jarvis

while 1:
    print jarvis.do(raw_input("> "), '0')

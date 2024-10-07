#!/home/jus/anaconda3/envs/autogen/bin/python
# -*- coding: utf-8 -*-
import autogenstudio.database.dbmanager

def init_db_samples(dbmanager: any):
    print('ignore defaults')

autogenstudio.database.dbmanager.init_db_samples = init_db_samples

import re
import sys
from autogenstudio.cli import run
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(run())

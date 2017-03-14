from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_magic)
from IPython import get_ipython
import sys

sys.path.append("/home/jovyan/app")

@magics_class
class MyMagics(Magics):
    @line_magic

    def autoon(self, param):
        ipython = get_ipython()
        ipython.magic("load_ext autoreload")
        ipython.magic("autoreload 2")
        print('autoreload enabled')

ip = get_ipython()
ip.register_magics(MyMagics)

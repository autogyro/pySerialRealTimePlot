# -*- coding: utf-8 -*-
"""
Created on Sun May 07 13:37:40 2017

@author: lee
"""

class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const instance attribute (%s)" % name

        self.__dict__[name] = value

    def __delattr__(self, name):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't unbind const const instance attribute (%s)" % name

        raise AttributeError, "const instance has no attribute '%s'" % name

import sys
sys.modules[__name__] = _const()

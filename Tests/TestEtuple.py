""" tests ReOBJ  Classes
"""
from inspect import (
   getfile,
   currentframe
)
from os.path import (
   abspath,
   dirname,
   join
)
from sys import path as syspath

from nose.tools import (
   raises
)


SCRIPT_PATH = dirname(abspath(getfile(currentframe())))
PROJECT_ROOT = dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'ReOBJ'
ROOT_PACKAGE_PATH = join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

syspath.insert(0, PROJECT_ROOT)

from ReOBJ.MainCode import Etuple
from ReOBJ.ProjectErr import MethodDeactivatedErr


@raises(MethodDeactivatedErr)
def test_clear():
   """ Tests: test_clear
   """
   print('::: TEST: test_clear()')
   re_obj = Etuple([
      'value1',
      'value2',
      'value3',
   ])
   re_obj.clear()


@raises(MethodDeactivatedErr)
def test_copy():
   """ Tests: test_copy
   """
   print('::: TEST: test_copy()')
   re_obj = Etuple([
      'value1',
      'value2',
      'value3',
   ])
   re_obj.copy()


@raises(MethodDeactivatedErr)
def test_add():
   """ Tests: test_add
   """
   print('::: TEST: test_add()')
   re_obj = Etuple([
      'value1',
      'value2',
      'value3',
   ])
   re_obj2 = Etuple([
      'add1',
      'add2',
      'add3',
   ])
   re_obj_final = re_obj + re_obj2


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   pass

   test_clear()
   test_copy()

   test_add()

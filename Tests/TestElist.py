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
   raises,
   ok_
)


SCRIPT_PATH = dirname(abspath(getfile(currentframe())))
PROJECT_ROOT = dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'ReOBJ'
ROOT_PACKAGE_PATH = join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

syspath.insert(0, PROJECT_ROOT)

from ReOBJ.MainCode import Elist
from ReOBJ.ProjectErr import MethodDeactivatedErr


@raises(MethodDeactivatedErr)
def test_clear():
   """ Tests: test_clear
   """
   print('::: TEST: test_clear()')
   re_obj = Elist([
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
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   re_obj.copy()


def test_del():
   """ Tests: test_del
   """
   print('::: TEST: test_del()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   del re_obj[1]
   ok_('value2' not in re_obj, msg=None)


def test_pop():
   """ Tests: test_pop
   """
   print('::: TEST: test_pop()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   tmp_val = re_obj.pop(1)
   ok_(tmp_val == 'value2', msg=None)
   ok_('value2' not in re_obj, msg=None)


def test_remove():
   """ Tests: test_remove
   """
   print('::: TEST: test_remove()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   re_obj.remove('value2')
   ok_(len(re_obj) == 2, msg=None)


def test_change_value():
   """ Tests: test_change_value
   """
   print('::: TEST: test_change_value()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   re_obj[1] = 'CHANGED1'
   ok_(re_obj[1] == 'CHANGED1', msg=None)


@raises(IndexError)
def test_set_none_existing_index_value():
   """ Tests: test_set_none_existing_index_value
   """
   print('::: TEST: test_set_none_existing_index_value()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   re_obj[4] = 'NEW'
   ok_(re_obj[4] == 'NEW', msg=None)


def test_append():
   """ Tests: test_append
   """
   print('::: TEST: test_append()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   re_obj.append('none existing value')
   ok_(re_obj[3] == 'none existing value', msg=None)
   ok_(len(re_obj) == 4, msg=None)


def test_insert():
   """ Tests: test_insert
   """
   print('::: TEST: test_insert()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   re_obj.insert(0, 'none existing value')
   ok_(re_obj[0] == 'none existing value', msg=None)
   ok_(len(re_obj) == 4, msg=None)


@raises(MethodDeactivatedErr)
def test_add():
   """ Tests: test_add
   """
   print('::: TEST: test_add()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   re_obj2 = Elist([
      'add1',
      'add2',
      'add3',
   ])
   re_obj_final = re_obj + re_obj2


def test_extend():
   """ Tests: test_extend
   """
   print('::: TEST: test_extend()')
   re_obj = Elist([
      'value1',
      'value2',
      'value3',
   ])
   re_obj2 = Elist([
      'add1',
      'add2',
      'add3',
   ])
   re_obj.extend(re_obj2)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   pass

   test_clear()
   test_copy()

   test_del()
   test_pop()
   test_remove()

   test_change_value()
   test_set_none_existing_index_value()
   test_append()
   test_insert()
   test_add()
   test_extend()

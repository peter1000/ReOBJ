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

from ReOBJ.MainCode import RdictFO
from ReOBJ.ProjectErr import MethodDeactivatedErr


@raises(MethodDeactivatedErr)
def test_clear():
   """ Tests: test_clear
   """
   print('::: TEST: test_clear()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   re_obj.clear()


@raises(MethodDeactivatedErr)
def test_copy():
   """ Tests: test_copy
   """
   print('::: TEST: test_copy()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   re_obj.copy()


@raises(MethodDeactivatedErr)
def test_del():
   """ Tests: test_del
   """
   print('::: TEST: test_del()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   del re_obj['key2']
   ok_('key2' not in re_obj, msg=None)


@raises(MethodDeactivatedErr)
def test_pop():
   """ Tests: test_pop
   """
   print('::: TEST: test_pop()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   tmp_val = re_obj.pop('key2')
   ok_(tmp_val == 'value2', msg=None)
   ok_('key2' not in re_obj, msg=None)


@raises(MethodDeactivatedErr)
def test_popitem():
   """ Tests: test_popitem
   """
   print('::: TEST: test_popitem()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   tmp_val = re_obj.popitem()
   ok_(len(re_obj) == 2, msg=None)


def test_change_value():
   """ Tests: test_change_value
   """
   print('::: TEST: test_change_value()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   re_obj['key1'] = 'CHANGED1'
   ok_(re_obj['key1'] == 'CHANGED1', msg=None)


@raises(KeyError)
def test_set_none_existing_key_value():
   """ Tests: test_set_none_existing_key_value
   """
   print('::: TEST: test_set_none_existing_key_value()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   re_obj['key4'] = 'NEW'
   ok_(re_obj['key4'] == 'NEW', msg=None)


@raises(MethodDeactivatedErr)
def test_get():
   """ Tests: test_get
   """
   print('::: TEST: test_get()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   tmp_val = re_obj.get('key2', 'none existing key value')
   ok_(tmp_val == 'value2', msg=None)


@raises(MethodDeactivatedErr)
def test_get_none_exiting():
   """ Tests: test_get_none_exiting
   """
   print('::: TEST: test_get_none_exiting()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   tmp_val = re_obj.get('key4', 'none existing key value')
   ok_(tmp_val == 'none existing key value', msg=None)


@raises(MethodDeactivatedErr)
def test_update():
   """ Tests: test_update
   """
   print('::: TEST: test_update()')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   re_obj.update({
      'key4': 'value4',
      'key5': 'value5'
   })
   ok_(len(re_obj) == 5, msg=None)
   ok_(re_obj['key5'] == 'value5', msg=None)


@raises(MethodDeactivatedErr)
def test_setdefault():
   """ Tests: test_setdefault
   """
   print('::: TEST: test_setdefault')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)
   temp_val = re_obj.setdefault('mykey1', 'default')
   temp_val_2 = re_obj.setdefault('key1', 'default')
   ok_(re_obj['mykey1'] == 'default' and re_obj['key1'] == 'value1', msg=None)
   ok_(temp_val == 'default', msg=None)
   ok_(temp_val_2 == 'value1', msg=None)


@raises(MethodDeactivatedErr)
def test_fromkeys():
   """ Tests: test_fromkeys
   """
   print('::: TEST: test_fromkeys')
   re_obj = RdictFO.fromkeys(['key1', 'key2', 'key3'])
   ok_(re_obj['key2'] is True, msg=None)
   ok_(len(re_obj) == 3, msg=None)


def test_yield_key_value_order():
   """ Tests: test_yield_key_value_order
   """
   print('::: TEST: test_yield_key_value_order')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)

   key_list = ['key1', 'key2', 'key3']
   idx = -1
   for key, value in re_obj.yield_key_value_order():
      idx += 1
      ok_(key_list[idx] == key and re_obj[key] == value, msg=None)


def test_yield_extra_key_value_order():
   """ Tests: test_yield_extra_key_value_order
   """
   print('::: TEST: test_yield_extra_key_value_order')
   re_obj = RdictFO([
      ('key1', 'value1'),
      ('key2', 'value2'),
      ('key3', 'value3'),
   ], False)

   key_list = ['key3', 'key1', 'key2']
   re_obj.replace_extra_key_order(key_list)
   idx = -1
   for key, value in re_obj.yield_extra_key_value_order():
      idx += 1
      ok_(key_list[idx] == key and re_obj[key] == value, msg=None)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   pass

   test_clear()
   test_copy()

   test_del()
   test_pop()
   test_popitem()

   test_change_value()
   test_set_none_existing_key_value()
   test_get()
   test_get_none_exiting()

   test_update()
   test_setdefault()
   test_fromkeys()

   test_yield_key_value_order()
   test_yield_extra_key_value_order()



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

from ReOBJ.MainCode import Lmatrix
from ReOBJ.ProjectErr import (
   Err,
   MethodDeactivatedErr
)


@raises(MethodDeactivatedErr)
def test_clear():
   """ Tests: test_clear
   """
   print('::: TEST: test_clear()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.clear()


@raises(MethodDeactivatedErr)
def test_copy():
   """ Tests: test_copy
   """
   print('::: TEST: test_copy()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.copy()


def test_del():
   """ Tests: test_del
   """
   print('::: TEST: test_del()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   del re_obj[1]
   ok_(('steelblue', 70, 130, 180) not in re_obj, msg=None)


def test_pop():
   """ Tests: test_pop
   """
   print('::: TEST: test_pop()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   tmp_val = re_obj.pop(1)
   ok_(tmp_val == ('steelblue', 70, 130, 180), msg=None)
   ok_(('steelblue', 70, 130, 180) not in re_obj, msg=None)


def test_remove():
   """ Tests: test_remove
   """
   print('::: TEST: test_remove()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.remove(('steelblue', 70, 130, 180))
   ok_(len(re_obj) == 2, msg=None)


def test_change_value():
   """ Tests: test_change_value
   """
   print('::: TEST: test_change_value()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj[1] = ('flesh', 255, 125, 64)
   ok_(re_obj[1] == ('flesh', 255, 125, 64), msg=None)


@raises(IndexError)
def test_set_none_existing_index_value():
   """ Tests: test_set_none_existing_index_value
   """
   print('::: TEST: test_set_none_existing_index_value()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj[4] = ('flesh', 255, 125, 64)
   ok_(re_obj[4] == ('flesh', 255, 125, 64), msg=None)


def test_append():
   """ Tests: test_append
   """
   print('::: TEST: test_append()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.append(('flesh', 255, 125, 64))
   ok_(re_obj[3] == ('flesh', 255, 125, 64), msg=None)
   ok_(len(re_obj) == 4, msg=None)


@raises(Err)
def test_append2():
   """ Tests: test_append2
   """
   print('::: TEST: test_append2()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.append((255, 125, 64))


def test_insert():
   """ Tests: test_insert
   """
   print('::: TEST: test_insert()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.insert(0, ('flesh', 255, 125, 64))
   ok_(re_obj[0] == ('flesh', 255, 125, 64), msg=None)
   ok_(len(re_obj) == 4, msg=None)


@raises(Err)
def test_insert2():
   """ Tests: test_insert
   """
   print('::: TEST: test_insert()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.insert(0, 'NEW WRONG ITEM')


@raises(MethodDeactivatedErr)
def test_add():
   """ Tests: test_add
   """
   print('::: TEST: test_add()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj2 = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ], unique_column_names=True)
   re_obj_final = re_obj + re_obj2


def test_extend():
   """ Tests: test_extend
   """
   print('::: TEST: test_extend()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj2 = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ], unique_column_names=True)
   re_obj.extend(re_obj2)


def test_replace_column_names():
   """ Tests: test_replace_column_names
   """
   print('::: TEST: test_replace_column_names()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.replace_column_names(('new1', 'new2 ', 'new3', 'new4'))
   ok_(re_obj.column_names == ('new1', 'new2 ', 'new3', 'new4'), msg=None)


@raises(Err)
def test_replace_column_names2():
   """ Tests: test_replace_column_names2
   """
   print('::: TEST: test_replace_column_names2()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.replace_column_names(['new1', 'new2 ', 'new3'])


@raises(Err)
def test_replace_column_names3():
   """ Tests: test_replace_column_names3
   """
   print('::: TEST: test_replace_column_names3()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)
   re_obj.replace_column_names(('new1', 'new2 ', 'new3', 'new4', 'new5'))


def test_init_with_tuple_of_tuples():
   """ Tests: test_init_with_tuple_of_tuples
   """
   print('::: TEST: test_init_with_tuple_of_tuples()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ), unique_column_names=False)


def test_unique_column_names1():
   """ Tests: test_unique_column_names1
   """
   print('::: TEST: test_unique_column_names1()')
   re_obj = Lmatrix(('name', 'red', 'red', 'red'), (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ), unique_column_names=False)


@raises(Err)
def test_unique_column_names2():
   """ Tests: test_unique_column_names2
   """
   print('::: TEST: test_unique_column_names2()')
   re_obj = Lmatrix(('name', 'red', 'red', 'red'), (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ), unique_column_names=True)


def test__copy_recursively_tuple_of_tuples():
   """ Tests: test__copy_recursively_tuple_of_tuples
   """
   print('::: TEST: test__copy_recursively_tuple_of_tuples()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ), unique_column_names=True)

   re_obj.update_extra_data({'extrakey1': 'extravalue1', 'extrakey2': 'extravalue2'})

   new_obj = re_obj.copy_recursively()
   ok_(re_obj == new_obj, msg=None)
   ok_(re_obj.column_names == new_obj.column_names, msg=None)
   ok_(re_obj.column_names_idx_lookup == new_obj.column_names_idx_lookup, msg=None)
   ok_(re_obj.column_names_counted == new_obj.column_names_counted, msg=None)
   ok_(re_obj.extra_data == new_obj.extra_data, msg=None)
   ok_(re_obj.unique_column_names == new_obj.unique_column_names, msg=None)


def test__copy_recursively_list_of_tuples():
   """ Tests: test__copy_recursively_list_of_tuples
   """
   print('::: TEST: test__copy_recursively_list_of_tuples()')
   re_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
   ], unique_column_names=True)

   re_obj.update_extra_data({'extrakey1': 'extravalue1', 'extrakey2': 'extravalue2'})

   new_obj = re_obj.copy_recursively()
   ok_(re_obj == new_obj, msg=None)
   ok_(re_obj.column_names == new_obj.column_names, msg=None)
   ok_(re_obj.column_names_idx_lookup == new_obj.column_names_idx_lookup, msg=None)
   ok_(re_obj.column_names_counted == new_obj.column_names_counted, msg=None)
   ok_(re_obj.extra_data == new_obj.extra_data, msg=None)
   ok_(re_obj.unique_column_names == new_obj.unique_column_names, msg=None)


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
   test_append2()
   test_insert()
   test_insert2()
   test_add()
   test_extend()

   test_replace_column_names()
   test_replace_column_names2()
   test_replace_column_names3()

   test_init_with_tuple_of_tuples()
   test_unique_column_names1()
   test_unique_column_names2()

   test__copy_recursively_tuple_of_tuples()
   test__copy_recursively_list_of_tuples()

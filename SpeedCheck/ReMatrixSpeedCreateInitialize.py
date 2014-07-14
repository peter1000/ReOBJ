""" ReMatrixSpeedCreateInitialize
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
import sys
from sys import path as syspath

try:
   from SpeedIT.BenchmarkIT import speedit_func_benchmark_list
except ImportError as err:
   sys.exit('Example SpeedTest: Can not run example. This example needs the package <SpeedIT> to be installed: <{}>'.format(err))

SCRIPT_PATH = dirname(abspath(getfile(currentframe())))
PROJECT_ROOT = dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'ReOBJ'
ROOT_PACKAGE_PATH = join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

syspath.insert(0, PROJECT_ROOT)

from ReOBJ.MainCode import (
   Lmatrix,
   LmatrixF,
   Elist,
   Etuple
)


def init__py_list_of_tuples_direct():
   matrix_obj = [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ]


def init__py_list_of_tuples_constructor():
   matrix_obj = list([
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ])


def init__py_tuple_of_tuples_direct():
   matrix_obj = (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   )


def init__py_tuple_of_tuples_constructor__with_list():
   matrix_obj = tuple([
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ])


def init__py_tuple_of_tuples_constructor__with_tuple():
   matrix_obj = tuple((
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ))


def init__lmatrix__with_list_unique_names():
   matrix_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ], unique_column_names=True)


def init__lmatrix__with_tuple_unique_names():
   matrix_obj = Lmatrix(('name', 'red', 'green', 'blue'), (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ), unique_column_names=True)


def init__lmatrixf__with_list_unique_names():
   matrix_obj = LmatrixF(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ], unique_column_names=True)


def init__lmatrixf__with_tuple_unique_names():
   matrix_obj = LmatrixF(('name', 'red', 'green', 'blue'), (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ), unique_column_names=True)


def init__lmatrix__with_list_no_unique_names():
   matrix_obj = Lmatrix(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ], unique_column_names=False)


def init__lmatrix__with_tuple_no_unique_names():
   matrix_obj = Lmatrix(('name', 'red', 'green', 'blue'), (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ), unique_column_names=False)


def init__lmatrixf__with_list_no_unique_names():
   matrix_obj = LmatrixF(('name', 'red', 'green', 'blue'), [
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ], unique_column_names=False)


def init__lmatrixf__with_tuple_no_unique_names():
   matrix_obj = LmatrixF(('name', 'red', 'green', 'blue'), (
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ), unique_column_names=False)


def init__etuple_of_tuples_constructor__with_list():
   matrix_obj = Etuple([
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ])


def init__etuple_of_tuples_constructor__with_tuple():
   matrix_obj = Etuple((
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ))


def init__elist_of_tuples_constructor__with_list():
   matrix_obj = Elist([
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ])


def init__elist_of_tuples_constructor__with_tuple():
   matrix_obj = Elist((
      ('lavender', 230, 230, 250),
      ('steelblue', 70, 130, 180),
      ('lawngreen ', 124, 252, 0),
      ('darkorange', 255, 140, 0),
      ('flesh', 255, 125, 64),
      ('firebrick 3', 205, 38, 38),
   ))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   pass

   func_list = {
      'init__py_list_of_tuples_direct': (init__py_list_of_tuples_direct, [], {}),
      'init__py_list_of_tuples_constructor': (init__py_tuple_of_tuples_direct, [], {}),

      'init__py_tuple_of_tuples_direct': (init__py_tuple_of_tuples_direct, [], {}),
      'init__py_tuple_of_tuples_constructor__with_list': (init__py_tuple_of_tuples_constructor__with_list, [], {}),
      'init__py_tuple_of_tuples_constructor__with_tuple': (init__py_tuple_of_tuples_constructor__with_tuple, [], {}),

      'init__lmatrix__with_list_unique_names()': (init__lmatrix__with_list_unique_names, [], {}),
      'init__lmatrix__with_tuple_unique_names()': (init__lmatrix__with_tuple_unique_names, [], {}),

      'init__lmatrixf__with_list_unique_names()': (init__lmatrixf__with_list_unique_names, [], {}),
      'init__lmatrixf__with_tuple_unique_names()': (init__lmatrixf__with_tuple_unique_names, [], {}),

      'init__lmatrix__with_list_no_unique_names()': (init__lmatrix__with_list_no_unique_names, [], {}),
      'init__lmatrix__with_tuple_no_unique_names()': (init__lmatrix__with_tuple_no_unique_names, [], {}),

      'init__lmatrixf__with_list_no_unique_names()': (init__lmatrixf__with_list_no_unique_names, [], {}),
      'init__lmatrixf__with_tuple_no_unique_names()': (init__lmatrixf__with_tuple_no_unique_names, [], {}),

      'init__etuple_of_tuples_constructor__with_list': (init__etuple_of_tuples_constructor__with_list, [], {}),
      'init__etuple_of_tuples_constructor__with_tuple': (init__etuple_of_tuples_constructor__with_tuple, [], {}),

      'init__elist_of_tuples_constructor__with_list': (init__elist_of_tuples_constructor__with_list, [], {}),
      'init__elist_of_tuples_constructor__with_tuple': (init__elist_of_tuples_constructor__with_tuple, [], {}),
   }

   setup_line_list = [
      'from ReOBJ.MainCode import Lmatrix, LmatrixF, Etuple, Elist',
   ]

   check_run_sec = 0.1
   with open('result_output/ReMatrixSpeedCreateInitialize.txt', 'w') as file_:
      file_.write('\n\n ReMatrixSpeedCreateInitialize.py output\n\n')
      for count in range(4):
         file_.write('\n'.join(speedit_func_benchmark_list(func_list, setup_line_list, run_sec=check_run_sec, out_put_in_sec=False, use_func_name=False)))
         file_.write('\n\n')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()

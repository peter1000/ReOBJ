""" SpeedCreateAndAddNewItems
"""
from collections import OrderedDict
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
   from SpeedIT.MainCode import speed_it
except ImportError as err:
   sys.exit('Example SpeedTest: Can not run example. This example needs the package <SpeedIT >= 4.0.0> to be installed: <{}>'.format(err))

SCRIPT_PATH = dirname(abspath(getfile(currentframe())))
PROJECT_ROOT = dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'ReOBJ'
ROOT_PACKAGE_PATH = join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

syspath.insert(0, PROJECT_ROOT)

from ReOBJ.MainCode import (
   Edict,
   Rdict,
   RdictIO
)


def add_new_items__py_dict_direct():
   new_obj = {}
   new_obj['joe'] = 123
   new_obj['alex'] = 'old'
   new_obj['marin'] = 'young'
   new_obj['gustavo'] = None
   new_obj['max'] = [1, 2, 3, 4]
   new_obj['janet'] = {'salary': None, 'children': 5}
   new_obj['joe1'] = 123
   new_obj['alex1'] = 'old'
   new_obj['marin1'] = 'young'
   new_obj['gustavo1'] = None
   new_obj['max1'] = [1, 2, 3, 4]
   new_obj['janet1'] = {'salary': None, 'children': 5}
   new_obj['joe2'] = 123
   new_obj['alex2'] = 'old'
   new_obj['marin2'] = 'young'
   new_obj['gustavo2'] = None
   new_obj['max2'] = [1, 2, 3, 4]
   new_obj['janet2'] = {'salary': None, 'children': 5}
   new_obj['joe3'] = 123
   new_obj['alex3'] = 'old'
   new_obj['marin3'] = 'young'
   new_obj['gustavo3'] = None
   new_obj['max3'] = [1, 2, 3, 4]
   new_obj['janet3'] = {'salary': None, 'children': 5}


def add_new_items__py_dict_constructor():
   new_obj = dict()
   new_obj['joe'] = 123
   new_obj['alex'] = 'old'
   new_obj['marin'] = 'young'
   new_obj['gustavo'] = None
   new_obj['max'] = [1, 2, 3, 4]
   new_obj['janet'] = {'salary': None, 'children': 5}
   new_obj['joe1'] = 123
   new_obj['alex1'] = 'old'
   new_obj['marin1'] = 'young'
   new_obj['gustavo1'] = None
   new_obj['max1'] = [1, 2, 3, 4]
   new_obj['janet1'] = {'salary': None, 'children': 5}
   new_obj['joe2'] = 123
   new_obj['alex2'] = 'old'
   new_obj['marin2'] = 'young'
   new_obj['gustavo2'] = None
   new_obj['max2'] = [1, 2, 3, 4]
   new_obj['janet2'] = {'salary': None, 'children': 5}
   new_obj['joe3'] = 123
   new_obj['alex3'] = 'old'
   new_obj['marin3'] = 'young'
   new_obj['gustavo3'] = None
   new_obj['max3'] = [1, 2, 3, 4]
   new_obj['janet3'] = {'salary': None, 'children': 5}


def add_new_items__py_ordereddict():
   new_obj = OrderedDict()
   new_obj['joe'] = 123
   new_obj['alex'] = 'old'
   new_obj['marin'] = 'young'
   new_obj['gustavo'] = None
   new_obj['max'] = [1, 2, 3, 4]
   new_obj['janet'] = {'salary': None, 'children': 5}
   new_obj['joe1'] = 123
   new_obj['alex1'] = 'old'
   new_obj['marin1'] = 'young'
   new_obj['gustavo1'] = None
   new_obj['max1'] = [1, 2, 3, 4]
   new_obj['janet1'] = {'salary': None, 'children': 5}
   new_obj['joe2'] = 123
   new_obj['alex2'] = 'old'
   new_obj['marin2'] = 'young'
   new_obj['gustavo2'] = None
   new_obj['max2'] = [1, 2, 3, 4]
   new_obj['janet2'] = {'salary': None, 'children': 5}
   new_obj['joe3'] = 123
   new_obj['alex3'] = 'old'
   new_obj['marin3'] = 'young'
   new_obj['gustavo3'] = None
   new_obj['max3'] = [1, 2, 3, 4]
   new_obj['janet3'] = {'salary': None, 'children': 5}


def add_new_items__rdict():
   new_obj = Rdict()
   new_obj['joe'] = 123
   new_obj['alex'] = 'old'
   new_obj['marin'] = 'young'
   new_obj['gustavo'] = None
   new_obj['max'] = [1, 2, 3, 4]
   new_obj['janet'] = {'salary': None, 'children': 5}
   new_obj['joe1'] = 123
   new_obj['alex1'] = 'old'
   new_obj['marin1'] = 'young'
   new_obj['gustavo1'] = None
   new_obj['max1'] = [1, 2, 3, 4]
   new_obj['janet1'] = {'salary': None, 'children': 5}
   new_obj['joe2'] = 123
   new_obj['alex2'] = 'old'
   new_obj['marin2'] = 'young'
   new_obj['gustavo2'] = None
   new_obj['max2'] = [1, 2, 3, 4]
   new_obj['janet2'] = {'salary': None, 'children': 5}
   new_obj['joe3'] = 123
   new_obj['alex3'] = 'old'
   new_obj['marin3'] = 'young'
   new_obj['gustavo3'] = None
   new_obj['max3'] = [1, 2, 3, 4]
   new_obj['janet3'] = {'salary': None, 'children': 5}


def add_new_items__rdictio():
   new_obj = RdictIO([], False, init_extra_key_order=False)
   new_obj['joe'] = 123
   new_obj['alex'] = 'old'
   new_obj['marin'] = 'young'
   new_obj['gustavo'] = None
   new_obj['max'] = [1, 2, 3, 4]
   new_obj['janet'] = {'salary': None, 'children': 5}
   new_obj['joe1'] = 123
   new_obj['alex1'] = 'old'
   new_obj['marin1'] = 'young'
   new_obj['gustavo1'] = None
   new_obj['max1'] = [1, 2, 3, 4]
   new_obj['janet1'] = {'salary': None, 'children': 5}
   new_obj['joe2'] = 123
   new_obj['alex2'] = 'old'
   new_obj['marin2'] = 'young'
   new_obj['gustavo2'] = None
   new_obj['max2'] = [1, 2, 3, 4]
   new_obj['janet2'] = {'salary': None, 'children': 5}
   new_obj['joe3'] = 123
   new_obj['alex3'] = 'old'
   new_obj['marin3'] = 'young'
   new_obj['gustavo3'] = None
   new_obj['max3'] = [1, 2, 3, 4]
   new_obj['janet3'] = {'salary': None, 'children': 5}


def add_new_items__edict():
   new_obj = Edict()
   new_obj['joe'] = 123
   new_obj['alex'] = 'old'
   new_obj['marin'] = 'young'
   new_obj['gustavo'] = None
   new_obj['max'] = [1, 2, 3, 4]
   new_obj['janet'] = {'salary': None, 'children': 5}
   new_obj['joe1'] = 123
   new_obj['alex1'] = 'old'
   new_obj['marin1'] = 'young'
   new_obj['gustavo1'] = None
   new_obj['max1'] = [1, 2, 3, 4]
   new_obj['janet1'] = {'salary': None, 'children': 5}
   new_obj['joe2'] = 123
   new_obj['alex2'] = 'old'
   new_obj['marin2'] = 'young'
   new_obj['gustavo2'] = None
   new_obj['max2'] = [1, 2, 3, 4]
   new_obj['janet2'] = {'salary': None, 'children': 5}
   new_obj['joe3'] = 123
   new_obj['alex3'] = 'old'
   new_obj['marin3'] = 'young'
   new_obj['gustavo3'] = None
   new_obj['max3'] = [1, 2, 3, 4]
   new_obj['janet3'] = {'salary': None, 'children': 5}


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   pass

   func_dict = {
      'add_new_items direct {items}': (add_new_items__py_dict_direct, [], {}),
      'add_new_items dict(args) constructor': (add_new_items__py_dict_constructor, [], {}),
      'add_new_items OrderedDict(args)': (add_new_items__py_ordereddict, [], {}),
      'add_new_items Rdict(args)': (add_new_items__rdict, [], {}),
      'add_new_items RdictIO(args)': (add_new_items__rdictio, [], {}),
      'add_new_items__edict Edict(args)': (add_new_items__edict, [], {}),
      # RdictF, RdictFO, RdictFO2 can not add new items after creation
   }

   setup_line_list = [
      'from collections import OrderedDict',
      'from __main__ import OrderedDict, Edict, Rdict, RdictIO',
   ]

   with open('result_output/SpeedCreateAndAddNewItems.txt', 'w') as file_:
      file_.write('\n\n SpeedCreateAndAddNewItems.py output\n\n')
      file_.write(speed_it(func_dict, setup_line_list, use_func_name=True, output_in_sec=False, with_gc=False, rank_by='best', run_sec=1, repeat=3))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()

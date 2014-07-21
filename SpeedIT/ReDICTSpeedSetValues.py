""" SpeedSetValues
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
   RdictF,
   RdictFO,
   RdictIO
)


py_dict_direct_obj = {
   'jack': 4098,
   'aron': {
      'hair': 'brown',
      'eyes': 'blue',
      'interests': {
         'sport': {
            'summer_sport': {
               'tennis': 'good',
               'swimming': 'best'
            },
            'winter_sport': {
               'skating': 'some times'
            }
         },
         'others': ['reading', 'sightseeing']
      }
   }
}

py_dict_constructor_obj = dict(
   jack=4098,
   aron=dict(
      hair='brown',
      eyes='blue',
      interests=dict(
         sport=dict(
            summer_sport=dict(
               tennis='good',
               swimming='best'
            ),
            winter_sport=dict(
               skating='some times'
            )
         ),
         others=['reading', 'sightseeing']
      )
   )
)

py_ordereddict_obj = OrderedDict({
   'jack': 4098,
   'aron': OrderedDict({
      'hair': 'brown',
      'eyes': 'blue',
      'interests': OrderedDict({
         'sport': OrderedDict({
            'summer_sport': OrderedDict({
               'tennis': 'good',
               'swimming': 'best'
            }),
            'winter_sport': OrderedDict({
               'skating': 'some times'
            })
         }),
         'others': ['reading', 'sightseeing']
      })
   })
})

rdict_obj = Rdict(
   jack=4098,
   aron=Rdict(
      hair='brown',
      eyes='blue',
      interests=Rdict(
         sport=Rdict(
            summer_sport=Rdict(
               tennis='good',
               swimming='best'
            ),
            winter_sport=Rdict(
               skating='some times'
            )
         ),
         others=['reading', 'sightseeing']
      )
   )
)

rdictf_obj = RdictF(
   jack=4098,
   aron=RdictF(
      hair='brown',
      eyes='blue',
      interests=RdictF(
         sport=RdictF(
            summer_sport=RdictF(
               tennis='good',
               swimming='best'
            ),
            winter_sport=RdictF(
               skating='some times'
            )
         ),
         others=['reading', 'sightseeing']
      )
   )
)

rdictio_obj = RdictIO([
   ('jack', 4098),
   ('aron', RdictIO([
      ('hair', 'brown'),
      ('eyes', 'blue'),
      ('interests', RdictIO([
         ('sport', RdictIO([
            ('summer_sport', RdictIO([
               ('tennis', 'good'),
               ('swimming', 'best')
            ], False)),
            ('winter_sport', RdictIO([
               ('skating', 'some times')
            ], False))
         ], False)),
         ('others', ['reading', 'sightseeing'])
      ], False))
   ], False))
], False)

rdictfo_obj = RdictFO([
   ('jack', 4098),
   ('aron', RdictFO([
      ('hair', 'brown'),
      ('eyes', 'blue'),
      ('interests', RdictFO([
         ('sport', RdictFO([
            ('summer_sport', RdictFO([
               ('tennis', 'good'),
               ('swimming', 'best')
            ], False)),
            ('winter_sport', RdictFO([
               ('skating', 'some times')
            ], False))
         ], False)),
         ('others', ['reading', 'sightseeing'])
      ], False))
   ], False))
], False)

edict_obj = Edict(
   jack=4098,
   aron=Edict(
      hair='brown',
      eyes='blue',
      interests=Edict(
         sport=Edict(
            summer_sport=Edict(
               tennis='good',
               swimming='best'
            ),
            winter_sport=Edict(
               skating='some times'
            )
         ),
         others=['reading', 'sightseeing']
      )
   )
)


def set_value__py_dict_direct():
   py_dict_direct_obj['jack'] = 12345
   py_dict_direct_obj['aron']['hair'] = 12345
   py_dict_direct_obj['aron']['interests']['sport']['summer_sport']['swimming'] = 12345
   py_dict_direct_obj['aron']['interests']['sport']['winter_sport']['skating'] = 12345
   py_dict_direct_obj['aron']['interests']['others'] = 12345


def set_value__py_dict_constructor():
   py_dict_constructor_obj['jack'] = 12345
   py_dict_constructor_obj['aron']['hair'] = 12345
   py_dict_constructor_obj['aron']['interests']['sport']['summer_sport']['swimming'] = 12345
   py_dict_constructor_obj['aron']['interests']['sport']['winter_sport']['skating'] = 12345
   py_dict_constructor_obj['aron']['interests']['others'] = 12345


def set_value__py_ordereddict():
   py_ordereddict_obj['jack'] = 12345
   py_ordereddict_obj['aron']['hair'] = 12345
   py_ordereddict_obj['aron']['interests']['sport']['summer_sport']['swimming'] = 12345
   py_ordereddict_obj['aron']['interests']['sport']['winter_sport']['skating'] = 12345
   py_ordereddict_obj['aron']['interests']['others'] = 12345


def set_value__rdict():
   rdict_obj['jack'] = 12345
   rdict_obj['aron']['hair'] = 12345
   rdict_obj['aron']['interests']['sport']['summer_sport']['swimming'] = 12345
   rdict_obj['aron']['interests']['sport']['winter_sport']['skating'] = 12345
   rdict_obj['aron']['interests']['others'] = 12345


def set_value__rdictf():
   rdictf_obj['jack'] = 12345
   rdictf_obj['aron']['hair'] = 12345
   rdictf_obj['aron']['interests']['sport']['summer_sport']['swimming'] = 12345
   rdictf_obj['aron']['interests']['sport']['winter_sport']['skating'] = 12345
   rdictf_obj['aron']['interests']['others'] = 12345


def set_value__rdictio():
   rdictio_obj['jack'] = 12345
   rdictio_obj['aron']['hair'] = 12345
   rdictio_obj['aron']['interests']['sport']['summer_sport']['swimming'] = 12345
   rdictio_obj['aron']['interests']['sport']['winter_sport']['skating'] = 12345
   rdictio_obj['aron']['interests']['others'] = 12345


def set_value__rdictfo():
   rdictfo_obj['jack'] = 12345
   rdictfo_obj['aron']['hair'] = 12345
   rdictfo_obj['aron']['interests']['sport']['summer_sport']['swimming'] = 12345
   rdictfo_obj['aron']['interests']['sport']['winter_sport']['skating'] = 12345
   rdictfo_obj['aron']['interests']['others'] = 12345


def set_value__edict():
   edict_obj['jack'] = 12345
   edict_obj['aron']['hair'] = 12345
   edict_obj['aron']['interests']['sport']['summer_sport']['swimming'] = 12345
   edict_obj['aron']['interests']['sport']['winter_sport']['skating'] = 12345
   edict_obj['aron']['interests']['others'] = 12345


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   pass

   func_dict = {
      'set_value direct {items}': (set_value__py_dict_direct, [], {}),
      'set_value dict(args) constructor': (set_value__py_dict_constructor, [], {}),
      'set_value OrderedDict(args)': (set_value__py_ordereddict, [], {}),
      'set_value by key Rdict(args)': (set_value__rdict, [], {}),
      'set_value by key RdictF(args)': (set_value__rdictf, [], {}),
      'set_value by key RdictIO(key_value_list)': (set_value__rdictio, [], {}),
      'set_value by key RdictFO(key_value_list)': (set_value__rdictfo, [], {}),
      'set_value by key Edict(args)': (set_value__edict, [], {}),
      # RdictFO2 can not set Values
   }

   setup_line_list = [
      'from collections import OrderedDict',
      'from __main__ import py_dict_direct_obj, py_dict_constructor_obj, py_ordereddict_obj, rdict_obj, rdictf_obj, rdictio_obj, rdictfo_obj, edict_obj',
   ]

   with open('result_output/SpeedSetValues.txt', 'w') as file_:
      file_.write('\n\n SpeedSetValues.py output\n\n')
      file_.write(speed_it(func_dict, setup_line_list, use_func_name=True, output_in_sec=False, with_gc=False, rank_by='best', run_sec=1, repeat=3))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()

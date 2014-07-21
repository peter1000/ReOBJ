""" SpeedAccessValues
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
   RdictFO2,
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

rdictfo2_obj = RdictFO2([
   ('jack', 4098),
   ('aron', RdictFO2([
      ('hair', 'brown'),
      ('eyes', 'blue'),
      ('interests', RdictFO2([
         ('sport', RdictFO2([
            ('summer_sport', RdictFO2([
               ('tennis', 'good'),
               ('swimming', 'best')
            ], False)),
            ('winter_sport', RdictFO2([
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


def access_value__py_dict_direct():
   dummy = py_dict_direct_obj['jack']
   dummy = py_dict_direct_obj['aron']['hair']
   dummy = py_dict_direct_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_dict_direct_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_dict_direct_obj['aron']['interests']['others']
   dummy = py_dict_direct_obj['jack']
   dummy = py_dict_direct_obj['aron']['hair']
   dummy = py_dict_direct_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_dict_direct_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_dict_direct_obj['aron']['interests']['others']
   dummy = py_dict_direct_obj['jack']
   dummy = py_dict_direct_obj['aron']['hair']
   dummy = py_dict_direct_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_dict_direct_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_dict_direct_obj['aron']['interests']['others']


def access_value__py_dict_constructor():
   dummy = py_dict_constructor_obj['jack']
   dummy = py_dict_constructor_obj['aron']['hair']
   dummy = py_dict_constructor_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_dict_constructor_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_dict_constructor_obj['aron']['interests']['others']
   dummy = py_dict_constructor_obj['jack']
   dummy = py_dict_constructor_obj['aron']['hair']
   dummy = py_dict_constructor_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_dict_constructor_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_dict_constructor_obj['aron']['interests']['others']
   dummy = py_dict_constructor_obj['jack']
   dummy = py_dict_constructor_obj['aron']['hair']
   dummy = py_dict_constructor_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_dict_constructor_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_dict_constructor_obj['aron']['interests']['others']


def access_value__py_ordereddict():
   dummy = py_ordereddict_obj['jack']
   dummy = py_ordereddict_obj['aron']['hair']
   dummy = py_ordereddict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_ordereddict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_ordereddict_obj['aron']['interests']['others']
   dummy = py_ordereddict_obj['jack']
   dummy = py_ordereddict_obj['aron']['hair']
   dummy = py_ordereddict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_ordereddict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_ordereddict_obj['aron']['interests']['others']
   dummy = py_ordereddict_obj['jack']
   dummy = py_ordereddict_obj['aron']['hair']
   dummy = py_ordereddict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = py_ordereddict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = py_ordereddict_obj['aron']['interests']['others']


def access_value__rdict():
   dummy = rdict_obj['jack']
   dummy = rdict_obj['aron']['hair']
   dummy = rdict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdict_obj['aron']['interests']['others']
   dummy = rdict_obj['jack']
   dummy = rdict_obj['aron']['hair']
   dummy = rdict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdict_obj['aron']['interests']['others']
   dummy = rdict_obj['jack']
   dummy = rdict_obj['aron']['hair']
   dummy = rdict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdict_obj['aron']['interests']['others']


def access_value__rdictf():
   dummy = rdictf_obj['jack']
   dummy = rdictf_obj['aron']['hair']
   dummy = rdictf_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictf_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictf_obj['aron']['interests']['others']
   dummy = rdictf_obj['jack']
   dummy = rdictf_obj['aron']['hair']
   dummy = rdictf_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictf_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictf_obj['aron']['interests']['others']
   dummy = rdictf_obj['jack']
   dummy = rdictf_obj['aron']['hair']
   dummy = rdictf_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictf_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictf_obj['aron']['interests']['others']


def access_value__rdictio():
   dummy = rdictio_obj['jack']
   dummy = rdictio_obj['aron']['hair']
   dummy = rdictio_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictio_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictio_obj['aron']['interests']['others']
   dummy = rdictio_obj['jack']
   dummy = rdictio_obj['aron']['hair']
   dummy = rdictio_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictio_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictio_obj['aron']['interests']['others']
   dummy = rdictio_obj['jack']
   dummy = rdictio_obj['aron']['hair']
   dummy = rdictio_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictio_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictio_obj['aron']['interests']['others']


def access_value__rdictfo():
   dummy = rdictfo_obj['jack']
   dummy = rdictfo_obj['aron']['hair']
   dummy = rdictfo_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictfo_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictfo_obj['aron']['interests']['others']
   dummy = rdictfo_obj['jack']
   dummy = rdictfo_obj['aron']['hair']
   dummy = rdictfo_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictfo_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictfo_obj['aron']['interests']['others']
   dummy = rdictfo_obj['jack']
   dummy = rdictfo_obj['aron']['hair']
   dummy = rdictfo_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictfo_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictfo_obj['aron']['interests']['others']


def access_value__rdictfo2():
   dummy = rdictfo2_obj['jack']
   dummy = rdictfo2_obj['aron']['hair']
   dummy = rdictfo2_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictfo2_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictfo2_obj['aron']['interests']['others']
   dummy = rdictfo2_obj['jack']
   dummy = rdictfo2_obj['aron']['hair']
   dummy = rdictfo2_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictfo2_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictfo2_obj['aron']['interests']['others']
   dummy = rdictfo2_obj['jack']
   dummy = rdictfo2_obj['aron']['hair']
   dummy = rdictfo2_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = rdictfo2_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = rdictfo2_obj['aron']['interests']['others']


def access_value__edict():
   dummy = edict_obj['jack']
   dummy = edict_obj['aron']['hair']
   dummy = edict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = edict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = edict_obj['aron']['interests']['others']
   dummy = edict_obj['jack']
   dummy = edict_obj['aron']['hair']
   dummy = edict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = edict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = edict_obj['aron']['interests']['others']
   dummy = edict_obj['jack']
   dummy = edict_obj['aron']['hair']
   dummy = edict_obj['aron']['interests']['sport']['summer_sport']['swimming']
   dummy = edict_obj['aron']['interests']['sport']['winter_sport']['skating']
   dummy = edict_obj['aron']['interests']['others']


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   pass

   func_dict = {
      'access_value direct {items}': (access_value__py_dict_direct, [], {}),
      'access_value dict(args) constructor': (access_value__py_dict_constructor, [], {}),
      'access_value OrderedDict(args)': (access_value__py_ordereddict, [], {}),
      'access_value by key Rdict(args)': (access_value__rdict, [], {}),
      'access_value bey key RdictF(args)': (access_value__rdictf, [], {}),
      'access_value by key RdictIO(key_value_list)': (access_value__rdictio, [], {}),
      'access_value by key RdictFO(key_value_list)': (access_value__rdictfo, [], {}),
      'access_value by key RdictFO2(key_value_list)': (access_value__rdictfo2, [], {}),
      'access_value by key Edict(args)': (access_value__edict, [], {}),
   }

   setup_line_list = [
      'from collections import OrderedDict',
      'from __main__ import py_dict_direct_obj, py_dict_constructor_obj, py_ordereddict_obj, rdict_obj, rdictf_obj, rdictio_obj, rdictfo_obj, rdictfo2_obj, edict_obj',
   ]

   with open('result_output/SpeedAccessValues.txt', 'w') as file_:
      file_.write('\n\n SpeedAccessValues.py output\n\n')
      file_.write(speed_it(func_dict, setup_line_list, use_func_name=True, output_in_sec=False, with_gc=False, rank_by='best', run_sec=1, repeat=3))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()

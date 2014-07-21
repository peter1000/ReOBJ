""" ReDICTSpeedCreateInitialize
"""
from collections import (
   OrderedDict,
   namedtuple,
   UserDict
)

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
   RdictIO,
   RdictFO,
   RdictFO2,
)


def init__py_dict_direct():
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


def init__py_dict_constructor():
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


def init__py_dict_constructor_key_value_list():
   py_dict_constructor_key_value_list = dict([
      ('jack', 4098),
      ('aron', dict([
         ('hair', 'brown'),
         ('eyes', 'blue'),
         ('interests', dict([
            ('sport', dict([
               ('summer_sport', dict([
                  ('tennis', 'good'),
                  ('swimming', 'best')
               ])),
               ('winter_sport', dict([
                  ('skating', 'some times')
               ]))
            ])),
            ('others', ['reading', 'sightseeing'])
         ]))
      ]))
   ])


def init__py_ordereddict():
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


def init__py_ordereddict_key_value_list():
   py_ordereddict_key_value_list = OrderedDict([
      ('jack', 4098),
      ('aron', OrderedDict([
         ('hair', 'brown'),
         ('eyes', 'blue'),
         ('interests', OrderedDict([
            ('sport', OrderedDict([
               ('summer_sport', OrderedDict([
                  ('tennis', 'good'),
                  ('swimming', 'best')
               ])),
               ('winter_sport', OrderedDict([
                  ('skating', 'some times')
               ]))
            ])),
            ('others', ['reading', 'sightseeing'])
         ]))
      ]))
   ])


def init__edict():
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


def init__edict_key_value_list():
   edict_key_value_list = Edict([
      ('jack', 4098),
      ('aron', Edict([
         ('hair', 'brown'),
         ('eyes', 'blue'),
         ('interests', Edict([
            ('sport', Edict([
               ('summer_sport', Edict([
                  ('tennis', 'good'),
                  ('swimming', 'best')
               ])),
               ('winter_sport', Edict([
                  ('skating', 'some times')
               ]))
            ])),
            ('others', ['reading', 'sightseeing'])
         ]))
      ]))
   ])


def init__userdict():
   userdict_obj = UserDict(
      jack=4098,
      aron=UserDict(
         hair='brown',
         eyes='blue',
         interests=UserDict(
            sport=UserDict(
               summer_sport=UserDict(
                  tennis='good',
                  swimming='best'
               ),
               winter_sport=UserDict(
                  skating='some times'
               )
            ),
            others=['reading', 'sightseeing']
         )
      )
   )


def init__userdict_key_value_list():
   userdict_key_value_list = UserDict([
      ('jack', 4098),
      ('aron', UserDict([
         ('hair', 'brown'),
         ('eyes', 'blue'),
         ('interests', UserDict([
            ('sport', UserDict([
               ('summer_sport', UserDict([
                  ('tennis', 'good'),
                  ('swimming', 'best')
               ])),
               ('winter_sport', UserDict([
                  ('skating', 'some times')
               ]))
            ])),
            ('others', ['reading', 'sightseeing'])
         ]))
      ]))
   ])


def init__namedtuple():
   namedtuple_obj = namedtuple('example', ['jack', 'aron'])(
      4098,
      namedtuple('example', ['hair', 'eyes', 'interests'])(
         'brown',
         'blue',
         namedtuple('example', ['sport', 'others'])(
            namedtuple('example', ['summer_sport', 'winter_sport'])(
               namedtuple('example', ['tennis', 'swimming'])(
                  'good',
                  'best'
               ),
               namedtuple('example', ['skating'])(
                  'some times'
               ),
            ),
            ['reading', 'sightseeing']
         ),
      ),
   )


def init__rdict():
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


def init__rdict_key_value_list():
   rdict_key_value_list = Rdict([
      ('jack', 4098),
      ('aron', Rdict([
         ('hair', 'brown'),
         ('eyes', 'blue'),
         ('interests', Rdict([
            ('sport', Rdict([
               ('summer_sport', Rdict([
                  ('tennis', 'good'),
                  ('swimming', 'best')
               ])),
               ('winter_sport', Rdict([
                  ('skating', 'some times')
               ]))
            ])),
            ('others', ['reading', 'sightseeing'])
         ]))
      ]))
   ])


def init__rdictf():
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


def init__rdictf_key_value_list():
   rdictf_key_value_list = RdictF([
      ('jack', 4098),
      ('aron', RdictF([
         ('hair', 'brown'),
         ('eyes', 'blue'),
         ('interests', RdictF([
            ('sport', RdictF([
               ('summer_sport', RdictF([
                  ('tennis', 'good'),
                  ('swimming', 'best')
               ])),
               ('winter_sport', RdictF([
                  ('skating', 'some times')
               ]))
            ])),
            ('others', ['reading', 'sightseeing'])
         ]))
      ]))
   ])


def init__rdictio_key_value_list():
   rdictio_key_value_list = RdictIO([
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


def init__rdictio_key_value_list_use_tuple():
   rdictio_key_value_list_use_tuple = RdictIO([
      ('jack', 4098),
      ('aron', RdictIO([
         ('hair', 'brown'),
         ('eyes', 'blue'),
         ('interests', RdictIO([
            ('sport', RdictIO([
               ('summer_sport', RdictIO([
                  ('tennis', 'good'),
                  ('swimming', 'best')
               ], True)),
               ('winter_sport', RdictIO([
                  ('skating', 'some times')
               ], True))
            ], True)),
            ('others', ['reading', 'sightseeing'])
         ], True))
      ], True))
   ], True)


def init__rdictio_three_values():
   rdictio_three_values = RdictIO([
      ('jack', 4098, 1),
      ('aron', RdictIO([
         ('hair', 'brown', 1),
         ('eyes', 'blue', 1),
         ('interests', RdictIO([
            ('sport', RdictIO([
               ('summer_sport', RdictIO([
                  ('tennis', 'good', 1),
                  ('swimming', 'best', 1),
               ], True), 1),
               ('winter_sport', RdictIO([
                  ('skating', 'some times', 1),
               ], True), 1)
            ], True), 1),
            ('others', ['reading', 'sightseeing'], 1),
         ], True), 1),
      ], True), 1),
   ], True)


def init__rdictfo_key_value_list():
   rdictfo_key_value_list = RdictFO([
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


def init__rdictfo2_key_value_list():
   rdictfo2_key_value_list = RdictFO2([
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


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   pass

   func_dict = {
      'init direct {items}': (init__py_dict_direct, [], {}),
      'init dict(args) constructor': (init__py_dict_constructor, [], {}),
      'init dict(key_value_list) constructor ': (init__py_dict_constructor_key_value_list, [], {}),
      'init OrderedDict(args)': (init__py_ordereddict, [], {}),
      'init OrderedDict(key_value_list)': (init__py_ordereddict_key_value_list, [], {}),
      'init UserDict(args) constructor': (init__userdict, [], {}),
      'init UserDict(key_value_list) constructor ': (init__userdict_key_value_list, [], {}),
      'init namedtuple ': (init__namedtuple, [], {}),
      'init Rdict(args)': (init__rdict, [], {}),
      'init Rdict(key_value_list)': (init__rdict_key_value_list, [], {}),
      'init Edict(args)': (init__edict, [], {}),
      'init Edict(key_value_list)': (init__edict_key_value_list, [], {}),
      'init RdictF(args)': (init__rdictf, [], {}),
      'init RdictF(key_value_list)': (init__rdictf_key_value_list, [], {}),
      'init RdictIO(key_value_list)': (init__rdictio_key_value_list, [], {}),
      'init RdictIO(key_value_list) use_tuple_values': (init__rdictio_key_value_list_use_tuple, [], {}),
      'init RdictIO(key_value_list) use_tuple_values three_values': (init__rdictio_three_values, [], {}),
      'init RdictFO(key_value_list)': (init__rdictfo_key_value_list, [], {}),
      'init RdictFO2(key_value_list)': (init__rdictfo2_key_value_list, [], {}),
   }

   setup_line_list = [
      'from collections import OrderedDict, UserDict, namedtuple',
      'from ReOBJ.MainCode import Edict, Rdict, RdictF, RdictIO, RdictFO, RdictFO2',
   ]

   with open('result_output/ReDICTSpeedCreateInitialize.txt', 'w') as file_:
      file_.write('\n\n ReDICTSpeedCreateInitialize.py output\n\n')
      file_.write(speed_it(func_dict, setup_line_list, use_func_name=True, output_in_sec=False, with_gc=False, rank_by='best', run_sec=1, repeat=3))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()

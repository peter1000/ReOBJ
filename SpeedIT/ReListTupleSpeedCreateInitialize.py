""" ReListTupleSpeedCreateInitialize
"""
from collections import UserList

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
   Elist,
   Rlist,
   RlistF,
   Etuple,
)


def init__py_list_direct():
   py_list_direct_obj = [4098,
      ["brown", "blue",
         [
            [
               ["good", "best"],
               "some times"
            ],
            ["reading", "sightseeing"]
         ]
      ]
   ]


def init__py_list_constructor():
   py_list_constructor_obj = list([4098,
      list(["brown", "blue",
         list([
            list([
               list(["good", "best"]),
               "some times"
            ]),
            list(["reading", "sightseeing"])
         ])
      ])
   ])


def init__py_tuple_direct():
   py_tuple_direct_obj = (4098,
      ("brown", "blue",
         (
            (
               ("good", "best"),
               "some times"
            ),
            ["reading", "sightseeing"],
         )
      )
   )


def init__py_tuple_constructor():
   py_tuple_constructor_obj = tuple((4098,
      tuple(("brown", "blue",
         tuple((
            tuple((
               tuple(("good", "best")),
               "some times"
            )),
            tuple(["reading", "sightseeing"],)
         ))
      ))
   ))


def init__userlist_constructor():
   userlist_constructor_obj = UserList([4098,
      UserList(["brown", "blue",
         UserList([
            UserList([
               UserList(["good", "best"]),
               "some times"
            ]),
            UserList(["reading", "sightseeing"])
         ])
      ])
   ])


def init__elist_constructor():
   elist_constructor_obj = Elist([4098,
      Elist(["brown", "blue",
         Elist([
            Elist([
               Elist(["good", "best"]),
               "some times"
            ]),
            Elist(["reading", "sightseeing"])
         ])
      ])
   ])


def init__elist_constructor_with_tuple():
   elist_constructor_obj = Elist((4098,
      Elist(("brown", "blue",
         Elist((
            Elist((
               Elist(("good", "best")),
               "some times"
            )),
            Elist((["reading", "sightseeing"],))
         ))
      ))
   ))


def init__rlist_constructor():
   rlist_constructor_obj = Rlist([4098,
      Rlist(["brown", "blue",
         Rlist([
            Rlist([
               Rlist(["good", "best"]),
               "some times"
            ]),
            Rlist(["reading", "sightseeing"])
         ])
      ])
   ])


def init__rlistf_constructor():
   rlistf_constructor_obj = RlistF([4098,
      RlistF(["brown", "blue",
         RlistF([
            RlistF([
               RlistF(["good", "best"]),
               "some times"
            ]),
            RlistF(["reading", "sightseeing"])
         ])
      ])
   ])


def init__etuple_constructor():
   etuple_constructor_obj = Etuple([4098,
      Etuple(["brown", "blue",
         Etuple([
            Etuple([
               Etuple(["good", "best"]),
               "some times"
            ]),
            Etuple(["reading", "sightseeing"],)
         ])
      ])
   ])


def init__etuple_constructor_with_tuple():
   etuple_constructor_with_tuple_obj = Etuple((4098,
      Etuple(("brown", "blue",
         Etuple((
            Etuple((
               Etuple(("good", "best")),
               "some times"
            )),
            Etuple((["reading", "sightseeing"],))
         ))
      ))
   ))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   pass

   func_dict = {
      'init__py_list_direct': (init__py_list_direct, [], {}),
      'init__py_list_constructor': (init__py_list_constructor, [], {}),
      'init__py_tuple_direct': (init__py_tuple_direct, [], {}),
      'init__py_tuple_constructor': (init__py_tuple_constructor, [], {}),
      'init__userlist_constructor': (init__userlist_constructor, [], {}),
      'init__elist_constructor': (init__elist_constructor, [], {}),
      'init__elist_constructor_with_tuple': (init__elist_constructor_with_tuple, [], {}),
      'init__rlistf_constructor': (init__rlistf_constructor, [], {}),
      'init__etuple_constructor': (init__etuple_constructor, [], {}),
      'init__etuple_constructor_with_tuple': (init__etuple_constructor_with_tuple, [], {}),
   }

   setup_line_list = [
      'from collections import UserList',
      'from ReOBJ.MainCode import Elist, Rlist, RlistF, Etuple',
   ]

   with open('result_output/ReListTupleSpeedCreateInitialize.txt', 'w') as file_:
      file_.write('\n\n ReListTupleSpeedCreateInitialize.py output\n\n')
      file_.write(speed_it(func_dict, setup_line_list, use_func_name=True, output_in_sec=False, with_gc=False, rank_by='best', run_sec=1, repeat=3))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()

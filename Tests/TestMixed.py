""" tests ReOBJ  Classes
"""
from collections import OrderedDict
from inspect import (
   getfile,
   currentframe
)
from json import (
   dumps as jdumps,
   loads as jloads
)
from os.path import (
   abspath,
   dirname,
   join
)
from pickle import (
   dumps as pdumps,
   loads as ploads
)
from sys import path as syspath

from nose.tools import (
   ok_
)


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
   Elist,
   Rlist,
   RlistF,
   Etuple,
   Lmatrix,
   LmatrixF
)


def _get_orig__edict_with_all():
   """ Helper
   """
   edict_with_all = Edict({
      'pydict1': dict({
         'pydict_inner1': 'pydict_inner1 value',
         'pydict_inner2': 'pydict_inner2 value',
         'pydict_inner3': 'pydict_inner3 value',
      }),
      'pylist1': list([
         'pylist_inner value1',
         'pylist_inner value2',
         'pylist_inner value3',
      ]),
      'pytuple1': tuple((
         'pytuple_inner value1',
         'pytuple_inner value2',
         'pytuple_inner value3',
      )),
      'edict1': Edict(
         pydict1_edict_inner1='edict_inner1 value',
         pydict1_edict_inner2='edict_inner2 value',
         pydict1_edict_inner3='edict_inner3 value',
      ),
      'rdict1': Rdict(
         pydict1_rdict_inner1='rdict_inner1 value',
         pydict1_rdict_inner2='rdict_inner2 value',
         pydict1_rdict_inner3='rdict_inner3 value',
      ),
      'edictf1': RdictF(
         pydict1_edictf_inner1='edictf_inner1 value',
         pydict1_edictf_inner2='edictf_inner2 value',
         pydict1_edictf_inner3='edictf_inner3 value',
      ),
      'edictio1': RdictIO([
         ('edictio_inner1', 'edictio_inner1 value'),
         ('edictio_inner2', 'edictio_inner2 value'),
         ('edictio_inner3', 'edictio_inner3 value'),
      ], False),
      'edictfo1': RdictFO([
         ('edictfo_inner1', 'edictfo_inner1 value'),
         ('edictfo_inner2', 'edictfo_inner2 value'),
         ('edictfo_inner3', 'edictfo_inner3 value'),
      ], False),
      'edictfo2_1': RdictFO2([
         ('edictfo2_inner1', 'edictfo2_inner1 value'),
         ('edictfo2_inner2', 'edictfo2_inner2 value'),
         ('edictfo2_inner3', 'edictfo2__inner3 value'),
      ], False),
      'elist1': Elist([
         'elist_inner value1',
         'elist_inner value2',
         'elist_inner value3',
      ]),
      'rlist1': Rlist([
         'rlist_inner value1',
         'rlist_inner value2',
         'rlist_inner value3',
      ]),
      'rlistf1': RlistF([
         'rlistf_inner value1',
         'rlistf_inner value2',
         'rlistf_inner value3',
      ]),
      'etuple1': Etuple([
         'etuple_inner value1',
         'etuple_inner value2',
         'etuple_inner value3',
      ]),
      'lmatrix1': Lmatrix(('name', 'red', 'green', 'blue'), [
         ('lavender', 230, 230, 250),
         ('steelblue', 70, 130, 180),
         ('lawngreen ', 124, 252, 0),
      ]),
      'lmatrixf1': LmatrixF(('name', 'red', 'green', 'blue'), [
         ('darkorange', 255, 140, 0),
         ('flesh', 255, 125, 64),
         ('firebrick 3', 205, 38, 38),
      ]),
   })

   # Set extra info
   edict_with_all.set_extra_data('INFO', 'edict_obj with all directly supported other types')
   edict_with_all.update_extra_data({'edict extra1': 'edict extra_value1', 'edict extra2': 'edict extra_value2', 'edict extra3': 'edict extra_value3'})

   edict_with_all['edict1'].set_extra_data('INFO', 'edict_obj.edict1 inner')
   edict_with_all['edict1'].update_extra_data({'edict_obj.edict1 extra1': 'edict_obj.edict1 extra_value1', 'edict_obj.edict1 extra2': 'edict_obj.edict1 extra_value2', 'edict_obj.edict1 extra3': 'edict_obj.edict1 extra_value3'})

   edict_with_all['rdict1'].set_extra_data('INFO', 'edict_obj.rdict1 inner')
   edict_with_all['rdict1'].update_extra_data({'edict_obj.rdict1 extra1': 'edict_obj.rdict1 extra_value1', 'edict_obj.rdict1 extra2': 'edict_obj.rdict1 extra_value2', 'edict_obj.rdict1 extra3': 'edict_obj.rdict1 extra_value3'})

   edict_with_all['edictf1'].set_extra_data('INFO', 'edict_obj.edictf1 inner')
   edict_with_all['edictf1'].update_extra_data({'edict_obj.edictf1 extra1': 'edict_obj.edictf1 extra_value1', 'edict_obj.edictf1 extra2': 'edict_obj.edictf1 extra_value2', 'edict_obj.edictf1 extra3': 'edict_obj.edictf1 extra_value3'})

   edict_with_all['edictio1'].set_extra_data('INFO', 'edict_obj.edictio1 inner')
   edict_with_all['edictio1'].update_extra_data({'edict_obj.edictio1 extra1': 'edict_obj.edictio1 extra_value1', 'edict_obj.edictio1 extra2': 'edict_obj.edictio1 extra_value2', 'edict_obj.edictio1 extra3': 'edict_obj.edictio1 extra_value3'})

   edict_with_all['edictfo1'].set_extra_data('INFO', 'edict_obj.edictfo1 inner')
   edict_with_all['edictfo1'].update_extra_data({'edict_obj.edictfo1 extra1': 'edict_obj.edictfo1 extra_value1', 'edict_obj.edictfo1 extra2': 'edict_obj.edictfo1 extra_value2', 'edict_obj.edictfo1 extra3': 'edict_obj.edictfo1 extra_value3'})

   edict_with_all['edictfo2_1'].set_extra_data('INFO', 'edict_obj.edictfo2_1 inner')
   edict_with_all['edictfo2_1'].update_extra_data({'edict_obj.edictfo2_1 extra1': 'edict_obj.edictfo2_1 extra_value1', 'edict_obj.edictfo2_1 extra2': 'edict_obj.edictfo2_1 extra_value2', 'edict_obj.edictfo2_1 extra3': 'edict_obj.edictfo2_1 extra_value3'})

   edict_with_all['elist1'].set_extra_data('INFO', 'edict_obj.elist1 inner')
   edict_with_all['elist1'].update_extra_data({'edict_obj.elist1 extra1': 'edict_obj.elist1 extra_value1', 'edict_obj.elist1 extra2': 'edict_obj.elist1 extra_value2', 'edict_obj.elist1 extra3': 'edict_obj.elist1 extra_value3'})

   edict_with_all['rlist1'].set_extra_data('INFO', 'edict_obj.rlist1 inner')
   edict_with_all['rlist1'].update_extra_data({'edict_obj.rlist1 extra1': 'edict_obj.rlist1 extra_value1', 'edict_obj.rlist1 extra2': 'edict_obj.rlist1 extra_value2', 'edict_obj.rlist1 extra3': 'edict_obj.rlist1 extra_value3'})

   edict_with_all['rlistf1'].set_extra_data('INFO', 'edict_obj.rlistf1 inner')
   edict_with_all['rlistf1'].update_extra_data({'edict_obj.rlistf1 extra1': 'edict_obj.rlistf1 extra_value1', 'edict_obj.rlistf1 extra2': 'edict_obj.rlistf1 extra_value2', 'edict_obj.rlistf1 extra3': 'edict_obj.rlistf1 extra_value3'})

   edict_with_all['etuple1'].set_extra_data('INFO', 'edict_obj.etuple1 inner')
   edict_with_all['etuple1'].update_extra_data({'edict_obj.etuple1 extra1': 'edict_obj.etuple1 extra_value1', 'edict_obj.etuple1 extra2': 'edict_obj.etuple1 extra_value2', 'edict_obj.etuple1 extra3': 'edict_obj.etuple1 extra_value3'})

   edict_with_all['lmatrix1'].set_extra_data('INFO', 'edict_obj.lmatrix1 inner')
   edict_with_all['lmatrix1'].update_extra_data({'edict_obj.lmatrix1 extra1': 'edict_obj.lmatrix1 extra_value1', 'edict_obj.lmatrix1 extra2': 'edict_obj.lmatrix1 extra_value2', 'edict_obj.lmatrix1 extra3': 'edict_obj.lmatrix1 extra_value3'})

   edict_with_all['lmatrixf1'].set_extra_data('INFO', 'edict_obj.lmatrixf1 inner')
   edict_with_all['lmatrixf1'].update_extra_data({'edict_obj.lmatrixf1 extra1': 'edict_obj.lmatrixf1 extra_value1', 'edict_obj.lmatrixf1 extra2': 'edict_obj.lmatrixf1 extra_value2', 'edict_obj.lmatrixf1 extra3': 'edict_obj.lmatrixf1 extra_value3'})

   # Set for supported classes: extra_key_value_order
   edict_with_all['edictio1'].appendto_extra_key_value_order('edictio_inner1')  # just testing
   edict_with_all['edictio1'].replace_extra_key_order(['edictio_inner2', 'edictio_inner3', 'edictio_inner1'])

   edict_with_all['edictfo1'].appendto_extra_key_value_order('edictfo_inner1')  # just testing
   edict_with_all['edictfo1'].replace_extra_key_order(['edictfo_inner2', 'edictfo_inner3', 'edictfo_inner1'])

   edict_with_all['edictfo2_1'].appendto_extra_key_value_order('edictfo2_inner1')  # just testing
   edict_with_all['edictfo2_1'].replace_extra_key_order(['edictfo2_inner2', 'edictfo2_inner3', 'edictfo2_inner1'])

   return edict_with_all


def test_edict__copy_recursively():
   """ Tests: test_edict__copy_recursively
   """
   print('::: TEST: test_edict__copy_recursively()')
   edict_with_all = _get_orig__edict_with_all()
   new_reobj_all = edict_with_all.copy_recursively()

   ok_(edict_with_all == new_reobj_all, msg=None)
   ok_(isinstance(new_reobj_all, Edict), msg=None)
   ok_(edict_with_all.extra_data == new_reobj_all.extra_data, msg=None)
   ok_(new_reobj_all.extra_data['edict extra2'] == 'edict extra_value2', msg=None)

   ok_(edict_with_all['edict1'] == new_reobj_all['edict1'], msg=None)
   ok_(isinstance(new_reobj_all['edict1'], Edict), msg=None)
   ok_(edict_with_all['edict1'].extra_data == new_reobj_all['edict1'].extra_data, msg=None)
   ok_(new_reobj_all['edict1'].extra_data['edict_obj.edict1 extra2'] == 'edict_obj.edict1 extra_value2', msg=None)

   ok_(edict_with_all['rdict1'] == new_reobj_all['rdict1'], msg=None)
   ok_(isinstance(new_reobj_all['rdict1'], Rdict), msg=None)
   ok_(edict_with_all['rdict1'].extra_data == new_reobj_all['rdict1'].extra_data, msg=None)
   ok_(new_reobj_all['rdict1'].extra_data['edict_obj.rdict1 extra2'] == 'edict_obj.rdict1 extra_value2', msg=None)

   ok_(edict_with_all['edictf1'] == new_reobj_all['edictf1'], msg=None)
   ok_(isinstance(new_reobj_all['edictf1'], RdictF), msg=None)
   ok_(edict_with_all['edictf1'].extra_data == new_reobj_all['edictf1'].extra_data, msg=None)
   ok_(new_reobj_all['edictf1'].extra_data['edict_obj.edictf1 extra2'] == 'edict_obj.edictf1 extra_value2', msg=None)

   ok_(edict_with_all['edictio1'] == new_reobj_all['edictio1'], msg=None)
   ok_(isinstance(new_reobj_all['edictio1'], RdictIO), msg=None)
   ok_(edict_with_all['edictio1'].extra_data == new_reobj_all['edictio1'].extra_data, msg=None)
   ok_(new_reobj_all['edictio1'].extra_data['edict_obj.edictio1 extra2'] == 'edict_obj.edictio1 extra_value2', msg=None)
   ok_(edict_with_all['edictio1'].key_order == new_reobj_all['edictio1'].key_order, msg=None)
   ok_(new_reobj_all['edictio1'].key_order == ['edictio_inner1', 'edictio_inner2', 'edictio_inner3'], msg=None)
   ok_(edict_with_all['edictio1'].extra_key_order == new_reobj_all['edictio1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictio1'].extra_key_order == ['edictio_inner2', 'edictio_inner3', 'edictio_inner1'], msg=None)

   ok_(edict_with_all['edictfo1'] == new_reobj_all['edictfo1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo1'], RdictFO), msg=None)
   ok_(edict_with_all['edictfo1'].extra_data == new_reobj_all['edictfo1'].extra_data, msg=None)
   ok_(new_reobj_all['edictfo1'].extra_data['edict_obj.edictfo1 extra2'] == 'edict_obj.edictfo1 extra_value2', msg=None)
   ok_(edict_with_all['edictfo1'].key_order == new_reobj_all['edictfo1'].key_order, msg=None)
   ok_(new_reobj_all['edictfo1'].key_order == ['edictfo_inner1', 'edictfo_inner2', 'edictfo_inner3'], msg=None)
   ok_(edict_with_all['edictfo1'].extra_key_order == new_reobj_all['edictfo1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictfo1'].extra_key_order == ['edictfo_inner2', 'edictfo_inner3', 'edictfo_inner1'], msg=None)

   ok_(edict_with_all['edictfo2_1'] == new_reobj_all['edictfo2_1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo2_1'], RdictFO2), msg=None)
   ok_(edict_with_all['edictfo2_1'].extra_data == new_reobj_all['edictfo2_1'].extra_data, msg=None)
   ok_(new_reobj_all['edictfo2_1'].extra_data['edict_obj.edictfo2_1 extra2'] == 'edict_obj.edictfo2_1 extra_value2', msg=None)
   ok_(edict_with_all['edictfo2_1'].key_order == new_reobj_all['edictfo2_1'].key_order, msg=None)
   ok_(new_reobj_all['edictfo2_1'].key_order == ['edictfo2_inner1', 'edictfo2_inner2', 'edictfo2_inner3'], msg=None)
   ok_(edict_with_all['edictfo2_1'].extra_key_order == new_reobj_all['edictfo2_1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictfo2_1'].extra_key_order == ['edictfo2_inner2', 'edictfo2_inner3', 'edictfo2_inner1'], msg=None)

   ok_(edict_with_all['elist1'] == new_reobj_all['elist1'], msg=None)
   ok_(isinstance(new_reobj_all['elist1'], Elist), msg=None)
   ok_(edict_with_all['elist1'].extra_data == new_reobj_all['elist1'].extra_data, msg=None)
   ok_(new_reobj_all['elist1'].extra_data['edict_obj.elist1 extra2'] == 'edict_obj.elist1 extra_value2', msg=None)

   ok_(edict_with_all['rlist1'] == new_reobj_all['rlist1'], msg=None)
   ok_(isinstance(new_reobj_all['rlist1'], Rlist), msg=None)
   ok_(edict_with_all['rlist1'].extra_data == new_reobj_all['rlist1'].extra_data, msg=None)
   ok_(new_reobj_all['rlist1'].extra_data['edict_obj.rlist1 extra2'] == 'edict_obj.rlist1 extra_value2', msg=None)

   ok_(edict_with_all['rlistf1'] == new_reobj_all['rlistf1'], msg=None)
   ok_(isinstance(new_reobj_all['rlistf1'], RlistF), msg=None)
   ok_(edict_with_all['rlistf1'].extra_data == new_reobj_all['rlistf1'].extra_data, msg=None)
   ok_(new_reobj_all['rlistf1'].extra_data['edict_obj.rlistf1 extra2'] == 'edict_obj.rlistf1 extra_value2', msg=None)

   ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(edict_with_all['etuple1'].extra_data == new_reobj_all['etuple1'].extra_data, msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['edict_obj.etuple1 extra2'] == 'edict_obj.etuple1 extra_value2', msg=None)

   ok_(edict_with_all['lmatrix1'] == new_reobj_all['lmatrix1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)
   ok_(edict_with_all['lmatrix1'].extra_data == new_reobj_all['lmatrix1'].extra_data, msg=None)
   ok_(new_reobj_all['lmatrix1'].extra_data['edict_obj.lmatrix1 extra2'] == 'edict_obj.lmatrix1 extra_value2', msg=None)

   ok_(edict_with_all['lmatrixf1'] == new_reobj_all['lmatrixf1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrixf1'], LmatrixF), msg=None)
   ok_(edict_with_all['lmatrixf1'].extra_data == new_reobj_all['lmatrixf1'].extra_data, msg=None)
   ok_(new_reobj_all['lmatrixf1'].extra_data['edict_obj.lmatrixf1 extra2'] == 'edict_obj.lmatrixf1 extra_value2', msg=None)

   # some data checks
   ok_(edict_with_all['lmatrixf1'].this_column_values('name') == new_reobj_all['lmatrixf1'].this_column_values('name') and new_reobj_all['lmatrixf1'].this_column_values('name') == ['darkorange', 'flesh', 'firebrick 3'], msg=None)
   ok_(edict_with_all['lmatrixf1'][1][2] == new_reobj_all['lmatrixf1'][1][new_reobj_all['lmatrixf1'].column_names_idx_lookup['green']] and new_reobj_all['lmatrixf1'][1][2] == 125, msg=None)

   # Change original
   edict_with_all['etuple1'].replace_extra_data({'edict_obj.etuple1 UPDATED': 'UPDATED'})

   ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(edict_with_all['etuple1'].extra_data != new_reobj_all['etuple1'].extra_data, msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['INFO'] == 'edict_obj.etuple1 inner', msg=None)
   edict_with_all = {}
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['INFO'] == 'edict_obj.etuple1 inner', msg=None)

   ok_(isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)
   ok_(new_reobj_all['lmatrix1'].extra_data['INFO'] == 'edict_obj.lmatrix1 inner', msg=None)
   ok_(new_reobj_all['lmatrix1'].column_names == ('name', 'red', 'green', 'blue'), msg=None)


def test_copy_recursively_to_python_native_types():
   """ Tests: test_copy_recursively_to_python_native_types
   """
   print('::: TEST: test_copy_recursively_to_python_native_types()')
   edict_with_all = _get_orig__edict_with_all()
   new_reobj_all = edict_with_all.copy_recursively_to_python_native_types(use_extra_key_order=False)

   ok_(isinstance(new_reobj_all, dict) and not isinstance(new_reobj_all, Edict), msg=None)

   ok_(edict_with_all['edict1'] == new_reobj_all['edict1'], msg=None)
   ok_(isinstance(new_reobj_all['edict1'], dict) and not isinstance(new_reobj_all['edict1'], Edict), msg=None)

   ok_(edict_with_all['rdict1'] == new_reobj_all['rdict1'], msg=None)
   ok_(isinstance(new_reobj_all['rdict1'], dict) and not isinstance(new_reobj_all['rdict1'], Rdict), msg=None)

   ok_(edict_with_all['edictf1'] == new_reobj_all['edictf1'], msg=None)
   ok_(isinstance(new_reobj_all['edictf1'], dict) and not isinstance(new_reobj_all['edictf1'], RdictF), msg=None)

   ok_(edict_with_all['edictio1'] == new_reobj_all['edictio1'], msg=None)
   ok_(isinstance(new_reobj_all['edictio1'], dict) and not isinstance(new_reobj_all['edictio1'], RdictIO), msg=None)

   ok_(edict_with_all['edictfo1'] == new_reobj_all['edictfo1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo1'], dict) and not isinstance(new_reobj_all['edictfo1'], RdictFO), msg=None)

   ok_(edict_with_all['edictfo2_1'] == new_reobj_all['edictfo2_1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo2_1'], dict) and not isinstance(new_reobj_all['edictfo2_1'], RdictFO2), msg=None)

   ok_(edict_with_all['elist1'] == new_reobj_all['elist1'], msg=None)
   ok_(isinstance(new_reobj_all['elist1'], list) and not isinstance(new_reobj_all['elist1'], Elist), msg=None)

   ok_(edict_with_all['rlist1'] == new_reobj_all['rlist1'], msg=None)
   ok_(isinstance(new_reobj_all['rlist1'], list) and not isinstance(new_reobj_all['rlist1'], Rlist), msg=None)

   ok_(edict_with_all['rlistf1'] == new_reobj_all['rlistf1'], msg=None)
   ok_(isinstance(new_reobj_all['rlistf1'], list) and not isinstance(new_reobj_all['rlistf1'], RlistF), msg=None)

   ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], tuple) and not isinstance(new_reobj_all['etuple1'], Etuple), msg=None)

   ok_(edict_with_all['lmatrix1'] == new_reobj_all['lmatrix1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrix1'], list) and not isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)
   ok_(edict_with_all['lmatrixf1'] == new_reobj_all['lmatrixf1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrixf1'], list) and not isinstance(new_reobj_all['lmatrixf1'], LmatrixF), msg=None)

   # some data checks
   ok_(edict_with_all['edictfo1']['edictfo_inner2'] == new_reobj_all['edictfo1']['edictfo_inner2'] and new_reobj_all['edictfo1']['edictfo_inner2'] == 'edictfo_inner2 value', msg=None)
   ok_(edict_with_all['rlist1'][1] == new_reobj_all['rlist1'][1] and new_reobj_all['rlist1'][1] == 'rlist_inner value2', msg=None)

   ok_(edict_with_all['lmatrixf1'][1][2] == new_reobj_all['lmatrixf1'][1][2] and new_reobj_all['lmatrixf1'][1][2] == 125, msg=None)


def test_py_pickle():
   """ Tests: test_py_pickle frompickle
   """
   print('::: TEST: test_py_pickle()')
   edict_with_all = _get_orig__edict_with_all()
   new_reobj_all__pdumps = pdumps(edict_with_all)
   new_reobj_all = ploads(new_reobj_all__pdumps)

   ok_(edict_with_all == new_reobj_all, msg=None)
   ok_(isinstance(new_reobj_all, Edict), msg=None)
   ok_(edict_with_all.extra_data == new_reobj_all.extra_data, msg=None)
   ok_(new_reobj_all.extra_data['edict extra2'] == 'edict extra_value2', msg=None)

   ok_(edict_with_all['edict1'] == new_reobj_all['edict1'], msg=None)
   ok_(isinstance(new_reobj_all['edict1'], Edict), msg=None)
   ok_(edict_with_all['edict1'].extra_data == new_reobj_all['edict1'].extra_data, msg=None)
   ok_(new_reobj_all['edict1'].extra_data['edict_obj.edict1 extra2'] == 'edict_obj.edict1 extra_value2', msg=None)

   ok_(edict_with_all['rdict1'] == new_reobj_all['rdict1'], msg=None)
   ok_(isinstance(new_reobj_all['rdict1'], Rdict), msg=None)
   ok_(edict_with_all['rdict1'].extra_data == new_reobj_all['rdict1'].extra_data, msg=None)
   ok_(new_reobj_all['rdict1'].extra_data['edict_obj.rdict1 extra2'] == 'edict_obj.rdict1 extra_value2', msg=None)

   ok_(edict_with_all['edictf1'] == new_reobj_all['edictf1'], msg=None)
   ok_(isinstance(new_reobj_all['edictf1'], RdictF), msg=None)
   ok_(edict_with_all['edictf1'].extra_data == new_reobj_all['edictf1'].extra_data, msg=None)
   ok_(new_reobj_all['edictf1'].extra_data['edict_obj.edictf1 extra2'] == 'edict_obj.edictf1 extra_value2', msg=None)

   ok_(edict_with_all['edictio1'] == new_reobj_all['edictio1'], msg=None)
   ok_(isinstance(new_reobj_all['edictio1'], RdictIO), msg=None)
   ok_(edict_with_all['edictio1'].extra_data == new_reobj_all['edictio1'].extra_data, msg=None)
   ok_(new_reobj_all['edictio1'].extra_data['edict_obj.edictio1 extra2'] == 'edict_obj.edictio1 extra_value2', msg=None)
   ok_(edict_with_all['edictio1'].key_order == new_reobj_all['edictio1'].key_order, msg=None)
   ok_(new_reobj_all['edictio1'].key_order == ['edictio_inner1', 'edictio_inner2', 'edictio_inner3'], msg=None)
   ok_(edict_with_all['edictio1'].extra_key_order == new_reobj_all['edictio1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictio1'].extra_key_order == ['edictio_inner2', 'edictio_inner3', 'edictio_inner1'], msg=None)

   ok_(edict_with_all['edictfo1'] == new_reobj_all['edictfo1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo1'], RdictFO), msg=None)
   ok_(edict_with_all['edictfo1'].extra_data == new_reobj_all['edictfo1'].extra_data, msg=None)
   ok_(new_reobj_all['edictfo1'].extra_data['edict_obj.edictfo1 extra2'] == 'edict_obj.edictfo1 extra_value2', msg=None)
   ok_(edict_with_all['edictfo1'].key_order == new_reobj_all['edictfo1'].key_order, msg=None)
   ok_(new_reobj_all['edictfo1'].key_order == ['edictfo_inner1', 'edictfo_inner2', 'edictfo_inner3'], msg=None)
   ok_(edict_with_all['edictfo1'].extra_key_order == new_reobj_all['edictfo1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictfo1'].extra_key_order == ['edictfo_inner2', 'edictfo_inner3', 'edictfo_inner1'], msg=None)

   ok_(edict_with_all['edictfo2_1'] == new_reobj_all['edictfo2_1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo2_1'], RdictFO2), msg=None)
   ok_(edict_with_all['edictfo2_1'].extra_data == new_reobj_all['edictfo2_1'].extra_data, msg=None)
   ok_(new_reobj_all['edictfo2_1'].extra_data['edict_obj.edictfo2_1 extra2'] == 'edict_obj.edictfo2_1 extra_value2', msg=None)
   ok_(edict_with_all['edictfo2_1'].key_order == new_reobj_all['edictfo2_1'].key_order, msg=None)
   ok_(new_reobj_all['edictfo2_1'].key_order == ['edictfo2_inner1', 'edictfo2_inner2', 'edictfo2_inner3'], msg=None)
   ok_(edict_with_all['edictfo2_1'].extra_key_order == new_reobj_all['edictfo2_1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictfo2_1'].extra_key_order == ['edictfo2_inner2', 'edictfo2_inner3', 'edictfo2_inner1'], msg=None)

   ok_(edict_with_all['elist1'] == new_reobj_all['elist1'], msg=None)
   ok_(isinstance(new_reobj_all['elist1'], Elist), msg=None)
   ok_(edict_with_all['elist1'].extra_data == new_reobj_all['elist1'].extra_data, msg=None)
   ok_(new_reobj_all['elist1'].extra_data['edict_obj.elist1 extra2'] == 'edict_obj.elist1 extra_value2', msg=None)

   ok_(edict_with_all['rlist1'] == new_reobj_all['rlist1'], msg=None)
   ok_(isinstance(new_reobj_all['rlist1'], Rlist), msg=None)
   ok_(edict_with_all['rlist1'].extra_data == new_reobj_all['rlist1'].extra_data, msg=None)
   ok_(new_reobj_all['rlist1'].extra_data['edict_obj.rlist1 extra2'] == 'edict_obj.rlist1 extra_value2', msg=None)

   ok_(edict_with_all['rlistf1'] == new_reobj_all['rlistf1'], msg=None)
   ok_(isinstance(new_reobj_all['rlistf1'], RlistF), msg=None)
   ok_(edict_with_all['rlistf1'].extra_data == new_reobj_all['rlistf1'].extra_data, msg=None)
   ok_(new_reobj_all['rlistf1'].extra_data['edict_obj.rlistf1 extra2'] == 'edict_obj.rlistf1 extra_value2', msg=None)

   ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(edict_with_all['etuple1'].extra_data == new_reobj_all['etuple1'].extra_data, msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['edict_obj.etuple1 extra2'] == 'edict_obj.etuple1 extra_value2', msg=None)

   ok_(edict_with_all['lmatrix1'] == new_reobj_all['lmatrix1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)
   ok_(edict_with_all['lmatrix1'].extra_data == new_reobj_all['lmatrix1'].extra_data, msg=None)
   ok_(new_reobj_all['lmatrix1'].extra_data['edict_obj.lmatrix1 extra2'] == 'edict_obj.lmatrix1 extra_value2', msg=None)

   ok_(edict_with_all['lmatrixf1'] == new_reobj_all['lmatrixf1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrixf1'], LmatrixF), msg=None)
   ok_(edict_with_all['lmatrixf1'].extra_data == new_reobj_all['lmatrixf1'].extra_data, msg=None)
   ok_(new_reobj_all['lmatrixf1'].extra_data['edict_obj.lmatrixf1 extra2'] == 'edict_obj.lmatrixf1 extra_value2', msg=None)

   # some data checks
   ok_(edict_with_all['edictfo1']['edictfo_inner2'] == new_reobj_all['edictfo1']['edictfo_inner2'] and new_reobj_all['edictfo1']['edictfo_inner2'] == 'edictfo_inner2 value', msg=None)
   ok_(edict_with_all['rlist1'][1] == new_reobj_all['rlist1'][1] and new_reobj_all['rlist1'][1] == 'rlist_inner value2', msg=None)

   ok_(edict_with_all['lmatrixf1'].this_column_values('name') == new_reobj_all['lmatrixf1'].this_column_values('name') and new_reobj_all['lmatrixf1'].this_column_values('name') == ['darkorange', 'flesh', 'firebrick 3'], msg=None)
   ok_(edict_with_all['lmatrixf1'][1][2] == new_reobj_all['lmatrixf1'][1][new_reobj_all['lmatrixf1'].column_names_idx_lookup['green']] and new_reobj_all['lmatrixf1'][1][2] == 125, msg=None)

   # Change original
   edict_with_all['etuple1'].replace_extra_data({'edict_obj.etuple1 UPDATED': 'UPDATED'})

   ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(edict_with_all['etuple1'].extra_data != new_reobj_all['etuple1'].extra_data, msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['INFO'] == 'edict_obj.etuple1 inner', msg=None)
   edict_with_all = {}
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['INFO'] == 'edict_obj.etuple1 inner', msg=None)

   ok_(isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)
   ok_(new_reobj_all['lmatrix1'].extra_data['INFO'] == 'edict_obj.lmatrix1 inner', msg=None)
   ok_(new_reobj_all['lmatrix1'].column_names == ('name', 'red', 'green', 'blue'), msg=None)


def test_topickle_frompickle():
   """ Tests: topickle frompickle
   """
   print('::: TEST: test_topickle_frompickle()')
   edict_with_all = _get_orig__edict_with_all()
   new_reobj_all__pdumps = edict_with_all.topickle()
   new_reobj_all = Edict.frompickle(new_reobj_all__pdumps)

   ok_(edict_with_all == new_reobj_all, msg=None)
   ok_(isinstance(new_reobj_all, Edict), msg=None)
   ok_(edict_with_all.extra_data == new_reobj_all.extra_data, msg=None)
   ok_(new_reobj_all.extra_data['edict extra2'] == 'edict extra_value2', msg=None)

   ok_(edict_with_all['edict1'] == new_reobj_all['edict1'], msg=None)
   ok_(isinstance(new_reobj_all['edict1'], Edict), msg=None)
   ok_(edict_with_all['edict1'].extra_data == new_reobj_all['edict1'].extra_data, msg=None)
   ok_(new_reobj_all['edict1'].extra_data['edict_obj.edict1 extra2'] == 'edict_obj.edict1 extra_value2', msg=None)

   ok_(edict_with_all['rdict1'] == new_reobj_all['rdict1'], msg=None)
   ok_(isinstance(new_reobj_all['rdict1'], Rdict), msg=None)
   ok_(edict_with_all['rdict1'].extra_data == new_reobj_all['rdict1'].extra_data, msg=None)
   ok_(new_reobj_all['rdict1'].extra_data['edict_obj.rdict1 extra2'] == 'edict_obj.rdict1 extra_value2', msg=None)

   ok_(edict_with_all['edictf1'] == new_reobj_all['edictf1'], msg=None)
   ok_(isinstance(new_reobj_all['edictf1'], RdictF), msg=None)
   ok_(edict_with_all['edictf1'].extra_data == new_reobj_all['edictf1'].extra_data, msg=None)
   ok_(new_reobj_all['edictf1'].extra_data['edict_obj.edictf1 extra2'] == 'edict_obj.edictf1 extra_value2', msg=None)

   ok_(edict_with_all['edictio1'] == new_reobj_all['edictio1'], msg=None)
   ok_(isinstance(new_reobj_all['edictio1'], RdictIO), msg=None)
   ok_(edict_with_all['edictio1'].extra_data == new_reobj_all['edictio1'].extra_data, msg=None)
   ok_(new_reobj_all['edictio1'].extra_data['edict_obj.edictio1 extra2'] == 'edict_obj.edictio1 extra_value2', msg=None)
   ok_(edict_with_all['edictio1'].key_order == new_reobj_all['edictio1'].key_order, msg=None)
   ok_(new_reobj_all['edictio1'].key_order == ['edictio_inner1', 'edictio_inner2', 'edictio_inner3'], msg=None)
   ok_(edict_with_all['edictio1'].extra_key_order == new_reobj_all['edictio1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictio1'].extra_key_order == ['edictio_inner2', 'edictio_inner3', 'edictio_inner1'], msg=None)

   ok_(edict_with_all['edictfo1'] == new_reobj_all['edictfo1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo1'], RdictFO), msg=None)
   ok_(edict_with_all['edictfo1'].extra_data == new_reobj_all['edictfo1'].extra_data, msg=None)
   ok_(new_reobj_all['edictfo1'].extra_data['edict_obj.edictfo1 extra2'] == 'edict_obj.edictfo1 extra_value2', msg=None)
   ok_(edict_with_all['edictfo1'].key_order == new_reobj_all['edictfo1'].key_order, msg=None)
   ok_(new_reobj_all['edictfo1'].key_order == ['edictfo_inner1', 'edictfo_inner2', 'edictfo_inner3'], msg=None)
   ok_(edict_with_all['edictfo1'].extra_key_order == new_reobj_all['edictfo1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictfo1'].extra_key_order == ['edictfo_inner2', 'edictfo_inner3', 'edictfo_inner1'], msg=None)

   ok_(edict_with_all['edictfo2_1'] == new_reobj_all['edictfo2_1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo2_1'], RdictFO2), msg=None)
   ok_(edict_with_all['edictfo2_1'].extra_data == new_reobj_all['edictfo2_1'].extra_data, msg=None)
   ok_(new_reobj_all['edictfo2_1'].extra_data['edict_obj.edictfo2_1 extra2'] == 'edict_obj.edictfo2_1 extra_value2', msg=None)
   ok_(edict_with_all['edictfo2_1'].key_order == new_reobj_all['edictfo2_1'].key_order, msg=None)
   ok_(new_reobj_all['edictfo2_1'].key_order == ['edictfo2_inner1', 'edictfo2_inner2', 'edictfo2_inner3'], msg=None)
   ok_(edict_with_all['edictfo2_1'].extra_key_order == new_reobj_all['edictfo2_1'].extra_key_order, msg=None)
   ok_(new_reobj_all['edictfo2_1'].extra_key_order == ['edictfo2_inner2', 'edictfo2_inner3', 'edictfo2_inner1'], msg=None)

   ok_(edict_with_all['elist1'] == new_reobj_all['elist1'], msg=None)
   ok_(isinstance(new_reobj_all['elist1'], Elist), msg=None)
   ok_(edict_with_all['elist1'].extra_data == new_reobj_all['elist1'].extra_data, msg=None)
   ok_(new_reobj_all['elist1'].extra_data['edict_obj.elist1 extra2'] == 'edict_obj.elist1 extra_value2', msg=None)

   ok_(edict_with_all['rlist1'] == new_reobj_all['rlist1'], msg=None)
   ok_(isinstance(new_reobj_all['rlist1'], Rlist), msg=None)
   ok_(edict_with_all['rlist1'].extra_data == new_reobj_all['rlist1'].extra_data, msg=None)
   ok_(new_reobj_all['rlist1'].extra_data['edict_obj.rlist1 extra2'] == 'edict_obj.rlist1 extra_value2', msg=None)

   ok_(edict_with_all['rlistf1'] == new_reobj_all['rlistf1'], msg=None)
   ok_(isinstance(new_reobj_all['rlistf1'], RlistF), msg=None)
   ok_(edict_with_all['rlistf1'].extra_data == new_reobj_all['rlistf1'].extra_data, msg=None)
   ok_(new_reobj_all['rlistf1'].extra_data['edict_obj.rlistf1 extra2'] == 'edict_obj.rlistf1 extra_value2', msg=None)

   ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(edict_with_all['etuple1'].extra_data == new_reobj_all['etuple1'].extra_data, msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['edict_obj.etuple1 extra2'] == 'edict_obj.etuple1 extra_value2', msg=None)

   ok_(edict_with_all['lmatrix1'] == new_reobj_all['lmatrix1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)
   ok_(edict_with_all['lmatrix1'].extra_data == new_reobj_all['lmatrix1'].extra_data, msg=None)
   ok_(new_reobj_all['lmatrix1'].extra_data['edict_obj.lmatrix1 extra2'] == 'edict_obj.lmatrix1 extra_value2', msg=None)

   ok_(edict_with_all['lmatrixf1'] == new_reobj_all['lmatrixf1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrixf1'], LmatrixF), msg=None)
   ok_(edict_with_all['lmatrixf1'].extra_data == new_reobj_all['lmatrixf1'].extra_data, msg=None)
   ok_(new_reobj_all['lmatrixf1'].extra_data['edict_obj.lmatrixf1 extra2'] == 'edict_obj.lmatrixf1 extra_value2', msg=None)

   # some data checks
   ok_(edict_with_all['lmatrixf1'].this_column_values('name') == new_reobj_all['lmatrixf1'].this_column_values('name') and new_reobj_all['lmatrixf1'].this_column_values('name') == ['darkorange', 'flesh', 'firebrick 3'], msg=None)
   ok_(edict_with_all['lmatrixf1'][1][2] == new_reobj_all['lmatrixf1'][1][new_reobj_all['lmatrixf1'].column_names_idx_lookup['green']] and new_reobj_all['lmatrixf1'][1][2] == 125, msg=None)

   # Change original
   edict_with_all['etuple1'].replace_extra_data({'edict_obj.etuple1 UPDATED': 'UPDATED'})

   ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(edict_with_all['etuple1'].extra_data != new_reobj_all['etuple1'].extra_data, msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['INFO'] == 'edict_obj.etuple1 inner', msg=None)
   edict_with_all = {}
   ok_(isinstance(new_reobj_all['etuple1'], Etuple), msg=None)
   ok_(new_reobj_all['etuple1'].extra_data['INFO'] == 'edict_obj.etuple1 inner', msg=None)

   ok_(isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)
   ok_(new_reobj_all['lmatrix1'].extra_data['INFO'] == 'edict_obj.lmatrix1 inner', msg=None)
   ok_(new_reobj_all['lmatrix1'].column_names == ('name', 'red', 'green', 'blue'), msg=None)


def test_py_json():
   """ Tests: test_py_json frompickle
   """
   print('::: TEST: test_py_json()')
   edict_with_all = _get_orig__edict_with_all()
   new_reobj_all__jdumps = jdumps(edict_with_all)
   new_reobj_all = jloads(new_reobj_all__jdumps)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all == new_reobj_all, msg=None)
   ok_(isinstance(new_reobj_all, dict) and not isinstance(new_reobj_all, Edict), msg=None)

   ok_(edict_with_all['edict1'] == new_reobj_all['edict1'], msg=None)
   ok_(isinstance(new_reobj_all['edict1'], dict) and not isinstance(new_reobj_all['edict1'], Edict), msg=None)

   ok_(edict_with_all['rdict1'] == new_reobj_all['rdict1'], msg=None)
   ok_(isinstance(new_reobj_all['rdict1'], dict) and not isinstance(new_reobj_all['rdict1'], Rdict), msg=None)

   ok_(edict_with_all['edictf1'] == new_reobj_all['edictf1'], msg=None)
   ok_(isinstance(new_reobj_all['edictf1'], dict) and not isinstance(new_reobj_all['edictf1'], RdictF), msg=None)

   ok_(edict_with_all['edictio1'] == new_reobj_all['edictio1'], msg=None)
   ok_(isinstance(new_reobj_all['edictio1'], dict) and not isinstance(new_reobj_all['edictio1'], RdictIO), msg=None)

   ok_(edict_with_all['edictfo1'] == new_reobj_all['edictfo1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo1'], dict) and not isinstance(new_reobj_all['edictfo1'], RdictFO), msg=None)

   ok_(edict_with_all['edictfo2_1'] == new_reobj_all['edictfo2_1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo2_1'], dict) and not isinstance(new_reobj_all['edictfo2_1'], RdictFO2), msg=None)

   ok_(edict_with_all['elist1'] == new_reobj_all['elist1'], msg=None)
   ok_(isinstance(new_reobj_all['elist1'], list) and not isinstance(new_reobj_all['elist1'], Elist), msg=None)

   ok_(edict_with_all['rlist1'] == new_reobj_all['rlist1'], msg=None)
   ok_(isinstance(new_reobj_all['rlist1'], list) and not isinstance(new_reobj_all['rlist1'], Rlist), msg=None)

   ok_(edict_with_all['rlistf1'] == new_reobj_all['rlistf1'], msg=None)
   ok_(isinstance(new_reobj_all['rlistf1'], list) and not isinstance(new_reobj_all['rlistf1'], RlistF), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], list) and not isinstance(new_reobj_all['etuple1'], Etuple), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['lmatrix1'] == new_reobj_all['lmatrix1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrix1'], list) and not isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['lmatrixf1'] == new_reobj_all['lmatrixf1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrixf1'], list) and not isinstance(new_reobj_all['lmatrixf1'], LmatrixF), msg=None)

   # some data checks
   ok_(edict_with_all['edictfo1']['edictfo_inner2'] == new_reobj_all['edictfo1']['edictfo_inner2'] and new_reobj_all['edictfo1']['edictfo_inner2'] == 'edictfo_inner2 value', msg=None)
   ok_(edict_with_all['rlist1'][1] == new_reobj_all['rlist1'][1] and new_reobj_all['rlist1'][1] == 'rlist_inner value2', msg=None)

   ok_(edict_with_all['lmatrixf1'][1][2] == new_reobj_all['lmatrixf1'][1][2] and new_reobj_all['lmatrixf1'][1][2] == 125, msg=None)


def test_tojson_fromjson():
   """ Tests: tojson fromjson
   """
   print('::: TEST: test_tojson_fromjson()')
   edict_with_all = _get_orig__edict_with_all()
   new_reobj_all__jdumps = edict_with_all.tojson()
   new_reobj_all = jloads(new_reobj_all__jdumps)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all == new_reobj_all, msg=None)
   ok_(isinstance(new_reobj_all, dict) and not isinstance(new_reobj_all, Edict), msg=None)

   ok_(edict_with_all['edict1'] == new_reobj_all['edict1'], msg=None)
   ok_(isinstance(new_reobj_all['edict1'], dict) and not isinstance(new_reobj_all['edict1'], Edict), msg=None)

   ok_(edict_with_all['rdict1'] == new_reobj_all['rdict1'], msg=None)
   ok_(isinstance(new_reobj_all['rdict1'], dict) and not isinstance(new_reobj_all['rdict1'], Rdict), msg=None)

   ok_(edict_with_all['edictf1'] == new_reobj_all['edictf1'], msg=None)
   ok_(isinstance(new_reobj_all['edictf1'], dict) and not isinstance(new_reobj_all['edictf1'], RdictF), msg=None)

   ok_(edict_with_all['edictio1'] == new_reobj_all['edictio1'], msg=None)
   ok_(isinstance(new_reobj_all['edictio1'], dict) and not isinstance(new_reobj_all['edictio1'], RdictIO), msg=None)
   ok_(edict_with_all['edictio1'].key_order == ['edictio_inner1', 'edictio_inner2', 'edictio_inner3'], msg=None)

   ok_(edict_with_all['edictfo1'] == new_reobj_all['edictfo1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo1'], dict) and not isinstance(new_reobj_all['edictfo1'], RdictFO), msg=None)
   ok_(edict_with_all['edictfo1'].key_order == ['edictfo_inner1', 'edictfo_inner2', 'edictfo_inner3'], msg=None)

   ok_(edict_with_all['edictfo2_1'] == new_reobj_all['edictfo2_1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo2_1'], dict) and not isinstance(new_reobj_all['edictfo2_1'], RdictFO2), msg=None)
   ok_(edict_with_all['edictfo2_1'].key_order == ['edictfo2_inner1', 'edictfo2_inner2', 'edictfo2_inner3'], msg=None)

   ok_(edict_with_all['elist1'] == new_reobj_all['elist1'], msg=None)
   ok_(isinstance(new_reobj_all['elist1'], list) and not isinstance(new_reobj_all['elist1'], Elist), msg=None)

   ok_(edict_with_all['rlist1'] == new_reobj_all['rlist1'], msg=None)
   ok_(isinstance(new_reobj_all['rlist1'], list) and not isinstance(new_reobj_all['rlist1'], Rlist), msg=None)

   ok_(edict_with_all['rlistf1'] == new_reobj_all['rlistf1'], msg=None)
   ok_(isinstance(new_reobj_all['rlistf1'], list) and not isinstance(new_reobj_all['rlistf1'], RlistF), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], list) and not isinstance(new_reobj_all['etuple1'], Etuple), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['lmatrix1'] == new_reobj_all['lmatrix1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrix1'], list) and not isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['lmatrixf1'] == new_reobj_all['lmatrixf1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrixf1'], list) and not isinstance(new_reobj_all['lmatrixf1'], LmatrixF), msg=None)

   # some data checks
   ok_(edict_with_all['edictfo1']['edictfo_inner2'] == new_reobj_all['edictfo1']['edictfo_inner2'] and new_reobj_all['edictfo1']['edictfo_inner2'] == 'edictfo_inner2 value', msg=None)
   ok_(edict_with_all['rlist1'][1] == new_reobj_all['rlist1'][1] and new_reobj_all['rlist1'][1] == 'rlist_inner value2', msg=None)

   ok_(edict_with_all['lmatrixf1'][1][2] == new_reobj_all['lmatrixf1'][1][2] and new_reobj_all['lmatrixf1'][1][2] == 125, msg=None)


def test_tojson_keeporder():
   """ Tests: tojson_keeporder
   """
   print('::: TEST: test_tojson_keeporder()')
   edict_with_all = _get_orig__edict_with_all()
   new_reobj_all__jdumps_keeporder = edict_with_all.tojson_keeporder()
   new_reobj_all = jloads(new_reobj_all__jdumps_keeporder, object_pairs_hook=OrderedDict)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all == new_reobj_all, msg=None)
   ok_(isinstance(new_reobj_all, dict) and not isinstance(new_reobj_all, Edict), msg=None)

   ok_(edict_with_all['edict1'] == new_reobj_all['edict1'], msg=None)
   ok_(isinstance(new_reobj_all['edict1'], dict) and not isinstance(new_reobj_all['edict1'], Edict), msg=None)

   ok_(edict_with_all['rdict1'] == new_reobj_all['rdict1'], msg=None)
   ok_(isinstance(new_reobj_all['rdict1'], dict) and not isinstance(new_reobj_all['rdict1'], Rdict), msg=None)

   ok_(edict_with_all['edictf1'] == new_reobj_all['edictf1'], msg=None)
   ok_(isinstance(new_reobj_all['edictf1'], dict) and not isinstance(new_reobj_all['edictf1'], RdictF), msg=None)

   ok_(edict_with_all['edictio1'] == new_reobj_all['edictio1'], msg=None)
   ok_(isinstance(new_reobj_all['edictio1'], dict) and not isinstance(new_reobj_all['edictio1'], RdictIO), msg=None)
   ok_(edict_with_all['edictio1'].key_order == ['edictio_inner1', 'edictio_inner2', 'edictio_inner3'] and edict_with_all['edictio1'].key_order == [key for key in new_reobj_all['edictio1'].keys()], msg=None)

   ok_(edict_with_all['edictfo1'] == new_reobj_all['edictfo1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo1'], dict) and not isinstance(new_reobj_all['edictfo1'], RdictFO), msg=None)
   ok_(edict_with_all['edictfo1'].key_order == ['edictfo_inner1', 'edictfo_inner2', 'edictfo_inner3'] and edict_with_all['edictfo1'].key_order == [key for key in new_reobj_all['edictfo1'].keys()], msg=None)

   ok_(edict_with_all['edictfo2_1'] == new_reobj_all['edictfo2_1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo2_1'], dict) and not isinstance(new_reobj_all['edictfo2_1'], RdictFO2), msg=None)
   ok_(edict_with_all['edictfo2_1'].key_order == ['edictfo2_inner1', 'edictfo2_inner2', 'edictfo2_inner3'] and edict_with_all['edictfo2_1'].key_order == [key for key in new_reobj_all['edictfo2_1'].keys()], msg=None)

   ok_(edict_with_all['elist1'] == new_reobj_all['elist1'], msg=None)
   ok_(isinstance(new_reobj_all['elist1'], list) and not isinstance(new_reobj_all['elist1'], Elist), msg=None)

   ok_(edict_with_all['rlist1'] == new_reobj_all['rlist1'], msg=None)
   ok_(isinstance(new_reobj_all['rlist1'], list) and not isinstance(new_reobj_all['rlist1'], Rlist), msg=None)

   ok_(edict_with_all['rlistf1'] == new_reobj_all['rlistf1'], msg=None)
   ok_(isinstance(new_reobj_all['rlistf1'], list) and not isinstance(new_reobj_all['rlistf1'], RlistF), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['etuple1'] == new_reobj_all['etuple1'], msg=None)
   ok_(isinstance(new_reobj_all['etuple1'], list) and not isinstance(new_reobj_all['etuple1'], Etuple), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['lmatrix1'] == new_reobj_all['lmatrix1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrix1'], list) and not isinstance(new_reobj_all['lmatrix1'], Lmatrix), msg=None)

   # note is not equal because tuples are changed to list in json
   # ok_(edict_with_all['lmatrixf1'] == new_reobj_all['lmatrixf1'], msg=None)
   ok_(isinstance(new_reobj_all['lmatrixf1'], list) and not isinstance(new_reobj_all['lmatrixf1'], LmatrixF), msg=None)

   # some data checks
   ok_(edict_with_all['edictfo1']['edictfo_inner2'] == new_reobj_all['edictfo1']['edictfo_inner2'] and new_reobj_all['edictfo1']['edictfo_inner2'] == 'edictfo_inner2 value', msg=None)
   ok_(edict_with_all['rlist1'][1] == new_reobj_all['rlist1'][1] and new_reobj_all['rlist1'][1] == 'rlist_inner value2', msg=None)

   ok_(edict_with_all['lmatrixf1'][1][2] == new_reobj_all['lmatrixf1'][1][2] and new_reobj_all['lmatrixf1'][1][2] == 125, msg=None)

   # Check extra_key_order
   edict_with_all = _get_orig__edict_with_all()
   new_reobj_all__jdumps_keeporder = edict_with_all.tojson_keeporder(use_extra_key_order=True)
   new_reobj_all = jloads(new_reobj_all__jdumps_keeporder, object_pairs_hook=OrderedDict)

   # not the same because we use: use_extra_key_order
   # ok_(edict_with_all['edictio1'] == new_reobj_all['edictio1'], msg=None)
   ok_(isinstance(new_reobj_all['edictio1'], dict) and not isinstance(new_reobj_all['edictio1'], RdictIO), msg=None)
   ok_(edict_with_all['edictio1'].extra_key_order == ['edictio_inner2', 'edictio_inner3', 'edictio_inner1'] and edict_with_all['edictio1'].extra_key_order == [key for key in new_reobj_all['edictio1'].keys()], msg=None)

   # not the same because we use: use_extra_key_order
   # ok_(edict_with_all['edictfo1'] == new_reobj_all['edictfo1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo1'], dict) and not isinstance(new_reobj_all['edictfo1'], RdictFO), msg=None)
   ok_(edict_with_all['edictfo1'].extra_key_order == ['edictfo_inner2', 'edictfo_inner3', 'edictfo_inner1'] and edict_with_all['edictfo1'].extra_key_order == [key for key in new_reobj_all['edictfo1'].keys()], msg=None)

   # not the same because we use: use_extra_key_order
   # ok_(edict_with_all['edictfo2_1'] == new_reobj_all['edictfo2_1'], msg=None)
   ok_(isinstance(new_reobj_all['edictfo2_1'], dict) and not isinstance(new_reobj_all['edictfo2_1'], RdictFO2), msg=None)
   ok_(edict_with_all['edictfo2_1'].extra_key_order == ['edictfo2_inner2', 'edictfo2_inner3', 'edictfo2_inner1'] and edict_with_all['edictfo2_1'].extra_key_order == [key for key in new_reobj_all['edictfo2_1'].keys()], msg=None)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   pass

   test_edict__copy_recursively()

   test_copy_recursively_to_python_native_types()

   test_py_pickle()
   test_topickle_frompickle()

   test_py_json()
   test_tojson_fromjson()
   test_tojson_keeporder()

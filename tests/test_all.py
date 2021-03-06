"""
Unit test for lvm_read.py
"""

import numpy as np
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from lvm_read import read

def test_short_lvm():
    data = read('./data/pickle_only.lvm')
    np.testing.assert_equal(data[0]['data'][0,0],0.914018)

    data = read('./data/short.lvm', read_from_pickle=False)
    np.testing.assert_equal(data[0]['data'][0,0],0.914018)

    data = read('./data/short.lvm', read_from_pickle=True)
    np.testing.assert_equal(data[0]['data'][0, 0], 0.914018)

    data = read('./data/short_new_line_end.lvm', read_from_pickle=True, dump_file=False)
    np.testing.assert_equal(data[0]['data'][0, 0], 0.914018)

def test_with_empty_fields_lvm():
    data = read('./data/with_empty_fields.lvm', read_from_pickle=False, dump_file=False)
    np.testing.assert_equal(data[0]['data'][0,7],-0.011923)

def test_with_multi_time_column_lvm():
    data = read('./data/multi_time_column.lvm', read_from_pickle=False, dump_file=False)
    np.testing.assert_allclose(data[0]['data'][0],\
                               np.array([0.000000,-0.035229,0.000000,0.532608]))

def test_no_decimal_separator():
    data = read('./data/no_decimal_separator.lvm', read_from_pickle=False, dump_file=False)
    np.testing.assert_equal(data[0]['data'][0,1],-0.008807)


if __name__ == '__mains__':
    np.testing.run_module_suite()
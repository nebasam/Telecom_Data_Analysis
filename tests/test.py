import unittest
import sys
import os
from numpy import fix
import pandas as pd
from pandas._libs.tslibs.timestamps import Timestamp
sys.path.append(os.path.abspath(os.path.join('../scripts/')))
sys.path.insert(1, 'scripts')

import db_handling_missing

class TelecomData(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'Name': ['Tom'], 'FatherName': ['Jack'], 'Age': [20], 'dates': ['4/4/2019 12:01']})

        self.Nulldf = pd.DataFrame({"A":[11, 5, None, 3, None, 8],
                   "B":[1, 5, None, 11, None, 8]})


    def test_convert_to_datetime(self):
        df = db_handling_missing.convert_to_datetime(self.df, ['dates'])
        assert type(df['dates'][0]) is Timestamp
    
    def test_percent_missing(self):
        assert db_handling_missing.percent_missing(self.df) == 0
    
    def test_adding_columns(self):
        expected_df = pd.DataFrame({'Name': ['Tom'], 'FatherName': ['Jack'], 'Age': [20], 'dates': ['4/4/2019 12:01'], 'FullName': ['TomJack']})
        df2 = db_handling_missing.adding_columns(self.df, 'FullName', 'Name', 'FatherName')
        assert df2.equals(expected_df)
    
    def test_fix_missing_ffill(self):
        fixed_df = db_handling_missing.fix_missing_ffill(self.Nulldf)
        assert db_handling_missing.percent_missing(fixed_df) == 0
    
    def test_fix_missing_bfill(self):
        fixed_df = db_handling_missing.fix_missing_bfill(self.Nulldf)
        assert db_handling_missing.percent_missing(fixed_df) == 0

    def tearDown(self) -> None:
        print('Closed')

if __name__ == '__main__':
    unittest.main()
    
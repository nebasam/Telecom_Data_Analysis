import unittest
import sys
import os
import pandas as pd
from pandas._libs.tslibs.timestamps import Timestamp
sys.path.append(os.path.abspath(os.path.join('../scripts/')))
sys.path.insert(1, 'scripts')

import db_handling_missing

class TelecomData(unittest.TestCase):

    def setUp(self):
        self.df = {'Name': ['Tom'], 'FatherName': ['Jack'], 'Age': [20], 'dates': ['4/4/2019 12:01']}

        self.df = pd.DataFrame(self.df)

    def test_convert_to_datetime(self):
        df = db_handling_missing.convert_to_datetime(self.df, ['dates'])
        print(type(df['dates'][0]))
        assert type(df['dates'][0]) is Timestamp
    
    def test_adding_columns(self):
        expected_df = pd.DataFrame({'Name': ['Tom'], 'FatherName': ['Jack'], 'Age': [20], 'dates': ['4/4/2019 12:01'], 'FullName': ['TomJack']})
        df2 = db_handling_missing.adding_columns(self.df, 'FullName', 'Name', 'FatherName')
        assert df2.equals(expected_df)

    def tearDown(self) -> None:
        print('Closed')

if __name__ == '__main__':
    unittest.main()
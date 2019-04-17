import pandas as pd
import numpy as np

def read_congress_terms():
	'''Read congress-terms.csv from fivethirtyeight github.
	   The file congress-terms.csv has an entry for every
	   member of congress who served at any point during
	   a particular congress between January 1947 and Februrary 2014'''

	url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv'
	cols = ['firstname', 'lastname', 'termstart', 'age']
	return pd.read_csv(url, usecols=cols)

def test_create_dataframe(df):
	'''Calls read-congress_terms and performs
	   3 tests on the resulting dataframe:
	   		- The columns are only those selected in read_congress_terms().
	   		- The columns contain the correct data type.
	   		- There are at least 10 rows in the DataFrame.
	   If any one of these tests fails, returns False.
	   If all tests pass, returns True.'''

	cols = ['firstname', 'lastname', 'termstart', 'age']
	col_types = [object, object, object, np.float64]
	df = read_congress_terms()

	if list(df.columns) != cols:
		return False
	if df.dtypes.tolist() != col_types:
		return False
	if df.shape[0] < 10:
		return False
	return True

def main():
	'''Executes test_create_dataframe() on
	   the result of read_congress_terms()
	   prints results'''

	if test_create_dataframe(read_congress_terms()):
		print('Tests passed.')
	else:
		print('At least one test failed.')

if __name__ == '__main__':

	main()
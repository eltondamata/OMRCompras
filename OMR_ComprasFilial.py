#!/usr/bin/env python

import pandas as pd
df = pd.read_pickle('~/Downloads/OMR_COMPRASFILIAL.pkl')
print(df.head())
df2 = df.groupby('DESTIPCNLVNDOMR')[['VLRVNDFATLIQ']].sum()

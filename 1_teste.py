import pandas as pd
df = pd.read_pickle('~/Downloads/OMR_COMPRASFILIAL.pkl')
df2 = df.groupby('DESTIPCNLVNDOMR')[['VLRVNDFATLIQ']].sum()
print(df2)

df['VLRVNDFATLIQb'] = df['VLRVNDFATLIQ']
df['VLRVNDFATLIQc'] = df['VLRVNDFATLIQ']
df['VLRVNDFATLIQd'] = df['VLRVNDFATLIQ']

print(df.head().to_string())
#['CODGRPPRD', 'CODCTGPRD', 'CODSUBCTGPRD', 'CODDIVFRN', 'CODESTUNI', 'DESTIPCNLVNDOMR', 'CODFILEPD', 'VLRVNDFATLIQ', 'VLRRCTLIQAPU', 'VLRMRGBRT', 'VLRMRGCRB', 'VLRVNDFATLIQb', 'VLRVNDFATLIQc', 'VLRVNDFATLIQd']

#df.to_csv('teste.csv')

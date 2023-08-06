import pandas as pd
import ydata_profiling

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                 names=['ComprimentoSepala', 'LarguraSepala', 'ComprimentoPetala,'
                        'LarguraPetala', 'Especie'])

ydata_profiling.ProfileReport(df, explorative=True)
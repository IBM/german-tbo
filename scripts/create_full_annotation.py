"""
Create full annotation data
"""

import argparse
import pandas as pd
from itertools import chain

col_names=list(chain.from_iterable([ (f'T{k} Target',f'T{k} Argument') for k in range(1,6) ]))

if __name__ == '__main__':

    p = argparse.ArgumentParser()
    p.add_argument("--germeval_orig", '-i', type=str, help="original data with anonymized twitter handles.")
    p.add_argument("--germeval_tbo", '-t', required=True, type=str, help="IBM German TBO annotation file")
    p.add_argument("--out", '-o', required=True,type=str, help="full annotation output file")
    p.add_argument("--verbosity","-v", action="count",default=0, help="verbosity level")
    
    args=p.parse_args()

    if args.verbosity>0:
        print(f'col_names: {col_names}')
    
    df_germeval=pd.read_csv(args.germeval_orig,sep='\t', names=['tweet','offensive','type'])

    # move index into special column for merging
    df_germeval.reset_index(names=['orig_pos'],inplace=True)
    print(f'#germeval: {len(df_germeval)} .')
    if args.verbosity>0:
        print(df_germeval.head())
        
    
    df_tbo=pd.read_csv(args.germeval_tbo)
    print(f'#tbo: {len(df_tbo)} .')
    assert all([ t in df_tbo for t in col_names])
    
    df_merge=df_tbo.merge(right=df_germeval,on='orig_pos')

    print(f'#merge: {len(df_merge)} .')

    if args.verbosity>0:
        print(df_merge.head())

    df_merge=df_merge[ ['tweet','offensive','type'] +col_names ] 
        
    df_merge.to_csv(args.out,index=False)
    print(f'Wrote output: {args.out} .')


    

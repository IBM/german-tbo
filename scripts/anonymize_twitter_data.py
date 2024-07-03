import argparse
import re

if __name__ == '__main__':

    p = argparse.ArgumentParser()
    p.add_argument("input", type=str, help="input file")
    p.add_argument("output", type=str, help="output file")    
    
    args=p.parse_args()

    with open(args.input,'r') as f:
        lines = [ l.strip() for l in f]

    with open(args.output,'w') as f:

        for line in lines:

            def callback(match):
                return next(callback.id)
            user_strings=[ f'@USER{i}' for i in range(30) ]
            callback.id=iter(user_strings)

            line=re.sub(r"\B@\w+",callback, line)
            print(line,file=f)

            
    print('Done.')
    


    

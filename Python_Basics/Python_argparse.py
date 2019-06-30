import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-x',type=float,default=10.0,help='first number')

parser.add_argument('-y',type=float,default=7.0,help='second number')

parser.add_argument('-op',type=str,default='mul',help='operation')


arg = parser.parse_args()

def main():
    if arg.op == 'add':
        return arg.x+arg.y
    elif arg.op == 'sub':
        return arg.x-arg.y
    elif arg.op == 'mul':
        return arg.x*arg.y
    else:
        return arg.y/arg.x

print(main())
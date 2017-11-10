from subprocess import call
from sys import stdin

stdin = input()

#call('cd Documents/GitHub/algdat', shell = True)
call('git add .', shell = True)
call('git commit -m'+stdin, shell = True)
call('git push', shell = True)

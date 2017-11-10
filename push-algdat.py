from subprocess import call

c
stdin = input()

with cd("~/Library"):
    #call('cd Documents/GitHub/algdat', shell = True)
    call('git add .', shell = True)
    call('git commit -m'+stdin, shell = True)
    call('git push', shell = True)

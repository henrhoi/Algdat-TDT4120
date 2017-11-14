from subprocess import call

# Kjør denne filen i enten PyCharm, Idle eller Terminal for å pushe git-repositoriet.
# Slipper å skrive git add, commit og push hver gang.

# Dersom i Terminal, kall:
# python push_to_git.py

call('git add .', shell=True)
call('git commit -m ".."',shell=True)
call('git push', shell=True)

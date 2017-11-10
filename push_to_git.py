from subprocess import call

# Kall denne i terminalen for å slippe å skrive git add, commit og push hver gang:
# python push_to_git.py

call('git add .', shell=True)
call('git commit -m ".."',shell=True)
call('git push', shell=True)

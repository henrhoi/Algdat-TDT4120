from subprocess import call

#Kall denne i terminalen for å slippe 

call('git add .', shell=True)
call('git commit -m ".."',shell=True)


call('git push', shell=True)

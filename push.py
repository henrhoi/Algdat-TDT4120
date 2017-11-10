from subprocess import call

call('echo From which repository:', shell=True)
repo = input()

call('echo Message: ',shell=True)

message = input()



call('cd Documents/GitHub/'+str(repo), shell=True)
call('git add .', shell=True)

if message == "":
    call('git commit -m ".."',shell=True)

else:
    call('git commit -m '+message,shell=True)

call('git push')

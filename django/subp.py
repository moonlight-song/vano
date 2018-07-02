from subprocess import Popen, PIPE

p = Popen ("test", stdout = PIPE, shell = True)
p.communicate()
p_status = p.wait()
print (int (p_status)*2)
import os
import sys

readend, writeend = os.pipe()
pid = os.fork()
if pid != 0: #parent process
    os.close(writeend)
    r = os.fdopen(readend)
    print(r.read(), '- it arrived to the parent with pid: ', pid)
    sys.exit(0)
else: #child process
    os.close(readend)
    w = os.fdopen(writeend, 'w')
    w.write('message from child')
    w.close()

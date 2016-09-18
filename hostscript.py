import platform
import linuxhosts
#Detect OS
OS = platform.system()
release = platform.release()
version = platform.version()

if OS == 'Windows':
    print (OS)
    print (release)
    print (version)
    print ("Sorry your OS is not supported at this time. Please send system info to me!.")
    #%SystemRoot%\System32\drivers\etc\hosts
    
elif OS == 'Linux':
    print (OS)
    print (release)
    print (version)
    linuxhosts.linux()

else:
    print (OS)
    print (release)
    print (version)
    print ("Sorry your OS is not supported at this time. Please send system info to me!.")

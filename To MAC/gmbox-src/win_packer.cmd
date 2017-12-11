@echo off
rd gmbox /S /Q
python win_packer.py py2exe
xcopy c:\\GTK\etc gmbox\etc /E /I /R
xcopy c:\\GTK\lib gmbox\lib /E /I /R
xcopy c:\\GTK\Microsoft.VC90.CRT gmbox\Microsoft.VC90.CRT /E /I /R
rd build /S /Q

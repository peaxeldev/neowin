@echo off
echo Installing the packages necessary for neowin...

pip install wmi 
pip install GPUtil 
pip install py-cpuinfo 
pip install platform 

echo Successfully! Put neowin in PATH...

set /p neowinPATH=Enter the path to the main.py: 
setx PATH "%PATH%;%neowinPATH%"
pause 
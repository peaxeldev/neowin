import os 
import platform 
import cpuinfo 
import GPUtil
import wmi 


c = wmi.WMI()
oscore = os.name
osplatform = platform.win32_ver()
osprocessor = cpuinfo.get_cpu_info()

for gpu in GPUtil.getGPUs():
    osgpu = f'{gpu.name}'

for board in c.Win32_BaseBoard():
    oshost = board.Product

for os in c.Win32_OperatingSystem():
    osbusyram = int(os.TotalVisibleMemorySize) - int(os.FreePhysicalMemory) / 1024
    osramfull = int(os.TotalVisibleMemorySize) / 1024

if oscore == 'nt':
    print("                                              ")
    print("                           ....iilll          Core: " + oscore)
    print("                 ....iilllllllllllll          OS: Windows")
    print("     ....iillll  lllllllllllllllllll          Version: " + str(osplatform[1]))
    print(" iillllllllllll  lllllllllllllllllll          CPU: " + str(osprocessor['brand_raw']))
    print(" llllllllllllll  lllllllllllllllllll          GPU: " + osgpu)
    print(" llllllllllllll  lllllllllllllllllll          Host: " + oshost)
    print(f" llllllllllllll  lllllllllllllllllll          RAM: {osbusyram}MB / {osramfull}MB".format(osbusyram, osramfull))
    print(" llllllllllllll  lllllllllllllllllll")
    print(" llllllllllllll  lllllllllllllllllll")
    print("")
    print(" llllllllllllll  lllllllllllllllllll")
    print(" llllllllllllll  lllllllllllllllllll")
    print(" llllllllllllll  lllllllllllllllllll")
    print(" llllllllllllll  lllllllllllllllllll")
    print(" llllllllllllll  lllllllllllllllllll")
    print(" `^^^^^^lllllll  lllllllllllllllllll")
    print("       ````^^^^  ^^lllllllllllllllll")
    print("                      ````^^^^^^llll")
else:
    print("Sorry, but your OS does not support neowin.")
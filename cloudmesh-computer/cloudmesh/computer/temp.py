import socket
import wmi
from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.systeminfo import os_is_mac
from cloudmesh.common.systeminfo import os_is_linux
from cloudmesh.common.Shell import Console, Shell
from cloudmesh.common.util import readfile
import psutil

def HnameTemp():
    if os_is_windows():
        import wmi
        host_name = socket.gethostname()
        w_temp = wmi.WMI(namespace=r'root\wmi', privileges=["Security"])
        temp = ""
        try:
            temp = (w_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10) - 273.2
            temp = f"{temp}C"
            temp_dictionary = '{HostName:', host_name, 'Temperature', temp, '}'
            print(temp_dictionary)
            return temp_dictionary
        except:
            Console.error("Program failed. Try running as administrator.")
            return None

    elif os_is_linux():
        host_name = socket.gethostname()
        temp = None
        readfile("/sys/class/thermal/thermal_zone0/temp", temp)
        return {'HostName': host_name, 'Temperature': temp + 'C'}
        #psutil_temperatures = psutil.sensors_temperatures()['name'][0]

    elif os_is_mac():
        host_name = socket.gethostname()
        temp = None
        r = Shell.run('sudo powermetrics|grep -i "CPU die temperature"')
        temp = r
        return {'HostName': host_name, 'Temperature': temp + 'C'}



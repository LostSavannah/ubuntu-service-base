import os
import shutil
UNIT_REGION = "Unit"
SERVICE_REGION = "Service"
INSTALL_REGION = "Install"

service_path = '/etc/systemd/system'

service_definition = {
    UNIT_REGION: {
        "Description": None,
        "After": "multi-user.target",
        "Conflicts": "getty@tty1.service"
    },
    SERVICE_REGION: {
        "Type": "simple",
        "ExecStart": f"/usr/bin/python3 {os.path.abspath(os.curdir)}/main.py",
        "StandardInput": "tty-force"
    },
    INSTALL_REGION: {
        "WantedBy": "multi-user.target"
    }
}

def retrieve(region:str, title:str, deflt = None):
    data:str = input(title) or deflt
    service_definition[region][title] = data
    return data

service_name = input('Service_name: ')
service_definition[UNIT_REGION]["Description"] = service_name
filename:str = os.sep.join([
    'services', 
    service_name.lower().replace(' ', '_') + '.service'
    ])

with open(filename, 'w', encoding='latin1') as fo:
    for region in service_definition:
        fo.write(f'[{region}]\n')
        for config in service_definition[region]:
            value:str = service_definition[region][config]
            fo.write(f'{config}={value}\n')
        fo.write('\n')

shutil.copy(filename, service_path)
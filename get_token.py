# Press button on bridge then issue API

BRIDGE_IP='192.168.1.86'

from huesdk import Hue
username = Hue.connect(bridge_ip=BRIDGE_IP)
print(username)

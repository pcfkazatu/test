import serial
import re

hx = serial.Serial('/dev/ttyUSB_HX',9600, bytesize = serial.EIGHTBITS, timeout=1)
hx.write(b'\x02')
res_hx = hx.read(4)
res_hx_2 = int.from_bytes(res_hx, 'big')
print('hx', res_hx_2)


dist = serial.Serial('/dev/ttyUSB_Dist',9600)

res_dist = (str(dist.readline()))
res_dist = re.sub("b|'|\r|\n","",res_dist[:-5])

print('dist', res_dist)

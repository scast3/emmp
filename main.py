from pump import pump
from pump import comparison

#Parse data to obtain hourly energy rates
#using colorado average:
rate = 0.1228 # $/kWh

#Example Pump:
q = 485 #GPM
w = 910 #RPM
h = 40 #ft
n = 0.7
bhp = 0
whp = 0
specific_weight = 62.4
pump1 = pump('10009','PC4, PUMP, 02-644','WEMCO','9190501-1','01/01/1992','BUILDING 04 PRIMARY PUMP STATION',w,n,q,h,specific_weight)

def replacement_calcs(Q,h,w,n,sg):
    power = Q*h*sg/n
    
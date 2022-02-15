soc_level_state = {[0,20] : 'LOW_SOC_BREACH', [21,24] : 'LOW_SOC_WARNING', [24,75] : 'NORMAL', [76,80] : 'HIGH_SOC_WARNING', [81,100] : 'HIGH_SOC_BREACH' }
temperature_level_state = {[0,0] : 'LOW_SOC_BREACH', [0,2.25] : 'LOW_TEMPERATURE_WARNING', (2.25,42.75) : 'NORMAL', [42.75,45] : 'HIGH_TEMPERATURE_WARNING', [45,100] : 'HIGH_TEMPERATURE_BREACH'}
charge_rate_state = {(-100,0] : 'LOW_CHARGE_BREACH', [0,0.2] : 'LOW_CHARGE_WARNING', (0.2,0.8] : 'NORMAL', [76,80] : 'HIGH_CHARGE_WARNING', [81,100] : 'HIGH_CHARGE_BREACH' }

def temperature_check(temperature):
	if temperature < 0:
		print('Temperature is out of range!')
		temperature_tolerance_check
		low_range()
		return False
	elif temperature > 45:
		print('Temperature is out of range!')
		temperature_tolerance_check
		high_range()
		return False	
	else :
		return True

def temperature_tolerance_check(temperature):
  if ((temperature>=0) and (temperature<=((5/100)*45))):
    print('Warning: Approaching low temperature')
  elif ((temperature<=45) and (temperature>=(45-(5/100)*45))):
    print('Warning: Approaching peak temperature')
  else:
    print('Temperature is ok')
    
def soc_check(soc):
	if soc < 20:
		print('State of Charge is out of range!')
		soc_tolerance_check(soc)
		low_range()
		return False
	elif soc > 80:
		print('State of Charge is out of range!')
		soc_tolerance_check(soc)
		high_range()
		return False
	else:
		return True

def soc_tolerance_check(soc):
  if ((soc>=20) and (soc<=(80*5/100+20))):
    print('Warning: Approaching discharge')
  elif ((soc>=(80-80*(5/100))) and (soc<=80)):
    print('Warning: Approaching charge-peak')
  else:
    print('SOC Charge is ok')
    
def Charge_rate_check(charge_rate):
	if charge_rate > 0.8:
		print('Charge rate is out of range!')
		charge_rate_tolerance_check
		high_range()
		return False
	elif charge_rate < 0:
		print('Charge rate is out of range!')
		charge_rate_tolerance_check
		low_range()
		return False
	else:
		return True

def charge_rate_tolerance_check(charge_rate):
  if ((charge_rate>=0) and (charge_rate<=((5/100)*0.8))):
    print('Warning: Approaching low charge rate')
  elif ((charge_rate<=0.8) and (charge_rate>=(0.8-(5/100)*0.8))):
    print('Warning: Approaching peak charge rate') 
  else:
    print('Charge-rate is ok')
    
def battery_is_ok(temperature, soc, charge_rate):
	return (temperature_check(temperature) and soc_check(soc) and Charge_rate_check(charge_rate))

def low_range():
	print('Range is low!')

def high_range():
	print('Range is high!')

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(0, 46, 0.5 ) is True)
  assert(battery_is_ok(-1, 58, 0.6)is False)
  assert(battery_is_ok(45, 43, 0.7) is True)
  assert(battery_is_ok(46, 56, 0.5) is False)
  assert(battery_is_ok(15, 20 ,0.5) is True)
  assert(battery_is_ok(24, 80, 0.6)is True)
  assert(battery_is_ok(6, 19, 0.7 ) is False)
  assert(battery_is_ok(44, 81, 0.5) is False)
  assert(battery_is_ok(16, 46, 0.81) is False)
  assert(battery_is_ok(40, 58, 0.9)is False)
  assert(battery_is_ok(38, 43, 0.85) is False)
  assert(battery_is_ok(27, 56, 0.95) is False)
  assert(battery_is_ok(48, 85, 0.9) is False)
  assert(battery_is_ok(10, 50, 0.6) is True)

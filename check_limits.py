def temperature_check(temperature):
	if temperature < 0:
		print('Temperature is out of range!')
		return False
	elif temperature > 45:
		print('Temperature is out of range!')
		return False	
	else :
		return True

def soc_check(soc):
	if soc < 20:
		print('State of Charge is out of range!')
		return False
	elif soc > 80:
		print('State of Charge is out of range!')
		return False
	else:
		return True

def Charge_rate_check(charge_rate):
	if charge_rate > 0.8:
		print('Charge rate is out of range!')
		return False
	elif charge_rate < 0:
		print('Charge rate is out of range!')
		return False
	else:
		return True

def battery_is_ok(temperature, soc, charge_rate):
	return (temperature_check(temperature) and soc_check(soc) and Charge_rate_check(charge_rate)
	
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

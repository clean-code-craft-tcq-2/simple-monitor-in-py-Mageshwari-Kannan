

def battery_is_ok(temperature, soc, charge_rate):
	if (temperature < 0 or temperature > 45) or (soc < 20 or soc > 80) or (charge_rate > 0.8):
		abnormality_check(temperature, soc, charge_rate)
		return False
	else:
		return True

def abnormality_check(temperature, soc, charge_rate):
	print("Abnormal - Out of range!")

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

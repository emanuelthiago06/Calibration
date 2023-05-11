from calibration import Calibration

def run():
    data = [1.98]
    data_st = [1.9965]
    inc_dig = 5
    inc_equi = 0.01
    inc_dig_st = 4
    inc_equi_st = 0.02/100
    test_cal = Calibration(data, data_st,inc_dig,inc_equi,inc_dig_st,inc_equi_st)
    test_cal.is_calibrated()

if __name__ == "__main__":
    run()
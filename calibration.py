from math_helper import *

class Calibration:
    def __init__(self, data : list, data_st : list, inc_dig: int, inc_equi: float, inc_dig_st: int, inc_equi_st: float):
        self.__data = data
        self.__data_st = data_st
        self.__inc_dig_st = inc_dig_st
        self.__inc_equi_st = inc_equi_st
        self.__inc_dig = inc_dig
        self.__inc_equi = inc_equi

    def calc_inc_meas(self, data):
        if len(self.__data) == 1:
            return 0, data[0]
        desv_med,med = get_desv_med(data)
        return desv_med, med

    def calc_res(self,data):
        val = data[0]
        val_str = str(val)
        val_dec = val_str.split('.')
        res = "0."
        for i in range(len(val_dec[-1])-1):
            res = res + "0"
        res = res + "1"
        res = float(res)
        return res

    def calc_inc_res_st(self,res):
        delta_eq = self.__inc_equi_st*self.__med_data_st+self.__inc_dig_st*res
        inc_res = delta_eq/sqrt(3)
        return inc_res

    def calc_max_err(self,res_data):
        self.__max_err = self.__inc_equi*self.__med_data+self.__inc_dig*res_data

    def calc_inc(self):
        self.__inc_meas_data, self.__med_data = self.calc_inc_meas(self.__data)
        self.__inc_meas_data_st,self.__med_data_st = self.calc_inc_meas(self.__data_st)
        self.__res_data = self.calc_res(self.__data)
        res_data_st = self.calc_res(self.__data_st)
        self.__inc_eq_st = self.calc_inc_res_st(res_data_st)
        self.__inc_res = self.__res_data/(2*sqrt(3))
        self.__inc = sqrt(self.__inc_res**2+self.__inc_eq_st**2+self.__inc_meas_data**2+self.__inc_meas_data_st**2)


    def is_calibrated(self):
        self.calc_inc()
        self.calc_max_err(self.__res_data)
        self.__actual_err = abs(self.__med_data-self.__med_data_st)
        max_value = self.__inc+self.__max_err
        min_value = self.__max_err - self.__inc
        if self.__actual_err < min_value:
            print("Está calibrado")
        elif self.__actual_err < max_value:
            print("Zona de incerteza")
        else:
            print("Descalibrado")

    def get_max_err(self):
        return self.__max_err

    def get_actual_err(self):
        return self.__actual_err

    def get_inc(self):
        return self.__inc


        

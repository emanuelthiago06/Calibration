from math import sqrt

def get_desv_med(data):
    med = sum(data)/len(data)
    sum_ = 0
    for number in data:
        sum_ += (number-med)**2
    desv = sqrt(sum_/(len(data)-1))
    desv_med = desv/(sqrt(len(data)))
    return desv_med,med

# done


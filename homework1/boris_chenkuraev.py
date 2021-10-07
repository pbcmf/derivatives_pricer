# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np


class Linear_interpolator():
    def lin_intrplt(arr, value: float):               
        
        
        # Assume that 'arr' have ndarray type, 2 dimensional, and contains at least 2 elements, also value z in 
        # interval beetween min and max
        if (arr[:,0].min()>=value) or (arr[:,0].max()<=value):
            raise Warning("Value z is not in interval (min(x), max(x))")
            
            
        arr = arr[np.argsort(arr[:, 0])]
        
       
        # Finding nearest to value left element in array
        
        idx = np.searchsorted(arr[:, 0], value, side="left")
        if idx >= len(arr):
            idx_nearest = idx_sorted[len(arr)-1]
        elif idx == 0:
            idx_nearest = idx_sorted[0]
        else:
            if abs(value - arr[:, 0][idx-1]) < abs(value - arr[:, 0][idx]):
                idx_nearest = arr[:, 0][idx-1]
            else:
                idx_nearest = arr[:, 0][idx]
        
        # calculate left and right x and y
        
        x_l = arr[:, 0][idx_nearest]
        y_l = arr[:, 1][idx_nearest]
        x_r = arr[:, 0][idx_nearest + 1]
        y_r = arr[:, 1][idx_nearest + 1]
        
        # calculate empirical y for our value with using linear interpolation
        
        y_int = y_l+((value-x_l)/(x_r-x_l))*(y_r-y_l)
        
        return y_int
    
def tests(arr, value, correct_value):
    
    y = Linear_interpolator.lin_intrplt(arr, value)
    
    if (y==correct_value):    
        print("The test finished correctly: computed y = ", y, ", correct = ", correct_value)
    else:
        print("The test finished wrong: computed y = ", y, ", correct = ", correct_value)
        
if __name__ == "__main__":
  #  f(x) = -x + 8
    arr_test = np.array([[1, 7], [2, 6], [3, 5], [4, 4], [5, 3], [6, 2], [7, 1]])     
    tests(arr_test, 4.5, 3.5)       
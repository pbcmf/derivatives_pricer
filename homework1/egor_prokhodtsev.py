import numpy as np
import matplotlib.pyplot as plt

class Pricer:

    def lin_int(X,z):
        
        #check that z is in the range
        if (z< X[0].min()) or (z>X[0].max()):
            raise Warning("Z is not in the range (min(x);max(x))")
        
        #sorting array for all x's be in acending order
        X = X[:, X[0].argsort()]
        
        #finding nearest elemnt to the left of the "z"
        idx = np.argmin(np.abs(np.array(X[0,:])<z))-1
        
        #calculating x's and y's of neighbors of z
        x_0=X[:,idx][0]
        y_0 =X[:,idx][1]
        x_1=X[:,idx+1][0]
        y_1=X[:,idx+1][1]
        
        #calculate end value
        f_z = y_0+(y_1-y_0)/(x_1-x_0)*(z-x_0)

        #plotting position of z and nearest points in array
        plt.plot(X[0,:], X[1,:])
        plt.plot(x_0, y_0, marker="D", markersize=5, markeredgecolor = "black", markerfacecolor="black")
        plt.plot(x_1, y_1, marker="D", markersize=5, markeredgecolor = "black", markerfacecolor="black")
        plt.plot(z, f_z, marker="o", markersize=5, markeredgecolor="red")
        plt.show()

        return f_z

def lin_test(min_x,max_x,n_elements,z,k): #minimal x, maximal x, number of elements, z - parameter of interpolation, k - linear coefficient of initial arrat
    #creating range of x
    x = np.linspace(min_x,max_x,n_elements)
    #calculating related y
    f_x = x*k
    #getting everting together to pass it to lin_int function
    X = np.concatenate([x,f_x]).reshape(2,len(x))
    #getting value from lin_int funtion
    f_z = Pricer.lin_int(X,z)
    #compare result of function to expected value
    return print (f_z==z*k)


lin_test(-10,10,11,9.9,3)


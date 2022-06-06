"""
Created on Mon Jun  6 23:25:47 2022

@author: yipjiaqi
https://github.com/Yip-Jia-Qi/poisson-gap-sampling
"""
import math

def poisson(lmbd, rng):
    '''
    lmbd stands for lambda. 
    λ of 0.0 yields uniform sampling, while a λ of 1.0, for example, creates a nonuniform schedule of 50% overall sampling density
    
    rng is a numpy random generator that is passed into the function as input created using
    rng = np.random.default_rng(2021)
    https://towardsdatascience.com/stop-using-numpy-random-seed-581a9972805f
    '''
    L = math.exp(-lmbd)
    k = 0
    p = 1

    while p>=L:
        k += 1
        p = p*rng.random(1)[0]

    return k-1

def SPS(n_samples, total_samples, rng, apodization=False):
    '''
    n_samples = sampled number of indicies e.g. 64
    total_samples = total number of indices e.g. 256
    rng = numpy.random._generator.Generator object
    apodization = Toggle for whether FID to be subsampled is expected to be apodized. Set to True if FID will be aphodized. Defaults to False.
    '''
    p = n_samples       #sampled number of indicies e.g. 64
    z = total_samples   #total number of indices e.g. 256
    ld = z/p            #1/fraction of the total sampled
    adj = 2.0*(ld-1)    #initial guess of adjustment
    kill = 0            #built-in paramter to kill the while loop if it takes too many iterations
    k=0                 #setting k=0 to initiate the algorithm
    while k != p:
        if kill>50:
            print("algorithm could not converge within 50 iterations. While loop killed")
            break
        kill += 1
        
        i = 0
        k = 0
        v = []
        
        while i<z:
            v.append(i)     #store the point to be acquired
            i += 1          #put pointer to the next point
            k += 1          #next index of acquired point
            
            #now to make poisson distributed gaps that are scaled by a sinosoid 
            frac = ((i+0.5)/(z+1))
            if apodization:
                shape = math.pi/2
            else:
                shape = math.pi                
            sinwave = adj*(math.sin(frac*shape))
            g = poisson(sinwave,rng)
            i += g
            #at the end of this while loop, the number of samples might not be the desired number. 
            #To solve this problem we will scale the adj parameter and try again. 
            #The following if statements (outside of this while loop) will handle this.
                    
        if k>p:
            adj *= 1.01 #the literature uses 1.02 as the scaling factor but i have found that 1.01 seems to converge faster.
        if k<p:
            adj /= 1.01

    return v
        
        

# Sine-weighted Poisson-gap sampling (SPS)

## Introduction
SPS is an algorithm used for sub-sampling Nuclear Magnetic Resonance (NMR) spectra. 

This a python implementation of the Sinusoidal weighted Poisson-Gap Sampling algorithm implemented by Hyberts et. al. originally written in C

"Poisson-Gap Sampling and Forward Maximum Entropy Reconstruction for Enhancing the Resolution and Sensitivity of Protein NMR Data" 
J. Am. Chem. Soc. 2010, 132, 7, 2145–2147
Publication Date:February 2, 2010
https://doi.org/10.1021/ja908004w

    Exerpt from the above
    The quality of spectra obtained from NUS depends crucially on the sampling schedules. 
    In the past, we examined various forms of random sampling and realized that the quality 
    of data retrieval depended significantly on the choice of the seed number when using 
    standard Unix random number generators (e.g., drand48).
    (1) big gaps in the sampling schedule are generally unfavorable and 
    (2) gaps at the beginning or end of the sampling are worse than those in the middle. 
    A third, crucial criterion is that 
    (3) the sampling requires suitably random variation to prevent violation of the Nyquist theorem.
    
    The overall probability f for a specific gap size k ≥ 0 is assumed to 
    be given by the Poisson distribution: f(k; λ) = (λke−λ)/(k!). 
    This would satisfy criteria (1) and (3). 
    Obviously, no integer values of k less than zero are allowed, as no negative gap sizes are realizable.
    
    To satisfy point (2) above, we further optimized the sampling schedule with a sinusoidal variation of λ; 
    we call this sine-weighted Poisson-gap sampling (SPS). 
    Here λ = Λ sin θ, where Λ is an adjustment factor used to make the 
    average λ satisfy the targeted sampling density. θ varies linearly from 0 to π through the 
    sampling schedule when no apodization is applied prior to reconstruction. 
    
    As apodization commonly scales the signal to zero at the end of the evolution time, 
    we restrict the variation of θ from 0 to π/2 when apodization is intended. 
    The method intrinsically imposes some “order”, and sampling points are not chosen fully stochastically. 

Some of the code is also written with some help from https://gwagner.hms.harvard.edu/poisson-gap-sampling

## How to use
SPS.py contains the algorithm as the function SPS. The function will output a list of integers of the desired number of sub-samples.
SPS_test_script.py contains a function to plot the output of SPS and visualize the gaps created by the algoritm. It also serves as a test script and example of how to use the function.


## Code Documentation

SPS(n_samples, total_samples, rng, apodization=False)
Parameters
----------
n_samples : int
    number of sample in the sub sample. must be less than total_samples
total_samples : int
    Total number of samples in fid.
rng : numpy.random._generator.Generator
    numpy random number generator object with seed.
apodization : TYPE, optional
    Toggle for whether FID to be subsampled is expected to be apodized. Set to True if FID will be aphodized. The default is False.
    
Returns
----------
A list of integers of length n_samples, representing the points along the total_samples dimension to be sampled.

plotSPS(v)
    Parameters
    ----------
    v : list
        The output of the SPS function
    
    Returns
    ----------
    None.
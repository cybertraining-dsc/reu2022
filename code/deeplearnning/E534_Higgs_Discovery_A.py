#!/usr/bin/env python
# coding: utf-8

# # A: Studying Higgs Boson Analysis. Signal and Background
# 
# Sloping background as in real experiment

# ## Part 1 The Background
# 
# This file contains the code for the unit "The Elusive Mr. Higgs". It explains the experiment with the Higgs signal and background signal under different settings
# 
# In this part we look at the Background



try:
    from cloudmesh.common.StopWatch import StopWatch
except:  # noqa: E722
    get_ipython().system(' pip install cloudmesh-common')
    from cloudmesh.common.StopWatch import StopWatch




StopWatch.start("total")
StopWatch.start("import")
import numpy as np    # noqa: E402
import matplotlib.pyplot as plt    # noqa: E402
import pylab    # noqa: E402
StopWatch.stop("import")




StopWatch.start("Part 1")
''' Create the background for the setup and plot the same'''
StopWatch.start("data-create-1")
testrand = np.random.rand(42000)                    #A random array have 42000 elements according to the uniform distribution. The numbers generated will between 0 and 1
Base = 110 + 30* np.random.rand(42000)              #Generating a uniform background(base) between a 110 GeV and 140 GeV 
index = (1.0 - 0.5* (Base-110)/30) > testrand       #To create a boolean index which has True for 100% samples at 110GeV; This percentage reduces linearly as the value for background increases and has ture for 50% samples as 140 GeV
sloping = Base[index]                               #This generates a sloping background. Here the values in base corresponding the True values in "index" are retained rest are discarded. So this has a distribution as desribed above
StopWatch.stop("data-create-1")
####Plotting - Sloping Background. 
####See The Plot named "Sloping"
StopWatch.start("data-plot-1")
plt.figure("Sloping")
plt.hist(sloping, bins=15, range =(110,140), color = "green")
plt.title("Sloping Background from 42000 events", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-plot-1")
StopWatch.stop("Part 1")


# ## Part 2 The Higgs Signal
# 
# Create a Gaussian Higgs signal(Gaussian signal is what we will get due to error in measurement). The width of the Gaussian indicated the extent of measurement error. This signal has 300 samples.
# 
# We compare two histogram choices -- 2 GeV or 0.5 GeV  -- each for twop measurement errors 0.5 and 2 GeV
# 
# In the next part Part 3, we combine signal and background



StopWatch.start("Part 2")
StopWatch.start("data-create-2")
gauss = 2 * np.random.randn(300) +126               #The signal is centered at 126 GeV and has a width of 2.
narrowGauss = 0.5 * np.random.randn(300) +126        #A signal with centered at 126 GeV and width of 0.5(Error in measurement is less than previous signal"
StopWatch.start("data-create-2")
####Plotting - The Higgs Signal with width 2.0. 
####See The Plot named "HiggsAlone"
StopWatch.start("data-plot-2")
plt.figure("HiggsAlone-1")
plt.hist(gauss, bins=15, range =(110,140), color = "red")
plt.hist(narrowGauss, bins=15, range =(110,140), color = "black")
plt.title("2 Gev and 0.5 GeV Higgs in 2 GeV bins on their own", backgroundcolor = "white")
plt.show()
plt.figure("HiggsAlone-2")
plt.hist(gauss, bins=60, range =(110,140), color = "red")
plt.hist(narrowGauss, bins=60, range =(110,140), color = "black")
plt.title("2 Gev and 0.5 GeV Higgs in 0.5 GeV bins on their own", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-create-2")
StopWatch.stop("Part 2")


# ## Part 3 Higgs plus Background
# 
# Create the actual Signal by combining the Higgs signals(Gaussian shape) and the sloping background signal. 
# 
# We look at 2 different widths for the Higgs
# 
# Note Higgs width is entirely due to measurement error. The Higgs has a natural width as it is NOT stable but rather decays. This natural width can only be estimated at present from observed decay rate and it is < 10 MeV - a factor of more than 100 lower than observed width. 
# 
# As width coming from measurement errors, it is expected to be Gaussian. It would be a different shape (Breit Wigner) if coming from its Quantum properties
# 
# The three plots fix the measurement with at 0.5 GeV and vary your choice as a data analyst; namely the bin size of histogram. The 0.5 GeV bin size seems best



StopWatch.start("Part 3")
StopWatch.start("data-create-3")
total = np.concatenate((sloping, gauss))            #Accumalate the sloping Background and gauss(width = 2.0)
narrowTotal = np.concatenate((sloping, narrowGauss)) #Accumalate the sloping background and narrowGauss(width = 0.5)
StopWatch.stop("data-create-3")
####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 0.5. The plot has 15 bins(each bin represents 2 GeV). 
####See The Plot named "Total Narrow Higgs"
StopWatch.start("data-plot-3")
plt.figure("Total Narrow Higgs")
plt.hist(narrowTotal, bins=15, range =(110,140), alpha = 0.5, color = "blue")   #Total Signal
plt.hist(sloping, bins=15, range =(110,140), alpha = 0.5, color = "green")       #Sloping Signal.
plt.hist(narrowGauss, bins=15, range =(110,140), alpha = 0.5, color = "red")   #Only the Higgs Signal.
plt.title("0.5 Gev Higgs in 2 GeV bins with Sloping Background", backgroundcolor = "white")
plt.show()

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 0.5. The plot has 30 bins(each bin represents 1GeV).
####See The Plot named "Total Narrow Higgs Bin 1 GeV"
plt.figure("Total Narrow Higgs Bin 1 GeV")
plt.hist(narrowTotal, bins=30, range =(110,140), alpha = 0.5, color = "blue")   #Total Signal
plt.hist(sloping, bins=30, range =(110,140), alpha = 0.5, color = "green")       #Sloping Signal.      
plt.hist(narrowGauss, bins=30, range =(110,140), alpha = 0.5, color = "red")   #Only the Higgs Signal.
plt.title("0.5 Gev Higgs in 1 GeV bins with Sloping Background", backgroundcolor = "white")
plt.show()

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 0.5. The plot has 60 bins(each bin represents 0.5GeV).
####See The Plot named "Total Narrow Higgs Bin 0.5 GeV"
plt.figure("Total Narrow Higgs Bin 0.5 GeV")
plt.hist(narrowTotal, bins=60, range =(110,140), alpha = 0.5, color = "blue")   #Total Signal
plt.hist(sloping, bins=60, range =(110,140), alpha = 0.5, color = "green")       #Sloping Signal.
plt.hist(narrowGauss, bins=60, range =(110,140), alpha = 0.5, color = "red")   #Only the Higgs Signal.
plt.title("0.5 Gev Higgs in 0.5 GeV bins with Sloping Background", backgroundcolor = "white")
plt.show()


# Here we look at a 2 GeV wide Higgs Boson. It does not stand out!



####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) signal where Higgs Signal has width 2.0. The plot has 15 bins(each bin represents 2GeV).
####See The Plot named "Total Wide Higgs Bin 2 GeV"
plt.figure("Total Wide Higgs Bin 2 GeV")
values, binedges, junk = plt.hist(total, bins=15, range =(110,140), alpha = 0.5, color = "blue")     #Total Signal. We also store the histogram values(number of members per bin) and binedges.
plt.hist(sloping, bins=15, range =(110,140), alpha = 0.5, color = "green")                           #Sloping Signal.
plt.hist(gauss, bins=15, range =(110,140), alpha = 0.5, color = "red")                               #Only the Higgs Signal.
plt.title("2 Gev Higgs in 2 GeV bins with Sloping Background", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-plot-3")
StopWatch.stop("Part 3")


# ## Part 4 Error Estimates
# 
# Computing the bin Centers and Errors where latter come from rule for counting experiments that an observation of N events has an error sqrt(N)
# 
# The error bars are quite small as 2500 has error 50 which is 2%). They are bigger at the end when we reduce total number of events.



StopWatch.start("Part 4")
StopWatch.start("data-create-4")
centers = 0.5*(binedges[1:] + binedges[:-1])                            #Computing bin center as the average of its 2 bin-edges.
errors = np.sqrt(values)                                                #Computing expected error as the square root of values.
StopWatch.stop("data-create-4")
####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) and expected errors where Higgs Signal has width 2.0. The plot has 60 bins(each bin represents 0.5GeV).
####See The Plot named "Total Wide Higgs Bin 2 GeV with errors"
StopWatch.start("data-plot-4")
plt.figure("Total Wide Higgs Bin 2 GeV with errors")
plt.hist(total, bins=15, range =(110,140), alpha = 0.5, color = "blue")                                 #The total signal
plt.hist(sloping, bins=15, range =(110,140), alpha = 0.5, color = "green")                              #Sloping Signal.
plt.hist(gauss, bins=15, range =(110,140), alpha = 0.5, color = "red")                                  #Only the Higgs Signal.
plt.errorbar(centers, values, yerr = errors, ls='None', marker ='x', color = 'black', markersize= 6.0 ) #The error bar
plt.title("2 Gev Higgs in 2 GeV bins with Sloping Background + Errors", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-plot-4")
StopWatch.stop("Part 4")


# ## Part 5 A Larger Signal
# 
# Creating a Higgs Signal with 30000 elements. If we use this against the original backgrounds, we study the effect of making the Higgs 100 times more likely(The original number of Higgs samples was 300).



StopWatch.start("Part 5")
print('Higgs on its own with no background')
StopWatch.start("data-create-5")
gaussbig = 2 * np.random.randn(30000) +126                  #Creating a Higgs Signal with 30000 elements and width of 2.0
gaussnarrowbig = 0.5 * np.random.randn(30000) +126          #Creating a Higgs Signal with 30000 elements and width of 0.5(less error in measurement than previous case)
totalbig = np.concatenate((sloping, gaussbig))
StopWatch.stop("data-create-5")
####Plotting - The Pure Higgs Signals with weight 0.5 and 2. The signal with 30,000 elements is used. Plot has 60 bins(each of size .5GeV).
####See The Plot named "30000 Higgs in 0.5 GeV bins"
StopWatch.start("data-plot-5")
plt.figure("30000 Higgs in 0.5 GeV bins")
plt.hist(gaussnarrowbig, bins=60, range =(110,140), alpha = 0.5) #Higgs signal 
plt.hist(gaussbig, bins=60, range =(110,140), alpha = 0.5)
plt.title("30000 Narrow and Wide Higgs in 0.5 GeV bins", backgroundcolor = "white")
plt.show()

print('\nLarge Higgs signal on original size background')

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 2.0 and is 100 times more frequent. The plot has 15 bins(each bin represents 2GeV).
####See The Plot named "Total Wide Higgs Bin 2 GeV 100 times Higgs" 
plt.figure("Total Wide Higgs Bin 2 GeV 100 times Higgs")
plt.hist(totalbig, bins=15, range =(110,140), alpha = 0.5)                          #Total signal with Higgs being 100 times more frequent
plt.hist(sloping, bins=15, range =(110,140), alpha = 0.5)                           #sloping background
plt.hist(gaussbig, bins=15, range =(110,140), alpha = 0.5)                          #Higgs signal with 30,000 elements
plt.title("Total Wide Higgs Bin 2 GeV 100 times Higgs", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-plot-5")
StopWatch.stop("Part 5")


# ## Part 6 A Small Experiment (1% original)
# 
# Creating a setup with 1% data. Now the background has initially 420 elements
# 
# This data fluctuates too much and you wont see any signal from Higgs (only 3 particles expected)



StopWatch.start("Part 6")
StopWatch.start("data-create-6")
testrand420 = np.random.rand(420)                               #Creating random array with 420 elements.
Base420 = 110 + 30* np.random.rand(420)                         #Creating Background with 420 events 
index420 = (1.0 - 0.5* (Base420-110)/30) > testrand420          #Creating index to get the sloping background.
Sloping420 = Base420[index420]                                  #Creating Sloping Background
StopWatch.stop("data-create-6")
#### Plot - Plotting the 1% background data. Plot has 15 bins(each 2GeV)
####See The Plot named "Sloping 420 Events"
StopWatch.start("data-plot-6")
plt.figure("Sloping 420 Events")
plt.hist(Sloping420, bins=15, range =(110,140))
plt.title("Sloping Background from 420 events (1%)", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-plot-6")
StopWatch.stop("Part 6")


# ## Part 7 Medium Size Experiment
# 
# Creating setup with 10% data(4200 elements for background, 30 elements for Higgs signal) and computing the errors.



StopWatch.start("Part 7")
StopWatch.start("data-create-7")
testrand4200 = np.random.rand(4200)                             #Creating random array with 4200 elements.
Base4200 = 110 + 30* np.random.rand(4200)                       #Creating Background with 4200 events 
index4200 = (1.0 - 0.5* (Base4200-110)/30) > testrand4200       #Creating index to get the sloping background.
Sloping4200 = Base4200[index4200]                               #Creating Sloping Background
gauss30 = 2 * np.random.randn(30) +126                          #Creating Higgs signal with width 2.0 and center at 126GeV
total10percent = np.concatenate((Sloping4200, gauss30))         #Combining the Higgs signal and sloping background
StopWatch.stop("data-create-7")
####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 2.0 for 10% of data. The plot has 15 bins(each bin represents 2GeV).
####See The Plot named "Total Sloping Background 10% Data"
StopWatch.start("data-plot-7")
plt.figure("Total Sloping Background 10% Data")
values10percent, binedges10percent, junk = plt.hist(total10percent, bins=15, range =(110,140), alpha = 0.5, color = "blue") #Total signal and storing the number values/bin and the bin edges.
plt.hist(Sloping4200, bins=15, range =(110,140), alpha = 0.5, color = "green")                                              #Sloping background
plt.hist(gauss30, bins=15, range =(110,140), alpha = 0.5, color = "red")                                                    #Higgs Signal(width 2.0)
plt.title("Total with Sloping Background from 4200 events (10%)", backgroundcolor = "white")
plt.show()

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) and the error where Higgs Signal has width 2.0 for 10% of data. The plot has 15 bins(each bin represents 2GeV).
####See The Plot named "Total Sloping Background 10% Data with errors"
plt.figure("Total Sloping Background 10% Data with errors")
centers10percent = 0.5*(binedges10percent[1:] + binedges10percent[:-1])             #Computing the bin centers
errors10percent = np.sqrt(values10percent)                                          #Computing expected errors
plt.hist(total10percent, bins=15, range =(110,140), alpha = 0.5, color = "blue")    #Plotting the total signal
plt.hist(Sloping4200, bins=15, range =(110,140), alpha = 0.5, color = "green")      #Plotting the sloping background
plt.hist(gauss30, bins=15, range =(110,140), alpha = 0.5, color = "red")            #Plotting the Higgs Signal
plt.errorbar(centers10percent, values10percent, yerr = errors10percent, ls='None', marker ='x', color = 'black', markersize= 6.0 ) #Plotting the error
plt.title("Total with Sloping Background from 4200 events (10%) + Errors", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-plot-7")
StopWatch.stop("Part 7")
StopWatch.stop("total")
StopWatch.benchmark()







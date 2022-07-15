#!/usr/bin/env python
# coding: utf-8

# # B: Studying Higgs Boson Analysis. Signal and Background
# 
# ## Study of a Uniform -- not a Sloping Background



try:
    from cloudmesh.common.StopWatch import StopWatch
except:  # noqa: E722
    get_ipython().system(' pip install cloudmesh-common')
    from cloudmesh.common.StopWatch import StopWatch




StopWatch.start("total")
StopWatch.progress(0)
StopWatch.start("import")
import numpy as np    # noqa: E402
import matplotlib.pyplot as plt    # noqa: E402
# import pylab
StopWatch.stop("import")
StopWatch.progress(60)

StopWatch.start("data-create-1")
Base = 110 + 30 * np.random.rand(42000)
# Base is set of observations with an expected 2800 background events  per bin
# Note we assume here flat but in class I used a "sloping" curve that represented experiment better
gauss = 2 * np.random.randn(300) + 126
# Gauss is Number of Higgs particles
simpletotal = np.concatenate((Base, gauss))
# simpletotal is Higgs+Background
StopWatch.stop("data-create-1")
StopWatch.progress(61)

StopWatch.start("data-plot-1")
plt.figure("Total Wide Higgs Bin 2 GeV")
values, binedges, junk = plt.hist(simpletotal, bins=15, range=(110,140), alpha=0.5, color="blue")
centers = 0.5 * (binedges[1:] + binedges[:-1])
# centers is center of each bin
# values is number of events in each bin
# :-1 is same as :Largest Index-1
# binedges[:-1] gets you lower limit of bin
# 1: gives you array starts at second index (labelled 1 as first index 0)
# binedges[1:] is upper limit of each bin
# Note binedges has Number of Bins + 1 entries; centers has Number of Bins entries
errors =np.sqrt(values)
# errors is expected error for each bin
plt.hist(Base, bins=15, range =(110,140), alpha = 0.5, color="green")
plt.hist(gauss, bins=15, range =(110,140), alpha = 0.5, color="red")
plt.errorbar(centers, values, yerr = errors, ls='None', marker ='x', color = 'black', markersize= 6.0 )
plt.title("Uniform Background from 42000 events; 2 Gev Higgs", backgroundcolor = "white")
# For Agg backend
plt.show()
StopWatch.stop("data-plot-1")
StopWatch.progress(75)

StopWatch.start("data-create-2")
NarrowGauss = 0.5 * np.random.randn(300) + 126
# NarrowGauss is Number of Higgs particles
simpletotal = np.concatenate((Base, NarrowGauss))
plt.figure("Total Narrow Higgs Bin 2 GeV")
values, binedges, junk = plt.hist(simpletotal, bins=15, range =(110,140), alpha = 0.5, color="blue")
centers = 0.5*(binedges[1:] + binedges[:-1])
errors =np.sqrt(values)
StopWatch.stop("data-create-2")
StopWatch.progress(80)

StopWatch.start("data-plot-2")
plt.hist(Base, bins=15, range =(110,140), alpha = 0.5, color="green")
plt.hist(NarrowGauss, bins=15, range =(110,140), alpha = 0.5, color="red")
plt.errorbar(centers, values, yerr = errors, ls='None', marker ='x', color = 'black', markersize= 6.0 )
plt.title("Uniform Background from 42000 events; 0.5 Gev Higgs", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-plot-2")
StopWatch.progress(85)

StopWatch.start("data-create-3")
plt.figure("Total Narrow Higgs Bin 0.5 GeV")
values, binedges, junk = plt.hist(simpletotal, bins=60, range =(110,140), alpha = 0.5, color="blue")
centers = 0.5*(binedges[1:] + binedges[:-1])
errors =np.sqrt(values)
StopWatch.stop("data-create-3")
StopWatch.progress(90)

StopWatch.start("data-plot-3")
plt.hist(Base, bins=60, range =(110,140), alpha = 0.5, color="green")
plt.hist(NarrowGauss, bins=60, range =(110,140), alpha = 0.5, color="red")
plt.errorbar(centers, values, yerr = errors, ls='None', marker ='x', color = 'black', markersize= 6.0 )
plt.title("Uniform Background from 42000 events; 0.5 Gev Higgs", backgroundcolor = "white")
plt.show()
StopWatch.stop("data-plot-3")
StopWatch.stop("total")
StopWatch.benchmark()
StopWatch.progress(100)


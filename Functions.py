import pandas

from ConsumerGoods import ConsumerGoods
from ConsumerServices import ConsumerServices
from DowTransportation import DowTransportation
from DateEnum import DowDates
from DateEnum import SectorDates
from Financials import Financials
from HealthCare import HealthCare
import numpy
from DowIndustrial import DowIndustrial
from DowUtilities import DowUtilities
from MidCap import MidCap
from Materials import Materials
import time
from MegaCap import MegaCap
from OilAndGas import OilAndGas
from REITs import REITs
from SmallCap import SmallCap
from SmallCapREITs import SmallCapREITs
from Technology import Technology
from Telecom import Telecom
from TotalMarket import TotalMarket

dt = DowTransportation

def getAverageValue(start, startfromenum, end, endfromenum, datefunc, returnfunc):
    if startfromenum == True and endfromenum == True:
        startdate = start.value
        enddate = end.value
    elif startfromenum == True and endfromenum == False:
        startdate = start.value
        enddate = pandas.to_datetime(end)
    elif startfromenum == False and endfromenum == True:
        startdate = pandas.to_datetime(start)
        enddate = end.value
    elif startfromenum == False and endfromenum == False:
        startdate = pandas.to_datetime(start)
        enddate = pandas.to_datetime(end)
    else:
        print("invalid booleans")
    date = datefunc.tolist()
    startvalue = date.index(startdate)
    endvalue = date.index(enddate)
    volatilityvalues = returnfunc[startvalue:endvalue]
    volatilityvalues = numpy.array(volatilityvalues)
    averagevolatility = numpy.mean(volatilityvalues)
    return averagevolatility, startdate


def outliers(datefunc, returnfunc):
    array = numpy.array(returnfunc)
    returnlist = returnfunc.tolist()
    stddev = numpy.std(array)
    mean = numpy.mean(array)
    print(mean)
    print(stddev)
    print(mean + stddev * 2)
    for value in returnfunc:
        if value > (mean + stddev * 2) or value < (mean - stddev * 2):
            datevalue = returnlist.index(value)
            date = datefunc[datevalue]
            print(date, value)


def averagevaluemain():
    h = Technology()
    a = [e for e in SectorDates]
    h.timeseries()
    h.archmodel()
    h.egarchmodel()
    for date in a:
        start = a.index(date)
        end = start + 1
        endd = a[end]
        result = getAverageValue(date, True, endd, True, h.technologyDate, h.evolatility)
        print(result)
        time.sleep(0.05)


def outliersmain():
    h = Technology()
    h.timeseries()
    h.archmodel()
    h.egarchmodel()
    result = outliers(h.technologyDate, h.evolatility)
    print(result)


if __name__ == '__main__':
    outliersmain()
    #averagevaluemain()


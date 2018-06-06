import arch.univariate as arch
import pandas

from ConsumerGoods import ConsumerGoods
from ConsumerServices import ConsumerServices
from HealthCare import HealthCare
from MidCap import MidCap
from Materials import Materials
from MegaCap import MegaCap
from DowTransportation import DowTransportation
from DowUtilities import DowUtilities
from DowIndustrial import DowIndustrial
from DateEnum import SectorDates, DowDates
import math
import scipy

from OilAndGas import OilAndGas
from REITs import REITs
from SmallCap import SmallCap
from SmallCapREITs import SmallCapREITs
from Technology import Technology
from Telecom import Telecom
from TotalMarket import TotalMarket


def getarchreturn(start, startfromenum, end, endfromenum, datefunc, returnfunc):
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
    startindex = date.index(startdate)
    endindex = date.index(enddate)
    archrange = returnfunc[startindex:endindex]
    am = arch.arch_model(archrange)
    amres = am.fit(update_freq=5)
    print(amres.summary())

def getegarchreturn(start, startfromenum, end, endfromenum, datefunc, returnfunc):
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
    startindex = date.index(startdate)
    endindex = date.index(enddate)
    archrange = returnfunc[startindex:endindex]
    am = arch.arch_model(archrange)
    am.volatility = arch.EGARCH(p=2, o=1, q=1)
    amres = am.fit(update_freq=0)
    print(amres)
    return amres.params


if __name__ == '__main__':

    m = Technology()
    m1 = m.technologyDate[1517]
    m2 = m.technologyDate[0]
    getegarchreturn('1/3/2017', False, m1, False, m.technologyDate, m.technologyARCHReturn)

import pandas

from ConsumerGoods import ConsumerGoods
from ConsumerServices import ConsumerServices
from DateEnum import SectorDates
from Financials import Financials
from MidCap import MidCap
from MegaCap import MegaCap
from OilAndGas import OilAndGas
import time

from SmallCapREITs import SmallCapREITs
from REITs import REITs
from SmallCap import SmallCap
from Technology import Technology
from Telecom import Telecom
from TotalMarket import TotalMarket

PATH = r"C:\Users\test\Desktop\IR excel spreadsheets\Dow Jones Things.xlsx", \
       r"C:\Users\test\Desktop\IR excel spreadsheets\BIG MASTER SHEET .xlsx",\
       r"C:\Users\test\Desktop\IR excel spreadsheets\DGS10.xlsx", \
       r"C:\Users\test\Desktop\IR excel spreadsheets\DGS1.xlsx", \
       r"C:\Users\test\Desktop\IR excel spreadsheets\DGS1MO.xlsx"

treasury10YearData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\DGS10.xlsx")
treasury10YearDate = treasury10YearData.observation_date
treasury10YearDate = pandas.to_datetime(treasury10YearDate)
treasury10YearDate = treasury10YearDate.tolist()
treasury10YearReturn = treasury10YearData.DGS10

treasury1YearData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\DGS1.xlsx")
treasury1YearDate = treasury1YearData.observation_date
treasury1YearDate = pandas.to_datetime(treasury1YearDate)
treasury1YearDate = treasury1YearDate.tolist()
treasury1YearReturn = treasury1YearData.DGS1

treasury1MonthData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\DGS1MO.xlsx")
treasury1MonthDate = treasury1MonthData.observation_date
treasury1MonthDate = pandas.to_datetime(treasury1MonthDate)
treasury1MonthDate = treasury1MonthDate.tolist()
treasury1MonthReturn = treasury1MonthData.DGS1MO


def getMarketReturn(start, end, datefunc, returnfunc):
    """

    :param start: Start Date
    :param end: End Date
    :param datefunc: Function used for Date
    :param returnfunc: Function used for returns
    :return: Start Date, End Date, Percentage of market return over given period
    """
    startdate = pandas.to_datetime(start)
    enddate = pandas.to_datetime(end)
    date = datefunc.tolist()
    startvalue = date.index(startdate)
    startvalue = returnfunc.index[startvalue]
    endvalue = date.index(enddate)
    endvalue = returnfunc.index[endvalue]
    return startdate, enddate, (1 - (startvalue/endvalue)) * 100


def getIntersect(a):
    """

    :param a: Date of desired treasury yield
    :return: Desired treasury yield
    """
    date = pandas.to_datetime(a)
    intersect = treasury10YearDate.index(date)
    return intersect, treasury10YearReturn[intersect]

def getExcessReturn(start, startfromenum, end, endfromenum, datefunc, returnfunc, treasurylength):
    """

    :param start: Start Date
    :param end: End Date
    :param datefunc: Function of Dates
    :param returnfunc: Function of Market Returns
    :param treasurylength: Length of desired treasury bill
        Options: one month, one year, ten year
    :param startfromenum: Boolean, are start dates from Enum
    :param endfromenum: Boolean, are end dates from Enum
    :return: Start Date, End Date, Market Return, Treasury Yield, Excess Return
    """
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
    startvalue = returnfunc[startvalue]
    endvalue = date.index(enddate)
    endvalue = returnfunc[endvalue]
    if treasurylength == "ten year":
        intersect = treasury10YearDate.index(startdate)
        treasuryyield = treasury10YearReturn[intersect]
    elif treasurylength == "one year":
        intersect = treasury1YearDate.index(startdate)
        treasuryyield = treasury1YearReturn[intersect]
    elif treasurylength == "one month":
        intersect = treasury1MonthDate.index(startdate)
        treasuryyield = treasury1MonthReturn[intersect]
    else:
        print("invalid treasury length")
    marketreturn = (1 - (startvalue / endvalue)) * 100
    excessreturn = marketreturn - treasuryyield
    return startdate, marketreturn

def getExcessReturna(start, startfromenum, end, endfromenum, datefunc, returnfunc, treasurylength):
    """

    :param start: Start Date
    :param end: End Date
    :param datefunc: Function of Dates
    :param returnfunc: Function of Market Returns
    :param treasurylength: Length of desired treasury bill
        Options: one month, one year, ten year
    :param startfromenum: Boolean, are start dates from Enum
    :param endfromenum: Boolean, are end dates from Enum
    :return: Start Date, End Date, Market Return, Treasury Yield, Excess Return
    """
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
    startvalue = returnfunc[startvalue]
    endvalue = date.index(enddate)
    endvalue = returnfunc[endvalue]
    if treasurylength == "ten year":
        intersect = treasury10YearDate.index(startdate)
        treasuryyield = treasury10YearReturn[intersect]
    elif treasurylength == "one year":
        intersect = treasury1YearDate.index(startdate)
        treasuryyield = treasury1YearReturn[intersect]
    elif treasurylength == "one month":
        intersect = treasury1MonthDate.index(startdate)
        treasuryyield = treasury1MonthReturn[intersect]
    else:
        print("invalid treasury length")
    marketreturn = (1 - (startvalue / endvalue)) * 100
    excessreturn = marketreturn - treasuryyield
    return startdate, treasuryyield

def getExcessReturnb(start, startfromenum, end, endfromenum, datefunc, returnfunc, treasurylength):
    """

    :param start: Start Date
    :param end: End Date
    :param datefunc: Function of Dates
    :param returnfunc: Function of Market Returns
    :param treasurylength: Length of desired treasury bill
        Options: one month, one year, ten year
    :param startfromenum: Boolean, are start dates from Enum
    :param endfromenum: Boolean, are end dates from Enum
    :return: Start Date, End Date, Market Return, Treasury Yield, Excess Return
    """
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
    startvalue = returnfunc[startvalue]
    endvalue = date.index(enddate)
    endvalue = returnfunc[endvalue]
    if treasurylength == "ten year":
        intersect = treasury10YearDate.index(startdate)
        treasuryyield = treasury10YearReturn[intersect]
    elif treasurylength == "one year":
        intersect = treasury1YearDate.index(startdate)
        treasuryyield = treasury1YearReturn[intersect]
    elif treasurylength == "one month":
        intersect = treasury1MonthDate.index(startdate)
        treasuryyield = treasury1MonthReturn[intersect]
    else:
        print("invalid treasury length")
    marketreturn = (1 - (startvalue / endvalue)) * 100
    excessreturn = marketreturn - treasuryyield
    return startdate, excessreturn


if __name__ == '__main__':
    d = Technology()
    a = [e for e in SectorDates]
    tenyear = "ten year"
    month = "one month"
    year = "one year"
    for date in a:
        startd = a.index(date)
        end = startd+1
        endd = a[end]
        result = getExcessReturnb(date, True, endd, True, d.technologyDate, d.technologyReturn, tenyear)
        print(result)
        time.sleep(0.05)








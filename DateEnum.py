from enum import Enum
import pandas

PATH = r"C:\Users\test\Desktop\IR excel spreadsheets\Dow Jones Things.xlsx", r"C:\Users\test\Desktop\IR excel spreadsheets\BIG MASTER SHEET .xlsx"
dowData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\Dow Jones Things.xlsx")
secData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\BIG MASTER SHEET .xlsx")
dowDate = dowData.Date
secDate = secData.Date
dowDate = pandas.to_datetime(dowDate)
secDate = pandas.to_datetime(secDate)


class SectorDates(Enum):
    #D1 = secDate[1]
    #D2 = secDate[192]
    D2_5 = secDate[211]
    D3 = secDate[443]
    D4 = secDate[695]
    D5 = secDate[947]
    D6 = secDate[1198]
    D7 = secDate[1450]
    D8 = secDate[1702]


class DowDates(Enum):
    DJ1 = dowDate[0]
    DJ2 = dowDate[252]
    DJ3 = dowDate[503]
    DJ4 = dowDate[755]
    DJ5 = dowDate[1006]
    DJ5_5 = dowDate[1260]
    DJ6 = dowDate[1512]
    DJ7 = dowDate[1762]
    DJ8 = dowDate[2014]
    DJ9 = dowDate[2240]
    DJ10 = dowDate[2489]
    DJ11 = dowDate[2743]
    DJ12 = dowDate[2996]
    DJ13 = dowDate[3248]
    DJ14 = dowDate[3500]
    DJ15 = dowDate[3753]
    DJ16 = dowDate[4005]
    DJ17 = dowDate[4258]
    DJ18 = dowDate[4510]
    DJ19 = dowDate[4763]
    DJ20 = dowDate[5016]
    DJ21 = dowDate[5269]
    DJ22 = dowDate[5521]
    DJ23 = dowDate[5774]
    DJ23_5 = dowDate[6029]
    DJ24 = dowDate[6281]
    DJ25 = dowDate[6533]
    DJ26 = dowDate[6786]
    DJ27 = dowDate[7038]
    DJ28 = dowDate[7291]
    DJ29 = dowDate[7544]
    DJ30 = dowDate[7796]
    DJ31 = dowDate[8050]
    DJ32 = dowDate[8303]
    DJ33 = dowDate[8556]
    DJ34 = dowDate[8809]
    DJ35 = dowDate[9065]
    DJ36 = dowDate[9326]
    DJ37 = dowDate[9581]
    DJ38 = dowDate[9838]
    DJ39 = dowDate[10096]
    DJ40 = dowDate[10355]
    DJ41 = dowDate[10610]
    DJ42 = dowDate[10862]
    DJ43 = dowDate[11114]
    DJ44 = dowDate[11365]
    DJ45 = dowDate[11617]
    DJ46 = dowDate[11868]





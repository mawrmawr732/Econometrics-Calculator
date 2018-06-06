import matplotlib.pyplot as plt
import arch.univariate as arch
import pandas


PATH = r"C:\Users\test\Desktop\IR excel spreadsheets\Dow Jones Things.xlsx"


class DowIndustrial():
    def __init__(self):
        dowData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\Dow Jones Things.xlsx")
        self.dowDate = dowData.Date
        self.dowDate = pandas.to_datetime(self.dowDate)
        self.modelDate = self.dowDate.drop(self.dowDate.index[0])
        self.modelOneDate = self.dowDate.index[0:4000]
        self.modelTwoDate = self.dowDate.index[4000:8000]
        self.modelThreeDate = self.dowDate[8000:11928]
        self.dowIndustrialReturn = dowData.Industrial
        self.dowIndustrialARCHReturn = 100 * self.dowIndustrialReturn.pct_change().dropna()

        self.xposition = ['20JANUARY1961', '3JANUARY1963', '20JANUARY1965', '3JANUARY1967',
                          '20JANUARY1969', '3JANUARY1971', '20JANUARY1973', '3JANUARY1975',
                          '20JANUARY1977', '3JANUARY1979', '20JANUARY1981', '3JANUARY1983',
                          '20JANUARY1985', '3JANUARY1987', '20JANUARY1989', '3JANUARY1991',
                          '20JANUARY1993', '3JANUARY1995', '20JANUARY1997', '3JANUARY1999',
                          '20JANUARY2001', '3JANUARY2003', '20JANUARY2005', '3JANUARY2007',
                          '20JANUARY2009', '3JANUARY2011', '20JANUARY2013', '3JANUARY2015',
                          '20JANUARY2017']
        self.xposition = pandas.to_datetime(self.xposition)

    def timeseries(self):
        print(self.modelDate)
        print(self.dowDate)
        print(self.dowIndustrialReturn)
        fig1 = plt.figure()
        dowIndustrialGraph = fig1.add_subplot(111)
        dowIndustrialGraph.plot(self.dowDate, self.dowIndustrialReturn)
        fig1.autofmt_xdate()
        dowIndustrialGraph.set_title('Time Series')
        fig1.draw

        plt.show()

    def archmodel(self):
        self.am = arch.arch_model(self.dowIndustrialARCHReturn)
        self.amres = self.am.fit(update_freq=5)
        print(self.amres.summary())

        archFig = plt.figure()

        self.aresiduals = self.amres.resid / self.amres.conditional_volatility
        argraphone = archFig.add_subplot(212)
        argraphone.plot(self.modelDate, self.aresiduals)


        self.avolatility = self.amres._volatility
        avgraphone = archFig.add_subplot(211)
        avgraphone.plot(self.modelDate, self.avolatility)
        argraphone.set_title('ARCH Standardized Residuals')
        avgraphone.set_title('ARCH Conditional Volatility')


        plt.show()

    def egarchmodel(self):
        ae = self.am
        ae.volatility = arch.EGARCH(p=2, o=1, q=1)
        self.aeres = ae.fit(update_freq=0)
        print(self.aeres.summary())

        egarchFig = plt.figure()

        self.eresiduals = self.aeres.resid / self.aeres.conditional_volatility
        ergraphone = egarchFig.add_subplot(212)
        ergraphone.plot(self.modelDate, self.eresiduals)

        self.evolatility = self.aeres._volatility
        evgraphone = egarchFig.add_subplot(211)
        evgraphone.plot(self.modelDate, self.evolatility)
        ergraphone.set_title('EGARCH Standardized Residuals')
        evgraphone.set_title('EGARCH Conditional Volatility')

        for xc in self.xposition:
            ergraphone.axvline(x=xc, color='k', linestyle='-')
            evgraphone.axvline(x=xc, color='k', linestyle='-')


        plt.show()


if __name__ == '__main__':
    d = DowIndustrial()
    d.timeseries()
    d.archmodel()
    d.egarchmodel()

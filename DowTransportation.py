import matplotlib.pyplot as plt
import arch.univariate as arch
import pandas


PATH = r"C:\Users\test\Desktop\IR excel spreadsheets\Dow Jones Things.xlsx"


class DowTransportation():
    def __init__(self):
        dowData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\Dow Jones Things.xlsx")
        self.dowDate = dowData.Date
        self.dowDate = pandas.to_datetime(self.dowDate)
        self.modelDate = self.dowDate.drop(self.dowDate.index[0])
        self.dowTransportationReturn = dowData.Transportation
        self.dowTransportationARCHReturn = 100 * self.dowTransportationReturn.pct_change().dropna()

        self.xposition = ['20JANUARY1961', '3JANUARY1963', '20JANUARY1965', '3JANUARY1967',
                          '20JANUARY1969', '3JANUARY1971', '20JANUARY1973', '3JANUARY1975',
                          '20JANUARY1977', '3JANUARY1979', '20JANUARY1981', '3JANUARY1983',
                          '20JANUARY1985', '3JANUARY1987', '20JANUARY1989', '3JANUARY1991',
                          '20JANUARY1993', '3JANUARY1995', '20JANUARY1997', '3JANUARY1999',
                          '20JANUARY2001', '3JANUARY2003', '20JANUARY2005', '3JANUARY2007',
                          '20JANUARY2009', '3JANUARY2011', '20JANUARY2013', '3JANUARY2015',
                          '20JANUARY2017']
        self.xposition = pandas.to_datetime(self.xposition)
        self.evolatility = None

    def timeseries(self):
        fig1 = plt.figure()
        dowTransportationGraph = fig1.add_subplot(111)
        dowTransportationGraph.plot(self.dowDate, self.dowTransportationReturn)
        dowTransportationGraph.set_title('Time Series')

        fig1.autofmt_xdate()
        fig1.draw

        plt.show()

    def archmodel(self):
        self.am = arch.arch_model(self.dowTransportationARCHReturn)
        self.amres = self.am.fit(update_freq=5)
        print(self.amres.summary())
        archFig = plt.figure()
        self.aresiduals = self.amres.resid / self.amres.conditional_volatility
        argraph = archFig.add_subplot(212)
        argraph.plot(self.modelDate, self.aresiduals)
        self.avolatility = self.amres._volatility
        avgraph = archFig.add_subplot(211)
        avgraph.plot(self.modelDate, self.avolatility)
        argraph.set_title('ARCH Standardized Residuals')
        avgraph.set_title('ARCH Conditional Volatility')

        plt.show()

    def egarchmodel(self):
        ae = self.am
        ae.volatility = arch.EGARCH(p=2, o=1, q=1)
        self.aeres = ae.fit(update_freq=0)
        print(self.aeres.summary())
        egarchFig = plt.figure()
        self.eresiduals = self.aeres.resid / self.aeres.conditional_volatility
        ergraph = egarchFig.add_subplot(212)
        ergraph.plot(self.modelDate, self.eresiduals)
        self.evolatility = self.aeres._volatility
        evgraph = egarchFig.add_subplot(211)
        evgraph.plot(self.modelDate, self.evolatility)
        ergraph.set_title('EGARCH Standardized Residuals')
        evgraph.set_title('EGARCH Conditional Volatility')

        for xc in self.xposition:
            ergraph.axvline(x=xc, color='k', linestyle='-')
            evgraph.axvline(x=xc, color='k', linestyle='-')

        plt.draw()
        plt.show()

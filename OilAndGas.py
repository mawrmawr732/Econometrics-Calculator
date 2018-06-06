import matplotlib.pyplot as plt
import arch.univariate as arch
import pandas


PATH = r"C:\Users\test\Desktop\IR excel spreadsheets\Oil and Gas.xlsx"


class OilAndGas():
    def __init__(self):
        oilandgasData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\Oil and Gas.xlsx")
        self.oilandgasDate = oilandgasData.Date
        self.modelDate = self.oilandgasDate.drop(self.oilandgasDate.index[0])
        self.oilandgasReturn = oilandgasData.Level
        self.oilandgasARCHReturn = 100 * self.oilandgasReturn.pct_change().dropna()
        self.xposition = ['3JANUARY2013', '3JANUARY2015', '3JANUARY2017']
        pandas.to_datetime(self.xposition)

    def timeseries(self):
        fig1 = plt.figure()
        oilandgasGraph = fig1.add_subplot(111)
        oilandgasGraph.plot(self.oilandgasDate, self.oilandgasReturn)
        oilandgasGraph.set_title('Time Series')

        fig1.autofmt_xdate()
        fig1.draw

        plt.show()

    def archmodel(self):
        self.am = arch.arch_model(self.oilandgasARCHReturn)
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
        plt.draw()
        plt.show()

    def linesmodel(self):
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
            evgraph.axvline(x=xc, color='k', linestyle='-')
            ergraph.axvline(x=xc, color='k', linestyle='-')

        plt.draw()
        plt.show()
import matplotlib.pyplot as plt
import arch.univariate as arch
import pandas



PATH = r"C:\Users\test\Desktop\IR excel spreadsheets\Materials.xlsx"


class Materials():
    def __init__(self):
        materialsData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\Materials.xlsx")
        self.materialsDate = materialsData.Date
        self.modelDate = self.materialsDate.drop(self.materialsDate.index[0])
        self.materialsReturn = materialsData.Level
        self.materialsARCHReturn = 100 * self.materialsReturn.pct_change().dropna()
        self.xposition = ['3JANUARY2013', '3JANUARY2015', '3JANUARY2017']
        pandas.to_datetime(self.xposition)

    def timeseries(self):
        fig1 = plt.figure()
        materialsGraph = fig1.add_subplot(111)
        materialsGraph.plot(self.materialsDate, self.materialsReturn)
        materialsGraph.set_title('Time Series')

        fig1.autofmt_xdate()
        fig1.draw

        plt.show()

    def archmodel(self):
        self.am = arch.arch_model(self.materialsARCHReturn)
        print(self.am)
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
        self.ae = self.am
        self.ae.volatility = arch.EGARCH(p=2, o=1, q=1)
        self.aeres = self.ae.fit(update_freq=0)
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
        self.ae = self.am
        self.ae.volatility = arch.EGARCH(p=2, o=1, q=1)
        self.aeres = self.ae.fit(update_freq=0)
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


if __name__ == '__main__':
    m = Materials()
    m.timeseries()
    m.archmodel()
    m.egarchmodel()
    m.linesmodel()






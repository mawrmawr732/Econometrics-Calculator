import matplotlib.pyplot as plt
import arch.univariate as arch
import arch as ar
import pandas
import numpy

PATH = r"C:\Users\test\Desktop\IR excel spreadsheets\Health Care.xlsx"


class HealthCare():
    def __init__(self):
        healthCareData = pandas.read_excel(r"C:\Users\test\Desktop\IR excel spreadsheets\Health Care.xlsx")
        self.healthCareDate = healthCareData.Date
        self.modelDate = self.healthCareDate.drop(self.healthCareDate.index[0])
        self.healthCareReturn = healthCareData.Level
        self.healthARCHReturn = 100 * self.healthCareReturn.pct_change().dropna()
        self.amres = None
        self.aeres = None
        self.eresiduals = None
        self.xposition = ['3JANUARY2013', '3JANUARY2015', '3JANUARY2017']
        pandas.to_datetime(self.xposition)

    def timeseries(self):
        fig1 = plt.figure()
        date = self.healthCareDate
        date = pandas.to_datetime(date)
        date = date.tolist()
        datelist = list()
        for x in date:
            datelist.append(x.value)
        datearray = numpy.array(datelist)
        healthCareGraph = fig1.add_subplot(111)
        healthCareGraph.plot(datearray, self.healthCareReturn)
        healthCareGraph.set_title('Time Series')

        limits = healthCareGraph.axis()
        limits = numpy.array(limits)
        healthCareGraph.fill_between(datearray, limits[2], limits[3], where=datelist[600:700])

        fig1.draw

        plt.show()

    def archmodel(self):
        self.am = arch.arch_model(self.healthARCHReturn)
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
        ae.volatility = arch.EGARCH(p=2, q=1)
        self.aeres = ae.fit(update_freq=0)
        print(self.aeres.summary())
        egarchFig = plt.figure()
        self.eresiduals = self.aeres.resid / self.aeres.conditional_volatility
        # self.residuals = self.residuals.set_value(0, 0)
        ergraph = egarchFig.add_subplot(212)
        ergraph.plot(self.modelDate, self.eresiduals)
        self.evolatility = self.aeres._volatility
        evgraph = egarchFig.add_subplot(211)
        evgraph.plot(self.modelDate, self.evolatility)


        plt.draw()
        plt.show()

    def linesmodel(self):
        ae = self.am
        ae.volatility = arch.EGARCH(p=2, q=1)
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


def main():
    health_care = HealthCare()
    health_care.timeseries()
    # health_care.archmodel()
    # health_care.egarchmodel()


if __name__ == "__main__":
    main()

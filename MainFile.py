from HealthCare import HealthCare
from ConsumerGoods import ConsumerGoods
from ConsumerServices import ConsumerServices
from Financials import Financials
from Industrials import Industrials
from Materials import Materials
from OilAndGas import OilAndGas
from REITs import REITs
from Technology import Technology
from Telecom import Telecom
from TotalMarket import TotalMarket
from Utilities import Utilities
from LargeCap import LargeCap
from MidCap import MidCap
from SmallCap import SmallCap
from MegaCap import MegaCap
from DowIndustrial import DowIndustrial
from DowUtilities import DowUtilities
from DowTransportation import DowTransportation
from SmallCapREITs import SmallCapREITs


def smallcapreits():
    small_cap_reits = SmallCapREITs()
    small_cap_reits.timeseries()
    small_cap_reits.archmodel()
    small_cap_reits.linesmodel()


def dowtransportation():
    dow_transportation = DowTransportation()
    dow_transportation.timeseries()
    dow_transportation.archmodel()
    dow_transportation.egarchmodel()


def dowutilities():
    dow_utilities = DowUtilities()
    dow_utilities.timeseries()
    dow_utilities.archmodel()
    dow_utilities.egarchmodel()


def dowindustrial():
    dow_industrial = DowIndustrial()
    dow_industrial.timeseries()
    dow_industrial.archmodel()
    dow_industrial.egarchmodel()


def megacap():
    mega_cap = MegaCap()
    mega_cap.timeseries()
    mega_cap.archmodel()
    mega_cap.linesmodel()


def smallcap():
    small_cap = SmallCap()
    small_cap.timeseries()
    small_cap.archmodel()
    small_cap.linesmodel()


def midcap():
    mid_cap = MidCap()
    mid_cap.timeseries()
    mid_cap.archmodel()
    mid_cap.linesmodel()


def largecap():
    large_cap = LargeCap()
    large_cap.timeseries()
    large_cap.archmodel()
    large_cap.linesmodel()


def utilities():
    utilities_model = Utilities()
    utilities_model.timeseries()
    utilities_model.archmodel()
    utilities_model.linesmodel()


def totalmarket():
    total_market = TotalMarket()
    total_market.timeseries()
    total_market.archmodel()
    total_market.linesmodel()


def telecom():
    telecom_model = Telecom()
    telecom_model.timeseries()
    telecom_model.archmodel()
    telecom_model.linesmodel()


def technology():
    technology_model = Technology()
    technology_model.timeseries()
    technology_model.archmodel()
    technology_model.linesmodel()


def reits():
    reits_model = REITs()
    reits_model.timeseries()
    reits_model.archmodel()
    reits_model.linesmodel()


def oilandgas():
    oil_and_gas = OilAndGas()
    oil_and_gas.timeseries()
    oil_and_gas.archmodel()
    oil_and_gas.linesmodel()


def materials():
    materials_model = Materials()
    materials_model.timeseries()
    materials_model.archmodel()
    materials_model.linesmodel()


def industrials():
    industrials_model = Industrials()
    industrials_model.timeseries()
    industrials_model.archmodel()
    industrials_model.linesmodel()


def financials():
    financials_model = Financials()
    financials_model.timeseries()
    financials_model.archmodel()
    financials_model.linesmodel()


def healthcare():
    health_care = HealthCare()
    health_care.timeseries()
    health_care.archmodel()
    health_care.linesmodel()


def consumergoods():
    consumer_goods = ConsumerGoods()
    consumer_goods.timeseries()
    consumer_goods.archmodel()
    consumer_goods.linesmodel()


def consumerservices():
    consumer_services = ConsumerServices()
    consumer_services.timeseries()
    consumer_services.archmodel()
    consumer_services.linesmodel()


def modelchooser():
    print("Choose from: " + '\n'
          "Health Care" + '\n'
          "Consumer Goods" + '\n'
          "Consumer Services" + '\n'
          "Financials" + '\n'
          "Industrials" + '\n'
          "Materials" + '\n'
          "Oil And Gas" + '\n'
          "REITs" + '\n'
          "Technology" + '\n'
          "Telecom" + '\n'
          "Total Market" + '\n'
          "Utilities" + '\n'
          "Large Cap" + '\n'
          "Mid Cap" + '\n'
          "Small Cap" + '\n'
          "Mega Cap" + '\n'
          "Dow Industrial" + '\n'
          "Dow Utilities" + '\n'
          "Dow Transportation" + '\n'
          "Small Cap REITs" + '\n'
          "Quit" + '\n' + '\n'
          "Selection: ")
    inpt = input()
    inpt = inpt.lower()
    if inpt == "health care":
        healthcare()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "consumer goods":
        consumergoods()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "utilities":
        utilities()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "consumer services":
        consumerservices()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "financials":
        financials()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "industrials":
        industrials()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "oil and gas":
        oilandgas()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "materials":
        materials()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "small cap":
        smallcap()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "mid cap":
        midcap()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "large cap":
        largecap()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "mega cap":
        megacap()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "technology":
        technology()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "telecom":
        telecom()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "dow industrial":
        dowindustrial()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "dow utilities":
        dowutilities()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "dow transportation":
        dowtransportation()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "reits":
        reits()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "small cap reits":
        smallcapreits()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "total market":
        totalmarket()
        input("Press enter to continue")
        modelchooser()
    elif inpt == "quit":
        print("Ending Program")
        exit(code=1)
    else:
        print("Not a valid option")
        modelchooser()


def main():
    modelchooser()


if __name__ == '__main__':
    main()

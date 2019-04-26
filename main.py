# coding=utf-8
"""
There are currently problems on the regression quadratic
"""

from sympy import *


class Prediction:
    """
Predict fi people made a roast in a day with a temperature of 85

|-----------------|
|   X    |   Y    |
|--------|--------|
|---85---|---85---|
|---80---|---90---|
|---83---|---78---|
|---70---|---90---|
|---68---|---80---|
|---65---|---70---|
|---64---|---65---|
|---72---|---64---|
|---69---|---72---|
|---75---|---69---|
|---80---|---80---|
|---72---|---70---|
|---81---|---75---|
|---70---|---80---|
|-----------------|

 Correlation coefficient 0.44786246684374104
|---------------------------------------------|
| Y = 35.36816037735849 + 0.5540094339622641x |
|---------------------------------------------|
    """

    def __init__(self, temperature):
        self.__temperature = temperature
        self.__humidity = 0
        self.__wind = false
        self.__climate = ""
        self.approach_result = ""
        #
        self.__approach_humidity()
        self.__approach_wind()
        self.__approach_climate()

    @property
    def humidity(self):
        """
        The properties not cover the variable temperature,
        this is the entry for the prediction.
        """
        return self.__humidity

    @property
    def wind(self):
        """
        Property for see the value of wind
        :return: boolean
        """
        return self.__wind

    @property
    def climate(self):
        """
        Property for the value forecast
        :return: string
        """
        return self.__climate

    def __approach_humidity(self):
        """
        h = f(t) = 35.22932662051604 + 0.5585903083700441t
        t = temperature
        h = humidity
        """
        self.__humidity = 35.22932662051604 + (0.5585903083700441 * self.__temperature)
        self.__approach_concat_result("humidity", self.__humidity)

    def __approach_concat_result(self, dat, value):
        self.approach_result = self.approach_result + dat + " : " + str(value) + "; "

    def __approach_wind(self):
        """
        Applying the clustering with the default information to generate two groups.
        Taking identifiers of the group 0, the reporting wind, is deduced the following condition.
        """
        if self.__humidity > self.__temperature:
            self.__wind = true
        self.__approach_concat_result("wind", self.__wind)

    def __approach_climate(self):
        """
        Evaluate the weather forecast, establishing different ranges with the help of a decision tree.
        """
        if 72 <= self.__temperature <= 85 \
                and 64 <= self.__humidity <= 90:
            self.__climate = "SUNNY"
        if 65 <= self.__temperature <= 80 \
                and 70 <= self.__humidity <= 80:
            self.__climate = "RAINY"
        if 64 <= self.__temperature <= 83 \
                and 65 <= self.__humidity <= 78:
            self.__climate = "CLOUDY"
        self.__approach_concat_result("climate", self.__climate)


if "__main__" == __name__:
    event = Prediction(80)
    print(event.approach_result)

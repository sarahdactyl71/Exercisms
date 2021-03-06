class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = seconds / 31557600

    def on_earth(self):
        return self.makes_pretty(1)

    def on_mercury(self):
        return self.makes_pretty(0.2408467)

    def on_venus(self):
        return self.makes_pretty(0.61519726)

    def on_mars(self):
        return self.makes_pretty(1.8808158)

    def on_jupiter(self):
        return self.makes_pretty(11.862615)

    def on_saturn(self):
        return self.makes_pretty(29.447498)

    def on_uranus(self):
        return self.makes_pretty(84.016846)

    def on_neptune(self):
        return self.makes_pretty(164.79132)

    def makes_pretty(self, ratio):
        return round((self.earth_years / ratio) , 2)

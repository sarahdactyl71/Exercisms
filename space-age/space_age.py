class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = seconds / 31557600

    def on_earth(self):
        return self.makes_pretty(self.seconds)

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




# Given an age in seconds, calculate how old someone would be on:
#
# Earth: orbital period 365.25 Earth days, or 31557600 seconds == 1 year
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you were told someone were 1,000,000,000 seconds old, you should be able to say that they're 31.69 Earth-years old.

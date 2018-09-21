class SpaceAge(object):
    def __init__(self, seconds):
        seconds = self.seconds
        earth_years = self.seconds / 31557600

    def mercury(self, seconds):
        return earth_years / 0.2408467

    def venus(self, seconds):
        return earth_years / 0.61519726

    def mars(self, seconds):
        return earth_years / 1.8808158

    def jupiter(self, seconds):
        return earth_years / 11.862615

    def saturn(self, seconds):
        return earth_years / 29.447498

    def uranus(self, seconds):
        return earth_years / 84.016846

    def neptune(self, seconds):
        return earth_years / 164.79132






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

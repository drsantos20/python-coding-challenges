import math


class TimeConvert:
    def time_convert(self, num):

        # to get the hours, we divide num by 60 and round it down
        # e.g. 61 / 60 = 1 hour
        # e.g. 43 / 60 = 0 hours
        hours = int(math.floor(num / 60))

        # to get the minutes, now we use the remainder that we discarded above
        # the modulo operation is represented by the % symbol
        # e.g. 61 % 60 = 1 minute
        # e.g. 43 % 60 = 43 minutes
        minutes = num % 60

        return str(hours) + ':' + str(minutes);

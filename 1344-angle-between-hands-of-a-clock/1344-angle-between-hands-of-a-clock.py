class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6 * minutes
        hour_angle = 30 * hour
        hour_angle = hour_angle + (0.5 * minutes)
        difference = abs(hour_angle - minute_angle)
        if difference > 180:
            difference = 360 - difference
        else:
            difference
        return difference
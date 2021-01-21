from rest_framework import throttling

class CheckInThrottle(throttling.UserRateThrottle):
    scope = 'checkin'
    rate = '1/day'

class CheckOutThrottle(throttling.UserRateThrottle):
    scope = 'checkout'
    rate = '3/day'
 
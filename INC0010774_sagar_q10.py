def timeadd(t1,t2):
        t3 = Time(0,0)
        if t1.mins+t2.mins > 60:
            t3.hours =(t1.mins + t2.mins)/60
        t3.mins =(t1.mins + t2.mins)


class Time(object):
    def __init__(self,hours,minutes,seconds):
        self.hours =hours
        self.minutes=minutes
        self.seconds=seconds
        
    def timedisplay(self):
        return'{}:{}:{}'.format(self.hours, self.minutes, self.seconds)
        
    def minutedisplay(self):
        minutes=self.hours*60+self.minutes
        return minutes

Time.hours(10)
Time.minutes(15)
Time.seconds(5)

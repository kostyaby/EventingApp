class TimeKeeper( object ):

    def __init__( self, hours = 0, minutes = 0 ):
        self.__timevalue = hours * 60 + minutes

    def get_hours( self ):
        return self.__timevalue / 60

    def get_minutes( self ):
        return self.__timevalue % 60

    def set_hours( self, hours ):
        self = TimeKeeper( hours, self.minutes() )

    def set_minutes( self, minutes ):
        self = TimeKeeper( self.hours(), minutes )

    def __str__( self ):
        return "%02d:%02d" % ( self.get_hours(), self.get_minutes() )

    def __cmp__( self, other ):
        if self.__timevalue < other.__timevalue:
            return -1
        elif self.__timevalue > other.__timevalue:
            return 1
        else:
            return 0

    def __add__( self, other ):
        hours = self.get_hours() + other.get_hours()
        minutes = self.get_minutes() + other.get_minutes()
        timevalue = hours * 60 + minutes
        return TimeKeeper( timevalue / 60, timevalue % 60 )

    def __sub__( self, other ):
        hours = self.get_hours() - other.get_hours()
        minutes = self.get_minutes() - other.get_minutes()
        timevalue = hours * 60 + minutes
        if timevalue < 0:
            raise ValueError( "TimeKeeper cannot be negative!" )
        return TimeKeeper( timevalue / 60, timevalue % 60 )
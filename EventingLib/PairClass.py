from Rider import *
from TimeKeeper import *
from Horse import *

class PairClass( object ):

    def __init__( self, rider = Rider(), horse = Horse(), ShowNo = 100, StartTime = TimeKeeper( 9, 0 ) ):
        self.__rider = rider
        self.__horse = horse
        self.__ShowNo = ShowNo
        self.__StartTime = StartTime

    def get_rider( self ):
        return self.__rider

    def get_horse( self ):
        return self.__horse

    def get_ShowNo( self ):
        return self.__ShowNo

    def get_StartTime( self ):
        return self.__StartTime

    def set_rider( self, rider ):
        self.__rider = rider

    def set_horse( self, rider ):
        self.__horse = horse

    def set_ShowNo( self, ShowNo ):
        self.__ShowNo = ShowNo

    def set_StartTime( self, StartTime ):
        self.__StartTime = StartTime

    def __str__( self ):
        return "Pair: %s, %s, ShowNo: %d, Time: %s" % ( self.__rider, self.__horse, self.__ShowNo, self.__StartTime )

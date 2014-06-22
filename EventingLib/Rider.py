class Rider( object ):

    def __init__( self, name = "John Appleseed", ID = 10000000, NF = "USA" ):
        self.__name = name

        if 10000000 <= ID <= 99999999:
            self.__ID = ID
        else:
            raise ValueError( "ID must be an 8-digit number without leading zeroes!" )

        if NF in NationalFederations:
            self.__NF = NF
        else:
            raise ValueError( "Unknown national federation!" )

    def get_name( self ):
        return self.__name

    def get_ID( self ):
        return self.__ID

    def get_NF( self ):
        return self.__NF

    def set_name( self, name ):
        self.__name = name

    def set_ID( self, ID ):
        if 10000000 <= ID <= 99999999:
            self.__ID = ID
        else:
            raise ValueError( "ID must be an 8-digit number without leading zeroes!" )

    def set_NF( self, NF ):
        if NF in NationalFederations:
            self.__NF = NF
        else:
            raise ValueError( "Unknown national federation!" )

    def __cmp__( self, other ):
        if self.__ID < other.__ID:
            return -1
        elif self.__ID > other.__ID:
            return 1
        else:
            return 0

    def __hash__( self ):
        return self.__ID

    def __str__( self ):
        return "%s(ID: %d, NF: %s)" % ( self.__name, self.__ID, self.__NF ) 
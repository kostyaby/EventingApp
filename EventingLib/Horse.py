class Horse( object ):

    def __init__( self, name = "Pepper", ID = "999AZ00" ):
        self.__name = name
        self.__ID = ID

    def get_name( self ):
        return self.__name

    def get_ID( self ):
        return self.__ID

    def set_name( self, name ):
        self.__name = name

    def set_ID( self, ID ):
        self.__ID = ID

    def __cmp__( self, other ):
        if hash( self.__ID ) < hash( other.__ID ):
            return -1
        elif hash( self.__ID ) > hash( other.__ID ):
            return 1
        else:
            return 0

    def __str__( self ):
        return "Horse %s, ID: %s" % ( self.__name, self.__ID ) 
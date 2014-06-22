import __builtin__

__builtin__.NationalFederations = []

def input_NF( file ):
    global NationalFederations
    NationalFederations = []
    fin = open( file, "r" )
    for line in fin:
        __builtin__.NationalFederations.append( line.strip() )

input_NF( "NF.txt" )
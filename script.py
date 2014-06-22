import csv
import random
from EventingLib import *
from EventingLib.TimeKeeper import *
from EventingLib.Rider import *
from EventingLib.Horse import *
from EventingLib.PairClass import *

def ParseInput( file ):
    fin = open( file, "r" )
    csvreader = csv.reader( fin, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL )
    pairs = []
    for row in csvreader:
        pairs.append( PairClass( rider = Rider( row[0], int( row[1] ), row[4] ), horse = Horse( row[2], row[3] ), ShowNo = int( row[5] ) ) )
    return pairs

def TryRandomOrder( StartTime, pairs ):
    GapBetweenStarts = TimeKeeper( 0, 10 )
    GapBetweenEqual = TimeKeeper( 0, 40 )
    random.shuffle( pairs )
    gaps = {}
    for pair in pairs:
        current_time = StartTime + GapBetweenStarts
        if current_time > gaps.get( pair.get_rider(), StartTime + GapBetweenStarts ):
            current_time = gaps[ pair.get_rider() ] + GapBetweenEqual
        pair.set_StartTime( current_time )
        StartTime = current_time
    return pairs

def MakeTheOrder( StartTime, pairs ):
    best_order = TryRandomOrder( StartTime, pairs )
    for it in range( 100 ):
        candidate = TryRandomOrder( StartTime, pairs )
        if best_order[ -1 ].get_StartTime() > candidate[ -1 ].get_StartTime():
            best_order = candidate
    return best_order

def OutputCSV( file, pairs ):
    csvfile = open( file, "w" )
    csvwriter = csv.writer( csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL )
    for pair in pairs:
        cur = []
        cur.append( pair.get_rider().get_name() )
        cur.append( pair.get_rider().get_ID() )
        cur.append( pair.get_rider().get_NF() )
        cur.append( pair.get_horse().get_name() )
        cur.append( pair.get_horse().get_ID() )
        cur.append( pair.get_ShowNo() )
        cur.append( str( pair.get_StartTime() ) )
        csvwriter.writerow( cur )

pairs = ParseInput( "log.csv" )
pairs = MakeTheOrder( TimeKeeper( 9, 0 ), pairs ) 
OutputCSV( "order.csv", pairs )


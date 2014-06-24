#!/usr/bin/env python

import csv
import copy
import random
from EventingLib import *
from EventingLib.TimeKeeper import *
from EventingLib.Rider import *
from EventingLib.Horse import *
from EventingLib.PairClass import *
from Tkinter import *
import tkMessageBox
import tkFileDialog 
import ttk

Prev = Next = None
pairs = None
pairs2 = None
IsOrdered = False

def ParseInput( file ):
    try:
        fin = file
        csvreader = csv.reader( fin, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL )
        pairs = []
        for row in csvreader:
            pairs.append( PairClass( ID = row[0], rider = Rider( row[1], int( row[2] ), row[3] ), ShowNo = int( row[4] ), horse = Horse( row[5], row[6] ) ) )
        return pairs
    except:
        tkMessageBox.showerror("EventingApp.Error", "Your CSV file cannot be parsed!")
        return None

def TryOrder( StartTime, pairs, GapBetweenStarts = TimeKeeper( 0, 10 ), GapBetweenEqual = TimeKeeper( 0, 40 ) ):
    gaps = {}
    index = 1
    _pairs = []
    for pair in pairs:
        current_time = StartTime
        cur = copy.copy( pair )
        if cur.get_rider() in gaps:
            current_time = max( current_time, gaps[ cur.get_rider() ] + GapBetweenEqual )
        cur.set_ID( index )
        index += 1
        cur.set_StartTime( current_time )
        gaps[ cur.get_rider() ] = current_time
        StartTime = current_time + GapBetweenStarts
        _pairs.append( cur )
    return _pairs

def MakeTheOrder( StartTime, _pairs ):
    pairs = _pairs[:]
    random.shuffle( pairs )
    best_order = TryOrder( StartTime, pairs )
    for it in range( 1000 ):
        random.shuffle( pairs )
        candidate = TryOrder( StartTime, pairs )
        if best_order[ -1 ].get_StartTime() > candidate[ -1 ].get_StartTime():
            best_order = candidate
    return best_order

def OutputCSV( file, pairs, pairs2 ):
    try:
        csvfile = file
        csvwriter = csv.writer( csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL )
        for pair in pairs:
            cur = []
            cur.append( pair.get_ID() )
            cur.append( str( pair.get_StartTime() ) )
            cur.append( pair.get_rider().get_name() )
            cur.append( pair.get_rider().get_ID() )
            cur.append( pair.get_rider().get_NF() )
            cur.append( pair.get_ShowNo() )
            cur.append( pair.get_horse().get_name() )
            cur.append( pair.get_horse().get_ID() )
            csvwriter.writerow( cur )
        cur = []
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        csvwriter.writerow( cur )
        for pair in pairs2:
            cur = []
            cur.append( pair.get_ID() )
            cur.append( str( pair.get_StartTime() ) )
            cur.append( pair.get_rider().get_name() )
            cur.append( pair.get_rider().get_ID() )
            cur.append( pair.get_rider().get_NF() )
            cur.append( pair.get_ShowNo() )
            cur.append( pair.get_horse().get_name() )
            cur.append( pair.get_horse().get_ID() )
            csvwriter.writerow( cur )
        cur = []
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        cur.append( "" )
        csvwriter.writerow( cur )
        for pair in pairs:
            cur = []
            cur.append( pair.get_ID() )
            cur.append( str( TimeKeeper( 0, 0 ) ) )
            cur.append( pair.get_rider().get_name() )
            cur.append( pair.get_rider().get_ID() )
            cur.append( pair.get_rider().get_NF() )
            cur.append( pair.get_ShowNo() )
            cur.append( pair.get_horse().get_name() )
            cur.append( pair.get_horse().get_ID() )
            csvwriter.writerow( cur )
    except:
        tkMessageBox.showerror("EventingApp.Error", "Your CSV file cannot be saved!")
        
def update_show( *argv ):
    global _ID, _Rider, _RiderID, _NF, _ShowNo, _Horse, _HorseID, Prev, Next
    if _Index == 0:
        Prev.configure( state=DISABLED )
    else:
        Prev.configure( state=NORMAL )
    if _Index + 1 == len( pairs ):
        Next.configure( state=DISABLED )
    else:
        Next.configure( state=NORMAL )
    pair = pairs[ _Index ]
    _ID.set( pair.get_ID() )
    _Rider.set( pair.get_rider().get_name() )
    _RiderID.set( pair.get_rider().get_ID() )
    _NF.set( pair.get_rider().get_NF() )
    _ShowNo.set( pair.get_ShowNo() )
    _Horse.set( pair.get_horse().get_name() )
    _HorseID.set( pair.get_horse().get_ID() )
    _Time1.set( pair.get_StartTime() )
    _Time2.set( pairs2[ _Index ].get_StartTime() )

def previous_fun( *argv ):
    global _Index
    _Index -= 1
    update_show()

def next_fun( *argv ):
    global _Index
    _Index += 1
    update_show()

def ImportCSV():
    global pairs, IsOrdered
    file = tkFileDialog.askopenfile( filetypes=( ( "CSV Table", "*.csv" ), ( "All files", "*.*" ) ) )
    pairs = ParseInput( file )
    IsOrdered = False
    if pairs != None:
        tkMessageBox.showinfo("EventingApp.Message", "Success! Table has been imported!")

def BuildTheOrder():
    global pairs, pairs2, IsOrdered
    if pairs == None:
        tkMessageBox.showerror("EventingApp.Error", "Error! Cannot build the order! You haven't imported a CSV table!")
    else:
        pairs = MakeTheOrder( TimeKeeper( 0, 0 ), pairs )
        pairs2 = copy.deepcopy( pairs )
        pairs2 = TryOrder( TimeKeeper( 0, 0 ), pairs2, GapBetweenStarts = TimeKeeper( 0, 4 ), GapBetweenEqual = TimeKeeper( 0, 40 ) )
        IsOrdered = True
        tkMessageBox.showinfo("EventingApp.Message", "Success! Order has been built!")

def StartTheShow():
    global pairs, pairs2, IsOrdered
    global Prev, Next
    if IsOrdered == False:
        tkMessageBox.showerror("EventingApp.Error", "Error! Cannot start the show! You either haven't imported a CSV table or haven't built the order!")
    else:
        showroot = Toplevel()
        showroot.title("EventingApp.Show")
        width_screen = showroot.winfo_screenwidth()
        height_screen = showroot.winfo_screenheight()
        width = width_screen / 2
        height = height_screen / 2
        x_center = width_screen / 2 - width / 2
        y_center = height_screen / 2 - height / 2
        showroot.geometry("%dx%d+%d+%d" % ( width, height, x_center, y_center ) )
        showroot.minsize( width_screen / 3, height_screen / 3 )
        showroot.columnconfigure( 0, weight = 1 )
        showroot.rowconfigure( 0, weight = 7 )
        showroot.rowconfigure( 1, weight = 3 )
        showroot.rowconfigure( 2, weight = 1 )
        # 
        topframe = ttk.Frame( showroot, padding = "5 5", borderwidth = 3, relief = "ridge" )
        topframe.grid( column = 0, row = 0, sticky = ( N, W, E, S ) )
        topframe.rowconfigure( 0, weight = 1 )
        topframe.rowconfigure( 1, weight = 1 )
        topframe.rowconfigure( 2, weight = 1 )
        topframe.rowconfigure( 3, weight = 1 )
        topframe.rowconfigure( 4, weight = 1 )
        topframe.rowconfigure( 5, weight = 1 )
        topframe.rowconfigure( 6, weight = 1 )
        topframe.columnconfigure( 0, weight = 1 )
        topframe.columnconfigure( 1, weight = 1 )
        ttk.Label( topframe, text = "ID:", ).grid( column = 0, row = 0, sticky = E )
        ttk.Label( topframe, text = "Rider:" ).grid( column = 0, row = 1, sticky = E )
        ttk.Label( topframe, text = "Rider ID:" ).grid( column = 0, row = 2, sticky = E )
        ttk.Label( topframe, text = "National Fed.:" ).grid( column = 0, row = 3, sticky = E )
        ttk.Label( topframe, text = "Show No:" ).grid( column = 0, row = 4, sticky = E )
        ttk.Label( topframe, text = "Horse:" ).grid( column = 0, row = 5, sticky = E )
        ttk.Label( topframe, text = "Horse ID:" ).grid( column = 0, row = 6, sticky = E )

        ttk.Label( topframe, textvariable = _ID, width = 30 ).grid( column = 1, row = 0, sticky = W )
        ttk.Label( topframe, textvariable = _Rider, width = 30 ).grid( column = 1, row = 1, sticky = W )
        ttk.Label( topframe, textvariable = _RiderID, width = 30 ).grid( column = 1, row = 2, sticky = W )
        ttk.Label( topframe, textvariable = _NF, width = 30 ).grid( column = 1, row = 3, sticky = W )
        ttk.Label( topframe, textvariable = _ShowNo, width = 30 ).grid( column = 1, row = 4, sticky = W )
        ttk.Label( topframe, textvariable = _Horse, width = 30 ).grid( column = 1, row = 5, sticky = W )
        ttk.Label( topframe, textvariable = _HorseID, width = 30 ).grid( column = 1, row = 6, sticky = W )

        #
        middleframe = ttk.Frame( showroot, padding = "3 3", borderwidth = 3, relief = "ridge" )
        middleframe.grid( column = 0, row = 1, sticky = ( N, W, E, S ) )
        middleframe.rowconfigure( 0, weight = 1 )
        middleframe.rowconfigure( 1, weight = 1 )
        middleframe.rowconfigure( 2, weight = 1 )
        middleframe.columnconfigure( 0, weight = 1 )
        middleframe.columnconfigure( 1, weight = 1 )
        ttk.Label( middleframe, text = "Dressage Start Time:" ).grid( column = 0, row = 0, sticky = E )
        ttk.Label( middleframe, text = "Cross-Country Start Time:" ).grid( column = 0, row = 1, sticky = E )
        ttk.Label( middleframe, text = "Show Jumping Start Number:" ).grid( column = 0, row = 2, sticky = E )

        ttk.Label( middleframe, textvariable = _Time1 ).grid( column = 1, row = 0, sticky = W )
        ttk.Label( middleframe, textvariable = _Time2 ).grid( column = 1, row = 1, sticky = W )
        ttk.Label( middleframe, textvariable = _ID ).grid( column = 1, row = 2, sticky = W )
        #
        bottomframe = ttk.Frame( showroot, padding = "3 3", borderwidth = 3, relief = "ridge" )
        bottomframe.grid( column = 0, row = 2, sticky = ( N, W, E, S ) )
        bottomframe.rowconfigure( 0, weight = 1 )
        bottomframe.columnconfigure( 0, weight = 1 )
        bottomframe.columnconfigure( 1, weight = 1 )
        bottomframe.columnconfigure( 2, weight = 1 )
        Prev = ttk.Button( bottomframe, text = "Previous", command = previous_fun )
        Prev.grid( column = 0, row = 0 )
        Next = ttk.Button( bottomframe, text = "Next", command = next_fun )
        Next.grid( column = 1, row = 0 )
        ttk.Button( bottomframe, text = "Finish", command = showroot.destroy ).grid( column = 2, row = 0 )
        #root.bind( "a" , update_show )
        #root.event_generate( "a" )
        update_show()

def ExportCSV():
    global pairs, pairs2, IsOrdered
    if IsOrdered == False:
        tkMessageBox.showerror("EventingApp.Error", "Error! Cannot export CSV file! You either haven't imported a CSV table or haven't built the order!")
    else:
        file = tkFileDialog.asksaveasfile(mode='w', defaultextension=".csv")
        OutputCSV( file, pairs, pairs2 )
        tkMessageBox.showinfo("EventingApp.Message", "Success! Table has been exported!")

if __name__ == "__main__":
    # Global declaration
    _Index = 0
    # Main Window declaration
    root = Tk()
    root.title("EventingApp")
    width_screen = root.winfo_screenwidth()
    height_screen = root.winfo_screenheight()
    width = width_screen / 2
    height = height_screen / 2
    x_center = width_screen / 2 - width / 2
    y_center = height_screen / 2 - height / 2
    root.geometry("%dx%d+%d+%d" % ( width, height, x_center, y_center ) )
    root.minsize( width_screen / 3, height_screen / 3 )
    root.columnconfigure( 0, weight = 1 )
    root.rowconfigure( 0, weight = 1 )
    root.rowconfigure( 1, weight = 7 )
    # Top Frame declaration
    topframe = ttk.Frame( root, padding = "5 5", borderwidth = 3, relief = "ridge" )
    topframe.grid( column = 0, row = 0, sticky = ( N, W, E, S ) )
    topframe.rowconfigure( 0, weight = 1 )
    topframe.columnconfigure( 0, weight = 1 )
    ttk.Label( topframe, text = "EventingApp welcomes you!" ).grid( column = 0, row = 0 )
    # Bottom Frame declaration
    bottomframe = ttk.Frame( root, padding = "5 5", borderwidth = 3, relief = "ridge" )
    bottomframe.grid( column = 0, row = 1, sticky = ( N, W, E, S ) )
    bottomframe.rowconfigure( 0, weight = 1 )
    bottomframe.rowconfigure( 1, weight = 1 )
    bottomframe.rowconfigure( 2, weight = 1 )
    bottomframe.rowconfigure( 3, weight = 1 )
    bottomframe.rowconfigure( 4, weight = 1 )
    bottomframe.columnconfigure( 0, weight = 1 )

    _ID = StringVar()
    _Rider = StringVar()
    _RiderID = StringVar()
    _NF = StringVar()
    _ShowNo = StringVar()
    _Horse = StringVar()
    _HorseID = StringVar()
    _Time1 = StringVar()
    _Time2 = StringVar()

    ImportButton = ttk.Button( bottomframe, text = "Import CSV file", command = ImportCSV )
    BuildButton = ttk.Button( bottomframe, text = "Build the Order", command = BuildTheOrder )
    ShowButton = ttk.Button( bottomframe, text = "Start the Show!", command = StartTheShow )
    ExportButton = ttk.Button( bottomframe, text = "Export CSV file", command = ExportCSV )
    QuitButton = ttk.Button( bottomframe, text = "Quit", command = root.quit )

    ImportButton.grid( column = 0, row = 0 )
    BuildButton.grid( column = 0, row = 1 )   
    ShowButton.grid( column = 0, row = 2 )   
    ExportButton.grid( column = 0, row = 3 )   
    QuitButton.grid( column = 0, row = 4 )   

    root.focus()
    root.mainloop()
    root.quit()



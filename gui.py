from Tkinter import *
import ttk

def calculate( *args ):
    try:
        value = float( feet.get() )
        meters.set( ( 0.3048 * value * 10000.0 + 0.5 ) / 10000.0 )
    except ValueError:
        pass

"""def calculate( *args ):
    aboutroot = Tk()
    aboutroot.title("EventingApp About")
    aboutroot.columnconfigure( 0, weight = 1 )
    aboutroot.rowconfigure( 0, weight = 1 )
    aboutframe = ttk.Frame( aboutroot, padding = "3 3" )
    aboutframe.grid( column = 0, row = 0, sticky = ( N, W, E, S ) )
    aboutframe.columnconfigure( 0, weight = 1 )
    aboutframe.rowconfigure( 0, weight = 1 )
    ttk.Label( aboutframe, text = "About Page!" ).grid( column = 0, row = 0, padx = 10, pady = 10 )
    aboutroot.mainloop()"""

root = Tk()
root.title("EventingApp")
root.geometry('600x400+100+100')
root.resizable( FALSE, FALSE )
root.columnconfigure( 0, weight = 1 )
root.rowconfigure( 0, weight = 1 )

mainframe = ttk.Frame( root, padding = "3 3 12 12" )
mainframe.grid( column = 0, row = 0, sticky = ( N, W, E, S ) )
mainframe.columnconfigure( 0, weight = 1 )
mainframe.columnconfigure( 1, weight = 1 )
mainframe.columnconfigure( 2, weight = 1 )
mainframe.columnconfigure( 3, weight = 1 )
mainframe.rowconfigure( 0, weight = 1 )
mainframe.rowconfigure( 1, weight = 1 )
mainframe.rowconfigure( 2, weight = 1 )
mainframe.rowconfigure( 3, weight = 1 )

feet = StringVar()
meters = StringVar() 
meters.set( 124 )

feet_entry = ttk.Entry( mainframe, width = 10, textvariable = feet )
feet_entry.grid( column = 2, row = 1, sticky = ( W, E ) )
ttk.Label( mainframe, textvariable = meters ).grid( column = 2, row = 2, sticky = ( W, E ) )
ttk.Button( mainframe, text = "Calculate!", command = calculate ).grid( column = 3, row = 3, sticky = W )

ttk.Label( mainframe, text = "feet" ).grid( column = 3, row = 1, sticky = W )
ttk.Label( mainframe, text = "is equal to" ).grid( column = 1, row = 2, sticky = E )
ttk.Label( mainframe, text = "meters" ).grid( column = 3, row = 2, sticky = W )

for child in mainframe.winfo_children():
    child.grid_configure( padx = 10, pady = 10 )

feet_entry.focus()

root.mainloop()

#===================================================
"""
# Menu declaration
    menubar = Menu(root)
    menubar.add_command(label="About", command = foo)
    # File declaration
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Import CSV file", command = foo)
    filemenu.add_command(label="Build the Order", command = foo)
    filemenu.add_command(label="Start the Show",  command = foo)
    filemenu.add_command(label="Export CSV file", command = foo)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    # About declaration
    menubar.add_command(label="About", command = foo)
    #
"""
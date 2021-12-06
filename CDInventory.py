#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AWillie, 2021-Dec-03, added script for adding a CD
# AWillie, 2021-Dec-04, added more script
# AWillie, 2021-Dec-05, worked on object script and finalized everything else
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
strFileName = 'cdInventory.dat'
lstOfCDObjects = []
import pickle
class CD(object):
    """Stores data about a CD:

    properties:
        ID: (int) with CD ID
        Title: (string) with the title of the CD
        Artist: (string) with the artist of the CD
    methods:
        add_CD(list)
        del_CD(list)

    """
    # Fields
    ID = int()
    Title = ''
    Artist = ''
    def __init__(self, ID, Title, Artist):
        self.__ID = ID
        self.__Title = Title
        self.__Artist = Artist
    @property
    def ID(self):
        return self.__ID
    @property
    def Title(self):
        return self.__Title
    @property
    def Artist(self):
        return self.__Artist
    @staticmethod
    def add_CD(cd):
        global lstOfCDObjects
        lstOfCDObjects.append(cd)
    @staticmethod  
    def del_CD(ID):
        global lstOfCDObjects
        intRowNr = -1
        blnCDRemoved = False
        for cd in lstOfCDObjects:
            intRowNr += 1
            if cd.ID == ID:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
     
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # load file
    @staticmethod
    def read_file(FileName):
        """"Function to read a binary file and to return the list data

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        global lstOfCDObjects
        lstOfCDObjects.clear()
        with open(FileName, 'rb+') as objFile:
            try:
                lstOfCDObjects = pickle.load(objFile)
            except:
                print('Something has gone wrong!')
            else:
                print ('Successful read: %s' % (objFile))
            objFile.close()
            return list(lstOfCDObjects)
    @staticmethod
    def write_file(FileName):
        # Added code here
        """Function to save data to a binary file
        
        Takes the current memory and moves it to a binary file
        
        Args:
            file_name(string): name of file used to copy memory to
            table (list of dict): 2D data structure holding the inventory
        Returns:
            None.
        """
        global lstOfCDObjects
        with open(FileName, 'wb+') as objFile:
            try:
                pickle.dump(lstOfCDObjects, objFile)
            except:
                print('An error has occured')
            else:
                print ('Successful write: %s' % (objFile))
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    # User Menu
    def print_Menu():
         print('\n[a] add data to list\n[w] to write data to file\n[r] to read data from file')
         print('[d] display data\n[i] to show inventory\n[x] to quit')
    # Menu choice
    def user_Choice():
        choice = ' '
        while choice not in ['a', 'w', 'r', 'd', 'i', 'x']:
            choice = input('Which operation would you like to perform? [a, w, r, d, i, x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # Inventory
    def show_inventory():
         global lstOfCDObjects
         print(':::::::The Current Inventory: :::::::')
         print('ID\tCD Title (by: Artist)\n')
         for cd in lstOfCDObjects:
            print('{}\t{} (by: {})'.format(cd.ID, cd.Title, cd.Artist))
         print(':::::::::::::::::::::::::::::::::::::')
    # CD information
    def CD_addition():
        ID = input('Please provide an ID: ')
        title = input('Please provide the CD title: ')
        artist = input('Please provide the CD artist: ')
        return int(ID), title, artist
# -- Main Body of Script -- #
# Menu loop
# Load data from file into a list of CD objects on script start
# Display menu to user
    print('Write or Read file data.')
while True:
    IO.print_Menu()
    strChoice = IO.user_Choice()
    # let user exit program
    if strChoice == 'x':
        break
    # let user add data to the inventory
    if strChoice == 'a':  
        intID, strtitle, strartist = IO.CD_addition()
        newCD = CD(intID, strtitle, strartist)
        CD.add_CD(newCD)
        IO.show_inventory()
        continue
     # let user load inventory from file
    elif strChoice == 'r':
        print('WARNING: If you continue, all current memory will be lost.')
        strYesNo = input('Load inventory from file? [y/n] ').strip().lower()
        if strYesNo.lower() == 'y':
            print('reading file now...')
            FileIO.read_file(strFileName)
            IO.show_inventory()
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory()
        continue  # start loop back at top
         # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory()
        continue
    
    # let user save inventory to file
    elif strChoice == 'w':
        IO.show_inventory()
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        FileIO.write_file(strFileName)
        continue  
    elif strChoice == 'd':
        intIDDel = input('Which ID would you like to delete? ')
        CD.del_CD(int(intIDDel))
        IO.show_inventory()
        continue
    else:
        print('Please choose either a, l, s, d, or x!')


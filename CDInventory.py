#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
#--------------------------------------#
# Title: CDIventory
# Desc: Script will ask for user input either to save data load data or add new information
# Update to the CDInventory using pickling to save data and user validation checks
# Used setter and Getters
# Saduq Rahman, 2021 March 07, created file
#---------------------------------------#


# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []
objFile = None  # file object
strChoice = ''

import pickle


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
 
    
  
   
    def __init__(self,cd_id,cd_title,cd_artist):
        self.__ID = cd_id
        self.__Title = cd_title
        self.__Artist = cd_artist
        
       
                    
       
 
     
         
    @property  
    def ID(self):
       return self.__ID
   
   
    @property
    def Title(self):
       return self.__Title
   
    @property
    def Artist(self):
        return self.__Artist
    
    @ID.setter
    def ID(self,value):
       
        if type(value) == int:
            self.__ID = value
            
           
    @Title.setter   
    def Title(self,value):
        if type(value) == str:
            self.__Title = value
              

    @Artist.setter     
    def Artist(self,value): 
        if type(value) == str:
           self.__Artist = value
          
    def __str__(self):
         
         return f' {str (self.ID)} , {self.Title} , {self.Artist}'
    

# -- PROCESSING -- #
class DataProcessor:
    """ Function to manage data ingestion and append data to the table
            passed the parameters listed below.
        

        Parameters
        ----------
        strID : TYPE
            DESCRIPTION.
        strTitle : TYPE
            DESCRIPTION.
        strArtist : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
    @staticmethod
    def invetory_update(table):
          new_cd = CD (cd_id, cd_title, 
cd_artist)
          table.append(new_cd )
     
          return table
      
        
class FileIO:
    """Function to manage data ingestion from file to a object

        Reads the data from file identified by file_name into a 2D table
        

        Args:
            file_name (string): name of file used to read the data from
            table is used to pass information to the object

        Returns:
            None.
        """
    @staticmethod    
    def Load_inventory(file_name, table):
        table.clear()
        # this clears existing data and allows to load data from file
        try:
            with open(file_name, "rb+") as ObjFile:# using pickle to read file 
             table = pickle.load(ObjFile)
            
        except FileNotFoundError:
           
            with open(file_name, 'wb+') as ObjFile:#writes/creates dat file.
                pickle.dump(lstOfCDObjects, ObjFile)
                print('It appears the dat file has not been created, I\'ll go ahead and get you started!')
                print()
                print('Now that the file has been created let\'s go ahead and get started.\n')
        
                
    # TODO Add code to process data from a file
    
    # TODO Add code to process data to a file
    
    @staticmethod
    def write_inventory(file_name, table):
        """
        Parameters
        ----------
        file_name : TYPE
            DESCRIPTION.
        table : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
    
             #Save the data to a text file CDInventory.dat if the user chooses so
        with open(file_name, 'wb+') as ObjFile:#writes/creates dat file.
           pickle.dump(lstOfCDObjects, ObjFile) 
   
 
         

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    # TODO add code to show menu to user
    @staticmethod 
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
        """

    print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[s] Save Inventory to file\n[x] exit\n')
    # TODO add code to captures user's choice
    @staticmethod 
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
    """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODO add code to display the current data on screen
    
    @staticmethod 
    def show_inventory(table):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
    # TODO add code to get CD data from user
    
    @staticmethod 
    def add_CD():
        while True:
            try:
                cd_id = int(input ('Please enter the ID number:').strip())
                break
            except ValueError:
                          print ('ID must be an integer!')
        
        cd_title = input('What is the name of the Album. You want to add to inventory list: ').strip()
        cd_artist = input('Please enter the name of the Artist: ').strip()
        print()
        print ('*******CD added successfully*******')
     
        return cd_id, cd_title, cd_artist

# -- Main Body of Script -- #
FileIO.Load_inventory(strFileName, lstOfCDObjects)

##### start main loop ### (no change)
while True:
   
    IO.print_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.Load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
            
            
        continue  # start loop back at top (No Change)
    elif strChoice == 'a':  
    
        cd_id, cd_title, cd_artist = IO.add_CD()
   
        # The input_append method returns lstOfCDObjects at its conclusion
        # As such we should then reassign the returned value back into lstOfCDObjects
        # Also we need to pass lstOfCDObjects to the method as we're operating on it.
        # FileIO.append_inventory(cd_id, cd_title, cd_artist)
        lstOfCDObjects = DataProcessor.invetory_update(lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        
        
        continue  # start loop back at top.
    
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects) ## Calls for show function dispalying user inventory
        continue  # start loop back at top.
   
  
    elif strChoice == 's':
        
        IO.show_inventory(lstOfCDObjects) ## Calls for show function dispalying user inventory
        
        try:
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        except:
            print('=====Invaild selection please try again=====')

            if strYesNo.lower() in ['yes', 'y']:
                FileIO.write_inventory(strFileName,lstOfCDObjects) ## Calls for to save inventory to target .txt file 

            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')

            continue  # start loop back at top.

### catch-all should not be possible, as user choice gets vetted in IO, but to be save (no change):
    else:
         print('General Error') 

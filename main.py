from Board import window
from kivy.config import Config
from kivy.core.window import Window

def setup():
    width_of_board = 820
    height_of_board = 800

    #Set the Hight and Width of the App
    Config.set('graphics', 'width', str(width_of_board))
    Config.set('graphics', 'height', str(height_of_board))

    #Make the App non-resizable
    Config.set('graphics', 'resizable', '0')
    Config.write()

    #Make the top windows bar go away
    Window.borderless = True

    #Runs the
    window().run()


if __name__ == "__main__":
    setup()

'''
TODO LIST



2.5 CODE A DRAGGING SYSTEM AND A TOUCH-BASED SYSTEM
    2.75 MAKE THE DRAGGING SYSTEM HAVE THE PIECES MOVE A LAYER UP FROM THE BOARD
3. CODE ALL OF THE MOVES FOR THE PIECES (HARD; MAKE CODE STILL NEAT)
4. CREATE A SYSTEM OF TURN-BASED GAMEPLAY (MEDIUM; NEED TO KEEP CODE CLEAN)
5. CREATE A SYSTEM TO SHOW THE USER WHERE TO PLACE: AND A CHECK-BASED SYSTEM
6. CREATE A SYSTEM FOR KILLING OTHER PIECES

DONE;
THE GAMEPLAY SHOULD BE BASICALLY DONE

'''

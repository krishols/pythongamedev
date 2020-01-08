## Events: generated to inform you of user input (such as mouse movements and key presses) 
    
   * Events can be generated at any time, regardless of what the program is doing
    
   * Events are stored in a queue until the program acknowledges and handles them 
    
   * pygame.event.get() retrieves all of the events and removes them from the queue 

   * pygame.event.poll() returns a single event 

   * pygame.event.pump() can be used if the program doesn’t use any events 

####It is important to include some sort of event-handling function because otherwise the events build-up in the queue. 

##Mouse motion events are issued whenever the user moves the mouse over the Pygame window. 
    
   These events contain three values:

   * Buttons: a tuple of three numbers that correspond to the left, middle, and right buttons on the mouse. A value of 0 indicates that the button is not pressed, 1 indicates that the button is pressed

   * Pos: a tuple containing the position of the mouse when the event was generated

   * Rel: a tuple containing the distance the mouse has moved since the last mouse motion event (also called mouse mickies) 

Mouse button events indicate whether the mouse was pressed (down) or released (up).
 
   These events contain two values: 
    
   * Button: the number of the button pressed. 1-left mouse button. 2-middle mouse button. 3-right mouse button. 
    
   * Pos: a tuple containing the position of the mouse when the event was generated 
    
##Keyboard events indicate whether a button has been pressed (KEYDOWN) or released (KEYUP).
 
   They contain three values: 
    
   * Key: a number representing the key that was pressed or released. K_a is a key, K_z is z key, K_SPACE is space bar, etc. 
    
   * Mod: represents keys that are used in combination with other keys 
    
### Unicode: the unicode value of the key pressed. Produced by combining the pressed key with any of the modifier keys that was pressed 

### You can block events from the event queue with pygame.event.set_blocked() 

### You can allow certain events to enter the event queue with pygame.event.set_allowed() 

## Opening a display: 
pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0)

* Size: pair of numbers representing height and width of window 

* Flags: controls what type of screen you want. Could pass through FULLSCREEN to make display full screen. 

* Depth: should not usually pass a depth argument, as pygame will default to best and fastest color depth for the system

* Display: display 0 means the default display is used 

### To use a font, a font object must be created. 

* The easiest way to do this is: pygame.font.SysFont 
* Ex. arial_font = pygame.font.SysFont(“arial”, 16) 

## Color: 
When passing a color in Pygame, colors are represented in a tuple of 3 integers-one for each color component in red, green, and blue. 

## Storing images: 
* Use JPEG for large images with lots of color variation

* Otherwise use PNGs 

* Pygame also supports GIF, BMP, PCX, TGA, TIF, LBM, PBM, XPM 

## Loading images: 
pygame.image.load takes the file name of the image you want to load and returns a surface object 

## Rectangles: 
You can define a rectangle using a tuple that contains four values: the x and y coordinate of the top-left corner followed by the width and height of the rectangle.
 
 Otherwise, you can give 2 tuples: a tuple with the x and y coordinates of the top-left corner, and then a tuple with the width and height. 

Rect(100, 100, 200, 150) 

Rect((100, 100), (200, 150)) 

## Clipping Area: 
a rectangle defining what part of the screen can be drawn to 

screen.set_clip(0, 300, 640, 180)

## Subsurfaces: 
a subsurface is a surface inside another surface. When you draw onto a subsurface you also draw onto its parent surface. Subsurfaces are often used to draw graphical fonts from an image containing the alphabet and making subsurfaces of each letter 

pygame.image.load(“font.png”).subsurface((0, 0), (80, 80))

## Filling surfaces: 
screen.fill((0,0,0)) takes a color and fills the screen with that color 

## Blitting:
* blitting, bit block transfer, occurs by copying image data from one surface to another, useful in drawing backgrounds, characters, etc. “To blit a surface, you call blit from the destination surface object (often the display) and give it the source surface (your sprite, background, and so forth), followed by the coordinate you want to blit it to. You can also blit just a portion of the surface by adding a Rect-style object to the parameter that defines the source region” (82). 
* screen.blit(character, (0,0)) 
* screen.blit(character, (250, 250), (0, 0, 100, 100))

## Draw: 
drawing in pygame https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

Moving sprites functions by changing the coordinates of the sprite 

Vectors and vector math are used to move sprites 

I hit a block around the implementation of vector math and keyboard/mouse movement...taking notes became difficult. I think this is where application and critical thinking comes into play and I’m not sure how to communicate that.  

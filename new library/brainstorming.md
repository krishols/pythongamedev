# Why are we doing this?
* in CS1 we wanted to have a final project including game dev, because games are good
* using Python as the most popular intro language
* data demonstrating poor results using Arcade (fall sem data) for local needs
* a thing to separate is the library itself and the teaching of it, phrasing
* fall sem data:
    * data set had 12 different options of games falling within easy, medium,
    and hard categories
    * regarding functionality less than half the class succeeded in all features working
    * testing quality was variable
    * data suggests there was no time to polish, possibly not comfortable creating creative games in 
    arcade 
* summary evaluations:
    * barely half claim arcade is engaging
    * "what 1-3 things would you change of the c ourse", out of 112 lines, arcade comes up 54 times
* looking for lightweight in terms of content, provides a motivating context:
 not looking to dedicate entirety of CS1 to game development. Arcade requires too much
 instructional time/support to dedicate to final project.
* Arcade unable to test
* Arcade API issues
* Arcade graphics speed
    * built on pyglet
* Repl.it supports pygame not pyglet

# Researh Questions
1. How to design the user experience of learning and using the library?
    * using the library comes after learning the library
    * presentation-->participation-->feedback on participation
        * give context in paper regarding design and treatment of these aspects
        regarding the learning of the library
2. Long-term: Can a properly designed library increase student motivation and project
outcomes?

--
3. (Not a research question) Can you make a CS1 Python library with our desired features?


# Where to go from here
* has specific curriculum/tools to learn and then use
* need to push earlier in the semester but not make it a gamedev course
* natural, understandable API, tutorial, docs, that supports our learning objectives
    * dictionaries, lists
    * but also testing
    * approaching from learning sciences: language, user interface
* "misconceptions are so yesterday" and "re: misconceptions are so yesterday"
* collect concrete user data: interview for syntax
* distribution of students' abilities 
* GameObjects: Sprite, Image, Texture 

# Feature set 
* ability to manipulate graphics 
    * load from file and urls 
    * get and set as 2D array 
    * image primitives (shapes/lines)
    * image composition (below, above, overlay) to combine images 
    * print images to console 
    * unit testing for graphics: methodology 
* Game/Animation 
    * visible main game loop vs invisible main game loop- introducing visible game loop further 
    in curriculum 
    * inputs* (it would be nice but...)
* What set of game objects do we want-what do we call them/what is their design? (scene/camera/view/window/screen)
* double buffering and dirty (changed/needs to be updated)

##### Language hierarchy
Python/Java Script-high level
Java
C++
C - low level
MIPS/X86 
Binary
Physical gates
Physics
* The advantage of going down is speed but complexity 
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


"what do i want my API to look like?"
"

"
week 1 
1. literature review-2 hr 
2. pygame-2 
3. what should the API look like-1 hr
    think of some assignments for the semester
    
google scholar cite backtrack quorum research 

professor pollock

flip and blit semantics 

realpython for pygame tutorials 

week 2 
1. literature review - hone in on semantics    
    * larger constructs and understanding of language semantics and api design 
    
2. pygame 

---
next steps 3/3/2020

* think of actual assignments 

### API 
1. graphic/pictures
    - media comp
    - PIL/pillow 
        - scale
        - rotate
        - load a file from a url 
        - make shapes 
2. animation 
    - arcade 
    - pygame 
        - collisions 
        - have a sprite in a window 
        - movement 
        - events 
    
    
### Things to think about 
Order of teaching: 
- variables, values, types/operators
- functions 
- if statements 
- for, while, recursion, classes, dictionaries ??? modules 
- What do we want the user to write/see/use? 

2 different ways to approach: 
1. subclassing 
2. while True: main game loop 

Week 1: 
from banana import image 
dog = image("dog.png")
print(dog) # dog = dog * 2 
dog.scale(2) 

* user study: what type of code would you write to design game? 

---
week 4 
- (function definitions and if statements)

        def dog_game(score): 
        
        if is_clicked(dog): 
    
        score += 1 
        
        return game
        
        run_game(dog, dog_game, 0)

(takes in dog image and function)
---
week 8 - 12 
introduce game 
https://dl-acm-org.udel.idm.oclc.org/doi/pdf/10.1145/1539024.1508947?download=true

@inproceedings{luxton2009simple,
  title={A simple framework for interactive games in CS1},
  author={Luxton-Reilly, Andrew and Denny, Paul},
  booktitle={Proceedings of the 40th ACM technical symposium on Computer science education},
  pages={216--220},
  year={2009}
}

## Notes 
* "Constructivists hold that knowledge cannot be passively
absorbed from others, but rather that each person constructs
their own understanding of a concept based on the interaction between new information and their prior knowledge.
Teachers provide guidance to help students overcome misconceptions and build a more accurate internal model [5]" (216)
    * This is an interesting epistemological perspective to take
    * How does learning occur when students enter new disciplines with very little
    prior knowledge to interact with? Is this where misconceptions come in? 
        * How do forming new habits and breaking old habits differ? 

## Framework 
Basic framework is 20 lines of code-students are expected to expand upon
as their learning progresses to personalize the game.
##### Properties: 
* window creation
* handling of key events 
* animation 
* collision testing 
##### Classes: 
Initially there are two classes: 
* GameFramework: 
    * handles events 
* Player class: 
    * represents user-controlled object 
    * intially moves horizontally or vertically in response to arrow keys 
    
#### Extending the framework: 
Adding new objects is a two step process of: 
1. Defining the object as a new class
2. Updating the GameFramework class with respect to the new class created 
* A suggestion the author provides for extending the framework is to create
a new Goal class that creates a new object for the Player object to collide with,
and after detecting a collision prompts another action to occur 


## Value
The authors of this paper conducted and presented their research (see discussion + gender issues sections)
in a comphrehensive way: provided appropriate stats and acknowledged threats to validity 
They considered female response to their framework to consider gender discrepancies, but I think it 
would have been valuable to provide male responses as well. 
## Conclusion of Paper
The paper came to the conclusion that game development in CS1 is engaging: 
       
       "Interactive, graphical games are a good fit with a constructivist pedagogy. They bring fun into the classroom,
        motivate students, provide real-world context and help students visualise the interaction between objects" (220) 

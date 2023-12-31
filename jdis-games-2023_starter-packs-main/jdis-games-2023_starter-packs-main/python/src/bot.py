import random
from core.action import Action, Direction, Pattern, Teleport
from core.game_state import GameState, Player


class MyBot:
    """
    (fr)
    Cette classe représente votre bot. Vous pouvez y définir des attributs et des méthodes qui 
    seront conservés entre chaque appel de la méthode `tick`.

    (en)
    This class represents your bot. You can define attributes and methods in it that will be kept 
    between each call of the `tick` method.
    """
    def __init__(self):
        self.__name = "BICHON"
        self.__first_turn = True
        self.counter = 5
        self.counterCopy = self.counter
        self.counterDirection = 4


    def __random_action(self) -> Action:
        return random.choice(list(Direction))


    def SetDeconnectionPattern(self) -> Action:
        return Action(Pattern([Direction.UP, Direction.UP, Direction.UP,Direction.UP, Direction.UP,
                               Direction.RIGHT,Direction.RIGHT,Direction.RIGHT, Direction.RIGHT,
                               Direction.DOWN,Direction.DOWN,Direction.DOWN,
                               Direction.LEFT,Direction.LEFT,Direction.LEFT,Direction.LEFT,
                               Direction.LEFT,Direction.LEFT,Direction.LEFT]))


    def cube(self) ->Action : 
        if self.counterCopy > 0:
            if self.counterDirection == 4 :
                self.counterCopy =-1
                return Action(Direction.UP)
            if self.counterDirection == 3 :
                self.counterCopy =-1
                return Action(Direction.RIGHT)
            if self.counterDirection == 2 :
                self.counterCopy =-1
                return Action(Direction.DOWN)
            if self.counterDirection == 1 :
                self.counterCopy =-1
                return Action(Direction.LEFT) 
        self.counterDirection -= 1
        if self.counterDirection == 0 :
            self.counter += 1  
        self.counterCopy = self.counter
        return Action(Direction.LEFT)


    def tick(self, state: GameState) -> Action:
        """
        (en)
        This method is called every game tick. You can define the behavior of your bot. It must 
        return an instance of `Action` which will be executed by the server.

        Args:
            state (GameState):  (fr) L'état du jeu.
                                (en) The state of the game.
        """
        if self.__first_turn:
            self.__first_turn = False
            self.SetDeconnectionPattern()
        
        
        return self.cube()
    

class HangmanDrawing:
    def __init__(self):
        self.stages = [
            """
               ------
               |    |
               |    
               |   
               |    
               |   
            --------
            """,
            """
               ------
               |    |
               |    O
               |   
               |    
               |   
            --------
            """,
            """
               ------
               |    |
               |    O
               |    |
               |    
               |   
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |    
               |   
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |    
               |   
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / 
               |   
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |   
            --------
            """
        ]

    def draw(self, stage, word_guessed):
        if stage < len(self.stages):
            print(self.stages[stage])
        else:
            print("No more stages.")

        print("Word: " + " ".join(word_guessed))


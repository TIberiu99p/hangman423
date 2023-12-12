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

    def draw(self, stage):
        if stage < len(self.stages):
            print(self.stages[stage])
        else:
            print("No more stages.")




import vector

class Chessboard:
    def __init__(self, m):
        self.m = m
        self.squares = {}
        self.init_board()
    
    def insert_piece(self, position, piece):
        if(position.x < 0 or position.y < 0 or position.x >= self.m or position.y >= self.m):
            raise ValueError("Position not in Board")
        
        if(position in self.squares):
            raise ValueError("Position is already taken")
        
        self.squares[position] = piece 
    
    def init_board(self):
        if(self.m == 8):
            color_upper = "black"
            color_lower = "white"
            for j in range(self.m):
                self.squares[vector.Vector(1, j)] = Pawn(color_upper)
            
            self.squares[vector.Vector(0, 0)] = Rook(color_upper)
            self.squares[vector.Vector(0, 1)] = Knight(color_upper)
            self.squares[vector.Vector(0, 2)] = Bishop(color_upper)
            self.squares[vector.Vector(0, 3)] = Queen(color_upper)
            self.squares[vector.Vector(0, 4)] = King(color_upper)
            self.squares[vector.Vector(0, 5)] = Bishop(color_upper)
            self.squares[vector.Vector(0, 6)] = Knight(color_upper)
            self.squares[vector.Vector(0, 7)] = Rook(color_upper)

            for j in range(self.m):
                self.squares[vector.Vector(self.m - 2, j)] = Pawn(color_lower)
            
            self.squares[vector.Vector(self.m - 1, 0)] = Rook(color_lower)
            self.squares[vector.Vector(self.m - 1, 1)] = Knight(color_lower)
            self.squares[vector.Vector(self.m - 1, 2)] = Bishop(color_lower)
            self.squares[vector.Vector(self.m - 1, 3)] = Queen(color_lower)
            self.squares[vector.Vector(self.m - 1, 4)] = King(color_lower)
            self.squares[vector.Vector(self.m - 1, 5)] = Bishop(color_lower)
            self.squares[vector.Vector(self.m - 1, 6)] = Knight(color_lower)
            self.squares[vector.Vector(self.m - 1, 7)] = Rook(color_lower)
        else:
            raise ValueError("init_board not implemented for size != 8")
    
    def __str__(self):
        """
        res = ""
        for i in range(self.m):
            for j in range(self.m):
                pos = vector.Vector(i, j)
                if(pos in self.squares):
                    res += str(self.squares[pos])
                else:
                    res += " "
                res += " "
            res += "\n"
        return res"
        """
        # ANSI color codes
        RESET = "\033[0m"
        BG_LIGHT = "\033[48;5;180m"  # Light brown background
        BG_DARK = "\033[48;5;94m"    # Dark brown background
        FG_RED = "\033[31;1m"        # Bold red text (for black pieces)
        FG_WHITE = "\033[37;1m"      # Bold white text (for white pieces)
        
        # Size of each square in characters (width x height)
        #square_width = 5
        square_width = 3
        square_height = 3
        
        # Column labels
        column_labels = "    " + "     ".join([chr(97 + j) for j in range(self.m)])
        
        # Initialize the result string with column labels
        res = column_labels + "\n"
        
        # For each row of the board
        for i in range(self.m):
            # Each square has square_height lines
            for line in range(square_height):
                # Add row label on the first line of each row
                if line == square_height // 2:
                    res += f" {8-i} "
                else:
                    res += "   "
                
                # For each column in the row
                for j in range(self.m):
                    pos = vector.Vector(i, j)
                    # Determine background color (alternating)
                    bg_color = BG_LIGHT if (i + j) % 2 == 0 else BG_DARK
                    
                    # Get piece at this position, if any
                    piece_str = " "
                    if pos in self.squares:
                        piece = self.squares[pos]
                        # Determine text color based on piece color
                        fg_color = FG_RED if piece.color == "black" else FG_WHITE
                        piece_str = str(piece)
                    else:
                        fg_color = RESET
                    
                    # Middle line contains the piece, other lines are empty
                    if line == square_height // 2:
                        content = f"  {fg_color}{piece_str}{RESET}  " if pos in self.squares else "     "
                    else:
                        content = "     "  # Empty space for top and bottom lines
                    
                    # Add the square with appropriate colors
                    res += f"{bg_color}{content}{RESET}"
                
                # Add row label on the first line of each row (right side)
                if line == square_height // 2:
                    res += f" {8-i} "
                
                res += "\n"
                
        # Add column labels at the bottom
        res += column_labels
        
        return res



        
class Piece:
    def __init__(self, color):
        self.color = color  
    def __str__(self):
        return "*"
    def __repr__(self):
        return "*"
class Rook(Piece):
    
    def __str__(self):
        return "R"

class Knight(Piece):
    def __str__(self):
        return "k"

class Bishop(Piece):
    def __str__(self):
        return "B" 

class Queen(Piece):
    def __str__(self):
        return "Q"

class King(Piece):
    def __str__(self):
        return "K" 

class Pawn(Piece):
    def __str__(self):
        return "P"

if __name__ == "__main__":
    board = Chessboard(8)
    print(board)
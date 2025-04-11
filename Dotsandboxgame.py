from typing import List, Tuple, Optional

class DotsAndBoxes:
    def __init__(self, rows: int = 5, cols: int = 5):
        """
        Initialize the Dots and Boxes game.
        
        Args:
            rows: Number of rows of dots (creates rows-1 boxes vertically)
            cols: Number of columns of dots (creates cols-1 boxes horizontally)
        """
        self.rows = rows
        self.cols = cols
        self.h_lines = [[False for _ in range(cols-1)] for _ in range(rows)]
        self.v_lines = [[False for _ in range(cols)] for _ in range(rows-1)]
        self.box_owners = [[None for _ in range(cols-1)] for _ in range(rows-1)]
        self.current_player = 1  # Player 1 starts
        self.scores = {1: 0, 2: 0}
    
    def make_move(self, line_type: str, row: int, col: int) -> bool:
        """
        Attempt to make a move.
        
        Args:
            line_type: 'h' for horizontal line, 'v' for vertical line
            row: Row index of the line
            col: Column index of the line
            
        Returns:
            True if the move was valid and completed, False otherwise
        """
        if line_type == 'h' and 0 <= row < self.rows and 0 <= col < self.cols-1:
            if not self.h_lines[row][col]:
                self.h_lines[row][col] = True
                return self.check_boxes_after_move(line_type, row, col)
        elif line_type == 'v' and 0 <= row < self.rows-1 and 0 <= col < self.cols:
            if not self.v_lines[row][col]:
                self.v_lines[row][col] = True
                return self.check_boxes_after_move(line_type, row, col)
        return False
    
    def check_boxes_after_move(self, line_type: str, row: int, col: int) -> bool:
        """
        Check if the move completed any boxes and update scores accordingly.
        
        Returns:
            True if boxes were completed (player gets another turn), False otherwise
        """
        boxes_completed = False
        
        if line_type == 'h':
            # Check box above the horizontal line
            if row > 0:
                if (self.h_lines[row-1][col] and 
                    self.v_lines[row-1][col] and 
                    self.v_lines[row-1][col+1] and 
                    self.box_owners[row-1][col] is None):
                    self.box_owners[row-1][col] = self.current_player
                    self.scores[self.current_player] += 1
                    boxes_completed = True
            
            # Check box below the horizontal line
            if row < self.rows-1:
                if (self.h_lines[row+1][col] and 
                    self.v_lines[row][col] and 
                    self.v_lines[row][col+1] and 
                    self.box_owners[row][col] is None):
                    self.box_owners[row][col] = self.current_player
                    self.scores[self.current_player] += 1
                    boxes_completed = True
        
        elif line_type == 'v':
            # Check box to the left of the vertical line
            if col > 0:
                if (self.v_lines[row][col-1] and 
                    self.h_lines[row][col-1] and 
                    self.h_lines[row+1][col-1] and 
                    self.box_owners[row][col-1] is None):
                    self.box_owners[row][col-1] = self.current_player
                    self.scores[self.current_player] += 1
                    boxes_completed = True
            
            # Check box to the right of the vertical line
            if col < self.cols-1:
                if (self.v_lines[row][col+1] and 
                    self.h_lines[row][col] and 
                    self.h_lines[row+1][col] and 
                    self.box_owners[row][col] is None):
                    self.box_owners[row][col] = self.current_player
                    self.scores[self.current_player] += 1
                    boxes_completed = True
        
        if not boxes_completed:
            self.current_player = 3 - self.current_player  # Switch player (1->2, 2->1)
        
        return boxes_completed
    
    def is_game_over(self) -> bool:
        """Check if all lines have been drawn (game over)."""
        return (all(all(row) for row in self.h_lines) and 
                all(all(row) for row in self.v_lines))
    
    def get_winner(self) -> Optional[int]:
        """Return the player with higher score, or None if tie."""
        if not self.is_game_over():
            return None
        if self.scores[1] > self.scores[2]:
            return 1
        elif self.scores[2] > self.scores[1]:
            return 2
        return None

import pygame
import sys
from typing import Tuple
from .game import DotsAndBoxes

# Constants
DOT_COLOR = (0, 0, 0)
LINE_COLOR = (100, 100, 100)
PLAYER_COLORS = {
    1: (255, 0, 0),  # Red
    2: (0, 0, 255)   # Blue
}
BACKGROUND_COLOR = (255, 255, 255)
DOT_RADIUS = 5
LINE_WIDTH = 3
GRID_SPACING = 60
MARGIN = 50

class DotsAndBoxesGUI:
    def __init__(self, rows: int = 5, cols: int = 5):
        self.game = DotsAndBoxes(rows, cols)
        self.rows = rows
        self.cols = cols
        
        # Calculate window size
        width = (cols - 1) * GRID_SPACING + 2 * MARGIN
        height = (rows - 1) * GRID_SPACING + 2 * MARGIN
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Dots and Boxes")
        self.font = pygame.font.SysFont('Arial', 24)
    
    def draw_board(self):
        """Draw the current state of the board."""
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw dots
        for row in range(self.rows):
            for col in range(self.cols):
                x = MARGIN + col * GRID_SPACING
                y = MARGIN + row * GRID_SPACING
                pygame.draw.circle(self.screen, DOT_COLOR, (x, y), DOT_RADIUS)
        
        # Draw horizontal lines
        for row in range(self.rows):
            for col in range(self.cols - 1):
                if self.game.h_lines[row][col]:
                    x1 = MARGIN + col * GRID_SPACING
                    x2 = MARGIN + (col + 1) * GRID_SPACING
                    y = MARGIN + row * GRID_SPACING
                    pygame.draw.line(self.screen, LINE_COLOR, (x1, y), (x2, y), LINE_WIDTH)
        
        # Draw vertical lines
        for row in range(self.rows - 1):
            for col in range(self.cols):
                if self.game.v_lines[row][col]:
                    y1 = MARGIN + row * GRID_SPACING
                    y2 = MARGIN + (row + 1) * GRID_SPACING
                    x = MARGIN + col * GRID_SPACING
                    pygame.draw.line(self.screen, LINE_COLOR, (x, y1), (x, y2), LINE_WIDTH)
        
        # Draw boxes with owner colors
        for row in range(self.rows - 1):
            for col in range(self.cols - 1):
                if self.game.box_owners[row][col] is not None:
                    x = MARGIN + col * GRID_SPACING + GRID_SPACING // 2
                    y = MARGIN + row * GRID_SPACING + GRID_SPACING // 2
                    pygame.draw.rect(
                        self.screen, 
                        PLAYER_COLORS[self.game.box_owners[row][col]],
                        (x - GRID_SPACING//2 + 2, y - GRID_SPACING//2 + 2, 
                         GRID_SPACING - 4, GRID_SPACING - 4)
                    )
        
        # Draw scores
        score_text = self.font.render(
            f"Player 1: {self.game.scores[1]}  |  Player 2: {self.game.scores[2]}", 
            True, (0, 0, 0))
        self.screen.blit(score_text, (20, 10))
        
        # Draw current player indicator
        player_text = self.font.render(
            f"Current Player: {self.game.current_player}", 
            True, PLAYER_COLORS[self.game.current_player])
        self.screen.blit(player_text, (20, 40))
        
        # Check for game over
        if self.game.is_game_over():
            winner = self.game.get_winner()
            if winner:
                end_text = self.font.render(
                    f"Player {winner} wins!", True, PLAYER_COLORS[winner])
            else:
                end_text = self.font.render("It's a tie!", True, (0, 0, 0))
            
            text_rect = end_text.get_rect(center=(self.screen.get_width()//2, 
                                             self.screen.get_height()//2))
            pygame.draw.rect(self.screen, (255, 255, 200), 
                           (text_rect.x-10, text_rect.y-10, 
                            text_rect.width+20, text_rect.height+20))
            self.screen.blit(end_text, text_rect)
        
        pygame.display.flip()
    
    def handle_click(self, pos: Tuple[int, int]):
        """Handle mouse click events."""
        x, y = pos
        
        # Check if click is within grid bounds
        if not (MARGIN <= x <= MARGIN + (self.cols-1)*GRID_SPACING and
                MARGIN <= y <= MARGIN + (self.rows-1)*GRID_SPACING):
            return
        
        # Find nearest grid point
        col = round((x - MARGIN) / GRID_SPACING)
        row = round((y - MARGIN) / GRID_SPACING)
        
        # Determine if click is closer to horizontal or vertical line
        dx = abs(x - MARGIN - col * GRID_SPACING)
        dy = abs(y - MARGIN - row * GRID_SPACING)
        
        if dx < dy and dy > DOT_RADIUS + 5:  # Near vertical line
            if 0 <= row < self.rows-1 and 0 <= col < self.cols:
                self.game.make_move('v', row, col)
        elif dx > DOT_RADIUS + 5:  # Near horizontal line
            if 0 <= row < self.rows and 0 <= col < self.cols-1:
                self.game.make_move('h', row, col)
    
    def run(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self.handle_click(event.pos)
            
            self.draw_board()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()

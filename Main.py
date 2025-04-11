from dotsandboxes.gui import DotsAndBoxesGUI

if __name__ == "__main__":
    # Create a 5x5 dots grid (4x4 boxes)
    game = DotsAndBoxesGUI(rows=5, cols=5)
    game.run()

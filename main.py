import numpy as np

   def move(self, BorW, brick):
        if BorW == "w":
            if brick == "b1" or brick == "b2" or brick == "b3" or brick == "b4" or brick == "b5" or brick == "b6" or brick == "b7" or brick == "b8":
                self.move_BW(brick)
            elif brick=="h1" or brick=="h2":
                self.move_HW(brick)
            elif brick=="l1" or brick=="l2":
                self.move_LW(brick)
        else:
            if brick == "b1" or brick == "b2" or brick == "b3" or brick == "b4" or brick == "b5" or brick == "b6" or brick == "b7" or brick == "b8":
                self.move_BB(brick)
            elif brick=="h1" or brick=="h2":
                self.move_HB(brick)
             
        self.plot_board()

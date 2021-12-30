"""
Movement analysis of each horse for both black and white.

move_HW == move Horse White

"""
  
  
  
  
    def move_HW(self,brick):
        
        moves_x= np.array([2,1,-1,-2,1,-1,-2,2])
        moves_y= np.array([1,2,-2,-1,-2,2,1,-1])
        
        pos_x = self.white_bricks[brick][0]
        pos_y = self.white_bricks[brick][1]
        moves_x+=pos_x
        moves_y+=pos_y
        
        
        true_args = np.argwhere(self.white_board == False)
        true_args_x = true_args[:,1]
        true_args_y = true_args[:,0]
        
        
        DEL = np.argwhere((moves_x==true_args_x) & (moves_y==true_args_y))
        
        mov_x = []
        mov_y = []
        for a,b in zip(moves_x, moves_y):
            for r,g in zip(true_args_x,true_args_y):
                if a == r and b == g:
                    mov_x.append(a)
                    mov_y.append(b)
        
        moves_x = mov_x
        moves_y = mov_y
        
        
        m=np.random.randint(len(moves_x))
        move = np.array([moves_x[m],moves_y[m]])
        self.white_board[self.white_bricks[brick][1],self.white_bricks[brick][0]]=False
        self.white_bricks[brick][0] = move[0]
        self.white_bricks[brick][1] = move[1]
        self.white_board[self.white_bricks[brick][1],self.white_bricks[brick][0]]=True
        
        for i in self.bricks:
                if self.black_bricks[i][0] == self.white_bricks[brick][0] and self.black_bricks[i][1] == self.white_bricks[brick][1]:

                    self.black_bricks[i][3] = False
       
    def move_HB(self,brick):
        
        moves_x= np.array([2,1,-1,-2,1,-1,-2,2])
        moves_y= np.array([1,2,-2,-1,-2,2,1,-1])
        
        pos_x = self.black_bricks[brick][0]
        pos_y = self.black_bricks[brick][1]
        moves_x+=pos_x
        moves_y+=pos_y
        
        
        true_args = np.argwhere(self.black_board == False)
        true_args_x = true_args[:,1]
        true_args_y = true_args[:,0]
        
        
        DEL = np.argwhere((moves_x==true_args_x) & (moves_y==true_args_y))
        
        mov_x = []
        mov_y = []
        for a,b in zip(moves_x, moves_y):
            for r,g in zip(true_args_x,true_args_y):
                if a == r and b == g:
                    mov_x.append(a)
                    mov_y.append(b)
        
        moves_x = mov_x
        moves_y = mov_y
        
        
        m=np.random.randint(len(moves_x))
        move = np.array([moves_x[m],moves_y[m]])
        self.black_board[self.black_bricks[brick][1],self.black_bricks[brick][0]]=False
        self.black_bricks[brick][0] = move[0]
        self.black_bricks[brick][1] = move[1]
        self.black_board[self.black_bricks[brick][1],self.black_bricks[brick][0]]=True
        
        for i in self.bricks:
                if self.white_bricks[i][0] == self.black_bricks[brick][0] and self.white_bricks[i][1] == self.black_bricks[brick][1]:

                    self.white_bricks[i][3] = False  

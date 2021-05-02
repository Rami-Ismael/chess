class Pond(Piece):
    def __inti__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
        self.pond_moves=[(1,0)]
        self.relative_position
        #white will alway be on the bottom 
        if color=="white":
            self.relativev_positive = 0
        else :
            self.relativev_positive = 1
    def valid_move():
        return 0
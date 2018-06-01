class NQueens:
    def __init__(self,size):
        self.size = size
        self.solution = 0
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.put(positions,0)
        print "Found :",
        print  self.solution

    def put(self,positions,row):
        if row==self.size:
            self.show_full_board(positions)
            self.solution +=1
        else:
            for column in range(self.size):
                if self.checkPlace(positions,column,row):
                    positions[row] = column;
                    self.put(positions,row+1)

    def checkPlace(self,positions,column,row):
        for i in range(row):
            if positions[i]==column or\
               positions[i]-i == column - row or\
               positions[i]+i == column + row:
                return False
        return True

    def show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print

def main():
    NQueens(8)

if __name__ == '__main__':
    main()

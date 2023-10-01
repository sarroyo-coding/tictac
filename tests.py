import gamelib
import unittest

class TestGameMethod(unittest.TestCase):
    def test_check_win(self):
        row_win = [
                    [1,1,1],
                    [0,0,0],
                    [0,0,0]
        ] 
        self.assertTrue(gamelib.check_win(row_win), "Row win should be true")


    def test_col_win(self):
        col_win = [
                    [0,0,1],
                    [0,0,1],
                    [1,0,1]
                    ]
        self.assertTrue(gamelib.check_win(col_win), "Col win should be true")

    def test_diag_win(self):
        diag_win_1 = [
                    [0,0,1],
                    [0,1,0],
                    [1,0,0]
                    ]
        diag_win_2 = [
                    [1,0,0],
                    [0,1,0],
                    [0,0,1]
        ]
        self.assertTrue(gamelib.check_win(diag_win_1), "Diag win should be true")
        self.assertTrue(gamelib.check_win(diag_win_2), "Diag win should be true")
    
    def test_no_win(self):
        no_win = [
                    [0,0,1],
                    [0,0,0],
                    [1,0,0]
                    ]
        self.assertFalse(gamelib.check_win(no_win), "No win should be false")

    def test_is_stalemate(self):
        stalemate_true = [
                    [1,-1,-1],
                    [-1,1,-1],
                    [1,1,-1]
                    ]
        stalemate_false = [
                    [1,-1,-1],
                    [-1,1,0],
                    [1,1,-1]
                    ]
        self.assertTrue(gamelib.is_stalemate(stalemate_true), "Stalemate should be true")
        self.assertFalse(gamelib.is_stalemate(stalemate_false), "Stalemate should be false")

    def clear_board(self):
        stalemate_true = [
                    [1,-1,-1],
                    [-1,1,-1],
                    [1,1,-1]
                    ]
        

if __name__ == '__main__':
    unittest.main()
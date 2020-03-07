import unittest
import Tokenizecat
from Tokenizecat import Tokenizer
from Tokenizecat import Token

class TestCat(unittest.TestCase):

    maxDiff = None
    
    def setUp(self):
        self.Tokenizer = Tokenizer()

    def test_one(self):
        s = 'И это хорошо'
        self.assertEqual(self.Tokenizer.tokcat(s), ['(И:alpha, [0,1]),( :space, [1,2]),\
                            (это:alpha, [2,5]),( :space, [5,6]),(хорошо:alpha, [6,12])'])
    
    def test_numbers(self):
        s = '12487529'
        self.assertEqual(self.Tokenizer.tokcat(s),['(12487529:digit,[0,8])'])

    def test_num_n_let(self):
        s = '12This45is90good'
        self.assertEqual(self.Tokenizer.tokcat(s),['(12:digit,[0,2]),(This:alpha,[2,6]),\
                        (45:digit,[6,8]),(is:alpha,[8,10]),(90:digit,[10,12]),(good:alpha,[12,16])'])

    def test_evth_but_let(self):
        s = '&28^?!#:;'
        self.assertEqual(self.Tokenizer.tokcat(s),['(&:unk,[0,1]),(28:digit,[1,3]),\
                        (^:unk,[3,4]),(?!:punct,[4,6]),(#:unk,[6,7]),(:;:punct,[7,9])'])

    def test_no_spaces(self):
        s = 'thisisgood'
        self.assertEqual(self.Tokenizer.tokcat(s),['(thisisgood:alpha,[0,10])'])

    def test_start_unlet(self):
        s = '24this 56is 98good'
        self.assertEqual(self.Tokenizer.tokcat(s),['(24:digit,[0,2]),(this:alpha,[2,6]),\
                        ( :space,[6,7]),(56:digit,[7,9]),(is:alpha,[9,11]),( :space,[11,12]),\
                        (98:digit,[12,14]),(good:alpha,[14,18])'])

    def test_end_unlet(self):
        s = 'this24 is56 good98'
        self.assertEqual(self.Tokenizer.tokcat(s),['(this:alpha,[0,4])(24:digit,[4,6],\
                        ( :space,[6,7]),(is:alpha,[7,9]),(56:digit,[9,11]),\
                        ( :space,[11,12]),(good:alpha,[12,16]),(98:digit,[16,18])'])

class TestFirstOne(unittest.TestCase):

    def setUp(self):
        self.Tokenizer = Tokenizer()

    def test_one(self):
        s = 'И это хорошо'
        self.assertEqual(self.Tokenizer.tokenize(s),['И','это','хорошо'])
    
    def test_numbers(self):
        s = '12487529'
        self.assertEqual(self.Tokenizer.tokenize(s),[])

    def test_num_n_let(self):
        s = '12This45is96969809348590good'
        self.assertEqual(self.Tokenizer.tokenize(s),['This','is','good'])

    def test_evth_but_let(self):
        s = '&287^^&!#98'
        self.assertEqual(self.Tokenizer.tokenize(s),[])

    def test_no_spaces(self):
        s = 'thisisgood'
        self.assertEqual(self.Tokenizer.tokenize(s),['thisisgood'])

    def test_start_unlet(self):
        s = '24this 56is 98good'
        self.assertEqual(self.Tokenizer.tokenize(s),['this','is','good'])

    def test_end_unlet(self):
        s = 'this24 is56 good98'
        self.assertEqual(self.Tokenizer.tokenize(s),['this','is','good'])

    def test_null(self):
        s = ''
        self.assertEqual(self.Tokenizer.tokenize(s),[])

class TestSecondOne(unittest.TestCase):

    def test_one(self):
        s = 'И это хорошо'
        self.assertEqual(Tokenizecat.tokenize(s),['И','это','хорошо'])
    
    def test_numbers(self):
        s = '12487529'
        self.assertEqual(Tokenizecat.tokenize(s),[])

    def test_num_n_let(self):
        s = '12This45is96969809348590good'
        self.assertEqual(Tokenizecat.tokenize(s),['This','is','good'])

    def test_evth_but_let(self):
        s = '&287^^&!#98'
        self.assertEqual(Tokenizecat.tokenize(s),[])

    def test_no_spaces(self):
        s = 'thisisgood'
        self.assertEqual(Tokenizecat.tokenize(s),['thisisgood'])

    def test_start_unlet(self):
        s = '24this 56is 98good'
        self.assertEqual(Tokenizecat.tokenize(s),['this','is','good'])

    def test_end_unlet(self):
        s = 'this24 is56 good98'
        self.assertEqual(Tokenizecat.tokenize(s),['this','is','good'])

    def test_null(self):
        s = ''
        self.assertEqual(Tokenizecat.tokenize(s),[])
        
if __name__== '__main__':
    unittest.main()

import unittest
import Alpha01
from Alpha01 import Tokenizer

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
        
if __name__== '__main__':
    unittest.main()

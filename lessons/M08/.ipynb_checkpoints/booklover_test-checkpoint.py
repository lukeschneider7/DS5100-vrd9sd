import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "War of the Worlds"
        test_1.add_book(book_name, 4)
        self.assertTrue(book_name in test_1.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_2 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "World war 2"
        test_2.add_book(book_name, 4)
        test_2.add_book(book_name, 4)
        self.as
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
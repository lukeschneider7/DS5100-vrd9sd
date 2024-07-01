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
        book_count = (test_2.book_list['book_name'] == book_name).sum()
        self.assertTrue(book_count == 1, f'{book_name} in book list twice' )
          
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_3 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "How to win friends and influence people"
        test_3.add_book(book_name, 4)
        self.assertTrue(test_3.has_read("How to win friends and influence people"))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_4 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "How to win friends and influence people"
        test_4.add_book(book_name, 4)
        self.assertFalse(test_4.has_read("Harry Potter"))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_5 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "How to win friends and influence people"
        test_5.add_book(book_name, 4)
        test_5.add_book('Harry potter', 5)
        test_5.add_book('Dune', 4)
        expected = 3
        self.assertEqual(test_5.num_books_read(), expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_5 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_5.add_book('Beltway boys', 2)
        test_5.add_book('Harry potter', 5)
        test_5.add_book('Dune', 4)  
        fav_books = test_5.fav_books()
        self.assertTrue((fav_books['book_rating'] > 3).all())
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
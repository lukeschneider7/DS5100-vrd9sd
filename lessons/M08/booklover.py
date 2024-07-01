# Task 1
import pandas as pd
class BookLover():
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    
    def add_book(self, book_name, book_rating):
        if book_name in self.book_list['book_name'].values:
            print("book name given already in book list")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
            
    def num_books_read(self):
        return len(self.book_list['book_name'])
        
    def fav_books(self):
        book_list_filtered = self.book_list[self.book_list['book_rating'] > 3]
        return book_list_filtered


if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("lord of the rings", 2)
    print(test_object.has_read("elmo"))
    print(test_object.num_books_read())
    print(test_object.fav_books())
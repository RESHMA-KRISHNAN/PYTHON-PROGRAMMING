class Publisher:
    def __init__(self,Pubname):
        self.Pubname=Pubname
    def display(self):
        print("Publisher name is:",self.Pubname)


class Book(Publisher):
    def __init__(self,Pubname,title,author):
        Publisher.__init__(self,Pubname)
        self.title=title
        self.author=author
    def display(self):
        print("\nTitle:",self.title)
        print("\nAuthor:",self.author)

        
class Python(Book):
    def __init__(self,Pubname,title,author,price,no_of_pages):
        Book.__init__(self,Pubname,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("\nTitle:",self.title)
        print("\nAuthor:",self.author)
        print("\nPrice:",self.price)
        print("\nNo of pages:",self.no_of_pages,"\n")
b1=Python("DC BOOKS","Wings of Fire","A.P.J Abdul Kalam", 180, 335)
b1.display()
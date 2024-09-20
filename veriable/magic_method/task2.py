class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self,other):
        return f' {self.title} by {self.author} and pages {self.pages}'
b=Book("wealth of world","adam",20)    
print(b)
            
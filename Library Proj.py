class Library:
    def __init__(self,list,name):
        self.list = list
        self.name = name
        self.lend_dict = {}

    def displaybooks(self):
        print(f"we have following books in our library : {self.name}")
        for book in self.list:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book:user})
            print("Updated succefully,You can take the book")
        else:
            print(f"the book is already taken by {self.lend_dict[book]}")

    def addbook(self,book):
        self.list.append(book)
        print("book added successfully")

    def returnbook(self, book):
        self.lend_dict.pop(book)
        print("book returned successfully")

if __name__ == '__main__':
    revanth = Library(["python","c","html","css","java script","my sql"],"Revanth")

    while True:
        print(f"Hello , Welcome to {revanth.name} Library ")
        print("Enter your choice\n1.Display book\n2.Lend book\n3.Add book\n4.Return book")
        user_choice = input()
        if user_choice not in ["1","2","3","4"]:
            print("invalid input")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1 :
            revanth.displaybooks()

        elif user_choice == 2 :
            user = input("Enter your name : ")
            book = input("enter the book you want")
            revanth.lendbook(user,book)

        elif user_choice == 3 :
            book = input("Enter book : ")
            revanth.addbook(book)

        elif user_choice == 4:
            book = input("enter book : ")
            revanth.returnbook(book)

        else:
            print("enter a valid input")

        print("press any key to continue and q to exit")
        user_choice2 = input()
        if user_choice2 == "q":
            exit()
        else:
            continue

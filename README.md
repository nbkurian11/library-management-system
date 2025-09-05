                +------------------+
                |      Book        |
                +------------------+
                | - title: String  |
                | - author: String |
                | - ISBN: String   |
                | - available: boolean |
                +------------------+
                | + borrow(): void |
                | + returnBook(): void |
                | + toString(): String |
                +------------------+


                +-------------------+
                |   User (abstract) |
                +-------------------+
                | - id: int         |
                | - name: String    |
                +-------------------+
                | + getId(): int    |
                | + getName(): String |
                +-------------------+
                   /           \
                  /             \
   +--------------------+   +--------------------+
   |     Student        |   |      Teacher       |
   +--------------------+   +--------------------+
   | - gradeLevel: int  |   | - department: String |
   +--------------------+   +--------------------+


                +--------------------+
                |      Library       |
                +--------------------+
                | - books: List<Book>|
                | - users: List<User>|
                +--------------------+
                | + addBook(b: Book) |
                | + addUser(u: User) |
                | + searchBook(title:String): Book |
                | + listAllBooks(): void |
                +--------------------+

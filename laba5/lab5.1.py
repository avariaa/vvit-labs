class Book:
    title, author, year = '"Гарри Поттер и философский камень"', 'Джоан Роулинг', 1997

    @classmethod
    def get_info(cls):
        return f"Название книги: {cls.title}\nАвтор: {cls.author}\nГод издания: {cls.year}"


print(Book.get_info())
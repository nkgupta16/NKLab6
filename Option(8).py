class Book:
    def __init__(self, number_of_pages, reading_time_per_page, number_of_pictures):
        self.number_of_pages = number_of_pages
        self.reading_time_per_page = reading_time_per_page
        self.number_of_pictures = number_of_pictures

    def book_reading_time(self):
        return self.number_of_pages * self.reading_time_per_page


class Encyclopedia(Book):
    def __init__(self, number_of_pages, reading_time_per_page, number_of_pictures, number_of_articles):
        super().__init__(number_of_pages, reading_time_per_page, number_of_pictures)
        self.number_of_articles = number_of_articles

    def articles_per_page(self):
        return self.number_of_articles / self.number_of_pages


class TelephoneDirectory(Book):
    def __init__(self, number_of_pages, reading_time_per_page, number_of_pictures, number_of_issues):
        super().__init__(number_of_pages, reading_time_per_page, number_of_pictures)
        self.number_of_issues = number_of_issues

    def issues_per_page(self):
        return self.number_of_issues / self.number_of_pages


# Example usage:
encyclopedia = Encyclopedia(500, 2, 100, 1500)
telephone_directory = TelephoneDirectory(250, 0.5, 0, 10000)

encyclopedia_reading_time = encyclopedia.book_reading_time()
encyclopedia_articles_per_page = encyclopedia.articles_per_page()

telephone_directory_reading_time = telephone_directory.book_reading_time()
telephone_directory_issues_per_page = telephone_directory.issues_per_page()

print(f"The total reading time for the encyclopedia is {encyclopedia_reading_time} minutes.")
print(f"The average number of articles per page in the encyclopedia is {encyclopedia_articles_per_page:.2f}.")

print(f"The total reading time for the telephone directory is {telephone_directory_reading_time} minutes.")
print(f"The average number of issues per page in the telephone directory is {telephone_directory_issues_per_page:.2f}.")

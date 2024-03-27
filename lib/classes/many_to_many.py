
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        return self.__name

    def articles(self):
        return self.__articles

    def magazines(self):
        return list(set(article.magazine for article in self.__articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.__articles.append(article)
        return article

    def topic_areas(self):
        if not self.__articles:
            return None
        return list(set(article.magazine.category for article in self.__articles))


class Magazine:
    __all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self.__name = name
        self.__category = category
        self.__articles = []
        Magazine.__all_magazines.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    def articles(self):
        return self.__articles

    def contributors(self):
        authors = [article.author for article in self.__articles]
        return list(set(authors))

    def article_titles(self):
        return [article.title for article in self.__articles]

    def contributing_authors(self):
        authors = [article.author for article in self.__articles]
        return [author for author in authors if authors.count(author) > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.__all_magazines:
            return None
        return max(cls.__all_magazines, key=lambda magazine: len(magazine.articles()))


class Article:
    def __init__(self, author, magazine, title):
        self.__author = author
        self.__magazine = magazine
        self.__title = title
        author.articles().append(self)
        magazine.articles().append(self)

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine

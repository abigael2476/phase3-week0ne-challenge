class Article:
    all = []

    def __init__(self, author, magazine, title):
        # validations
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        if not 5 <= len(title) <= 50:
            raise Exception("Title length must be 5–50 characters.")

        if not isinstance(author, Author):
            raise Exception("Author must be Author instance.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be Magazine instance.")

        self._title = title
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # IMMUTABLE: ignore attempts to change
        pass

    @classmethod
    def all_articles(cls):
        return cls.all


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be string.")
        if len(name) == 0:
            raise Exception("Name cannot be empty.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # immutable: ignore changes
        pass

    # Relationship helpers
    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        mags = list({a.magazine for a in self.articles()})
        return mags if mags else None

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = [a.magazine.category for a in self.articles()]
        return list(set(topics)) if topics else None  # <-- change: return None if empty


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None

        self.name = name
        self.category = category

    # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            return
        if not (2 <= len(val) <= 16):
            return
        self._name = val

    # category
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, val):
        if not isinstance(val, str):
            return
        if len(val) == 0:
            return
        self._category = val

    # Relationships
    def articles(self):
        arts = [a for a in Article.all if a.magazine == self]
        return arts if arts else None  # <-- change: return None if empty

    def contributors(self):
        contribs = list({a.author for a in self.articles()}) if self.articles() else None
        return contribs

    def article_titles(self):
        titles = [a.title for a in self.articles()] if self.articles() else None
        return titles

    def contributing_authors(self):
        result = []
        if not self.contributors():
            return None  # <-- change: no contributors
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                result.append(author)
        return result if result else None  # <-- change: return None if empty
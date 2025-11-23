class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        # Validate title type and length
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        if not 5 <= len(title) <= 50:
            raise Exception("Title length must be 5–50 characters.")
        # Validate author and magazine types
        if not isinstance(author, Author):
            raise Exception("Author must be Author instance.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be Magazine instance.")
        
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)  # Add to class list

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass  # Title is immutable

    @classmethod
    def all_articles(cls):
        return cls.all


class Author:
    def __init__(self, name):
        # Validate name type and length
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
        pass  # Name is immutable

    def articles(self):
        # Return all articles by this author
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        # Return unique magazines author has written for
        mags = list({a.magazine for a in self.articles()})
        return mags if mags else None

    def add_article(self, magazine, title):
        # Create new article for this author
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return unique categories of magazines author has written for
        topics = [a.magazine.category for a in self.articles()]
        return list(set(topics)) if topics else None


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # Uses setter for validation
        self.category = category  # Uses setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        # Validate name type and length
        if not isinstance(val, str):
            return
        if not (2 <= len(val) <= 16):
            return
        self._name = val

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, val):
        # Validate category type and length
        if not isinstance(val, str):
            return
        if len(val) == 0:
            return
        self._category = val

    def articles(self):
        # Return all articles in this magazine
        arts = [a for a in Article.all if a.magazine == self]
        return arts if arts else None

    def contributors(self):
        # Return unique authors who contributed to this magazine
        contribs = list({a.author for a in self.articles()}) if self.articles() else None
        return contribs

    def article_titles(self):
        # Return list of all article titles in this magazine
        titles = [a.title for a in self.articles()] if self.articles() else None
        return titles

    def contributing_authors(self):
        # Return authors with more than 2 articles in this magazine
        result = []
        if not self.contributors():
            return None
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                result.append(author)
        return result if result else None
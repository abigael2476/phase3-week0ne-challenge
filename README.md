# Articles Project — Phase 3 Code Challenge

## Overview

This project is a Python **Object-Oriented Programming (OOP)** implementation of a **Magazine domain**, designed for the Phase 3 Code Challenge.  

It models a system with three main entities: **Authors, Magazines, and Articles**, and demonstrates relationships, validation, and aggregate methods.  

**Key Relationships:**

- **Author ↔ Article:** one-to-many  
- **Magazine ↔ Article:** one-to-many  
- **Author ↔ Magazine:** many-to-many (through Article)  

Bonus features include methods like `topic_areas`, `contributing_authors`, and `top_publisher`.  
All classes and methods are designed to **pass the provided pytest tests**.

---

## Folder Structure

articles_project/
│
├── lib/ # Contains main classes
│ ├── init.py # Marks this folder as a package
│ ├── author.py # Author class
│ ├── article.py # Article class
│ └── magazine.py # Magazine class
│
├── tests/ # Optional, contains pytest files
├── debug.py # Optional, for manual testing
└── README.md # This file


---

## Classes and Responsibilities

### **1. Author**
- Represents a writer who can write multiple articles.  
- Stores all articles written by the author.  
- Validates name (string, non-empty, immutable).  

**Key Methods:**
- `articles()` → list of Article objects written by the author  
- `magazines()` → unique list of magazines the author contributed to  
- `add_article(magazine, title)` → creates a new Article instance linked to this author  
- `topic_areas()` → unique categories of magazines the author has contributed to  

---

### **2. Magazine**
- Represents a magazine that publishes multiple articles.  
- Stores all articles published.  
- Validates name (2–16 characters) and category (non-empty string).  

**Key Methods:**
- `articles()` → list of all articles in the magazine  
- `contributors()` → unique list of authors who wrote for the magazine  
- `article_titles()` → list of article titles  
- `contributing_authors()` → authors with more than 2 articles  
- `top_publisher()` → class method returning magazine with most articles  

---

### **3. Article**
- Represents an article written by an author for a magazine.  
- Validates title (5–50 characters).  
- Stores references to both `author` and `magazine`.  

**Relationships:**
- Article belongs to one Author and one Magazine  
- Adding an Article automatically updates the `Author` and `Magazine` lists  

---

## Installation & Setup

1. Clone or create the project folder.  
2. Open terminal in the **project root**:

```bash
cd /path/to/articles_project
pip install pipenv
pipenv install
pipenv shell
pytest

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:08:02 2022

@author: Joshua
"""

import pandas as pd

pd.options.display.max_rows = 100
pd.options.display.max_columns = 4


bookstore_df = pd.read_csv('C:/Users/Joshua/Documents/PYTHON/booksutf.csv', delimiter=",")

 # Number of reviews for each rating
# reviews = bookstore_df['rating'].value_counts().sort_index()
# print(reviews)

# ax = reviews.plot(kind='bar', \
#                 title='Rating Distribution')
# ax.set_xlabel("Rating (stars)")
# ax.set_ylabel("Number of Reviews")
 
 # Average rating by genre  
# rating_genre = bookstore_df.groupby('genre')['rating'].mean().sort_values(ascending=False)

# print(rating_genre)

# ax = rating_genre.plot(kind='bar', \
#                 title='Genre Rating Distribution')
# ax.set_xlabel("Genre")
# ax.set_ylabel("Rating (stars)")

 # Average price by genre  
# price_genre = bookstore_df.groupby('genre')['price'].mean().sort_values(ascending=False)

# print(price_genre)

# ax = price_genre.plot(kind='bar', \
#                 title='Average Book Price by Genre')
# ax.set_xlabel("Genre")
# ax.set_ylabel("Price ($)")

 # Average rating by price  
rating_price = bookstore_df.groupby('rating')['price'].mean()

print(rating_price)

ax = rating_price.plot(kind='bar', \
                title='Average Book Price by Rating')
ax.set_xlabel("Rating (stars)")
ax.set_ylabel("Price ($)")


#### :books: bookstore_web_scrape.py
##### A simple code that highlights some of the more basic aspects of web scraping. The code first creates a list of book genres from the homepage of a faux e-commerce website. It then iterates over the genre-specific urls to extract the *Book Title*, *Rating*, and *Price* from each container. The data is then written to a csv file for later analysis. The code is able to handle conditional instances where there is either one or multiple pages for a given genre. 

#### :books: bookstore_analysis.py

##### From the csv file created by [bookstore_web_scrape.py](https://github.com/Josh-Em/Data-Collection/blob/main/bookstore_web_scrape.py), a brief analysis is done using the pandas package. The data is plotted in various figures in an attempt to ascertain trends. The figures are presented below. 

![rating_dist](https://user-images.githubusercontent.com/98699929/153882568-885b2613-a51a-40bb-9778-a5e9f623ba03.png)

###### Figure 1. We might have expeted a more bell shaped distribution for this one, or even ideally one in which most of the books have a four or five star review. That the number of one star reviews exceeds that of four and five does not bode well for the reputation of this book store. 

![price_rating_dist](https://user-images.githubusercontent.com/98699929/153882566-d4832fed-4e06-482e-9086-9a1c091b2a7f.png)

###### Figure 2. So it turns out that a books price does not depend on it rating. It might make more sense to have lower rated books be less expensive than higher rated books. 

![genre_dist](https://user-images.githubusercontent.com/98699929/153882561-04f56c16-4a38-4a17-afd0-9529ef6b30e4.png)

###### Figure 3. Well, it looks like the erotica and adult-fiction genres are pretty steamy. This becomes less statistically significant though when we consider that there is only a single book in each of the genres. The same can be said for those genres found on the opposite end of the scale (i.e. crime, cultural, and paranormal).

![price_dist](https://user-images.githubusercontent.com/98699929/153882564-1e9b9528-d08a-4ef0-8fc4-43772b00e87a.png)

###### Figure 4. A similar shape to Fig. 3. It seems that most genres have an average book price within the $35-40ish region while the outliers are not statistically significant. 





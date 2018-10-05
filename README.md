# SuperWiemen

# SuperWiemen


Data_Analysis

Our data is collected from three sources and then processed to rate a place based on safety. The three parameters that we used are:

1. From Crowd Sourcing : In our app, there is a google form through which people can rate a place on the basis of its safety at day 
or night. This data is then used to contribute to the the overall rating of a place. This is done by data_analysis/xlsx_file.py. 

2. From Web Crawling : This is just like anyone of us would do if we want to know about the safety of a place. The file 
"data_analysis/text_processing.py" searches for a particular place throughout the web. It basically looks for the crime or rape
news in that area and its frequency. Based on this crawling, a rating has been generated that also contributes to the overall rating 
of a place. If there is any place that has not been rated by anyone, then this is the only method to rate it.

3. From Existing Databases : This is the number of crimes happening in a particular place that are available on various websites. 
This data has also been processed and contribute to final rating.This is done by "data_analysis/crime_analysis.py".





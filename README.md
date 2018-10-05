# SuperWiemen

WieAssist

This app collects data from different sources such as crowd sourcing and news to rate a place in terms of safety for women. This is a personalised app that tracks your daily schedule and alerts you in case of any anamoly for ex - if you are running late. It aims to take care of all the daily habits like taking the safest route and means of transport that can make safety a priority. Thus this app embeds safety in your life. After all, 'Prevention is better than cure'.

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

The final rating is decided by final_rating.py and uploaded on firebase from where these ratings can be accessed according to the requirement. 







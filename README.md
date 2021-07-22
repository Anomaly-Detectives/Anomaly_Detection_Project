# Anomaly Detection Project

By: Alberto Puentes & Natasha Rivers

In this project, we attempted to resolve several questions regarding anomalous acitivty in the curriculum log data.  Utilizing continuous/discrete probabilistic methods as well as methods to detect time series anomalies, we were able to navigate a dataframe of over 900,000 observations across 11 features and detect anamolous activity.   Our project goals were to address the following questions:

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
3. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
5. Which lessons are least accessed?


### Takeaways:

- By looping through the Program IDs we were able to identify 2 Web Development and 1 Data Science Program
    * For the Web Development Programs, javascript-i was the most accessed curriculum followed by html-css & java-iii.
        * spring, jquery and mysql curriculum pages were also highly visited across both Programs
    * For the Data Science Program, the classification/overview curriculum page was the most visited, closely follewed by: 1-fundamentals/modern-data-scientist.jpg 1655, 1-fundamentals/AI-ML-DL-timeline.jpg 1651, 1-fundamentals/1.1-intro-to-data-science 1633, classification/scale_features_or_not.svg

- By utilizing Bollinger Bands and %B metrics, we were able to identify potential anomalous curriculum log activity by isolating page log counts that exceeded the upper boundary.  During our exploration of the most egregious occurences, we identified the following:

* excessive daily page visits don't necessarily indicate foul access.  In most cases, timestamps and dates suggested the students were downloading material for their own benefit or to retain locally after ending the course.  
    * However, by evaluating IP usage throughout the course window and timestamps on dates where activity appeared anomalous, we found that cerain user id's had been compromised and that an automated/algo was likely driving page log counts.  


<br>

- Student who accessed curriculum  the least:

| User_id      |   times accessed    |   Cohort      |  Program |
|--------------|---------------------|---------------|----------|
| 388          | 8                   |  31           | 2        | 
| 812          | 7                   |  58           | 2        | 
| 956          | 5                   |  139          | 2        | 
| 278          | 4                   |  24           | 2        | 
| 832          | 3                   |  62           | 2        | 
| 679          | 3                   |  59           | 3        | 
| 879          | 1                   |  135          | 2        | 


    
    ***These are the only users who accessed the curriculum less than 10 times***

- program 2 (Java) seems to have the users that access curriculum the least

<br>

- The topics that post-graduates are continuing to access (by program) are:
    - Program 1 (PHP):
        - javascript-i
        - html-ss
        - spring

    - Program 2 (Java):
        - javascript-i
        - spring
        - html-ss

    - Program 3 (Data Science):
        - my_sql overview
        - classification/overview
        - classification/scale_features_or_not

<br>

- The least accessed curriculum pages are:
    - 5-stats/sampling
    - 7-clustering/3-wrangle
    - capstone-workbook
    - professional-development/professionalism-101
    - 12-distributed-ml/4-acquire
    - 10_Appendix_EntityLabeling
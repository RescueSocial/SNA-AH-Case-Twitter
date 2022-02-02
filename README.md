# SNA-AH-Case - Twitter 
Twitter - Social Network Analysis on Amber Heard's Case Example from Data Analysts, Researchers, and Technologists.
- Analysis and data of timelines, accounts, peaks, wordclouds, hashtags, top shared urls, are included.

Twitter is the most studied platform, so after a cyber intelligence researcher collected data with APIs, obtaining analysis on it was relatively fast with previous models already created and high levels of anomalies. Although YouTube, one of the least studied platforms, has higher volume of accounts and repeated texts, the operation on Twitter is continual, risk-infused, and dense.

A first team of 3 Udacity graduates in data analysis quickly studied the years 2018-2021 for peaks, anomalies, and new account layers. NLP analysis is included, though mainly studying timelines and correlations. They used machine learning and botometer to create botscores.
<i><br><b>New accounts created each month and day correlate to peaks on Twitter</b></i>

A 2nd team did Coordination Analysis of Top 475 accounts, including Network Graphs of following coordination. With public safety grants, they had previously studied identifying risk groups on Twitter: https://www.sciencedirect.com/science/article/abs/pii/S1751157720306386

A Cyber Intelligence Researcher in Italy collected Twitter, Reddit, and Instagram Data on Amber Heard and created Twitter and Reddit Dashboards of statistics.
### Topic-based account groups - Cyber Intelligence Researcher Analysis

Using Google’s <a href="https://tfhub.dev/google/universal-sentence-encoder/1">Universal Sentence Encoder</a> which encodes text into high dimensional vectors, a cyber intelligence researcher analyzed topics shared by accounts each month during 2020. To do that, they used <a href="https://umap-learn.readthedocs.io/en/latest/parameters.html">UMAP</a> for non-linear dimension reduction, then they clustered similar tweets through <a href="https://hdbscan.readthedocs.io/en/latest/basic_hdbscan.html">HDBCAN</a>.
Next, they generated a network of co-occurrences for the accounts that appeared in the same clusters. They applied a community detection algorithm to the resulting network, in this case <a href="https://www.nature.com/articles/s41598-019-41695-z">Leiden</a> to find clusters of accounts that shared tweets on the same topic.

#### Arsenal network (February)

Most of the groups of accounts have expressed their desire not to see Amber in the upcoming Aquaman sequel. 
Users belonging to one of these groups, however, show similarities, in this case about 30 users have a picture of the Arsenal team as their banner image.

#### Movies network (February)

This group stands out from the others because instead of focusing on the events, they just tweeted to offend Amber. 
What's suspicious is that all 35 or so accounts have a picture from a movie as their banner image, mostly from DC.

#### Mentions network (November)
This group of 60 accounts in addition to the most used keywords and hashtags, shared words that didn't seem to make sense. 
These are probably mentions to accounts, which anyway have very unusual screen_names: tsAHuahu6E, t4m4UWQ0S5 etc..

#### Mentions network (part 2) (November)
Similar to the previous group, this group of 50 accounts also shared meaningless keywords.

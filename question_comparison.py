
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://localhost:5432/math')


# In[2]:


import pandas as pd
sql = "SELECT * from votes" 
df_votes= pd.read_sql_query(sql, engine)


# In[3]:


df_votes.head()


# In[4]:


import pandas as pd
sql_posts = "SELECT * from posts"
df_posts= pd.read_sql_query(sql_posts, engine)


# In[5]:



# import datetime
# import matplotlib.pyplot as plt
# import numpy as np

# import plotly.plotly as py
# import plotly.tools as tls
# tls.set_credentials_file(username='ankothari', api_key='wAHcYidcpyWuQuVSLdJx')
# # Learn about API authentication here: https://plot.ly/python/getting-started
# # Find your api_key here: https://plot.ly/settings/api

# x = np.array([datetime.datetime(2014, i, 9) for i in range(1,13)])
# y = df_votes[df_votes['postid'] == 1].groupby(['postid', 'creationdate'])['votetypeid'].value_counts()

# plt.plot(x,y)
# plt.tight_layout()

# fig = plt.gcf()
# plotly_fig = tls.mpl_to_plotly( fig )

# py.iplot(plotly_fig, filename='mpl-time-series')


# In[6]:


# took 5 years to get an accepted answer.
# is still active and getting answers? 
# is it still get upvotes after getting an accepted answer?

# activity after it has received an accepted answer ? 
# should we consider the upvotes received in the first yr, or uptil it got an accepted answer. 
# number of answers. If the number of answers is inceasing even after receiving an accepted answer then this questions seem good. 
# till the question receives an accepted answer
# after the question receives an accepted answer. 
# once an accepted answer has been received, does the rate of upvotes increases? I suppose it does.

# if the user doesnt like a question or doesnt like it, how do we suggest him a better question? What features do we select? 
# how do u compare questions to increase the likelihood of being selected by the user? 

# if you see the graph then in the first two years it receives a few upvotes, but then there has to be some signal that 
# can predict the future and thus we can start looking at questions that are only a few years old and are in have the same
# slope this old question has when it had started. 

# df = df_votes[(df_votes['postid']==19048) & (df_votes['votetypeid']==2)]
# d = df.groupby('date')['votetypeid'].value_counts()
# per = df.date.dt.to_period("Y")
# g = df.groupby(per)
# g['votetypeid'].value_counts()

df_votes['date'] = pd.to_datetime(df_votes['creationdate']).dt.year
df_votes.head()


# In[7]:


df_votes.info()


# In[193]:


import pandas as pd
sql_postlinks = "SELECT * from postlinks" 
df_postlinks = pd.read_sql_query(sql_postlinks, engine)


# In[194]:


df_postlinks['date'] = pd.to_datetime(df_postlinks['creationdate']).dt.year
df_postlinks.head()


# In[202]:


df_postlinks[df_postlinks['relatedpostid'] == 668]


# In[259]:


import numpy as np
df_postlinks_grouped = df_postlinks[df_postlinks['linktypeid'] == 1].groupby(['relatedpostid', 'linktypeid'])['relatedpostid'].value_counts()


values = df_postlinks_grouped.keys().tolist()
counts = df_postlinks_grouped.tolist()

post_links = pd.DataFrame(df_postlinks_grouped.keys().tolist())


# In[260]:


# if a question just 4-5 years old then we need to recalculate its score so that we move it the top. 
# We will have to consider the number of answers it has, the scores it has received, etc

post_links.index.name = "id"
post_links.columns = ["post_id", "year", "count"]
post_links['counts'] = counts


# In[261]:


post_links = post_links[['post_id', 'counts']]
post_links.head()


# In[262]:


post_links.set_index('post_id', inplace=True)


# In[263]:


post_links


# In[13]:


# 76,745 questions on linear algebra
# How do u find which question to show and in what order? 
# rank the questions, give more importance to questions taking into time into consideration. 
# high score but no accepted answer yet. 
# there are questions which dont an accepted answer but are really have a very high score. I dont want to show them this
# sort of question anyway. Because this is an open ended answer. 
d = df.groupby(['postid', "year"])['votetypeid']


# In[15]:


df_votes['year'] = df_votes['creationdate'].dt.year


# In[17]:


df_votes['date'] = pd.to_datetime(df_votes['creationdate'])


df = df_votes[(df_votes['votetypeid']==2)]#(df_votes['postid']==668) & 


# In[18]:


df


# In[19]:


d = df.groupby(['postid', "year"])['votetypeid']


# In[20]:


v = df.groupby(['postid', "year"])['votetypeid'].value_counts()


# In[21]:


values = v.keys().tolist()
counts = v.tolist()


# In[22]:


n = pd.DataFrame(v.keys().tolist())


# In[23]:


n.index.name = "id"
n.columns = ["post_id", "year", "votes"]
n['counts'] = counts


# In[26]:


n.columns


# In[27]:


df_year_votes = n.pivot(index='post_id', columns='year', values='counts')


# In[28]:


df_year_votes.to_csv("df_year_votes", sep='\t')


# In[29]:


votes = df_year_votes.sum(axis=1)


# In[30]:


votes = votes.astype("int")


# In[31]:


votes.shape, df_year_votes.shape


# In[32]:


df_year_votes


# In[33]:


df_year_votes.fillna(0, inplace=True)


# In[34]:


for column in df_year_votes.columns:
    df_year_votes[column] = df_year_votes[column].astype(int)


# In[35]:


votes = df_year_votes.sum(axis=1)


# In[36]:


votes.index


# In[37]:


df_year_votes.index


# In[38]:


upvotes = df_year_votes.sum(axis=1)


# In[39]:


upvotes.shape


# In[40]:


df_year_votes


# In[41]:


df_year_votes['upvotes'] = df_year_votes.sum(axis=1)


# In[42]:


df_year_votes.sort_values("upvotes", ascending=False, inplace=True)


# In[268]:


post_links.loc[3]


# In[264]:


df_posts_links = pd.merge(df_posts, post_links,left_on=["id"], right_index=True)


# In[272]:


df_posts_links.head()


# In[269]:


merged_year_posts = pd.merge(df_posts_links, df_year_votes,left_on=["id"], right_index=True)



# In[270]:


merged_year_posts.set_index("id", inplace=True)


# In[274]:


merged_year_posts.counts


# In[276]:


merged_year_posts.head()


# In[48]:


df_year_votes.index


# In[49]:


# joined = df_year_votes.join(df_posts, how="left")


# In[50]:


# joined.head()


# In[51]:


# df_posts


# In[52]:


# df_posts.set_index('id', inplace=True)


# In[277]:


questions = merged_year_posts[merged_year_posts['posttypeid'] == 1]


# In[278]:


questions.columns


# In[279]:


questions[[2010, 2011, 2012 , 2013, 2014, 2015, 2016, 2017, 2018, 'counts', 'favoritecount','creationdate', 'upvotes','tags', 'score', 'title']]


# In[286]:


linear_algebra = questions[questions.tags.str.contains("linear-algebra") & questions.tags.notnull()]



# In[287]:


linear_algebra.columns


# In[288]:


linear_algebra = linear_algebra[[2010, 2011, 2012 , 2013, 2014, 2015, 2016, 2017, 2018,'counts','favoritecount',  'viewcount', 'creationdate' ,'upvotes','tags', 'score', 'title']]



# In[289]:


linear_algebra


# In[290]:


linear_algebra[linear_algebra['upvotes'] > 0].sort_values("upvotes")


# In[293]:


linear_algebra.sort_values(['upvotes', 'score'], ascending=False)[["upvotes","score", 'counts']]


# In[294]:


# for the above need to calculate slope. 
questions['starting_year'] = questions['creationdate'].dt.year 
questions['diff_year'] = 2018 - questions['starting_year'] + 1
questions['upvotes_slope'] = questions['upvotes']/questions['diff_year']
questions['net_votes_slope'] = questions['score']/questions['diff_year'] 


# In[295]:


# for the above need to calculate slope. 
linear_algebra['starting_year'] = linear_algebra['creationdate'].dt.year 
linear_algebra['diff_year'] = 2018 - linear_algebra['starting_year'] + 1
linear_algebra['upvotes_slope'] = linear_algebra['upvotes']/linear_algebra['diff_year']
linear_algebra['favorite_count_slope'] = linear_algebra['favoritecount']/linear_algebra['diff_year']
linear_algebra['net_votes_slope'] = linear_algebra['score']/linear_algebra['diff_year'] 
linear_algebra['view_count_slope'] = linear_algebra['viewcount']/linear_algebra['diff_year'] 


# In[296]:


linear_algebra.sort_values(['favorite_count_slope', 'upvotes_slope', 'net_votes_slope'], ascending=False).head()


# In[297]:


questions.head()


# In[298]:


questions.sort_values(['upvotes_slope', 'net_votes_slope'], ascending=False).head()


# In[299]:


# what other features can we use to find the slope or the number that depicts why the question might be interesting. 
# can we use the views feature to explain the question popularity? the viewcount should also be bought to the same scale. 


# In[300]:


linear_algebra.sort_values(['view_count_slope'], ascending=False)


# In[301]:


# not everyone who sees the question is going to vote for it, also taking to into account the favorites, 
# maybe we need to nornmaize the counnts. checking again 
# we also need to take into accounnt the number of inlinks and outlinks. and find out a poperequation which 
# we can fix later onj depdnding on the some results. 

# what if could use the year wise votes with the viewcounts. 

Favorites are important, upvotes are important, downvotes are important as well 


# In[302]:


linear_algebra_slope = linear_algebra[["tags", 2010, 2011,2012,2013, 2014, 2015, 2016, 2017, 2018, "counts", "score", "upvotes", "upvotes_slope", "net_votes_slope","view_count_slope", "viewcount"]]


# In[305]:


linear_algebra_slope[((linear_algebra_slope[2010] == 0)) & (linear_algebra_slope[2011] > 0)].sort_values("counts", 
                                                                 ascending=False)




# In[306]:


linear_algebra_slope.sort_values("upvotes_slope", ascending=False)


# In[307]:


questions.head()


# In[309]:


filtered_questions = questions[["tags", 2010, 2011,2012,2013, 2014, 2015, 2016, 2017, 2018, "counts", "score", "upvotes", "upvotes_slope", "net_votes_slope", "viewcount"]]


# In[310]:


filtered_questions.head()


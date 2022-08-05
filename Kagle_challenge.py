import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




fifa = pd.read_csv('fifa_data.csv')
print(fifa.head(5))


##HISTOGRAMS
bins = [40,50,60,70,80,90,100]

plt.hist(fifa.Overall,bins = bins)
plt.xticks((bins))
plt.ylabel('Number of players')
plt.xlabel('Skills Level')
plt.title('Distribution of player skills in Fifa 2018')

plt.show()

##PIECHARTS

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot']== 'Right'].count()[0]
plt.pie([left,right],labels =['Left','Right'], colors =['r','g'], autopct = '%.2f%%')
plt.title('Foot preference of FIfa PLayers')
plt.show()


##PIE CHART2

#weight has lbs attached to it so we need to reset weight column so strip of lbs from the weight

fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa)]

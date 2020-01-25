#import pandas as pd
statical={'BatsMan':{'Virat Kohli':{'Matches':'200','Runs':'4000','Average':'130','Highscore':'120'},
          'Rohit Sharma':{'Matches':'200','Runs':'40000','Average':'400','Highscore':'264'},
          'Hardik Pandey':{'Matches':'227','Runs':'300000','Average':'67.8','Highscore':'183'}}}
#df=pd.DataFrame(squad['BatsMan'])
c=[]
for p_id in statical.keys():
    for high in statical[p_id].keys():
        c.append(statical[p_id][high]['Highscore'])
print("HighScore =",max(c))


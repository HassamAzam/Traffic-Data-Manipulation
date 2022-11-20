import pandas as pd

df = pd.read_csv('data.csv')
q=df['Vehicle_ID']
q=q.unique().tolist()
q.sort()
print('Number of unique Vehicle IDs are: ',len(q)-1)
i=1
print('          Vehicle-ID         MinVel                 MaxVel              AverageVel           TotalTime    ')
while i<len(q):
    num=q[i]
    df2=((df.loc[df['Vehicle_ID']==int(num)]))

    p=df2['v_Vel'].max()
    r=df2['v_Vel'].min()
    s=df2['v_Vel'].mean()
    t=df2['Global_Time'].sum()
    print(i, '     ',int(num),'              ',r,'              ',p,'              ',s,'              ',t)
    i=i+1




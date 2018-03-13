import pandas as pd

teams = {}

teams['2003'] = {}
teams['2004'] = {}
teams['2005'] = {}
teams['2006'] = {}
teams['2007'] = {}
teams['2008'] = {}
teams['2009'] = {}
teams['2010'] = {}
teams['2011'] = {}
teams['2012'] = {}
teams['2013'] = {}
teams['2014'] = {}
teams['2015'] = {}
teams['2016'] = {}
teams['2017'] = {}

tdf = pd.read_csv('data\\Teams.csv')

for index, row in tdf.iterrows():
    #W,L,Score,FGM,FGA,FGM3,FGA3,FTM,FTA,OR,DR,Ast,TO,Stl,Blk,PF
    teams['2003'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2004'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2005'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2006'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2007'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2008'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2009'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2010'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2011'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2012'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2013'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2014'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2015'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2016'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    teams['2017'][row['TeamID']] = [0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#Season,DayNum,WTeamID,WScore,LTeamID,LScore,WLoc,NumOT,WFGM,WFGA,WFGM3,WFGA3,WFTM,WFTA,WOR,WDR,WAst,WTO,WStl,WBlk,WPF,LFGM,LFGA,LFGM3,LFGA3,LFTM,LFTA,LOR,LDR,LAst,LTO,LStl,LBlk,LPF
df = pd.read_csv('data\\RegularSeasonDetailedResults.csv')
for index, row in df.iterrows():
    #W
    teams[str(row['Season'])][row['WTeamID']][0] += 1
    #L
    teams[str(row['Season'])][row['LTeamID']][1] += 1
    #Score
    teams[str(row['Season'])][row['WTeamID']][2] += row['WScore']
    teams[str(row['Season'])][row['LTeamID']][2] += row['LScore']
    #FGM
    teams[str(row['Season'])][row['WTeamID']][3] += row['WFGM']
    teams[str(row['Season'])][row['LTeamID']][3] += row['LFGM']
    #FGA
    teams[str(row['Season'])][row['WTeamID']][4] += row['WFGA']
    teams[str(row['Season'])][row['LTeamID']][4] += row['LFGA']
    #FGM3
    teams[str(row['Season'])][row['WTeamID']][5] += row['WFGM3']
    teams[str(row['Season'])][row['LTeamID']][5] += row['LFGM3']
    #FGA3
    teams[str(row['Season'])][row['WTeamID']][6] += row['WFGA3']
    teams[str(row['Season'])][row['LTeamID']][6] += row['LFGA3']
    #FTM
    teams[str(row['Season'])][row['WTeamID']][7] += row['WFTM']
    teams[str(row['Season'])][row['LTeamID']][7] += row['LFTM']
    #FTA
    teams[str(row['Season'])][row['WTeamID']][8] += row['WFTA']
    teams[str(row['Season'])][row['LTeamID']][8] += row['LFTA']
    #OR
    teams[str(row['Season'])][row['WTeamID']][9] += row['WOR']
    teams[str(row['Season'])][row['LTeamID']][9] += row['LOR']
    #DR
    teams[str(row['Season'])][row['WTeamID']][10] += row['WDR']
    teams[str(row['Season'])][row['LTeamID']][10] += row['LDR']
    #Ast
    teams[str(row['Season'])][row['WTeamID']][11] += row['WAst']
    teams[str(row['Season'])][row['LTeamID']][11] += row['LAst']
    #TO
    teams[str(row['Season'])][row['WTeamID']][12] += row['WTO']
    teams[str(row['Season'])][row['LTeamID']][12] += row['LTO']
    #Stl
    teams[str(row['Season'])][row['WTeamID']][13] += row['WStl']
    teams[str(row['Season'])][row['LTeamID']][13] += row['LStl']
    #Blk
    teams[str(row['Season'])][row['WTeamID']][14] += row['WBlk']
    teams[str(row['Season'])][row['LTeamID']][14] += row['LBlk']
    #PF
    teams[str(row['Season'])][row['WTeamID']][15] += row['WPF']
    teams[str(row['Season'])][row['LTeamID']][15] += row['LPF']


for season in teams.keys():
    for team in teams[season].keys():
        games = teams[season][team][0] + teams[season][team][1]
        if games > 0:
            for i in range(2, 16):
                teams[season][team][i] /= games

with open('teamstats.csv', 'w') as fh:
    fh.write('Season,TeamID,W,L,Score,FGM,FGA,FGM3,FGA3,FTM,FTA,OR,DR,Ast,TO,Stl,Blk,PF\n')
    for season in teams.keys():
        for team in teams[season].keys():
            fh.write(str(season) + ',' + str(team) + ',' + ','.join(map(str,teams[season][team])) + '\n')

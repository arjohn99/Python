import pandas as pd
import os

#Read in first csv file
data_file = os.path.join("election_data_1.csv")
df1 = pd.read_csv(data_file)

#Read in second csv file
data_file = os.path.join("election_data_2.csv")
df2 = pd.read_csv(data_file)

#merge_table = pd.merge(customer_df, items_df, on="customer_id", how="inner")
#print(df1)
#print(df2)
df = df1.append(df2)
#print(df)
vestal = df.loc[df['Candidate'] == 'Vestal', :]
torres = df.loc[df['Candidate'] == 'Torres', :]
seth = df.loc[df['Candidate'] == 'Seth', :]
cordin = df.loc[df['Candidate'] == 'Cordin', :]
khan = df.loc[df['Candidate'] == 'Khan', :]
correy = df.loc[df['Candidate'] == 'Correy', :]
li = df.loc[df['Candidate'] == 'Li', :]
otooley = df.loc[df['Candidate'] == "O'Tooley", :]

percentVestal = len(vestal) / len(df)
percentTorres = len(torres) / len(df)
percentSeth = len(seth) / len(df)
percentCordin = len(cordin) / len(df)
percentKhan = len(khan) / len(df)
percentCorrey = len(correy) / len(df)
percentLi = len(li) / len(df)
percentOtooley = len(otooley) / len(df)


#print(df['Candidate'].unique())
#print(vestal)

print('Election Results')
print('---------------------------')
print('Total Votes: ' + str(df['Voter ID'].nunique()))
print('---------------------------')
print('Vestal: ' + "{:.2%}".format(percentVestal) + ' ' + str(len(vestal)))
print('Torres: ' + "{:.2%}".format(percentTorres) + ' ' + str(len(torres)))
print('Seth: ' + "{:.2%}".format(percentSeth) + ' ' + str(len(seth)))
print('Cordin: ' + "{:.2%}".format(percentCordin) + ' ' + str(len(cordin)))
print('Khan: ' + "{:.2%}".format(percentKhan) + ' ' + str(len(khan)))
print('Correy: ' + "{:.2%}".format(percentCorrey) + ' ' + str(len(correy)))
print('Li: ' + "{:.2%}".format(percentLi) + ' ' + str(len(li)))
print("O'Tooley: " + "{:.2%}".format(percentOtooley) + ' ' + str(len(otooley)))
print('---------------------------')
print('Winner: Khan')
print('---------------------------')

text_file = open("PyPoll.txt", "w")
text_file.write('Election Results')
text_file.write('---------------------------')
text_file.write('Total Votes: ' + str(df['Voter ID'].nunique()))
text_file.write('---------------------------')
text_file.write('Vestal: ' + "{:.2%}".format(percentVestal) + ' ' + str(len(vestal)))
text_file.write('Torres: ' + "{:.2%}".format(percentTorres) + ' ' + str(len(torres)))
text_file.write('Seth: ' + "{:.2%}".format(percentSeth) + ' ' + str(len(seth)))
text_file.write('Cordin: ' + "{:.2%}".format(percentCordin) + ' ' + str(len(cordin)))
text_file.write('Khan: ' + "{:.2%}".format(percentKhan) + ' ' + str(len(khan)))
text_file.write('Correy: ' + "{:.2%}".format(percentCorrey) + ' ' + str(len(correy)))
text_file.write('Li: ' + "{:.2%}".format(percentLi) + ' ' + str(len(li)))
text_file.write("O'Tooley: " + "{:.2%}".format(percentOtooley) + ' ' + str(len(otooley)))
text_file.write('---------------------------')
text_file.write('Winner: Khan')
text_file.write('---------------------------')
text_file.close()

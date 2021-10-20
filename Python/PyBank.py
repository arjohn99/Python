import pandas as pd
import os

#Read in first csv file
data_file = os.path.join("budget_data_1.csv")
df1 = pd.read_csv(data_file)

#Read in second csv file
data_file = os.path.join("budget_data_2.csv")
df2 = pd.read_csv(data_file)

#Replace the first two digits in the date so that a merge can be made
df2['Date'] = df2['Date'].str.replace('20','')

#merge the two files to create a single data frame
merge_table = pd.merge(df1, df2, on="Date", how="outer")
merge_table.fillna(0, inplace=True)

#sum the two revenue columns that were created on the merge and drop the two columns leaving only a single Revenue column
merge_table['Revenue'] = merge_table['Revenue_x'] + merge_table['Revenue_y']
mt = merge_table.drop('Revenue_x', 1)
mt = mt.drop('Revenue_y', 1)

#find the difference from month to month
diffMonth = pd.DataFrame(mt['Revenue'].diff(1))
diffMonth.fillna(0, inplace=True)
#find average of the differences
avgMonth = diffMonth.sum() / len(mt['Revenue'])

#dataframe of differences with original
mt2 = mt.merge(diffMonth, how='outer', left_index=True, right_index=True)

#Min and Max diff values saved to variables for printing
maxVal = diffMonth['Revenue'].max()
minVal = diffMonth['Revenue'].min()
#Min and Max dates for printing
maxMonth = mt2.loc[mt2['Revenue_y'] == maxVal, :]
minMonth = mt2.loc[mt2['Revenue_y'] == minVal, :]

print('Financial Analysis')
print('---------------------------')
print('Total Months: ' + str(mt['Date'].nunique()))
print('Total Revenue: ' + '${:,.2f}'.format(mt['Revenue'].sum()))
print('Average Revenue Change: ' + '${:,.2f}'.format(avgMonth['Revenue']))
print('Greatest Increase in Revenue: ' + maxMonth['Date'].to_string(index = False) + ' (' + '${:,.2f}'.format(maxVal) + ')')
print('Greatest Decrease in Revenue: ' + minMonth['Date'].to_string(index = False) + ' (' + '${:,.2f}'.format(minVal) + ')')

text_file = open("PyBank.txt", "w")
text_file.write('Financial Analysis')
text_file.write('---------------------------')
text_file.write('Total Months: ' + str(mt['Date'].nunique()))
text_file.write('Total Revenue: ' + '${:,.2f}'.format(mt['Revenue'].sum()))
text_file.write('Average Revenue Change: ' + '${:,.2f}'.format(avgMonth['Revenue']))
text_file.write('Greatest Increase in Revenue: ' + maxMonth['Date'].to_string(index = False) + ' (' + '${:,.2f}'.format(maxVal) + ')')
text_file.write('Greatest Decrease in Revenue: ' + minMonth['Date'].to_string(index = False) + ' (' + '${:,.2f}'.format(minVal) + ')')
text_file.close()


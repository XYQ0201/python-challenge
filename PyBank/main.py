import os 
import csv
csvpath=os.path.join("PyBank/Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader=next(csvreader)
    # calculate total loss/gain
    
    total=[]
    daily_change=[]
    total_month=[]
    print('Financial Analysis')
    print('----------------------------')
    #calculate how many months in the dataset
    for row in csvreader: 
        total_month.append(row[0])
        total.append(int(row[1]))
    print(f"Total Months: {len(total_month)}")

    #calculate total amount of profit gain/loss 
    total_net=0
    for value in total: 
        total_net = value + total_net
    print(f"Total: ${total_net}")
   
    #calculate average change & greatest increase/decrease
    monthly_change_total=0
    profit=[]
    #change of profit/loss start from the second month, for the first month, initial value =0
    monthly_change=0
    profit.append(monthly_change)
    for x in range(len(total)-1): 
        monthly_change= total[x+1]-total[x]
        profit.append(monthly_change)
        monthly_change_total = monthly_change_total + monthly_change
        average_change = monthly_change_total/(len(total)-1)
    print(f'Average change:${round(average_change,2)}')
    date_change = list(zip(total_month,profit))
    for row in date_change:
        if row [1] == max(profit):
           print(f'Greatest Increase in Profits: {row[0]} (${max(profit)})')
        elif row [1] == min(profit):
           print(f'Greatest Decrease in Profits: {row[0]} (${min(profit)})')
        
  
     
         
  

    

  
    




          
   




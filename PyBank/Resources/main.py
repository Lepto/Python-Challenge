import os
import csv

#Setting up variables
MonthsList = []

ChangesToPnL = []

TotalMonths = 0

NetLoss = 0

PriorMonthLoss = 0

PresentMonthLoss = 0

DifferenceProfitLoss = 0

#Path to collect data from the Resources folder - had to determine absolute path
This_File = os.path.dirname(os.path.abspath(__file__))

budget_data = os.path.join(This_File, "budget_data.csv")

#Open and read csv
with open(budget_data, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row first and ignore
    header = next(csvfile)

    #Read through each row of data after the header
    for row in csvreader:

        #Count of months
        TotalMonths += 1

        #Net total amount of "Profit/Losses" over the entire period
        PresentMonthLoss = int(row[1])

        NetLoss += PresentMonthLoss 

        if (TotalMonths == 1):

            #Make the value of previous month to be equal to current month
            PriorMonthLoss = PresentMonthLoss

            continue

        else:

	    #Calculating the change between profit and loss 
            DifferenceProfitLoss = PresentMonthLoss - PriorMonthLoss
	
	    #Establishing PriorMonthLoss for the next loop
            PriorMonthLoss = PresentMonthLoss
            
	    #Appending each month to the MonthsList[]
            MonthsList.append(row[0])

            #Appending each DifferenceProfitLoss to the ChangesToPnL list[]
            ChangesToPnL.append(DifferenceProfitLoss)
   
    #Sum in PnL
    SumPnL = sum(ChangesToPnL)
      
    #Average of PnL changes for the year (counting rows and exclude the first month)
    PnLAverage = round(SumPnL/(TotalMonths - 1), 2)

    #Maximum and Minimum changes in PnL
    MaxChange = max(ChangesToPnL)

    MinChange = min(ChangesToPnL)

    #Find the index or list position of PnL Max and Min value changes
    IndexMaxMonth = ChangesToPnL.index(MaxChange)

    IndexMinMonth = ChangesToPnL.index(MinChange)

    #Assign Max and Min value
    MaxMonth = MonthsList[IndexMaxMonth]

    MinMonth = MonthsList[IndexMinMonth]

#Display the final analysis summary
print("Final Financial Analysis Summary")

print("--------------------------------")

print(f"Total Months: {TotalMonths}")

print(f"Total: ${NetLoss}")

print(f"Average Change: ${PnLAverage}")

print(f"Greatest Increase in Profits: {MaxMonth} (${MaxChange})")

print(f"Greatest Decrease in Losses: {MinMonth} (${MinChange})")

#Export text file of Final Analysis Summary
OutFile = os.path.dirname(os.path.abspath(__file__))

SummaryFileExport = os.path.join(OutFile, "output_summary.txt")

with open(SummaryFileExport, 'w') as TextFile:
    TextFile.write(" \n")
    TextFile.write(" \n")
    TextFile.write(" \n")
    TextFile.write("Final Financial Analysis Summary\n")
    TextFile.write("--------------------------------\n")
    TextFile.write(f"Total Months: {TotalMonths}\n")
    TextFile.write(f"Total: ${NetLoss}\n")
    TextFile.write(f"Average Change: ${PnLAverage}\n")
    TextFile.write(f"Greatest Increase in Profits: {MaxMonth} (${MaxChange})\n")
    TextFile.write(f"Greatest Decrease in Losses: {MinMonth} (${MinChange})\n")



#%% I/O functionsimport osimport csv#%% I/O pathpnl_csv = os.path.join('budget_data.csv')months = int(0)revenue = float(0)monthly_data = []#%%with open(pnl_csv, 'r') as csvfile:        csvreader = csv.reader(csvfile, delimiter=',')        header = next(csvreader)                for row in csvreader:            #months+=1            #revenue+=float(row[1])            monthly_data.append(float(row[1]))                                    #print(months)#months = len(monthly_data)months = len(monthly_data)first_month = 0last_month = months - 1#print(revenue)            #print(monthly_data[first])#print(monthly_data[last])print(sum(monthly_data))
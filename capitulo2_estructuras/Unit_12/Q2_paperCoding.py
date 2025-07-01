count_reduced =0
sales_record =(100,121,120,130,140,120,122,123,190,125)

for i in range(1,len(sales_record)):
    if sales_record[i]<sales_record[i-1]:
        count_reduced+=1

print("In the past {} days,{} days had reduced sales compared to the previous day".format(len(sales_record),count_reduced))
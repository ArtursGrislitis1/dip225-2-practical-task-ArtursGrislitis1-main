import pandas
fails=pandas.read_excel("description.xlsx", sheet_name="LookupAREA")
info_list = fails.values.tolist()
get_info=input()
reg_id=0
for row in info_list:
    if row[1]==get_info:
        reg_id=row[0]
        break
if reg_id==0:
    print(0)
    exit()
CSV=pandas.read_csv('data.csv').values.tolist()
geo_count=[]
for line in CSV:
    if line[1]==reg_id:
        geo_count.append(int(line[3]))
print(sum(geo_count))

import xlrd
import os
import matplotlib.pyplot as plt
def retrivingyearlydata(crop_year,crop,production):
    n=int(input("Enter the year for which you need cropwise productivity details in bw 1997-2006 & year 2010 :"))
    for i in range(len(crop_year)):
        if(crop_year[i]==n):
            print(str(crop[i])+" : "+str(production[i]))
def cropwisegraph(crop_year,crop,production):
    n=input("Enter the crop for which you year vs crop productivity graph:")
    x1=[]
    y1=[]
    for i in range(len(crop_year)):
        if(crop[i]==n):
            x1.append(crop_year[i])
            y1.append(production[i])
    plt.plot(x1, y1) 
    plt.xlabel('Year') 
    plt.ylabel('Production') 
    plt.title('year vs crop productivity graph') 
    plt.show() 
def cropwisedataretive(crop_year,crop,production,area,season,state,district):
     n=input("Enter the crop for rest of data")
     for i in range(len(crop_year)):
        if(crop_year[i]==n):
            print("\n crop : "+str(crop[i])+"\n production : "+str(production[i])+" \n crop year: " +str(crop_year[i])+"\n season:" +str(season[i])+"\n state:" + str(state[i])+ "\n district:"+ str(district[i]))
os.chdir("C:\\Users\\Admin\\Documents\\college syllabous\\Data structure\\Class Hackthon\\hackthon- 3")
loc = "CropsDataFile.xlsx" 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
state=sheet.col_values(0)
district=sheet.col_values(1)
crop_year=sheet.col_values(2)
season=sheet.col_values(3)
crop=sheet.col_values(4)
area=sheet.col_values(5)
production=sheet.col_values(6)

while(1):
    print(" \n Enter : \n 1 for retrivingyearlydata \n 2 for cropwisegraph \n 3 for crop wise retriveal \n 4 for exit")
    cl=int(input("Enter the comand line:"))
    if(cl==1):
        retrivingyearlydata(crop_year,crop,production)
    elif(cl==2):
        cropwisegraph(crop_year,crop,production)
    elif(cl==3):
        cropwisedataretive(crop_year,crop,production,area,season,state,district)
    else:
        break
    
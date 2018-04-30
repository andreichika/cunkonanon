import pandas as pd
import foo.data_vis as dv


file_path = '/Users/deepthisen/Desktop/Courses/stat656/FinalExam/'
df = pd.read_excel(file_path+"HondaComplaints.xlsx")

attribute_map={
    'description':[3,("HONDA","ACURA"),[0,0]],
    'NhtsaID':[4,(1,2,3,4),[0,0]],
    'Make':[1,("HONDA","ACURA"),[0,0]],
    'Model':[2,('TL','ODYSSEY','CR-V','CL','CIVIC','ACCORD'),[0,0]], 
    'Year':[2,('2001','2002','2003'),[0,0]],
    'State':[4,(1,2,3,4),[0,0]],
    'abs':[1,('Y','N'),[0,0]],
    'cruise':[1,('Y','N'),[0,0]],
    'crash':[1,('Y','N'),[0,0]],
    'mph':[0,(0,80),[0,0]],
    'mileage':[0,(0,80),[0,0]],}

print("Data Visualization")
print("******************")
i=0
for item in df.columns:
 
    my_dict={}
    vartype=attribute_map[item][0]
    i_int=0
    i_cat=0
    if vartype==0:
        i_int+=1
        print("\n"+item+" is an interval variable")
        s='vis_int'+str(i)
        my_dict[s]=dv.inter_visual(df[item],vartype)
        my_dict[s].histogram('factor')
        print(item+" Mean: "+str(my_dict[s].mean))
        print(item+" Mode: "+str(my_dict[s].mode))
        print(item+" Std Dev: "+str(my_dict[s].stdev))
        
    elif vartype==1 or vartype==2:
        i_cat+=1
        print("\n"+item+" is an categorical variable")
        s='vis_cat'+str(i)
        my_dict[s]=dv.nomi_visual(df[item],vartype,display_bar=0)
        my_dict[s].piechart()
        print(item+" Mode: "+str(my_dict[s].mode))
        my_dict[s].frequency()
    elif vartype==3:
        print("\n"+item+" is an text variable")
        continue
    else:
        print("\n"+item+" has been deleted from dataframe")
        df=df.drop([item],axis=1)

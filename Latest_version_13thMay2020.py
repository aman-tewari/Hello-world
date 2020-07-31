import pandas as pd
import numpy as np


def query_convert(text):
    df1=pd.read_csv("Queries_convert.csv")

    df2 = pd.read_csv("Queries_Alter.csv")

    HIVE_Query = df1['HIVE_Queries'].to_list()
    Snowflake_Query = df1['Snowflake_Queries'].to_list()


    HIVE_Alter = df2['HIVE_Alter'].to_list()
    Snowflake_Alter = df2['Snowflake_Alter'].to_list()


    HIVE_sym = ['(',')',',',';']

    HIVE_sym1 = ['(',')']

    u = pd.read_csv("Undefined_Snowflake_commands.csv")

    v = pd.read_csv("defined_snowflake.csv")

    undefined_snowflake = u['undefined_snowflake'].to_list()

    defined_snowflake = v['defined_snowflake'].to_list()

    t = pd.read_csv("lolz.csv")

    undefined = t["undefined"].to_list()

    # undefined

    new_line=""  #for create

    lin1=''    #for alter

    new_line1=""

    new_line=""

    lines = """ """

    if text is not None:
        lines = text

    line = lines.split(";")

    list_of_line = " "

    for i in range(0,len(line)-1):
        line[i]=line[i]+' ;'
        split_words=line[i].split()

        if split_words[0].lower() == "create":
            new_line=''
            lin1=""
            for j in range(0,len(line[i])):
                if line[i][j] in HIVE_sym:
                    if line[i][j-1].isspace() == True:
                        if j!=(len(line[i])-1):
                            if line[i][j+1].isspace()== True:
                                lin1=lin1+line[i][j]
                            else:
                                lin1=lin1+line[i][j]+" "
                        else:
                            lin1=lin1+line[i][j]
                    else:
                        if j!=(len(line[i])-1):
                            if line[i][j+1].isspace()== True:
                                lin1=lin1+" "+line[i][j]
                            else:
                                lin1=lin1+" "+line[i][j]+" "
                        else:
                            lin1=lin1+" "+line[i][j]
                else:
                    lin1=lin1+line[i][j]
            split_words1=lin1.split()
            for i in split_words1:
                for j in range(0,len(HIVE_Query)):
                    if i.lower()==HIVE_Query[j]:
                        i=Snowflake_Query[j]
                new_line=new_line+" "+i
            list_of_line = list_of_line+" "+new_line+"\n"
            print(new_line+"\n")
            
        elif split_words[0].lower() == "alter":
            lin1=""
            for j in range(0,len(line[i])):
                if line[i][j] in HIVE_sym:
                    if line[i][j-1].isspace() == True:
                        if j!=(len(line[i])-1):
                            if line[i][j+1].isspace()== True:
                                lin1=lin1+line[i][j]
                            else:
                                lin1=lin1+line[i][j]+" "
                        else:
                            lin1=lin1+line[i][j]
                    else:
                        if j!=(len(line[i])-1):
                            if line[i][j+1].isspace()== True:
                                lin1=lin1+" "+line[i][j]
                            else:
                                lin1=lin1+" "+line[i][j]+" "
                        else:
                            lin1=lin1+" "+line[i][j]
                else:
                    lin1=lin1+line[i][j]
            
            split_words1=lin1.split()
            new_line1=""
            count=0
            for i in split_words1:
                if i[0]=='\'':
                    count+=1
                if count%2==0:
                    for j in range(0,len(HIVE_Alter)):
                        if i.lower()==HIVE_Alter[j]:
                            k=Snowflake_Alter[j]
                            break
                        elif i in HIVE_sym1:
                            k=""
                            break
                        else:
                            k=i
                    new_line1=new_line1+" "+k
                else:
                    new_line1=new_line1+" "+i
        
                if i[len(i)-1]=='\'':
                    count+=1
                
            split_words2=new_line1.split()
            new_line=""
            for i in range(0,len(split_words2)):
                if split_words2[i].lower()=="change":
                    if split_words2[i+1]==split_words2[i+2]:
                        split_words2[i]="ALTER"
                        split_words2[i+1]="COLUMN"
                    else:
                        if split_words2[i+1] != split_words2[i+2]:
                            split_words2[i]="RENAME COLUMN"
                            split_words2[i+3]=split_words2[i+2]
                            split_words2[i+2]="To"
                new_line=new_line+" "+split_words2[i]
            list_of_line = list_of_line+" "+new_line+"\n"

    retuurn list_of_line
        # print(new_line+"\n") 

# list_of_line

# struct = pd.read_csv("structured_keywords.csv")

# structured_keywords = struct['structured_keywords'].to_list()

# # structured_keywords

# my_list = list(list_of_line.split())

# print(my_list)

# hashcount=1

# for i in range(0,len(my_list)):
#     if my_list[i].upper() in undefined:
#         if hashcount==1:
#             my_list[i]='/*'+my_list[i]
#             hashcount=0
#     elif my_list[i].lower() in defined_snowflake:
#         if hashcount==0:
#             hashcount=1
#             if my_list[i-1]==';':
#                 my_list[i-2]=my_list[i-2]+'*/'
#             else:
#                 my_list[i-1]=my_list[i-1]+'*/'
# print(my_list)

# for pattern in my_list:
#     a=pattern.upper();
#     if a in structured_keywords:                     
#         print("\n",a,end=' ')
#         if a=="(":
#             print("\n",end='')
#         if a==")":
#             print("\n",end='')
#     elif a==';':
#         print(a,"\n",end='')
#         print("\n",end='')
#         print("\n",end='')
#         #print(a, end=" ")
#     else:
#         print(pattern, end=' ')



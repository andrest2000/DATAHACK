import numpy as np
import pandas as pd
from itertools import permutations
def split(word):
    return [char for char in word]
def Phrases_all_combination_func(text):
    #First, we separate the given text into a list of letters (string variables)
    text_separated=split(text)
    #Now, everytime we find a ".", we create reunite the strings in between the points
    i=0
    text_separated_by_periods=[]
    while (i<len(text_separated)):
        text_separated_by_periods_aux=""
        while (text_separated[i]!="."):
            text_separated_by_periods_aux=text_separated_by_periods_aux+text_separated[i]
            i=i+1
            if i==len(text_separated):
                break
        i=i+1
        text_separated_by_periods.append(text_separated_by_periods_aux)
    text_separated_by_periods_all_permutations=permutations(text_separated_by_periods)    
    return text_separated_by_periods_all_permutations

#Extraxting the data for covid vaccines
# df_COVID_Vaccine_side_effects_1 = pd.read_csv("2021VAERSVAX.csv")
# df_COVID_Vaccine_side_effects_2 = pd.read_csv("2021VAERSSYMPTOMS.csv")
df_COVID_Vaccine_side_effects_3 = pd.read_csv("2021VAERSDATA.csv",encoding='latin1')
# student_mental = pd.read_csv("Student_Mental_health.csv")
side_effects_text=pd.Series(df_COVID_Vaccine_side_effects_3["SYMPTOM_TEXT"])
side_effects_text_list=side_effects_text.to_numpy()



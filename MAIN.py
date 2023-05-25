import random
import math                                  # LIBRARIES TO COEM IN USE 
import unicodedata
import matplotlib.pyplot as plt
from tkinter import *       



# Open the data file and read the weights
with open(r'C:\Users\lenovo\OneDrive\Desktop\weights_data.csv', 'r', encoding='utf-8') as f:                   #HANDLED ERROR HERE USING KEYWORD r , and using unicodeta library
    weights = [float(x) for x in f.read().splitlines()]            #REMOVE WEIGHTS FROM THE FILE CSV , BECAUSE ITS A STRING , THAN COD EWILL RUN 
# Define sample sizes
N1 = 10
N2= 100                           # sample sizes accoding to the question given in cep


# Generate 1000 samples of size N2 and calculate z scores

z_scores_n2 = []                                                        # array for storing z scores for sample 2 of size 100


for i in range(1000):                                                                      # STATEMENT 2 ., FOR LOOP TO ITERATE A 1000 TIMES
    
    sample = random.sample(weights, N2)                                           # SAMPLE SIZE , USING OBJECT OFA CLASS IN NUMPY LIBRARY       
    
    bar_x = sum(sample) / N2                            # CALCULATING X BAR , USING MATH LIBRARY , ADDING ALL WEIGHTS AND DIVIDING BY THE SAMPLE SIZE 
    
    sigma = math.sqrt(sum([(x - bar_x)**2 for x in weights]) / (len(weights) - 1))         #CALCULATING SIGMA USED MATH LIBRARY FOR UNDER ROOT FUNCTION** IS FOR EXPONENT, LEN IS USED FOR RETURNING ALL WEIGHTS
    
    z = (bar_x - sum(weights) / len(weights)) / (sigma / math.sqrt(N2))   # USING MATH,,WE CALCULATE Z THROUGH FORMULA GIVEN
    
    z_scores_n2.append(z)        # STORING ALL Z SCORES IN ARRAY z_scores_n2 =[];
    
    
    
    
    
    
    
    
# Generate 1000 samples of size N1 and calculate z scores
z_scores_n1 = []
for i in range(1000):
    sample = random.sample(weights, N1)                           #it calculates the sample mean bar_x
    
    bar_x = sum(sample) / N1
    
    
    sigma = math.sqrt(sum([(x - bar_x)**2 for x in weights]) / (len(weights) - 1))          #he sample standard deviation sigma
    
    z = (bar_x - sum(weights) / len(weights)) / (sigma / math.sqrt(N1))            #score z. 
    #The z-score is a measure of how many standard deviations a sample mean is from the population mean.
    
    
    z_scores_n1.append(z)
    
    

# Plot histograms of z scores for n1 and n2 side-by-side               
fig, OBJ1 = plt.subplots(1, 2, figsize=(10, 5))                                      # making object , which will plot my results in two differnt graphs
      
OBJ1[0].hist(z_scores_n1, bins=30 , color='black' , alpha=0.5)
OBJ1[0].set_title('Distribution of Z values (n = 10)')

OBJ1[1].hist(z_scores_n2, bins=30, color='blue', alpha=0.5) # sample size 100 graph would be in blue color and with a 0.5 spacing and opacity

OBJ1[1].set_title('Distribution of Z values (n = 100)')        # setting title for sample size 100 graph 


plt.show() # thsi is used to show the plots that we made
    
    
    
   
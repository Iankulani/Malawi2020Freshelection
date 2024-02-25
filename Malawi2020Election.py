# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:09:18 2024

@author: IAN CARTER KULANI
"""

#This software prompts the user to enter total number of published centers,total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward,it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.
print("==============================MALAWI ELECTROL COMMISSION==============================\n")    
#Get total number of published centers
percent=100
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Votes:"))
Totalvotescast=int(input("Enter Total Votes Cast:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null and Void Votes:"))
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get total valid votes for Dr Lazarus Chakwera.
Totalvalidvotesfor_lazaruschakwera=int(input("Enter Total valid votes for Dr Lazarus Chakwera:"))
#Get total valid votes for Peter Kuwani.
Totalvalidvotesfor_peterdominicsinosdriverkuwani=int(input("Enter Total Valid Votes for Peter Driver Sinos Kuwani:"))
#Get total valid votes for Professor Arthur Peter Muthalika
Totalvalidvotesfor_arthurpetermuthalika=int(input("Enter Total Valid Votes for Professor Arthur Peter Muthalika:"))
if Totalvalidvotesfor_lazaruschakwera>Totalvalidvotes/2+1 :
        print("Cogratulations Dr Lazarus Maccathy Chakwera you're a winner of 2020 election\n\n\n")
elif Totalvalidvotesfor_peterdominicsinosdriverkuwani>Totalvalidvotes/2+1: 
    print("Cogratulations Peter Kuwani you're a winner of 2020 election\n\n")
elif Totalvalidvotesfor_arthurpetermuthalika>Totalvalidvotes/2+1: 
    print("Cogratulations Professor Arthur Peter Muthalika  you're a winner of 2020 election\n\n\n")
else:
    print("No majority winner was found RUNOFF may be required\n")
    
  
print("______________________________ELECTION STATISTICS_______________________________\n")   
   #calculating percentage for candidates
majority=Totalvalidvotesfor_lazaruschakwera*percent/Totalvalidvotes;
print("Total Valid Votes for Dr Lazarus Chakwera in Percent=",majority)
majority=Totalvalidvotesfor_peterdominicsinosdriverkuwani*percent/Totalvalidvotes;
print("Total Valid Votes for Peter Kuwani in percent=",majority)
majority=Totalvalidvotesfor_arthurpetermuthalika*percent/Totalvalidvotes;
print("Total Valid Votes for Peter Mutharika in perent=",majority) 
 
print("==========================================================================================\n")   




















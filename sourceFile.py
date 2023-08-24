# import the libraries
import os
import time
import warnings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
# from matplotlib import style
# from sklearn import metrics

warnings.filterwarnings("ignore")

def clear_terminal():
    os.system('cls')

clear_terminal()
def dateFormat(fileName):
    csv_file_path = fileName
    df = pd.read_csv(csv_file_path)

    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

    output_file_path = fileName
    df.to_csv(output_file_path, index=False)

    print("Dates converted and saved to", output_file_path)

df = pd.read_csv("Standard Chartered Bank (Pak) Ltd.csv")
df1 = pd.read_csv("Dawood Hercules Corporation Limited.csv")
df2 = pd.read_csv("Pakistan State Oil Company Limited.csv")
df3 = pd.read_csv("Fauji Fertilizer Company Limited.csv")
# df4 = pd.read_csv("Data\")


print("Reading Data")
time.sleep(2)
clear_terminal()
print("Data Read Sucessfully")

#Making an instance of the Label Encoder
le = LabelEncoder()
print("Label Encode Initilized")
time.sleep(2)
clear_terminal()

#Encoding Date Data
print("Encoding Date Data")
time.sleep(3)
clear_terminal()
df["Encoded Date"] = le.fit_transform(df["Date"])
df1["Encoded Date"] = le.fit_transform(df1["Date"])
df2["Encoded Date"] = le.fit_transform(df2["Date"])
df3["Encoded Date"] = le.fit_transform(df3["Date"])
print("Data Encoded")
time.sleep(1)
clear_terminal()

df.dropna()
df1.dropna()
df2.dropna()
df3.dropna()
# df4.dropna()

#model initiation
model = RandomForestRegressor()
lr = LinearRegression()
lgr = LogisticRegression()

condition = True

while (condition):
    print("\n\n")
    print("\t(1) For Visualizing Graph (Press 1)")
    print("\t(2) For Predicting Close Vlues: ")
    print("\t(3) For Checking Effectiveness of diffrent Models")
    print("\tEnter 'X' to Quit")
    decision_variable = input("\tEnter Input:")

    if (decision_variable == "X" or decision_variable == "x"):
        break
    elif (decision_variable == "1"):
        print("\tAvailable Companies:\n")
        print("\t(1) Standard Chartered Bank (Pak) Ltd")
        print("\t(2) Dawood Hercules Corporation Limited")
        print("\t(3) Pakistan State Oil Company Limited")
        print("\t(4) Fauji Fertilizer Company Limited")
        print("\t(5) Press 5 to compare all in a single Graph")
        # print("\t() ")
        decision_company = input("\tSelect Company Number: ")
        if (decision_company == "1"):
            sns.regplot(x = df["Encoded Date"], y = df["Close"], color = "Red", scatter_kws={'s': 0}, logistic = False)
            sns.lineplot(x = df["Encoded Date"], y = df["Close"], color = "Red", label = "SCB")
            plt.grid(1)
            plt.legend()
            plt.show()
            clear_terminal()
            continue
        elif (decision_company == "2"):
            sns.regplot(x = df1["Encoded Date"], y = df1["Close"], color = "green", scatter_kws={'s': 0}, logistic = False)
            sns.lineplot(x = df1["Encoded Date"], y = df1["Close"], color = "green", label = "Dawood Hercules")
            plt.grid(1)
            plt.legend()
            plt.show()
            clear_terminal()
            continue
        elif (decision_company == "3"):
            sns.regplot(x = df2["Encoded Date"], y = df2["Close"], color = "blue", scatter_kws={'s': 0}, logistic = False)
            sns.lineplot(x = df2["Encoded Date"], y = df2["Close"], color = "blue", label = "Pakistan State Oil")
            plt.grid(1)
            plt.legend()
            plt.show()
            clear_terminal()
            continue
        elif (decision_company == "4"):
            sns.regplot(x = df3["Encoded Date"], y = df3["Close"], color = "orange", scatter_kws={'s': 0}, logistic = False)
            sns.lineplot(x = df3["Encoded Date"], y = df3["Close"], color = "orange", label = "Fauji Fertilizer")
            plt.grid(1)
            plt.legend()
            plt.show()
            clear_terminal()
            continue
        # elif (decision_company == "5"):
        #     sns.regplot(x = df4["Encoded Date"], y = df4["Close"], color = "black", scatter_kws={'s': 0}, logistic = False)
        #     sns.lineplot(x = df4["Encoded Date"], y = df4["Close"], color = "black", label = "Fauji Fertilizer")
        #     plt.grid(1)
        #     plt.legend()
        #     plt.show()
        #     clear_terminal()
        #     continue
        elif (decision_company == "5"):
            clear_terminal()
            print("\n\n\t\tLoading.....\n\t\tPlease Wait Patiently")
            sns.regplot(x = df["Encoded Date"], y = df["Close"], color = "Red", scatter_kws={'s': 0}, logistic = False)
            sns.lineplot(x = df["Encoded Date"], y = df["Close"], color = "Red", label = "SCB")
            sns.regplot(x = df1["Encoded Date"], y = df1["Close"], color = "green", scatter_kws={'s': 0}, logistic = False)
            sns.lineplot(x = df1["Encoded Date"], y = df1["Close"], color = "green", label = "Dawood Hercules")
            sns.regplot(x = df2["Encoded Date"], y = df2["Close"], color = "blue", scatter_kws={'s': 0}, logistic = False)
            sns.lineplot(x = df2["Encoded Date"], y = df2["Close"], color = "blue", label = "Pakistan State Oil")
            sns.regplot(x = df3["Encoded Date"], y = df3["Close"], color = "orange", scatter_kws={'s': 0}, logistic = False)
            sns.lineplot(x = df3["Encoded Date"], y = df3["Close"], color = "orange", label = "Fauji Fertilizer")
            plt.title("Pakistani Companies In 22 Years")
            plt.grid(1)
            plt.legend()
            plt.show()
            clear_terminal()
            continue
        else:
            print("\n\n\t\tWrong Input, Try again")
            time.sleep(3)
            clear_terminal()
            continue
    elif (decision_variable == "2"):
        clear_terminal()
        print("\tAvailable Companies:\n")
        print("\t(1) Standard Chartered Bank (Pak) Ltd")
        print("\t(2) Dawood Hercules Corporation Limited")
        print("\t(3) Pakistan State Oil Company Limited")
        print("\t(4) Fauji Fertilizer Company Limited")
        # print("\t() ")
        decision_company = input("\tSelect Company Number: ")
        if (decision_company == "1"):
            #train the model
            x=df[["Open","High","Low","Volume"]]
            y=df["Close"]
            model.fit(x,y)
            clear_terminal()
            inpOpen = float(input("\n\tEnter Market Open(Strictly in Numbers): "))
            inpHigh = float(input("\tEnter Market High(Strictly in Numbers): "))
            inpLow = float(input("\tEnter Market Low(Strictly in Numbers): "))
            inpVolume = float(input("\tEnter Market Volume(Strictly in Numbers): "))
            clear_terminal()
            new_data=[[inpOpen,inpHigh,inpLow,inpVolume]]
            predictionModel =  model.predict(new_data)
            time.sleep(0.5)
            clear_terminal()
            print("\n\n\tTodays market open for 'Standard Chartered Bank (Pak) Ltd' is", inpOpen)
            time.sleep(0.2)
            print("\tTodays market high for 'Standard Chartered Bank (Pak) Ltd' is", inpHigh)
            time.sleep(0.2)
            print("\tTodays market low for 'Standard Chartered Bank (Pak) Ltd' is", inpLow)
            time.sleep(0.2)
            print("\tTodays market volums for 'Standard Chartered Bank (Pak) Ltd' is", inpVolume)
            time.sleep(0.5)
            print("\n\n\tPrediction for todays close for 'Standard Chartered Bank (Pak) Ltd' is ", predictionModel)
            input("press anything to move back to home screen")
            clear_terminal()
            continue
        elif (decision_company == "2"):
            #train the model
            x=df1[["Open","High","Low","Volume"]]
            y=df1["Close"]
            model.fit(x,y)
            clear_terminal()
            inpOpen = float(input("\n\tEnter Market Open(Strictly in Numbers): "))
            inpHigh = float(input("\tEnter Market High(Strictly in Numbers): "))
            inpLow = float(input("\tEnter Market Low(Strictly in Numbers): "))
            inpVolume = float(input("\tEnter Market Volume(Strictly in Numbers): "))
            clear_terminal()
            new_data=[[inpOpen,inpHigh,inpLow,inpVolume]]
            predictionModel =  model.predict(new_data)
            time.sleep(0.5)
            clear_terminal()
            print("\n\n\tTodays market open for 'Dawood Hercules Corporation Limited' is", inpOpen)
            time.sleep(0.2)
            print("\tTodays market high for 'Dawood Hercules Corporation Limited' is", inpHigh)
            time.sleep(0.2)
            print("\tTodays market low for 'Dawood Hercules Corporation Limited' is", inpLow)
            time.sleep(0.2)
            print("\tTodays market volums for 'Dawood Hercules Corporation Limited' is", inpVolume)
            time.sleep(0.5)
            print("\n\n\tPrediction for todays close for 'Dawood Hercules Corporation Limited' is ", predictionModel)
            input("press anything to move back to home screen")
            clear_terminal()
            continue
        elif (decision_company == "3"):
            #train the model
            x=df2[["Open","High","Low","Volume"]]
            y=df2["Close"]
            model.fit(x,y)
            clear_terminal()
            inpOpen = float(input("\n\tEnter Market Open(Strictly in Numbers): "))
            inpHigh = float(input("\tEnter Market High(Strictly in Numbers): "))
            inpLow = float(input("\tEnter Market Low(Strictly in Numbers): "))
            inpVolume = float(input("\tEnter Market Volume(Strictly in Numbers): "))
            clear_terminal()
            new_data=[[inpOpen,inpHigh,inpLow,inpVolume]]
            predictionModel =  model.predict(new_data)
            time.sleep(0.5)
            clear_terminal()
            print("\n\n\tTodays market open for 'Pakistan State Oil Company Limited' is", inpOpen)
            time.sleep(0.2)
            print("\tTodays market high for 'Pakistan State Oil Company Limited' is", inpHigh)
            time.sleep(0.2)
            print("\tTodays market low for 'Pakistan State Oil Company Limited' is", inpLow)
            time.sleep(0.2)
            print("\tTodays market volums for 'Pakistan State Oil Company Limited' is", inpVolume)
            time.sleep(0.5)
            print("\n\n\tPrediction for todays close for 'Pakistan State Oil Company Limited' is ", predictionModel)
            input("press anything to move back to home screen")
            clear_terminal()
            continue
        elif (decision_company == "4"):
            #train the model
            x=df3[["Open","High","Low","Volume"]]
            y=df3["Close"]
            model.fit(x,y)
            clear_terminal()
            inpOpen = float(input("\n\tEnter Market Open(Strictly in Numbers): "))
            inpHigh = float(input("\tEnter Market High(Strictly in Numbers): "))
            inpLow = float(input("\tEnter Market Low(Strictly in Numbers): "))
            inpVolume = float(input("\tEnter Market Volume(Strictly in Numbers): "))
            clear_terminal()
            new_data=[[inpOpen,inpHigh,inpLow,inpVolume]]
            predictionModel =  model.predict(new_data)
            time.sleep(0.5)
            clear_terminal()
            print("\n\n\tTodays market open for 'Fauji Fertilizer Company Limited' is", inpOpen)
            time.sleep(0.2)
            print("\tTodays market high for 'Fauji Fertilizer Company Limited' is", inpHigh)
            time.sleep(0.2)
            print("\tTodays market low for 'Fauji Fertilizer Company Limited' is", inpLow)
            time.sleep(0.2)
            print("\tTodays market volums for 'Fauji Fertilizer Company Limited' is", inpVolume)
            time.sleep(0.5)
            print("\n\n\tPrediction for todays close for 'Fauji Fertilizer Company Limited' is ", predictionModel)
            input("press anything to move back to home screen")
            clear_terminal()
            continue
        # elif (decision_company == "5"):
        #     #train the model
        #     x=df4[["Open","High","Low","Volume"]]
        #     y=df4["Close"]
        #     model.fit(x,y)
        #     clear_terminal()
        #     inpOpen = float(input("\n\tEnter Market Open(Strictly in Numbers): "))
        #     inpHigh = float(input("\tEnter Market High(Strictly in Numbers): "))
        #     inpLow = float(input("\tEnter Market Low(Strictly in Numbers): "))
        #     inpVolume = float(input("\tEnter Market Volume(Strictly in Numbers): "))
        #     clear_terminal()
        #     new_data=[[inpOpen,inpHigh,inpLow,inpVolume]]
        #     predictionModel =  model.predict(new_data)
        #     time.sleep(0.5)
        #     clear_terminal()
        #     print("\n\n\tTodays market open for ' ' is", inpOpen)
        #     time.sleep(0.2)
        #     print("\tTodays market high for ' ' is", inpHigh)
        #     time.sleep(0.2)
        #     print("\tTodays market low for ' ' is", inpLow)
        #     time.sleep(0.2)
        #     print("\tTodays market volums for ' ' is", inpVolume)
        #     time.sleep(0.5)
        #     print("\n\n\tPrediction for todays close for ' ' is ", predictionModel)
        #     input("press anything to move back to home screen")
        #     clear_terminal()
        #     continue
        else:
            input("Wrong input, press Enter to restart")
            clear_terminal()
            continue
    elif (decision_variable == "3"):
        clear_terminal()
        x=df[["Open","High","Low","Volume"]]
        y=df["Close"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.5, random_state= 42)
        print("\n\n\t(1) Random Forest Regressor (Working model) efficiency")
        print("\n\n\t(2) Linear Regression efficiency")
        print("\n\n\t(3) Logistic Regression efficiency")
        decision_test = input("Enter What test model Efficiency you Want: ")
        clear_terminal()
        if (decision_test == "1"):
            model.fit(x_train, y_train)
            prediction_score = model.score(x_test, y_test)
            print("The prediction Effectiveness of Random Forest Regressor ML algorithm is: ", prediction_score*100)
            continue
        elif (decision_test == "2"):
            lr.fit(x_train, y_train)
            prediction_score = lr.score(x_test, y_test)
            print("The prediction Effectiveness of Linear Regression ML algorithm is: ", prediction_score*100)
            continue
        elif (decision_test == "3"):
            try:
                lgr.fit(x_train, y_train)
                prediction_score = lgr.score(x_test, y_test)
                print("The prediction Effectiveness of Linear Regression ML algorithm is: ", prediction_score*100)
                continue
            except:
                clear_terminal()
                print("\n\n\tError Occured")
                print("\tLogistic regression does not support Continous data")
                input("\n\nPress Enter to Continue")
                clear_terminal()
                continue
        else:
            input("Wrong Input, Press Enter to restart")
            continue
    else:
        print("\n\n\tWrong Input")
        input("\tPress Enter to continue")
        clear_terminal()
        continue

clear_terminal()
print("\n\n\n\t\tThank you for using my model")
print("\n\t\tBye!!!")
time.sleep(0.5)
clear_terminal()
import pandas as pd
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(script_dir, "../data/raw")
    #Create dataframes for each CSV file
    df1 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(1_25).csv")
    df2 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(26_50).csv")
    df3 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(51_75).csv")
    df4 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(76_100).csv")
    df5 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(101_125).csv")
    df6 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(126_150).csv")
    df7 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(151_175).csv")
    df8 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(176_200).csv")
    df9 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(201_225).csv")
    df10 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(226_250).csv")
    df11 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(251_275).csv")
    df12 = pd.read_csv(f"{raw_data_dir}/doctors_raw_data(276_300).csv") 


    # Print the shape of each DataFrame
    print(df1.shape, df2.shape, df3.shape, df4.shape, df5.shape, df6.shape, df7.shape, df8.shape, df9.shape, df10.shape, df11.shape, df12.shape)

    # Combine all DataFrames into one
    df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12], ignore_index=True)
    print(df.shape)
    df.to_csv(f"{script_dir}/../data/combined/doctors_combined_data.csv", index=False)


if __name__ == "__main__":
    main()
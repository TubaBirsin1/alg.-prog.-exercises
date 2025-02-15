import pandas as pd

def get_data(data_path):
    df = pd.read_csv(data_path)
    return df

def print_data(df):
    print(df)



def main():
    df = get_data("data.csv")
    print_data(df)


if __name__ == "__main__":
    main()
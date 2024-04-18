import pandas as pd
import sys

def main():
    open_file()

file_name = sys.argv[1]
file_path = f"{file_name}"


def open_file():
    if len(sys.argv) < 2:
        print("Expected usage: python main.py <filename>")
        return
       

    try:
        df = pd.read_csv(file_path)
        df.to_excel("test.xlsx", sheet_name="idk", index=False)
        

    except FileNotFoundError:
        print(f"The file {file_name} does not exist in the directory.")


if __name__ == '__main__':
    main()
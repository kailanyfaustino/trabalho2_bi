import pandas as pd
import os
import re

SOURCE_PATH: str = "./data/bronze"
DEST_PATH: str = f"{SOURCE_PATH}/silver"

def get_files(src:str) -> list[str]:
    
    files = filter(
            lambda x: x.endswith('.csv'),
            os.listdir(src))

    files = list(map(
        lambda x: os.path.join(SOURCE_PATH, x), 
        files))

    return files

def main():
    files = get_files(SOURCE_PATH)

    for file in files:
        file_pq = os.path.join(
                DEST_PATH,
                re.findall(r'(\w+)\.csv', file)[0])

        print(f'[Processing] {file}')
        df = pd.read_csv(file)
        print(f'[Saving] {file_pq}.parquet')
        df.to_parquet(file_pq)
 
if __name__ == '__main__':
    main()

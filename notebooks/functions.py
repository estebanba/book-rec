import pandas as pd

def prepare_for_seeding(df, column, db_column):
    uniques = df[column].unique()
    print(f"Unique values for {column}:", uniques)

    def assign_index(row):
        return list(uniques).index(row[column])

    df[f"{column}_id"] = df.apply(assign_index, axis=1)
    print(f"{column}_id", df[[f"{column}_id", column]])
    prepared_df = pd.DataFrame(df[[f"{column}_id", f"{column}"]])
    prepared_df.drop_duplicates(inplace=True)
    prepared_df.rename(columns={f"{column}_id": 'id', column: db_column}, inplace=True)
        
    return df, prepared_df
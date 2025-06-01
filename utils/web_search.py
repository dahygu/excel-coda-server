def fill_missing_with_web(df, columns):
    for col in columns:
        for idx, val in df[col].items():
            if pd.isnull(val) or val == "":
                # TODO: Call web search API, set df.at[idx, col] = search_result
                df.at[idx, col] = "WEB_RESULT_PLACEHOLDER"
    return df
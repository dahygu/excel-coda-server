import requests

def push_to_coda(df, token, doc_id, table_name):
    url = f"https://coda.io/apis/v1/docs/{doc_id}/tables/{table_name}/rows"
    headers = {"Authorization": f"Bearer {token}"}
    results = []
    for _, row in df.iterrows():
        payload = {
            "cells": [{"column": k, "value": v} for k, v in row.items()]
        }
        r = requests.post(url, json=payload, headers=headers)
        results.append(r.status_code)
    return results
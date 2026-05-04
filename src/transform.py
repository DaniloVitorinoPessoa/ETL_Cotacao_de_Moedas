from extract import extract_cotacoes
import pandas as pd


def transform_data(dados_json):
    df_cotacoes = pd.DataFrame.from_dict(dados_json, orient="index")
    df_cotacoes.index.name = "moeda"
    df_cotacoes = df_cotacoes.reset_index()
    return df_cotacoes

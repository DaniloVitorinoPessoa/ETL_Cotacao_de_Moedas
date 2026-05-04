from transform import transform_data

def cria_xlsx(df_cotacoes):
    excel = df_cotacoes.to_excel("data/cotacoes.xlsx")
    return None


# from extract import extract_cotacoes
# extrair = extract_cotacoes()
# json = transform_data(extrair)
# resultado = cria_xlsx(json)


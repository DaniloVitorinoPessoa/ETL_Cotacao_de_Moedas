from extract import extract_cotacoes
from transform import transform_data
from load import cria_xlsx

def main():
    json = extract_cotacoes()
    df = transform_data(json)
    excel = cria_xlsx(df)
    return None

if __name__ == "__main__":
    main()
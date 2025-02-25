from utils.formatter import format_text, filter_results

def separador():
    print("=" * 50)

def display_news(news_list):
    if not news_list:
        print("Nenhuma notícia encontrada.")
        return

    separador()
    print("ÚLTIMAS NOTÍCIAS:")
    separador()

    for noticia in news_list:
        texto_formatado = format_text(noticia)
        print(filter_results(texto_formatado))
        separador()

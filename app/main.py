from services.scraper import get_latest_news
from utils.display import display_news

def main():
    noticias = get_latest_news()
    display_news(noticias)

if __name__ == "__main__":
    main()


import feedparser
from feedparser.util import FeedParserDict
import typer

app = typer.Typer()


@app.command()
def read_feed(url: str):
    feed: feedparser.FeedParserDict = feedparser.parse(url) #type: ignore (type of url_file or string is unknown ... not set in package)
    entries: list[FeedParserDict] = feed.entries 
    entry_titles: list[str] = [entry['title'] for entry in entries] #type: ignore ... idk man this thing is just incorrect sometimes
    print(entry_titles)

@app.command()
def hello():
    print("hello")


if __name__ == "__main__":
    app()


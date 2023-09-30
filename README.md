# Sreality

Tento projekt používá Scrapy framework pro stažení prvních 500 bytů (název, obrázek) k prodeji ze stránky sreality.cz

Data jsou ukládána do Postgresql databáze.

Pro prohlédnutí záznamů je implementován jednoduchý Flask server, který je dostupný na http://127.0.0.1:8080.

Projekt lze spustit pomocí 
```
docker compose up
```


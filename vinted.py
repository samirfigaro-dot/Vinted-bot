from pyvinted import Vinted

# Inizializza connessione
vinted = Vinted()

# Funzione per cercare annunci pubblici
def get_items(keyword="Hermes"):
    items = vinted.items.search(query=keyword, per_page=10)
    return items

# TEST
if __name__ == "__main__":
    data = get_items("borsa")
    for item in data:
        print(item["title"], item["price"]["amount"], item["url"])

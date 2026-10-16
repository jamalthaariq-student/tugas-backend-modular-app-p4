from app.repositories import product_repo

def get_categories():
    return product_repo.get_all_categories()

def get_items(category_query=None, min_price_query=None):
    filtered = product_repo.get_all_items()
    
    if category_query:
        filtered = [i for i in filtered if i['category'].lower() == category_query.lower()]
        
    if min_price_query is not None:
        filtered = [i for i in filtered if i['price'] >= min_price_query]
        
    return filtered

def get_item(item_id):
    return product_repo.get_item_by_id(item_id)

def update_item(item_id, data):
    # --- ATURAN BISNIS ---
    price = data.get('price')
    if price is not None and price < 0:
        return {"error": "Harga barang tidak boleh minus (negatif)!"}
    
    name = data.get('name')
    if name is not None and len(str(name).strip()) == 0:
        return {"error": "Nama barang tidak boleh kosong!"}
    # ---------------------

    return product_repo.update_item(
        item_id,
        name,
        data.get('category'),
        price
    )

def delete_item(item_id):
    return product_repo.delete_item(item_id)

def add_item(data):
    # --- ATURAN BISNIS ---
    price = data.get('price')
    if price is not None and price < 0:
        return {"error": "Harga barang tidak boleh minus (negatif)!"}
    
    name = data.get('name')
    if name is not None and len(str(name).strip()) == 0:
        return {"error": "Nama barang tidak boleh kosong!"}
    # ---------------------

    return product_repo.add_item(
        name,
        data.get('category'),
        price
    )
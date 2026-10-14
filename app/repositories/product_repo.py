categories = [
    {"id": 1, "name": "Elektronik"},
    {"id": 2, "name": "Pakaian"},
    {"id": 3, "name": "Peralatan Rumah Tangga"}
]

items = [
    {"id": 1, "name": "Laptop", "category": "Elektronik", "price": 7500000},
    {"id": 2, "name": "Smartphone", "category": "Elektronik", "price": 4000000},
    {"id": 3, "name": "Kaos Polos", "category": "Pakaian", "price": 50000},
    {"id": 4, "name": "Blender", "category": "Peralatan Rumah Tangga", "price": 350000}
]

def get_all_categories():
    return categories

def get_all_items():
    return items

def get_item_by_id(item_id):
    return next((i for i in items if i['id'] == item_id), None)

def update_item(item_id, name, category, price):
    item = get_item_by_id(item_id)
    if item:
        if name: item['name'] = name
        if category: item['category'] = category
        if price is not None: item['price'] = price
    return item

def delete_item(item_id):
    global items
    item = get_item_by_id(item_id)
    if item:
        items = [i for i in items if i['id'] != item_id]
        return True
    return False
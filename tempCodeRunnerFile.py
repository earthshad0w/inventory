    found = False
    item_id = input("Enter item I.D.".upper())
    # Check if item id is in inventory. Update quantity if True
    for item in items:
        if item.id == item_id:
            qty_to_add = get_valid_quantity()
            items.qty += qty_to_add
            found = True
            write_items(items)
            return
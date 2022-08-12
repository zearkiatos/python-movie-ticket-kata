BASE_PRICE = {
    "DINAMIX": 18800,
    "3D": 15500,
    "2D": 11300
}

PRICING_RULES = {
    "WITHOUT_PEEK_HOUR": 0.1,
    "500_PER_GRANT_EQUALS_TO_THREE": 500,
    "PAY_WITH_CINEMA_CARD": 0.05,
    "RESERVE_FEE": 2000,
    "PEEK_HOUR_INCREASE": 0.25,
    "PEEK_HOUR_INCREASE_DINAMAX": 0.50
}

THREE_D = "3D"
TWO_D = "2D"
DINAMIX = "DINAMIX"
QUANTITY_TICKETS_FOR_DISCOUNT = 3


def calculate_ticket_cost(ticket_quantity: int, type_hall: str, peek_hour: bool, payment_with_loyalty_card: bool, reserve: bool) -> int:
    base_price = BASE_PRICE[type_hall.upper()]
    total_price = base_price*ticket_quantity
    if(peek_hour):
        if (THREE_D == type_hall or TWO_D == type_hall):
            total_price = total_price + total_price * \
                PRICING_RULES["PEEK_HOUR_INCREASE"]
        elif(DINAMIX == type_hall):
            total_price = total_price + total_price * \
                PRICING_RULES["PEEK_HOUR_INCREASE_DINAMAX"]
    else:
        total_price = total_price - total_price * \
            PRICING_RULES["WITHOUT_PEEK_HOUR"]

    if(ticket_quantity >= QUANTITY_TICKETS_FOR_DISCOUNT):
        total_price = total_price + \
            PRICING_RULES["500_PER_GRANT_EQUALS_TO_THREE"]*ticket_quantity

    if (payment_with_loyalty_card):
        total_price = total_price - base_price * \
            PRICING_RULES["PAY_WITH_CINEMA_CARD"]

    if (reserve):
        total_price = total_price + \
            PRICING_RULES["RESERVE_FEE"]*ticket_quantity
    
    return round(total_price)

print(calculate_ticket_cost(3, 'DINAMIX', True, True, True))

import random

BUYER_CODES = [
    "0000263320", "0000324176", "0000330546", "0000330800", "0000355280",
    "0000699636", "0000701934", "0000706036", "0000706732", "0000707211",
    "0000708349", "0000710398", "0000712519", "0000713266", "0000714771",
    "0000715949", "0000716348", "0000722804", "0000731361", "0000740551",
    "0000801353", "0000831020", "0000850868", "0000865487", "0000874830",
    "0000920213", "0000928873", "0000932844", "0000938771", "0000941470",
    "0000972712", "0000976631", "0000981922", "0000981944", "0001005878",
    "0001016115", "0001016508", "0001018964", "0007190782", "0007289904",
    "0007336541", "0007372941", "0007382175", "0007423097", "0007438401",
    "0007442715", "0007450754", "0007496173", "0007501350", "0007507888"
]

def get_random_buyer_codes():
    # Escolher de 1 a 5 códigos de forma randômica
    num_codes = random.randint(1, 5)
    return random.sample(BUYER_CODES, num_codes)

PERSON_DELIVERY_WINDOW_QUERY = '''
query ValidacaoDeliveryWindow($buyer_codes: [String!]!, $allowed_low_shelf_life: Boolean) {
  get_person_delivery_window(
    filters: {buyer_codes: $buyer_codes, allowed_low_shelf_life: $allowed_low_shelf_life}
  ) {
    items {
      customer_shared_id
      delivery_windows {
        allowed_low_shelf_life
        delivery_date
        expiration_date
      }
      updated_at
    }
  }
}
'''

def get_person_delivery_window_variables():
    return {
        "buyer_codes": get_random_buyer_codes(),
        "allowed_low_shelf_life": random.choice([True, False])
    }

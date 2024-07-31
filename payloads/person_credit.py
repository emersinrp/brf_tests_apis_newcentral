import random

BUYER_CODES = [
    "0000010071", "0000010144", "0000002086", "0000004600",
    "0000004273", "0000010162", "0000010036", "0000010053",
    "0000010005", "0000010233", "0000010184", "0000010193",
    "0000010199", "0000010200", "0000010203", "0000010155",
    "0000010160", "0000010166", "0000010174", "0000010100",
    "0000010102", "0000010103", "0000010105", "0000010117",
    "0000010122", "0000010130", "0000010133", "0000010135",
    "0000010068", "0000010075", "0000010094", "0000010095",
    "0000010030", "0000010055", "0000010136", "0000010124",
    "0000010219", "0000010115", "0000010116", "0000010202",
    "0000010140", "0000010238", "0000010159", "0000010201",
    "0000010186", "0000010084", "0000010051", "0000010104",
    "0000010168", "0000010217", "0000010132", "0000010121",
    "0000010192", "0000010158", "0000010196", "0000010092",
    "0000010145", "0000010033", "0000010056", "0000010097"
]

def get_random_buyer_codes():
    # Escolher de 1 a 5 códigos de forma randômica
    num_codes = random.randint(1, 5)
    return random.sample(BUYER_CODES, num_codes)

PERSON_CREDIT_QUERY = '''
query FirstPersonCredit($buyer_codes: [String!]!, $credit_area: String) {
  get_person_credit(
    filters: {pagination_filter: {limit: 5}, credit_area: $credit_area, buyer_codes: $buyer_codes}
  ) {
    items {
      customer_shared_id
      consumed
      available
      credit_area
      overdue
      total
      updated_at
    }
    page_info {
      current_page
    }
  }
}
'''

def get_person_credit_variables():
    return {
        "buyer_codes": get_random_buyer_codes(),
        "credit_area": "0010"
    }

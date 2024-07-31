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

PERSON_CREDIT_VARIABLES = {
    "buyer_codes": ["0000010071"],
    "credit_area": "0010"
}

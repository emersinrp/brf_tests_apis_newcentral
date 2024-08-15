import random
from faker import Faker
from datetime import datetime, timedelta

faker = Faker()

# Lista de accounts_ids fornecidos
ACCOUNTS_IDS = [
    "00981411000105",
    "03493431000125",
    "36729158000144",
    "27598521000149",
    "02831172007226",
    "83648477003554",
    "02391271000221",
    "05903376000120",
    "07809682000127",
    "10985298000190",
    "20841976000102",
    "36956993000117",
    "22836002000158",
    "08399617000567",
    "41333242000184",
    "43086034000153",
    "20261799000187",
    "49391362000140",
    "18549494000123",
    "48982529000184"
]

# Lista de SKUs, Fifo Codes, Sales Organizations, States, Sales Regions e Segments fornecidos
SKUS = [
    "000000000000000307",
    "000000000000740042",
    "000000000000740042",
    "000000000000743035",
    "000000000000743035",
    "000000000000743373",
    "000000000000743373",
    "000000000000743374",
    "000000000000743375"
]

FIFO_CODES = [
    "Z098",
    "Z100",
    "Z101",
    "Z102"
]

SALES_ORGANIZATIONS = [
    "1634",
    "3002",
    "350",
    "R586",
    "H408",
    "1678",
    "654",
    "1102",
    "H394",
    "R742"
]

STATES = [
    "RS",
    "CE",
    "PI",
    "DF",
    "GO",
    "SP",
    "AP",
    "RJ",
    "RO",
    "PR",
    "ES",
    "MG",
    "MT",
    "MS",
    "RN",
    "MA",
    "AM",
    "PE",
    "SC",
    "BA"
]

SALES_REGIONS = [
    "996024",
    "932701",
    "SP0002",
    "VF0408",
    "VF0618",
    "316051",
    "VF0109",
    "SZ0436",
    "VF0150",
    "728050",
    "994116",
    "SZ0177",
    "996138",
    "996124",
    "994022"
]

SEGMENTS = [
    "V1",
    "C6",
    "N2",
    "65",
    "Q1",
    "B1",
    "G2",
    "O2",
    "N5",
    "16",
    "A4",
    "I1",
    "J5",
    "N6",
    "G3",
    "21",
    "C1",
    "A3",
    "C3",
    "12",
    "C7"
]

def generate_promotion_payload():
    random_name = f"TEST AUTOMACAO {faker.random_number(digits=5)}"
    random_account_id = random.choice(ACCOUNTS_IDS)
    
    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=2)
    
    start_date_str = start_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    random_sku_1 = random.choice(SKUS)
    random_sku_2 = random.choice(SKUS)
    random_fifo_code_1 = random.choice(FIFO_CODES)
    random_fifo_code_2 = random.choice(FIFO_CODES)
    random_sales_organization = random.choice(SALES_ORGANIZATIONS)
    random_state = random.choice(STATES)
    random_sales_region = random.choice(SALES_REGIONS)
    random_segment = random.choice(SEGMENTS)

    return {
        "name": random_name,
        "promotion_type": "OVERPRICE",
        "channel": "331ab83d-a95c-4a05-804d-5e0d5bf8fa9a",
        "exclusive": False,
        "start_date": start_date_str,
        "end_date": end_date_str,
        "enabled": True,
        "all_accounts_selected": False,
        "accounts_ids": [random_account_id],
        "items": [
            {
                "limit_type": "QUANTITY",
                "skus": [
                    {
                        "required": False,
                        "sku": random_sku_1,
                        "fifo_code": random_fifo_code_1,
                        "product_category": None
                    },
                    {
                        "required": False,
                        "sku": random_sku_2,
                        "fifo_code": random_fifo_code_2,
                        "product_category": None
                    }
                ]
            }
        ],
        "min_quantity": None,
        "discount_price_percent": 4,
        "limit": 99999,
        "sales_organizations": [
            random_sales_organization
        ],
        "states": [
            random_state
        ],
        "sales_regions": [
            random_sales_region
        ],
        "segments": [
            random_segment
        ]
    }

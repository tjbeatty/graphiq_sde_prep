

shares_list = [{'symbol': 'AMZN', 'shares': 3}, {'symbol': 'GOOG', 'shares': 2}, {'symbol': 'MU', 'shares': 4}]
quote_responses = [{'name': 'Amazon.com Inc.', 'price': 1636.85, 'symbol': 'AMZN'},
                   {'name': 'Alphabet Inc.', 'price': 1038.63, 'symbol': 'GOOG'},
                   {'name': 'Micron Technology Inc.', 'price': 37.44, 'symbol': 'MU'}]

total_value_all = 0

for i, row in enumerate(shares_list):
    shares_list[i]["company_name"] = quote_responses[i]["name"]
    shares_list[i]["cur_price"] = quote_responses[i]["price"]
    shares_list[i]["total_value"] = shares_list[i]["shares"] * shares_list[i]["cur_price"]
    total_value = shares_list[i]["shares"] * shares_list[i]["cur_price"]

    total_value_all += total_value

print(shares_list)
print("Total Value All = {}".format(total_value_all))
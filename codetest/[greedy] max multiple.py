def max_product(card_lists):
    # 코드를 작성하세요.
    multiple = 1
    for card_list in card_lists:
        multiple *= max(card_list)
    return multiple

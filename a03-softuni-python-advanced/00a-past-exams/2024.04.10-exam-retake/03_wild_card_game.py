def draw_cards(*card_tuples, **card_kwargs):
    monster_cards = []
    spell_cards = []

    for card_name, card_type in card_tuples:
        if card_type == "monster":
            monster_cards.append(card_name)
        elif card_type == "spell":
            spell_cards.append(card_name)

    for card_name, card_type in card_kwargs.items():
        if card_type == "monster":
            monster_cards.append(card_name)
        elif card_type == "spell":
            spell_cards.append(card_name)

    # Sort cards
    monster_cards.sort(reverse=True)
    spell_cards.sort()

    # Otput
    result = []
    if monster_cards:
        result.append("Monster cards:")
        for card in monster_cards:
            result.append(f"  ***{card}")
    if spell_cards:
        result.append("Spell cards:")
        for card in spell_cards:
            result.append(f"  $$${card}")

    return "\n".join(result)


# Examples
print(draw_cards(("cyber dragon", "monster"), freeze="spell"))
print(
    draw_cards(
        ("celtic guardian", "monster"),
        ("earthquake", "spell"),
        ("fireball", "spell"),
        raigeki="spell",
        destroy="spell",
    )
)
print(
    draw_cards(
        ("brave attack", "spell"),
        ("freeze", "spell"),
        lightning_bolt="spell",
        fireball="spell",
    )
)

def splitting_money(amount):
    notes = [500, 100, 50, 20, 10, 5, 2, 1]
    result = ""
    for note in notes:
        note_count = amount // note
        if note_count > 0:
            result += f"{note} Taka: {note_count} note(s)\n"
            amount %= note
    return result.strip()


amount = int(input())

split_result = splitting_money(amount)

print(split_result)

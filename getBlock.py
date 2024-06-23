def find_records(form, blockchain):
    for block in blockchain:
        print(block.data)
        condition = (
                    block.data[0] == form.get("course") and
                    block.data[1] == form.get("year") and
                    len(block.data[2]) == int(form.get("number")))
        if condition:
            return block.data[2]
    return -1

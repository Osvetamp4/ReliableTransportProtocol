def determine_adjacent(sack_block,seq_num):
    lower_bound = sack_block[0]
    upper_bound = sack_block[1]
    if lower_bound - 1 == seq_num:
        return "lower"
    elif upper_bound + 1 == seq_num:
        return "upper"
    else:
        return "none"

def find_sack_block_avg(sack_block):
    lower_bound = sack_block[0]
    upper_bound = sack_block[1]
    return (lower_bound + upper_bound) / 2


def update_SACK_blocks(sack_blocks,seq_num):
    avg_list = [find_sack_block_avg(sack_block) for sack_block in sack_blocks]
    #print(avg_list)
    lower_bound_index = 0
    upper_bound_index = len(sack_blocks) - 1
    while upper_bound_index - lower_bound_index > 1:
        middle_index = (lower_bound_index + upper_bound_index) // 2
        if avg_list[middle_index] < seq_num:
            lower_bound_index = middle_index
        else:
            upper_bound_index = middle_index
    #print(lower_bound_index,upper_bound_index)
    #print(sack_blocks[lower_bound_index],sack_blocks[upper_bound_index])

    lower_block = sack_blocks[lower_bound_index]
    upper_block = sack_blocks[upper_bound_index]

    if determine_adjacent(lower_block,seq_num) == "lower":
        sack_blocks[lower_bound_index][0] -= 1
    elif determine_adjacent(upper_block,seq_num) == "upper":
        sack_blocks[upper_bound_index][1] += 1
    elif determine_adjacent(lower_block,seq_num) == "none" and determine_adjacent(upper_block,seq_num) == "none":
        lower_bound_avg = find_sack_block_avg(lower_block)
        upper_bound_avg = find_sack_block_avg(upper_block)
        if lower_bound_avg > seq_num:
            sack_blocks.insert(lower_bound_index, [seq_num,seq_num])
        elif upper_bound_avg < seq_num:
            sack_blocks.insert(upper_bound_index + 1, [seq_num,seq_num])
        else:
            sack_blocks.insert(lower_bound_index + 1, [seq_num,seq_num])
    elif determine_adjacent(lower_block,seq_num) == "upper" and determine_adjacent(upper_block,seq_num) == "lower":
        sack_blocks[lower_bound_index][1] = sack_blocks[upper_bound_index][1]
        del sack_blocks[upper_bound_index]
    elif determine_adjacent(lower_block,seq_num) == "upper":
        sack_blocks[lower_bound_index][1] += 1
    elif determine_adjacent(upper_block,seq_num) == "lower":
        sack_blocks[upper_bound_index][0] -= 1
    return sack_blocks

alist = [[1,5],[7,9],[11,11],[14,20]]
#print("before:",alist)
#print("updated (13):",update_SACK_blocks(alist,13))
#print("updated (12):",update_SACK_blocks(alist,12))
#print("updated (21):",update_SACK_blocks(alist,21))
#print("updated (10):",update_SACK_blocks(alist,10))
#print("updated (6):",update_SACK_blocks(alist,6))
#print("updated (0):",update_SACK_blocks(alist,0))

def find_missing_seq(sack_blocks,cumulative_ack):
    missing_acks = []
    ack_pointer = cumulative_ack
    for sack_block in sack_blocks:
        lower_bound = sack_block[0]
        upper_bound = sack_block[1]
        missing_acks.extend(list(range(ack_pointer + 1,lower_bound)))
        ack_pointer = upper_bound
    return missing_acks



def cum_ack_absorb(sack_blocks,cumulative_ack):
    first_sack_block = sack_blocks[0]
    lower_bound = first_sack_block[0]
    upper_bound = first_sack_block[1]

    if abs(lower_bound - cumulative_ack) <= 1:
        cumulative_ack = upper_bound
        del sack_blocks[0]
    return sack_blocks,cumulative_ack


strike_dictionary = dict()
strike_dictionary[1] = 0
strike_dictionary[3] = 0
#assumes that ack already has entry in dictionary
def process_ack_strike(strike_dictionary,ack_num):
    if ack_num not in strike_dictionary:
        return False
    strike_dictionary[ack_num] += 1
    if strike_dictionary[ack_num] >= 3:
        strike_dictionary[ack_num] = 0 #reset the strike count and resend it
        return True
    return False #don't resend it

process_ack_strike(strike_dictionary,1)
print(process_ack_strike(strike_dictionary,1))
print(strike_dictionary)
print(process_ack_strike(strike_dictionary,1))
print(strike_dictionary)
def merge_sack_blocks(sack_block1,sack_block2):
        if sack_block1[0] <= sack_block2[0] and sack_block1[1] >= sack_block2[0] - 1: #if sack block 1 is to the left of sack block 2 and they are adjacent or overlapping, merge them
            return [min(sack_block1[0],sack_block2[0]),max(sack_block1[1],sack_block2[1])]
        elif sack_block2[0] <= sack_block1[0] and sack_block2[1] >= sack_block1[0] - 1: #if sack block 2 is to the left of sack block 1 and they are adjacent or overlapping, merge them
            return [min(sack_block1[0],sack_block2[0]),max(sack_block1[1],sack_block2[1])]
        else:
            return None

def merge_sack_block_lists(sack_blocks1,sack_blocks2):
        merged_sack_blocks = []
        i = 0
        j = 0
        while i < len(sack_blocks1) and j < len(sack_blocks2):
            merged_block = merge_sack_blocks(sack_blocks1[i],sack_blocks2[j])
            if merged_block:
                merged_sack_blocks.append(merged_block)
                i += 1
                j += 1
            elif sack_blocks1[i][0] < sack_blocks2[j][0]:
                merged_sack_blocks.append(sack_blocks1[i])
                i += 1
            else:
                merged_sack_blocks.append(sack_blocks2[j])
                j += 1
        while i < len(sack_blocks1):
            merged_sack_blocks.append(sack_blocks1[i])
            i += 1
        while j < len(sack_blocks2):
            merged_sack_blocks.append(sack_blocks2[j])
            j += 1
        return merged_sack_blocks

sack_blocks1 = []
sack_blocks2 = []
print(merge_sack_block_lists(sack_blocks1,sack_blocks2))

def absorb_sacks(cumulative_ack, sack_blocks):
    """
    Consolidates SACK blocks into the cumulative_ack if they touch or overlap.
    Returns the new cumulative_ack and the remaining (unabsorbed) sack_blocks.
    """
    if not sack_blocks:
        return cumulative_ack, []

    # Ensure blocks are sorted by start sequence
    sack_blocks.sort()
    
    # Merge overlapping or adjacent SACK blocks first
    merged = []
    curr_start, curr_end = sack_blocks[0]
    for next_start, next_end in sack_blocks[1:]:
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            merged.append([curr_start, curr_end])
            curr_start, curr_end = next_start, next_end
    merged.append([curr_start, curr_end])

    # Absorb merged blocks into the mainland
    final_sacks = []
    new_cum_ack = cumulative_ack
    
    for start, end in merged:
        # If block touches or is behind the mainland, it's absorbed
        if start <= new_cum_ack + 1:
            new_cum_ack = max(new_cum_ack, end)
        else:
            # It's still an island
            final_sacks.append([start, end])

    return new_cum_ack, final_sacks

sack_blocks = [[2, 4], [5, 7], [10, 12]]
cumulative_ack = 10
print(absorb_sacks(cumulative_ack, sack_blocks))
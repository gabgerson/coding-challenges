#my solution some edge cases don't merge correctly
def merge_meetings(meetings):
    
    sorted_meetings = sorted(meetings)

    for meeting_index in range(len(sorted_meetings)):
        # print(meeting_index)
        if meeting_index == len(sorted_meetings):
            break
        if sorted_meetings[meeting_index][1] >= sorted_meetings[meeting_index + 1][0]:
            if sorted_meetings[meeting_index][1] >= sorted_meetings[meeting_index + 1][1]:
                sorted_meetings.pop(meeting_index + 1)
            else:
                sorted_meetings[meeting_index] = (sorted_meetings[meeting_index][0], sorted_meetings[meeting_index + 1][1])
                sorted_meetings.pop(meeting_index + 1)

    return sorted_meetings


print(merge_meetings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_meetings([(1, 5), (2, 3)]))
# print(merge_meetings([(1, 10), (2, 6), (3, 5), (7, 9)]))

#interview cake solution 
def merge_ranges(meetings):

# Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    print(merged_meetings)

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                    max(last_merged_meeting_end,
                                        current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))
meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# meetings = [(1, 5), (1, 3), (2, 8), (8, 9), (10, 12), (11, 15), (16, 17)]


def merge_range(meetings):

    # sorting meeting by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the first meeting of the day
    merged_meetings = [sorted_meetings[0]]

    for current_meet_start_time, current_meet_end_time in sorted_meetings[1:]:

        # get the start and end time of the last meeting in the merged_meeting list
        # to compare with the current meeting
        last_merged_meet_start, last_merged_meet_end = merged_meetings[-1]

        # if current meeting overlap with the last merged meeting than
        # update it with later end of two meetings
        if current_meet_start_time <= last_merged_meet_end:
            merged_meetings[-1] = (
                last_merged_meet_start,
                max(last_merged_meet_end, current_meet_end_time),
            )
        else:
            # add current meeting as is because it doesn't overlap with any other meeting
            merged_meetings.append((current_meet_start_time, current_meet_end_time))

    return merged_meetings


print(merge_range(meetings))

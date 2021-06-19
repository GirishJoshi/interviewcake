"""
Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting. 
In HiCal, a meeting is stored as a tuple of integers (start_time, end_time). 
These integers represent the number of 30-minute blocks past 9:00am.

For example:

(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and 
returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers 
representing our time ranges. Here we've simplified our times down to the number of 
30-minute slots past 9:00 am. But we want the function to work even for very large numbers, 
like Unix timestamps. In any case, the spirit of the challenge is to merge meetings where 
start_time and end_time don't have an upper bound.
"""

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

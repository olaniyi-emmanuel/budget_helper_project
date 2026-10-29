# budget_helper_project
Group 8 - Talent Nation : Producing Quality Code


# event_summary
def event_summary (event_name, total, status):
    return f"{event_name}: {total} naira. {status}."

message = event_summary("Study Day", 15000, "WIthin budget")
message2= event_summary(event_name="Birthday", total=2000, status="Over budget")
print (message, message2)


#Hand_over Note
"""
Component Owned: event_summary
Returns: event_name, the total in naira and the status
Tests:-The required example 
      -different event name and total
Issue: None
"""
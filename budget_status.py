def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

def event_total(attendees, food_per_person, trasnport_per_person, venue_cost):
    sub_total = participant_cost(attendees, food_per_person, trasnport_per_person)
    return sub_total + venue_cost

def budget_status(budget, total):
    
    if total <= budget:
        return "Within budget"
    else:
    
        return "Over budget"

# Below budget test
budget_1 = budget_status(16000, 15000)
print(budget_1)

# Exactly equals to budget
budget_2 = budget_status(20000, 20000)
print(budget_2)
 
#  Over budget
budget_3 = budget_status(19000, 23000)
print(budget_3)


"""
Handover Note
Component owned: budget_status
Returns: "Within budget" when total <= budget, otherwise "Over budget"
Tests: below budget, exact budget, over budget
Issues: None 
"""

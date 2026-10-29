def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    sub_total = participant_cost(attendees, food_per_person, transport_per_person)
    return sub_total + venue_cost

def budget_status(budget, total):

    if total <= budget:
       return "Within budget"   
    else:
       return "Over budget"


def event_summary(event_name, total, status):
    return f"{event_name}: {total} naira. {status}."


#Test Case
if __name__ == "__main__":

    attendees = 10
    food_per_person = 800
    transport_per_person = 200 
    venue_cost = 5000
    budget = 16000
    event_name ="Study Day"
    total = event_total(attendees, food_per_person, transport_per_person, venue_cost)
    status= budget_status(budget, total)
    totalParticipantCost = participant_cost(attendees, food_per_person, transport_per_person)
    eventSummary = event_summary(event_name, total, status)
    print(
        f"Particpant_cost => {totalParticipantCost} \n" 
          f"event_total => {total} \n"
          f"budget_status => {status} \n"
          f"event_summary => {eventSummary}")
    
    
    

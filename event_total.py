def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    sub_total = participant_cost(attendees, food_per_person, transport_per_person)
    return sub_total + venue_cost


# Component Tests
# Normal attendee cost + venue
print(event_total(attendees=10, food_per_person=800, transport_per_person=200, venue_cost=5000))

# zero attendees with a non zero values
print(event_total(attendees=0, food_per_person=800, transport_per_person=200, venue_cost=5000))

# Handover Notes
#1. Component Owned: Event_total
#2. What It Returns: Calls participant_cost, adds venue_cost, returns the combined total.
#3. Test: (i) Normal attendee cost plus venue 
#         (ii)Zero attendees with a non-zero venue
#4. Issue: Didnt initially add my participant cost to the event total so i was getting an error but i eventually figured it out and fixed it

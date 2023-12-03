def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {room}!" for room, name in enumerate(names, start = 1)]

def printer(names):
    batch_badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in batch_badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
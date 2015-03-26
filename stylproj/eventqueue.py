subscribers = {}

def subscribe(subscriber, event):
    if event not in subscribers:
        subscribers[event] = list(subscriber)
    else:
        subscribers[event].append(subscriber)

def notify(event):
    for event in subscribers:
        for sub in subscribers[event]:
            sub(event)

from guizero import App, PushButton, info, yesno, error, ButtonGroup, CheckBox, Combo, Text, Slider

def layout_auditorium():
    """
    This function loads 648 tickets into the system using letters a-x for rows
    and number for seat locations 1-27.  In this particular auditorium, seats a-g are
    in the front section, h-o in the center, and p-x in the back.  Numbers 1-9 are on the left,
    10-18 in the middle, and 19-27 on the right.
    """
    seat_list = []
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
    for letter in alphabet:
        for number in range(27):
            seat_list.append(letter+str(number+1))
    return seat_list

def pick_seats(side, location, number, aisle):
    global seats
    """This function will return possible seats for the transaction.
        side is Left, Center, or Right
        location is Front, Middle, or Back
        number is how many tickets needed
        aisle is True or False depending on if an aisle seat is needed in the order
    """
    temp_seats = []
    possible_seats = []
    for seat in seats:
        if location == "Front":
            if int(seat[1:]) <= 9:
                if side =="Left":
                    if seat[0] < "h":
                        possible_seats.append(seat)
                if side =="Center":
                    if seat[0] < "p" and seat[0] > "h":
                        possible_seats.append(seat)
                if side =="Right":
                    if seat[0] > "p":
                        possible_seats.append(seat)
        if location == "Middle":
            if int(seat[1:]) > 9 and int(seat[1:])<=18:
                if side =="Left":
                    if seat[0] < "h":
                        possible_seats.append(seat)
                if side =="Center":
                    if seat[0] < "p" and seat[0] > "h":
                        possible_seats.append(seat)
                if side =="Right":
                    if seat[0] > "p":
                        possible_seats.append(seat)
        if location == "Back":
            if int(seat[1:])>18:
                if side =="Left":
                    if seat[0] < "h":
                        possible_seats.append(seat)
                if side =="Center":
                    if seat[0] < "p" and seat[0] > "h":
                        possible_seats.append(seat)
                if side =="Right":
                    if seat[0] > "p":
                        possible_seats.append(seat)
    aisleCheck = False
    while aisleCheck ==False and len(possible_seats)>number:
        for seat in range(number):
            temp_seats.append(possible_seats[seat])
        if aisle == True:
            for seat in temp_seats:
                #print(seat[1:])
                if seat[1:] == "8" or seat[1:] == "9" or seat[1:]=="18" or seat[1:]=="19":
                    aisleCheck = True
                    break
            if aisleCheck == False:
                for seat in temp_seats:
                    while possible_seats.count(seat)>0:
                        possible_seats.remove(seat)
                print(possible_seats)
                temp_seats=[]
        if aisle == False:
            aisleCheck = True
    if len(temp_seats) == 0:
        error("Out of Tickets", "Not enough tickets in this section for your request")
    return temp_seats

def remove_seats(sell_seats):
    """
    If a sale is confirmed.  Run this to take the tickets out of possible tickets to purchase.
    This function modifies seats as a global variable and doesn't return anything.
    """
    global seats
    
    for ticket in sell_seats:
        while seats.count(ticket)>0:
            seats.remove(ticket)

def slider_changed(slider_value):
    """
    This function is an event handler for the slider.
    It sets the global ticketNum so that it can be accessed later in the program
    """
    pass

def on_click():
    """
    There should be two global variables, ticketNum and seats
    It should call pick_seats and pass in the appropriate variables.
    It should check to see if pick_seats returned tickets.
    If it did, display an appropriate alert box telling the user which tickets will be
    purchased and how much it will cost.
    If accepted, prompt the user that the tickets have been purchased.
    Run remove_seats to take the sold seats out of the seats list.
    If not accepted, warn the user that no tickets have been purchased and do nothing.
    If pick_seats did not return tickets, that means that the section is sold out, warn the
    customer and do nothing.  The customer should then use the main window to make another
    selection.
    """
    pass

app = App(title="Musical Tickets")
nightLabel = Text(app, text="Which Night?")
ticketNumLabel = Text(app, text="How Many Tickets Would You Like?")
locationLabel = Text(app, text="Where would you like to sit?")
wheelChairLabel = Text(app, text="Do you need handicap accessible seating?")

COST = 10
seats = layout_auditorium()

app.display()
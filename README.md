# lesson9
Alert Boxes

### Steps

Use the file lesson9.py

1) Open the documentation at [https://lawsie.github.io/guizero/](https://lawsie.github.io/guizero/)
2) Using the grid method, put in the appropriate widgets so that the user can fill out the app form
3) Put in a PushButton so that the user can purchase tickets.  Point command to the on_click function.
4) If you are using a slider.  Read on the documentation how to make an event handler for a slider.  Use the slider changed function already in the program.
5) Now program the on_click function.  I have already written some helper functions to take care of the heavy lifting.  
..1. There should be two global variables, ticketNum and seats  
..2. It should call pick_seats and pass in the appropriate variables  
..3. It should check to see f pick_seats returned tickets.  
..4. If it did, display an appropriate alert box telling the user which tickets will be purchased and how much it will cost.  
..5. If accepted, prompt the user that the tickets have been purchased.  
..6. Run remove_seats to take the sold seats out of the seats list.  
..7. If not accepted, watn the user that no tickets have been purchased and do nothing.  
..8. If pick_seats did not return tickets, that means that the section is sold out, warn the customer and do nothing  
..9. The customer should then be able to return to the main window to make another selection.  

### Discussion Questions

1) For what information did you decide to use a combo box?  Why?

2) For what information did you decide to use a button group?  Why?

3) For what information did you decide to use a checkbox?  Why?

4) Why do you need to store a variable for the alert boxes?  Explain.

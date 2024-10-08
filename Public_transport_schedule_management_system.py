from tabulate import tabulate


class TransportationSchedule:
    def _init_(self):
        self.schedules = {"Pune-Shirur": {
            "01/03/2024": {"7.00AM": 30, "9.00AM": 30, "11.00AM": 30, "1.00PM": 30, "3.00PM": 30, "5.00PM": 17,
                           "7.00PM": 22},
            "02/03/2024": {"7.00AM": 30, "9.00AM": 30, "11.00AM": 30, "1.00PM": 30, "3.00PM": 30, "5.00PM": 30,
                           "7.00PM": 30}},
                          "Pune-Ahmadnager": {
                              "01/03/2024": {"7.00AM": 30, "9.00AM": 30, "11.00AM": 30, "1.00PM": 30, "3.00PM": 30,
                                             "5.00PM": 30, "7.00PM": 30},
                              "02/03/2024": {"7.00AM": 30, "9.00AM": 30, "11.00AM": 30, "1.00PM": 30, "3.00PM": 30,
                                             "5.00PM": 30, "7.00PM": 30}}}

        self.payment = {"Pune-Shirur": ["120Rs"],
                        "Pune-Ahmadnager": ["180Rs"]}

        self.users = {
            "ravi123": {"password": "Ravi@123", "name": "Ravi Taj", "dob": "02/01/2002", "email": "ravitaj2@gmail.com"},
            "rohan123": {"password": "Rohan@123", "name": "Rohan Mshere", "dob": "07/02/206",
                         "email": "roohanmashere2@gmail.com"}}
        self.logins = {}

        self.bookings = {
            "ravi123": [["Pune-Shirur", "01/03/2024", "7.00PM", 4], ["Pune-Shirur", "01/03/2024", "5.00PM", 4]],
            "rohan123": [["Pune-Shirur", "01/03/2024", "5.00PM", 9], ["Pune-Shirur", "01/03/2024", "7.00PM", 4]]}

        self.inquiry_request_data = {}
        self.inquiry_request_reply = {}

        self.admin_name = ["FE_AI.Group_13"]
        self.admin_password = ["BTAI@dypsst"]

    def register_user(self):
        print("\n---------------------------------------")
        print("|||      Registration Interface     |||")
        print("---------------------------------------")
        name = input("Enter Your Name: ")
        username = input("Enter Username: ")
        dob = input("Enter Your Date of Birth (DD/MM/YYYY): ")
        email = input("Enter Your Email: ")
        if username in self.users:
            print("Username already exists. Please choose another one.")
            print("-----------------------------------------------------")
            return
        password = input("Enter Password: ")

        self.users[username] = {
            "password": password,
            "name": name,
            "dob": dob,
            "email": email,

        }
        print("Your Account is Registered Successfully.")
        print("------------------------------------------")

    def login_user(self):
        print("\n---------------------------------")
        print("|||      Login Interface      |||")
        print("---------------------------------")
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        if username in self.users and self.users[username]["password"] == password:
            self.logins[username] = {"Password:", password}
            print("Login Successfully.")
            print("---------------------")
            return True
        else:
            print("Please Enter Valid Username or Password.")
            print("------------------------------------------")
            return False

    def display_all_schedules(self):
        if not self.schedules:
            print("No Schedules Available.")
            print("-------------------------")
        else:
            print("\n--------------------------------")
            print("|||       All Schedules       |||")
            print("--------------------------------")
            for route, dates in self.schedules.items():
                print(f"> Route: {route}")
                for date, times in dates.items():
                    print(f"Date: {date}")
                    schedule_table = []
                    for time, seats in times.items():
                        schedule_table.append([time, seats])
                    print(tabulate(schedule_table, tablefmt="grid", headers=["Time", "Seats"]))
                    print("Each Schedule Cost:-"f"{self.payment[route][0]}")
                    print("--------------------------------")

            a = input("\nIf you want to Book any Schedule Please enter 'Yes': ")
            if a == "Yes":
                username = input("Enter Your UserName: ")
                if username in self.logins:
                    route = input("Enter Route to Book Schedule: ")
                    if route in self.schedules:
                        date = input("Enter Date to Book: ")
                        if date in self.schedules[route]:
                            schedule_table = []
                            for time, seats in self.schedules[route][date].items():
                                schedule_table.append([time, seats])
                            print("\n**** The Schedule of This Date ****")
                            print(
                                tabulate(schedule_table, tablefmt="grid", headers=["Time", "Seats"], stralign="center"))

                            time = input("Enter Time to Book: ")
                            if time in self.schedules[route][date]:
                                seats = int(input("Enter Seat to Book: "))
                                if seats < self.schedules[route][date][time]:
                                    self.schedules[route][date][time] -= seats
                                    if self.bookings:
                                        if username not in self.bookings:
                                            self.bookings[username] = []
                                            p = []
                                            p.append(route)
                                            p.append(date)
                                            p.append(time)
                                            p.append(seats)
                                            self.bookings
                                            self.bookings[username].append(p)
                                            print(
                                                f"The Your {seats} seats is booked for Route {route} on {date} at time {time} is Successfully.")
                                            print(
                                                "-----------------------------------------------------------------------------------------------")
                                        else:
                                            p = []
                                            p.append(route)
                                            p.append(date)
                                            p.append(time)
                                            p.append(seats)
                                            self.bookings
                                            self.bookings[username].append(p)
                                            print(
                                                f"The Your {seats} seats is booked for Route {route} on {date} at time {time} is Successfully.")
                                            print(
                                                "-----------------------------------------------------------------------------------------------")
                                    else:
                                        self.bookings[username] = [[route, date, time, seats]]
                                        print(
                                            f"The Your {seats} seats is booked for Route {route} on {date} at time {time} is Successfully.")
                                        print(
                                            "-----------------------------------------------------------------------------------------------")
                                else:
                                    print(
                                        f"No {seats} Seats Available On This time. Only Available {self.schedules[route][date][time]} seats.")
                                    print("-------------------------------------------------------------------------")
                            else:
                                print(f"The Schedule for Route {route} at time {time} is not Available..")
                                print("-------------------------------------------------------------------")
                        else:
                            print(f"The Date {date} is not Available for the Route {route}. ")
                            print("-----------------------------------------------------------")
                    else:
                        print(f"The Route {route} is not Available.")
                        print("--------------------------------------")
                else:
                    print(f"The UserName {username} is Incorrect. Please enter Correct UserName.")
                    print("----------------------------------------------------------------------")
            else:
                print("No Booking for Any Schedule.")
                print("------------------------------")

    def my_bookings(self):
        print("\n------------------------------")
        print("|||      My  Bookings      |||")
        print("------------------------------")
        username = input("Enter Your UserName: ")
        if username in self.logins:
            if self.bookings:
                table = []
                for idx, booking in enumerate(self.bookings.get(username, []), start=1):
                    route = booking[0]
                    date = booking[1]
                    time = booking[2]
                    seats = booking[3]
                    table.append([idx, route, date, time, seats])
                print(tabulate(table, headers=["Sr.No", "Route", "Date", "Time", "Seats"], tablefmt="grid"))
                a = input("If You are Cancel this ticket then Enter The SR.No. of This Ticket: ")
                if a.isdigit():
                    a = int(a)
                    if a >= 1 and a <= len(table):
                        self.bookings[username].pop(a - 1)
                        route = table[a - 1][1]
                        date = table[a - 1][2]
                        time = table[a - 1][3]
                        seats = table[a - 1][4]
                        if route in self.schedules:
                            if date in self.schedules[route]:
                                if time in self.schedules[route][date]:
                                    self.schedules[route][date][time] += seats
                        print("The your Ticket is cancel.")
                        print("-----------------------------")
                        if len(self.bookings[username]) == 0:
                            self.bookings.pop(username)

                    else:
                        print("Enter The Number Between Sr. No.")
                        print("----------------------------------")
                else:
                    print("Your have not canceled any Ticket.")
                    print("------------------------------------")
            else:
                print("You Currently Have No Bookings.")
                print("---------------------------------")
        else:
            print(f"UserName {username} is not correct. Please Enter Correct UserName.")
            print("---------------------------------------------------------------------")

    def inquiry_request(self):
        print("\n--------------------------------------")
        print("|||      Any Inquiry & Request      |||")
        print("---------------------------------------")
        username = input("Enter Your UserName: ")
        if username in self.logins:
            inquiry_and_request = input("Enter Here for Any Inquiry & Request: ")
            if username in self.inquiry_request_data:
                self.inquiry_request_data[username].append(inquiry_and_request)
            else:
                self.inquiry_request_data[username] = [inquiry_and_request]

            print("The Your Inquiry & Request is send Successfully. The Admin Give the reply within 2-3 Days.")
            print("--------------------------------------------------------------------------------------------")
        else:
            print(f"UserName {username} is not correct. Please Enter Correct UserName.")
            print("---------------------------------------------------------------------")

    def view_response_inquiry_request(self):
        print("\n--------------------------------")
        print("|||      View Response       |||")
        print("--------------------------------")
        username = input("Enter Your UserName: ")
        if username in self.logins:
            for inquiry, answer in self.inquiry_request_reply[username].items():
                print("Your Question:", inquiry)
                print("Answer:", answer)
            print("-------------------------------------------------------------------")
        else:
            print(f"UserName {username} is Not Correct. Please enter  Correct UserName.")
            print("----------------------------------------------------------------------")

    def logout(self):
        self.logins.clear()

    def view_bookings(self):
        print("\n-------------------------------")
        print("|||      View Bookings      |||")
        print("-------------------------------")
        if self.bookings:
            for username, routes in self.bookings.items():
                print(f"UserName:{username}")
                table = []
                for idx, booking in enumerate(self.bookings.get(username, []), start=1):
                    route = booking[0]
                    date = booking[1]
                    time = booking[2]
                    seats = booking[3]
                    table.append([idx, route, date, time, seats])
                print(tabulate(table, headers=["Sr.No", "Route", "Date", "Time", "Seats"], tablefmt="grid"))
                print("-----------------------------------------------------------------------")
        else:
            print("No Bookings Available.")
            print("------------------------")

    def update_bookings(self):
        print("\n-------------------------------")
        print("|||      Update Bookings      |||")
        print("-------------------------------")
        if len(self.bookings) > 0:
            for username, routes in self.bookings.items():
                print(f"UserName:{username}")
                table = []
                for idx, booking in enumerate(self.bookings.get(username, []), start=1):
                    route = booking[0]
                    date = booking[1]
                    time = booking[2]
                    seats = booking[3]
                    table.append([idx, route, date, time, seats])
                print(tabulate(table, headers=["Sr.No", "Route", "Date", "Time", "Seats"], tablefmt="grid"))
                a = input("If You are Update this ticket then Enter The SR.No. of This Ticket: ")
                if a.isdigit():
                    a = int(a)
                    if a >= 1 and a <= len(table):
                        self.bookings[username].pop(a - 1)
                        route = table[a - 1][1]
                        date = table[a - 1][2]
                        time = table[a - 1][3]
                        seats = table[a - 1][4]
                        if route in self.schedules:
                            if date in self.schedules[route]:
                                if time in self.schedules[route][date]:
                                    self.schedules[route][date][time] += seats
                                    print("This Ticket is Updated.")
                                    print("-------------------------")


                    else:
                        print("Enter The Number Between Sr.No.")
                        print("----------------------------------")
                else:
                    print("You do not have update any Ticket.")
                    print("------------------------------------")

        else:
            print("No Bookings Available.")
            print("------------------------")
        keys = list(self.bookings.keys())
        for b in keys:
            if len(self.bookings[b]) == 0:
                del self.bookings[b]

    def add_route(self):
        print("\n---------------------------")
        print("|||      Add Route      |||")
        print("---------------------------")
        route = input("Enter Route: ")
        if route in self.schedules:
            print(f"The Route {route} is Already Exists.")
            print("---------------------------------------")
        else:

            time_and_seats = {}
            route_and_date = {}
            date = input("Enter Date to Add: ")
            time = input("Enter Time to Add: ")
            seats = input("Enter Seats to Add: ")
            cost = input("Enter Cost: ")
            time_and_seats[time] = seats
            route_and_date[date] = time_and_seats
            self.schedules[route] = route_and_date
            self.payment[route] = []
            self.payment[route].append(cost)
            print(f"The Route {route} at time {time} is Added.")
            print("---------------------------------------------")

    def remove_route(self):
        print("\n------------------------------")
        print("|||      Remove Route      |||")
        print("------------------------------")
        route = input("Enter route: ")
        if route in self.schedules and route in self.payment:
            self.schedules.pop(route)
            self.payment.pop(route)
            print(f"The Route {route} is Removed.")
            print("--------------------------------")
        else:
            print(f"The Route {route} is not Found.")
            print("----------------------------------")

    def add_schedule(self):
        print("\n------------------------------")
        print("|||      Add Schedule      |||")
        print("------------------------------")
        route = input("Enter route: ")
        if route in self.schedules:
            date = input("Enter Date: ")
            if date in self.schedules[route]:
                time = input("Enter Time to Add: ")
                seats = (input("Enter Seats to Add: "))
                if time in self.schedules[route][date]:
                    print(f"Time {time} is Already Exist")
                    print("-------------------------------")
                else:
                    self.schedules[route][time] = seats
                    print(f"The Schedule for Route {route} is Added.")
                    print("-------------------------------------------")
            else:
                print(f"The Date {date} is Not Found.")
                print("--------------------------------")
        else:
            print(f"The Route {route} is Not Found.")
            print("----------------------------------")

    def edit_schedule(self):
        print("\n-------------------------------")
        print("|||      Edit Schedule      |||")
        print("-------------------------------")
        route = input("Enter route: ")
        if route in self.schedules:
            date = input("Enter Date: ")
            if date in self.schedules[route]:
                old_time = input("Enter old time: ")
                if old_time in self.schedules[route][date]:
                    old_seats = int(input("Enter Old Seats: "))
                    new_time = input("Enter new time: ")
                    seats = int(input("Emter Initial Seats: "))
                    old_seats = self.schedules[route][date].pop(old_time)
                    self.schedules[route][date][new_time] = seats
                    print(f"The Schedule for Route {route} is Updated.")
                    print("---------------------------------------------")
                else:
                    print(f"This time {old_time} is not Found in Schedule.")
                    print("-------------------------------------------------")
            else:
                print(f"The Date {date} is Not Found.")
                print("--------------------------------")
        else:
            print(f"The Route {route} is not Found.")
            print("----------------------------------")

    def remove_schedule(self):
        print("\n---------------------------------")
        print("|||      Remove Schedule      |||")
        print("---------------------------------")
        route = input("Enter route: ")
        if route in self.schedules:
            date = input("Enter Date: ")
            if date in self.schedules[route]:
                time = input("Enter time to remove: ")
                if time in self.schedules[route][date]:
                    self.schedules[route][date].pop(time)
                    print(f"The Schedule {time} is Removed.")
                    print("----------------------------------")
                else:
                    print(f"The time {time} is not Found.")
                    print("--------------------------------")
            else:
                print(f"The Date {date} is not Found.")
                print("--------------------------------")
        else:
            print(f"The Route {route} is not Found.")
            print("----------------------------------")

    def add_date(self):
        print("\n--------------------------")
        print("|||      Add Date      |||")
        print("--------------------------")
        route = input("Enter Route: ")
        if route in self.schedules:
            date = input("Enter Date to Add: ")
            time = input("Enter Time to Add: ")
            seats = input("Enter Seats to Add: ")
            time_and_seats = {}
            time_and_seats[time] = seats
            self.schedules[route][date] = time_and_seats
            print(f"The Date {date} is Added.")
            print("----------------------------")
        else:
            print(f"The Route {route} is not Found.")
            print("----------------------------------")

    def remove_date(self):
        print("\n-----------------------------")
        print("|||      Remove Date      |||")
        print("-----------------------------")
        route = input("Enter Route: ")
        if route in self.schedules:
            date = input("Enter Date To Remove: ")
            if date in self.schedules[route]:
                self.schedules[route].pop(date)
                print(f"The Date {date} is Removed.")
                print("------------------------------")
            else:
                print(f"The Date {date} is not Found.")
                print("--------------------------------")
        else:
            print(f"The Route {route} is not Found.")
            print("----------------------------------")

    def update_cost(self):
        print("\n-----------------------------")
        print("|||      Update Cost      |||")
        print("-----------------------------")
        route = input("Enter Route: ")
        if route in self.schedules and self.payment:
            old_cost = input("Enter Old Cost: ")
            if old_cost in self.payment[route]:
                cost = input("Enter New Cost: ")
                self.payment[route].remove(old_cost)
                self.payment[route].append(cost)
                print(f"For {route} Route, the cost is {cost} Updated")
                print("------------------------------------------------")
            else:
                print("The old Cost is not Found.")
                print("----------------------------")
        else:
            print(f"The Route {route} is not Found.")
            print("----------------------------------")

    def info_inquiry_data(self):
        print("\n-----------------------------------")
        print("|||      Info Inquiry Data      |||")
        print("-----------------------------------")
        if self.inquiry_request_data:
            for username, inquirys in self.inquiry_request_data.items():
                self.inquiry_request_reply[username] = {}
                print(f"Username: {username}")
                for inquiry in self.inquiry_request_data[username]:
                    print(f"Inquiry : {inquiry}")
                    reply = input("Enter the reply for this inquiry: ")
                    if self.inquiry_request_reply[username] == {}:
                        self.inquiry_request_reply[username] = {
                            inquiry: reply
                        }
                    else:
                        self.inquiry_request_reply[username].update({
                            inquiry: reply
                        })
                print("-------------------------------------")

            self.inquiry_request_data.clear()
        else:
            print("The Inquiry & Request Data is not Available.")
            print("----------------------------------------------")


def main():
    schedule_manager = TransportationSchedule()

    while True:
        print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|||||                     WELCOME TO                    |||||")
        print("|||||    PUBLIC TRANSPORT SCHEDULE MANAGEMENT SYSTEM    |||||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        option = input("Enter Option: ")
        if option == "1":
            print("\n*")
            print("***      Admin Login Interface      ***")
            print("*")
            admin_name = input("Enter Admin Name: ")
            password = input("Enter Password: ")
            if admin_name in schedule_manager.admin_name:
                if password in schedule_manager.admin_password:
                    while True:
                        print("\n*")
                        print("***      Admin Interface      ***")
                        print("*")
                        print("1. View Bookings")
                        print("2. Update Bookings")
                        print("3. Add Route")
                        print("4. Remove Route")
                        print("5. Add Schedule")
                        print("6. Edit Schedule")
                        print("7. Remove Schedule")
                        print("8. Add Date")
                        print("9. Remove Date")
                        print("10. Update Cost")
                        print("11. Info Inquiry & Request Data")
                        print("12. Exit")

                        choice = input("\nEnter Choice: ")

                        if choice == "1":
                            schedule_manager.view_bookings()

                        elif choice == "2":
                            schedule_manager.update_bookings()

                        elif choice == "3":
                            schedule_manager.add_route()

                        elif choice == "4":
                            schedule_manager.remove_route()

                        elif choice == "5":
                            schedule_manager.add_schedule()

                        elif choice == "6":
                            schedule_manager.edit_schedule()

                        elif choice == "7":
                            schedule_manager.remove_schedule()

                        elif choice == "8":
                            schedule_manager.add_date()

                        elif choice == "9":
                            schedule_manager.remove_date()

                        elif choice == "10":
                            schedule_manager.update_cost()

                        elif choice == "11":
                            schedule_manager.info_inquiry_data()

                        elif choice == "12":
                            print("Exited And Opened The Main Page.")
                            print("----------------------------------")
                            break

                        else:
                            print("Invalid choice. Enter the number between 1 and 10.")
                            print("----------------------------------------------------")
                else:
                    print("Enter Valid Password.")
                    print("-----------------------")
            else:
                print("Enter Valid Admin Name;")
                print("-------------------------")

        elif option == "2":
            while True:
                print("\n**")
                print("***      User Reg-Log Interface      ***")
                print("")
                print("1. Register")
                print("2. Login")
                print("3. Main Menu")
                choice = input("Enter Choice: ")
                if choice == "1":
                    store_user = schedule_manager.register_user()

                elif choice == "2":
                    login = schedule_manager.login_user()
                    if login == True:
                        while True:
                            print("\n**")
                            print("***      User Interface      ***")
                            print("")
                            print("1. Display All Schedules")
                            print("2. My Bookings")
                            print("3. For Any Inquiry & Request")
                            print("4. View Responses to inquires and Requests")
                            print("5. Exit")
                            choice = input("Please Enter your choice (1-3): ")

                            if choice == "1":
                                displyschedule = schedule_manager.display_all_schedules()

                            elif choice == "2":
                                schedule_manager.my_bookings()

                            elif choice == "3":
                                schedule_manager.inquiry_request()

                            elif choice == "4":
                                schedule_manager.view_response_inquiry_request()

                            elif choice == "5":
                                schedule_manager.logout()
                                print("\nExit And Opened Register-Login Interface.")
                                print("---------------------------------------------")
                                break
                            else:
                                print("Invalid choice. Please enter a number between 1 and 3.")
                                print("--------------------------------------------------------")

                elif choice == "3":
                    print("Exit And Opened The Main Menu.")
                    print("--------------------------------")
                    break
                else:
                    print("Invalid Choice. Please Enter a number between 1 and 3.")
                    print("--------------------------------------------------------")

        elif option == "3":
            print("\n*")
            print("|||     THANK YOU     |||")
            print("*")
            break
        else:
            print("Invalid Option. Please enter a number between 1 and 3.")
            print("--------------------------------------------------------")


if __name__ == "__main__":
    main()


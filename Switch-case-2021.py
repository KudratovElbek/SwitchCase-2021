def switchcase(argument):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(argument, "Invalid day of the week")

#Switch Case in real projects


#01 - Switch Case , In command-line interface (CLI) applications

def handle_command(command):
    match command.split():
        case ["start"]:
            return "Starting the service..."
        case ["stop"]:
            return "Stopping the service..."
        case ["restart"]:
            return "Restarting the service..."
        case ["status"]:
            return "Checking the service status..."
        case _:
            return "Unknown command"

print(handle_command("start"))  # "Starting the service..."
print(handle_command("status")) # "Checking the service status..."

#02- Switch case , Handling HTTP Request Methods in a Web Application

def handle_request(method):
    match method:
        case "GET":
            return "Handling GET request"
        case "POST":
            return "Handling POST request"
        case "PUT":
            return "Handling PUT request"
        case "DELETE":
            return "Handling DELETE request"
        case _:
            return "Method not supported"

print(handle_request("GET"))    # "Handling GET request"
print(handle_request("POST"))   # "Handling POST request"
print(handle_request("PATCH"))  # "Method not supported"

#03- Switch case ,3. Parsing JSON Responses
def parse_response(response):
    match response:
        case {"status": "ok", "data": data}:
            return f"Success: {data}"
        case {"status": "error", "message": message}:
            return f"Error: {message}"
        case _:
            return "Unknown response format"

response1 = {"status": "ok", "data": "Here is your data"}
response2 = {"status": "error", "message": "Something went wrong"}

print(parse_response(response1))  # "Success: Here is your data"
print(parse_response(response2))  # "Error: Something went wrong"




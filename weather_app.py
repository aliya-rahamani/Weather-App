import PySimpleGUI as sg, requests

def createGUI():
    left_col = [
        [sg.Text("Enter City's name:")],
        [sg.In(key="-input-")],
        [sg.Button("GO")]
    ]
    right_col = [
        [sg.Text("Weather in the City:"),sg.Text(size=(10,1),key="-city-")],
        [sg.Text(key ="-output-", size=(45,15), background_color = "#8CC3BB")]

    ]
    layout = [
        [sg.Column(left_col, element_justification='l'),
    sg.VSeparator(),
    sg.Column(right_col, element_justification='c')]

    ]

    window = sg.Window('Weather GUI App', layout, resizable= True)

    while True:
        event,values = window.read()

        if event== sg.WIN_CLOSED:
            break

        if event == "GO":
            if values["-input-"]:
                getDataFromApi(values["-input-"],window)


def getDataFromApi(city,window):
     window["-city-"].update(city)
     url = f"http://api.weatherapi.com/v1/current.json?key=c17816652c0f4adaa2783656201708&q={city}"
     res = requests.get(url).json()

     data = {
         "City" : res["location"]["name"],
         "Region":res["location"]["region"],
         "Country":res["location"]["country"],
         "Temp *C":res["current"]["temp_c"],
         "Temp *F": res["current"]["temp_f"],
         "Condition": res["current"]["condition"]["text"],
     }

     output = ""


     for x,y in data.items():
         output += f"{x}:   {y}  \n"
     print(output)

     window["-output-"].update(output)

if __name__ == "__main__":
    createGUI()

import json
import PySimpleGUI as sg    
def read():
    with open("data/data.json", "r") as f:
        return json.load(f)
students = []
data = read()
for i in data['Students Info']:
    students.append(i)
tab1_layout =  [[sg.T('Class Details', font="Acme 40")],
                [sg.T(f"Class: {data['Class']}", font="Acme 14", key = "class", size=(30, 0))],
                [sg.T(f"Class Teacher: {data['Teacher']}", font="Acme 14", key = "teacher", size=(30, 0))],
                [sg.T(f"Total Students: {len(data['Students Info'])}", font="Acme 14")]] 
edit_layout = [[sg.T("Edit Class Details", font="Acme 40")],
               [sg.T("Class"), sg.Input("", size=((25,1)), key="classname"), sg.Button("Save", size=(10,0), key ="saveclassname")],
               [sg.T("Class Teacher"), sg.Input("", size=((25,1)), key="teachername"), sg.Button("Save", size=(10,0), key ="saveteachername")]]

tab2_layout = [[sg.T('Student Details', font="Acme 40")],
               [sg.T("Select Student: ", font="Acme 11"), sg.Combo(values = students,readonly=True, size = (20, 1), font="Acme 11", key= "selectstudent"), sg.Button("Search", font="Acme 11", key="searchstudent")],
               [sg.T(f'Roll No.: ', key="rollno", size = (30, 1))],
               [sg.T(f'Phone No.: ', key="phoneno", size = (30, 1))]]    

add_student = [[sg.T('Add Student', font="Acme 40")],
               [sg.T('Name: ', font="Acme 11"), sg.Input("", font="Acme 11", size=(20, 20), key="nametoadd")],
               [sg.T('Roll No.: ', font="Acme 11"), sg.Input("", font="Acme 11", size=(20, 20), key="rollnotoadd")],
               [sg.T('Phone No.: ', font="Acme 11"), sg.Input("", font="Acme 11", size=(20, 20), key="phonenotoadd")],
               [sg.Button("Add", key="addstudent")],
               [sg.Input("", size=(20,1)) , sg.FileBrowse(file_types=(("Custom Files", "*.xls"),))]]

manage_students = [[sg.T("Manage Students", font="Acme 40")],
                   [sg.T("Delete Student", font="Acme 15")],
                   [sg.Combo(values = students,readonly=True, size = (20, 1), font="Acme 11", key= "selectstudentfordelete"), sg.Button("Delete", key="deletestudent")]]

layout = [[sg.TabGroup([[sg.Tab('Class Details', tab1_layout), sg.Tab("Edit", edit_layout),sg.Tab('Student Details', tab2_layout), sg.Tab("Add Student", add_student), sg.Tab("Manage Students", manage_students)]])]]    

window = sg.Window('Class Manager', layout, default_element_size=(12,1))    

while True:    
    event, values = window.read()   
    if event == sg.WIN_CLOSED:  
        break 
    elif event == "saveclassname":
        data = read()
        data["Class"] = values['classname']
        with open("data/data.json", "w") as f:
            json.dump(data, f, indent=4)
        data=read()
        window['class'].update(f"Class: {data['Class']}")
    elif event == "saveteachername":
        data = read()
        data["Teacher"] = values['teachername']
        with open("data/data.json", "w") as f:
            json.dump(data, f, indent=4)
        data=read()
        window['teacher'].update(f"Class Teacher: {data['Teacher']}")
    elif event == "searchstudent":
        # print(values['selectstudent'])
        try:
            # print(data['Students Info'][values['selectstudent']])
            window['rollno'].update(f"Roll No.: {data['Students Info'][values['selectstudent']]['Roll No.']}")
            window['phoneno'].update(f"Phone No.: {data['Students Info'][values['selectstudent']]['Phone No.']}")
        except:
            pass
    elif event == "addstudent":
        # print(values['nametoadd']+values['rollnotoadd']+values['phonenotoadd'])
        data=read()
        data['Students Info'][values['nametoadd']] = {"Roll No.": values['rollnotoadd'], "Phone No.": values['phonenotoadd']}
        with open("data/data.json", "w") as f:
            json.dump(data, f, indent=4)
        students = []
        data = read()
        for i in data['Students Info']:
            students.append(i)
        window['selectstudent'].update(values=students,readonly=True, size = (20, 1), font="Acme 11")
        window['selectstudentfordelete'].update(values=students,readonly=True, size = (20, 1), font="Acme 11")
    elif event == "deletestudent":
        data=read()
        data['Students Info'].pop(values['selectstudentfordelete'])
        with open("data/data.json", "w") as f:
            json.dump(data, f, indent=4)
        students = []
        data = read()
        for i in data['Students Info']:
            students.append(i)
        window['selectstudent'].update(values=students,readonly=True, size = (20, 1), font="Acme 11")
        window['selectstudentfordelete'].update(values=students,readonly=True, size = (20, 1), font="Acme 11")
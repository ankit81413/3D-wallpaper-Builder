import eel


# Set web files folder
eel.init('web')

@eel.expose
def idex():
    # Define the functionality of idex
    print("idex function called")

@eel.expose
def choosemode(mode):
    global gmode
    if mode == "save":
        gmode = "save"
        idex()  # Call the idex function
        print("Save mode")
    else:
        gmode = "mass_production"
        print("Mass production mode")

# Calling choosemode to demonstrate idex function call
# choosemode("save")
eel.start('choose_mode.html', size=(400, 300))

import time
import os

stepsText = ["tleap","minimization (1/2)","minimization (2/2)","heat (1/2)","heat (2/2)","equilibrium","production (10ns)"]

def read_MDinfo(file_path):
    # Reads the file and extracts the required timing information
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            timing_info = lines[10:26]  # Modify this line based on where the timing info is located
        return timing_info
    except FileNotFoundError:
        return "mdinfo is not generated quite yet!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def read_status(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            #currentFolder = content[0]
            #currentStep = content[1]
        return content
    except FileNotFoundError:
        return ["files not generated quite yet", "files not generated quite yet"]
    except Exception as e:
        return f"An error occurred: {str(e)}"

def read_queue(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        return "files not generated quite yet"
    except Exception as e:
        return f"An error occurred: {str(e)}"


def signature():
    ascii_art = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣬⠷⣶⡖⠲⡄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠸⣿⡀⠀⡁⠈⠙⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠉⠣⠬⢧⠀⠀⠀⠀⠈⠻⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⡴⠃⠀⠀⢠⣴⣿⡿⠀⠀⠀⠐⠋⠀⠀⠀⠀⠀⠀⠘⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⡴⠋⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠒⠓⠛⠓⠶⠶⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⡞⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢷⡄⠀⠀⠀⠀⠀⠀
    ⢻⣇⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀
    ⠀⠻⣟⠋⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀
    ⠀⠀⠀⠉⠓⠒⠊⠉⠉⢸⡙⠇⠀⠀⠀dont worry be capy⠀⠀ ⠀⠀⡀⠀⠀⠀⠀⠘⣆⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⠀⠀⢻⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⣧⡀⠀⠀⢀⡄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠇⠀⠀⠀⠀⠀⠀⢣⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡧⢿⡀⠚⠿⢻⡆⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠘⡆
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠈⢹⡀⠀⠀⠀⠀⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⢷⣾⠀⠸⡷⠀⠀⠀⠘⡿⠂⠀⠀⠀⢀⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠳⢼⣧⡀⠀⠀⢶⡼⠦⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⡎⣽⠿⣦⣽⣷⠿⠒⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⣴⠃⡿⠀⠀⢠⠆⠢⡀⠀⠀⠀⠈⢧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣠⠏⠀⣸⢰⡇⠀⢠⠏⠀⠀⠘⢦⣀⣀⠀⢀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠿⢯⣤⣆⣤⣯⠼⠀⠀⢸⠀⠀⠀⠀⠀⣉⠭⠿⠛⠛⠚⠟⡇⠀⠀⣀⠀⢀⡤⠊⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⢸⣷⣶⣤⣦⡼⠀⠀⠀⣴⣯⠇⡀⣀⣀⠤⠤⠖⠁⠐⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⠁⢋⡀⠀⠀⠀⠀⣛⣛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(ascii_art)

def clear_console():
    # Clears the console output
    os.system('cls' if os.name == 'nt' else 'clear')

#main execution area:
if __name__ == "__main__":
    wait_sec = 1
    animation_counter_threshold = 5
    animation_counter = 1
    info_refresh_counter_threshold = 60
    info_refresh_counter = 0
    current_directory = os.getcwd()

    
    
    current_folder = read_status(current_directory + "/status.txt")[0].strip("\n")
    holdDisplayProgress = current_folder == "hold"
    current_step = read_status(current_directory + "/status.txt")[1].strip("\n")
    timimg_info = read_MDinfo(current_folder + "/mdinfo")
    queue = read_queue(current_directory + "/queue.txt")

    
    while True:
        


        if animation_counter == animation_counter_threshold:
            animation_counter = 1

        clear_console()
        if not holdDisplayProgress:
            if info_refresh_counter == info_refresh_counter_threshold:
                current_folder = read_status(current_directory + "/status.txt")[0].strip("\n")
                current_step = read_status(current_directory + "/status.txt")[1].strip("\n")
                timimg_info = read_MDinfo(current_folder + "/mdinfo")
                queue = read_queue(current_directory + "/queue.txt")
                info_refresh_counter = 0
            
            #timing info section
            if len(timimg_info) == 0:
                print("Timing info will be available once we are in the heating step!\nPlease wait patiently" + animation_counter * ".")
                info_refresh_counter_threshold = 10
            else:
                if timimg_info == "mdinfo is not generated quite yet!":
                    print(timimg_info +  + animation_counter * ".")
                    info_refresh_counter_threshold = 10
                else:
                    for lines in timimg_info:
                        lines = lines.strip()
                        if "Current Timing" in lines:
                            lines += " [insert current step with name of pose]"
                        print(lines.strip())
                    info_refresh_counter_threshold = 60
            #current status section
            print("\n"+"Steps in MD:")
            for text in stepsText:
                if (text == current_step) & (animation_counter % 2 == 0):
                    print("\t"+text + "  <")
                else:
                    print("\t"+text)
            #queue section
            print("\n"+"Folder queue:")
            for directory in queue:
                if (current_folder == directory.strip("\n")) & (animation_counter % 2 == 0):
                    print("\t"+directory.strip("\n") + "  <")
                else:
                    print("\t"+directory.strip("\n"))
        else:
            print("FILE CONVERSION IN PROGRESS!!")
            print("Please wait for as the pdbqt are converted to mol2 for tleap" + animation_counter * "!")
            current_folder = read_status(current_directory + "/status.txt")[0].strip("\n")
            holdDisplayProgress = current_folder == "hold"
            current_step = read_status(current_directory + "/status.txt")[1].strip("\n")
            info_refresh_counter = 0

        #capy
        signature()
        #animation and refresh math
        animation_counter += 1
        info_refresh_counter += 1
        if info_refresh_counter == info_refresh_counter_threshold:
            print("info updating...")
        else:
            print() #print(info_refresh_counter) for debug
        time.sleep(wait_sec)

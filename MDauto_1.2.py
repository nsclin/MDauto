import os
import subprocess
from datetime import datetime

stepNumber = 0
stepsText = ["tleap","minimization (1/2)","minimization (2/2)","heat (1/2)","heat (2/2)","equilibrium","production (10ns)"]

def returnCurrentDate():
    return str(datetime.now().date())

def returnCurrentTime():
    return str(datetime.now().time())

def broadcast(inputString):
    broadcastTime = returnCurrentTime()
    broadcastTime = str(broadcastTime)
    emphasize = ""
    
    if len(inputString) > len(broadcastTime):
        for i in range(len(inputString) - len(broadcastTime)):
            if i % 2 == 0:
                broadcastTime += " "
            else:
                broadcastTime = " " + broadcastTime
        for x in inputString:
            emphasize += "-"
    else:
        for i in range(len(broadcastTime) - len(inputString)):
            inputString += " "
        for x in broadcastTime:
            emphasize += "-"
    upperemphasize = "/" + emphasize + "\\"
    bottomemphasize = "\\" + emphasize + "/"
    print("\n\n" + upperemphasize + "\n" + "|" + inputString + "|" + "\n" + "|" + broadcastTime + "|"  + "\n" + bottomemphasize + "\n\n")

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

def folders_with_required_extensions_1(directory):
    required_extensions = {'.pdbqt'}
    matching_folders = []

    # Walk through all directories
    for root, dirs, files in os.walk(directory):
        # Create a set of file extensions present in the current folder
        extensions_in_folder = {os.path.splitext(file)[1] for file in files}

        # Check if the current folder contains all required extensions
        if required_extensions.issubset(extensions_in_folder):
            matching_folders.append(root)

    return matching_folders

def folders_with_required_extensions_2(directory):
    required_extensions = {'.mol2', '.frcmod','.pdb'}
    matching_folders = []

    # Walk through all directories
    for root, dirs, files in os.walk(directory):
        # Create a set of file extensions present in the current folder
        extensions_in_folder = {os.path.splitext(file)[1] for file in files}

        # Check if the current folder contains all required extensions
        if required_extensions.issubset(extensions_in_folder):
            matching_folders.append(root)

    return matching_folders

def tleap(folder):
    statusDocument(folder, "tleap")
    for file in os.listdir(folder):
        if file.endswith('ligand.mol2'):
            mol2_file = file
        elif file.endswith('ligand.frcmod'):
            frcmod_file = file
        elif file.endswith('AF_PTB_ren_prep.pdb'):
            pdb_file = file

        # Ensure all necessary files are found
    if mol2_file and frcmod_file and pdb_file:
        tleap_input = f"""source leaprc.protein.ff19SB
            source leaprc.gaff
            source leaprc.water.opc

            prot = loadpdb {pdb_file}
            fmod = loadamberparams {frcmod_file}
            lig = loadmol2 {mol2_file}

            complex = combine {{prot lig}}
            savepdb complex complex_dry.pdb
            solvatebox complex OPCBOX 15
            addions complex Na+ 0
            addions complex Cl- 0
            saveamberparm complex complex.prmtop complex.inpcrd
            quit
            """
        tleap_input_file = os.path.join(folder, 'tleap.in')
            
        # Write the tleap input to a file
        with open(tleap_input_file, 'w') as f:
            f.write(tleap_input)

        print(f"Running tleap in folder: {folder}")
            
        # Run tleap using subprocess
        try:
            subprocess.run(['tleap', '-f', tleap_input_file], cwd=folder, check=True)
            print(f"tleap successfully executed in {folder}")
        except subprocess.CalledProcessError as e:
            print(f"Error running tleap in {folder}: {e}")
    else:
        print(f"Missing required files in folder: {folder}")

def createDocuments(folder):
    min1 = os.path.join(folder, 'min1.in')
    min1_input = "Minimize heavy atoms\n &cntrl\n  imin=1,\n  ntx=1,\n  irest=0,\n  maxcyc=10000,\n  ncyc=1000,\n  ntpr=100,\n  ntwx=0,\n  cut=10.0,\n  ntr=1,\n  restraint_wt=10.0,\n  restraintmask='@CA,C,O,N&!:WAT',\n /\n"
    with open(min1, 'w') as f:
        f.write(min1_input)
    
    min2 = os.path.join(folder, 'min2.in')
    min2_input = "Minimize everything\n &cntrl\n  imin=1,\n  ntx=1,\n  irest=0,\n  maxcyc=100000,\n  ncyc=10000,\n  ntpr=100,\n  ntwx=0,\n  cut=10.0,\n /\n"
    with open(min2, 'w') as f:
        f.write(min2_input)

    heat1 = os.path.join(folder, 'heat1.in')
    heat1_input = "Heat step 1\n &cntrl\n  imin=0,\n  ntx=1,\n  irest=0,\n  tol=0.0000001,\n  nstlim=2000000,\n  dt=0.002,\n  ntf=2,\n  ntc=2,\n  tempi=10.0,\n  temp0=300.0,\n  ntpr=5000,\n  ntwx=5000,\n  ntwr=5000,\n  cut=10.0,\n  ntb=1,\n  ntp=0,\n  ntt=3,\n  gamma_ln=5.0,\n  nmropt=1,\n  ig=-1,\n  iwrap=1,\n  ntr=1,\n  restraint_wt=1.0,\n  restraintmask='@CA,C,O,N&!:WAT',\n /\n&wt type='TEMP0', istep1=0, istep2=2000000, value1=10.0, value2=300.0 /\n&wt type='END' /\n"
    with open(heat1, 'w') as f:
        f.write(heat1_input)

    heat2 = os.path.join(folder, 'heat2.in')
    heat2_input = "Heat step 2\n &cntrl\n  imin=0,\n  ntx=5,\n  irest=1,\n  tol=0.0000001,\n  nstlim=3000000,\n  dt=0.002,\n  ntf=2,\n  ntc=2,\n  ntt=3,\n  tempi=300.0,\n  temp0=300.0,\n  ntpr=5000,\n  ntwx=5000,\n  ntwr=5000,\n  cut=10.0,\n  ntb=1,\n  ntp=0,\n  gamma_ln=5.0,\n  nmropt=1,\n  ig=-1,\n  iwrap=1,\n  ntr=1,\n  restraint_wt=1.0,\n  restraintmask='@CA,C,O,N&!:WAT',\n /\n&wt type='TEMP0', istep1=0, istep2=3000000, value1=300.0, value2=300.0 /\n&wt type='END' /\n"
    with open(heat2, 'w') as f:
        f.write(heat2_input)

    equil = os.path.join(folder, 'equil.in')
    equil_input = "Equilibrate\n &cntrl\n  imin=0,\n  ntx=5,\n  irest=1,\n  tol=0.0000001,\n  nstlim=5000000,\n  dt=0.002,\n  ntf=2,\n  ntc=2,\n  ntb=2,\n  ntp=1,\n  pres0=1.0,\n  taup=1.0,\n  ntt=3,\n  temp0=300.0,\n  ntpr=5000,\n  ntwx=5000,\n  ntwr=5000,\n  cut=10.0,\n  gamma_ln=1.0,\n  ig=-1,\n  iwrap=1,\n  ntr=1,\n  restraint_wt=0.1,\n  restraintmask='@CA,C,O,N&!:WAT',\n /\n"
    with open(equil, 'w') as f:
        f.write(equil_input)

    prod = os.path.join(folder, 'prod.in')
    prod_input = "Production conventional MD\n &cntrl\n  imin=0,\n  ntx=5,\n  irest=1,\n  tol=0.0000001,\n  nstlim=5000000,\n  dt=0.002,\n  ntf=2,\n  ntc=2,\n  ntb=2,\n  ntp=1,\n  pres0=1.0,\n  taup=1.0,\n  ntt=3,\n  temp0=300.0,\n  ntpr=5000,\n  ntwx=5000,\n  ntwr=5000,\n  cut=10.0,\n  gamma_ln=1.0,\n  ig=-1,\n  iwrap=1,\n /\n"
    with open(prod, 'w') as f:
        f.write(prod_input)

def md10ns(folder):
    original_folder = os.getcwd()
    chunkedDownFolder = ""
    parts = folder.split(os.sep)
    chunkedDownFolder = "\\".join([parts[-2], parts[-1]])

    try:
        os.chdir(folder)
        with open("complex.pdb", "w") as output_file:
            subprocess.run(["ambpdb", "-p", "complex.prmtop", "-c", "complex.inpcrd",], stdout=output_file)
        broadcast("tleap complete @ " + chunkedDownFolder)
        statusDocument(folder, "minimization (1/2)")
        subprocess.run(["pmemd.cuda", "-O", "-i", "min1.in", "-o", "min1.out", "-p", "complex.prmtop", "-c", "complex.inpcrd", "-r", "min1.rst7", "-ref", "complex.inpcrd"])
        broadcast("minimization (1/2) @ " + chunkedDownFolder)
        statusDocument(folder, "minimization (2/2)")
        subprocess.run(["pmemd.cuda", "-O", "-i", "min2.in", "-o", "min2.out", "-p", "complex.prmtop", "-c", "min1.rst7", "-r", "min2.rst7", "-ref", "min1.rst7"])
        broadcast("minimization (2/2) @ " + chunkedDownFolder)
        statusDocument(folder, "heat (1/2)")
        subprocess.run(["pmemd.cuda", "-O", "-i", "heat1.in", "-o", "heat1.out", "-p", "complex.prmtop", "-c", "min2.rst7", "-r", "heat1.rst7", "-ref", "min2.rst7"])
        broadcast("heat (1/2) @ " + chunkedDownFolder)
        statusDocument(folder, "heat (2/2)")
        subprocess.run(["pmemd.cuda", "-O", "-i", "heat2.in", "-o", "heat2.out", "-p", "complex.prmtop", "-c", "heat1.rst7", "-r", "heat2.rst7", "-ref", "heat1.rst7"])
        broadcast("heat (2/2) @ " + chunkedDownFolder)
        statusDocument(folder, "equilibrium")
        subprocess.run(["pmemd.cuda", "-O", "-i", "equil.in", "-o", "equil.out", "-p", "complex.prmtop", "-c", "heat2.rst7", "-r", "equil.rst7", "-ref", "heat2.rst7"])
        broadcast("equilibrium complete @ " + chunkedDownFolder)
        statusDocument(folder, "production (10ns)")
        subprocess.run(["pmemd.cuda", "-O", "-i", "prod.in", "-o", "prod.out", "-p", "complex.prmtop", "-c", "equil.rst7", "-r", "prod.rst7", "-x", "prod.nc", "-inf", "prod.mdinfo"])
        broadcast("production (10ns) complete @ " + chunkedDownFolder)
        
    finally:
        os.chdir(original_folder)

def statusDocument(folder, step):
    with open(master_folder+"/status.txt", "w") as file:
        file.write(folder + "\n" + step + "\n")
    
    broadcast(step + " start")
    

def queueDocument(listOfDir):
    with open("queue.txt", "w") as file:
        for folder in listOfDir:
            file.write(folder + "\n")

def inputFilePrep(folder):
    for file in os.listdir(folder):
        if file.endswith('.pdbqt'):
            pdbqt = file
    os.chdir(folder)
    subprocess.run(["obabel", "-ipdbqt", pdbqt, "-omol2", "-O", "ligand_hadded.mol2", "-h"])
    print(pdbqt + " -> " + "ligand_hadded.mol2")
    subprocess.run(['antechamber', '-i', 'ligand_hadded.mol2', '-fi', 'mol2', '-o', 'ligand.mol2', '-fo', 'mol2', '-pf', 'y', '-nc', '0', '-c', 'bcc'])
    subprocess.run(['parmchk2', '-i', 'ligand.mol2', '-f', 'mol2', '-o', 'ligand.frcmod'])


#main execution area:
if __name__ == "__main__":
    #signal start
    master_folder = os.getcwd()
    broadcast("MD Mass Production 10ns Start")
    statusDocument("hold", "hold") #wait until status is properly updated to display progress
    #check right ingredients
    
    foldersRaw = folders_with_required_extensions_1(os.getcwd())
    #print(foldersRaw)
    #cooking ingrediants
    for folder in foldersRaw:
        inputFilePrep(folder)
    os.chdir("..")
    #broadcast("input files cooked")
    #double check if properly cooked
    foldersCooked = folders_with_required_extensions_2(os.getcwd())
    print(foldersCooked)
    queueDocument(foldersCooked)

    for folder in foldersCooked:
        #print()
        tleap(folder)
        createDocuments(folder)
        md10ns(folder)
        signature()
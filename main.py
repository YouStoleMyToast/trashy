goalCubes = []
GoalCubes = {}
colors = ["white","green","red","blue","orange","yellow"]
moveSets = {}

class Config:
	def __init__(self):
		self.enable_prompt = 0
		self.apply_solution = 1
		self.cube_display = 3
		self.depth_limit = 6
		self.generation_limit = "1e7"
		self.storage_limit = "1e7"
		self.solution_display = 1
	                
	def set_enable_prompt(self,value):
		self.enable_prompt = value

	def set_apply_solution(self,value):
		self.apply_solution = value

	def set_cube_display(self,value):
		self.cube_display = value

	def set_depth_limit(self,value):
		self.depth_limit = value
                
	def set_generation_limit(self,value):
		self.generation_limit = value
	
	def set_storate_limit(self,value):
                self.storage_limit = "1e7"

	def set_solution_display(self,value):
                self.solution_display = value

	def get_enable_prompt(self):
		return self.enable_prompt
	        
	def get_apply_solution(self):
		return self.apply_solution
               
	def get_cube_display(self):
		return self.cube_display

	def get_depth_limit(self):
		return self.depth_limit
                
	def get_generation_limit(self):
		return self.generation_limit

	def get_storage_limit(self):
		return self.storage_limit

	def get_solution_display(self):
		return self.solution_display 

config = Config() ##initialize config class here

def handleConfigCommand(command): ## recieves list of input -example: [config,depth_limit,=,6]
	if command[1] == "depth_limit":
		config.set_depth_limit(command[3])
	elif command[1] == "apply_solution":
		config.set_apply_solution(command[3])
	elif command[1] == "cube_display":
		config.set_cube_display(command[3])
	elif command[1] == "generation_limit":
		config.set_generation_limit(command[3])
	elif command[1] == "storage_limit":
		config.set_generation_limit(command[3])
	elif command[1] == "solution_display":
		config.set_solution_display(command[3])
	elif command[1] == "enable_prompt":
		config.set_enable_prompt(command[3])
	else:
		print("\nNo Case Found For Suggested Action...\n")
		return

def addGoalCube():
    cube = ""
    description = input("Goal Cube Description:\t")
    for i in range(len(colors)):
        side = ""
        while len(side) != 9:
            side = input("What Is The "+colors[i] +" Side")
            cube += side + " "
    GoalCubes[len(GoalCubes)] = [description,cube]
    return


def addMoves():
    name = input("Specify Move Name:\t")
    move = input("Specify Move:\t")
    moveSets[name] = move


def loadMoves():
    fin = open(input("Specify Filename:\t"),"r")
    for line in fin:
        move = ""
        line = line.strip()
        line = line.split()
        for i in range(1,len(line)):
            move += " " + line[i]
        moveSets[line[0]] = move

def loadGoalCubes():
    fin = open(input("specify filename: "),"r")
    for line in fin:
        line = line.strip()
        line = line.split("/")
        GoalCubes[len(GoalCubes)] = line
    fin.close()

def displayCubes():
    for key in GoalCubes:
        print("[",key,"]","\t",GoalCubes[key][0],"\n",GoalCubes[key][1])
    return

def displayMoves():
    for key in moveSets:
        print(key + ":\t" + moveSets[key])

def writeGoals():
    fout = open(input("Specify Filename:\t"),"w+")
    for key in GoalCubes:
        fout.write(GoalCubes[key][0] + "/" + GoalCubes[key][1])
    fout.close()

def writeMoves():
    fout = open(input("Specify Filename:\t"),"w+")
    for key in moveSets:
        fout.write(key + " " + moveSets[key])
    fout.close()

def writeCommandFile():
    fout = open(input("Specify Filename:\t"),"w+")
    print("Command File Menu\n\"Help\" For Options")
    while True:
        command = input("Specify Next To Write:\t")
        if command.startswith("goal"):
            displayCubes()
            index = input("Specify Goal To Write:\t")
            index = index.split()
            string = "init goal "
            for i in range(len(index)):
                string += GoalCubes[int(index[i])][1] + " "
            fout.write(string + "\n")
        elif command.startswith("move"):
            displayMoves()
            name = input("Specify Move To Write:\t")
            fout.write("moves " + name + moveSets[name])
        elif command.startswith("config"):
            fout.write("\n\nconfig enable_prompt = " + str(config.get_enable_prompt()) + "\n")
            fout.write("config apply_solution = " + str(config.get_apply_solution()) + "\n")	
            fout.write("config cube_display = " + str(config.get_cube_display()) + "\n")
            fout.write("config depth_limit = " + str(config.get_depth_limit()) + "\n")
            fout.write("config generation_limit = " + str(config.get_generation_limit()) + "\n")
            fout.write("config storage_limit = " + str(config.get_storage_limit()) + "\n")
            fout.write("config solution_display = " + str(config.get_solution_display()) + "\n\n\n")
        elif command.startswith("init"):
            displayCubes()
            fout.write("init cube ",GoalCubes[input("Select Cube To Initialize:\t")][1])
        elif command.startswith("quit") or command.startswith("exit") or command.startswith("done"):
            fout.close()
            return
        else:
            print("Invalid Command")

    

def main():
    while True:
        command = input("Rubiks Command Script Builder\n\"Help\"\tFor Available Options\n")
        commands = command.split()
        if commands[0] == "help":
            print("Help Menu:\n")
        elif commands[0] == "add":
            if commands[1].startswith("goal") or commands[1].startswith("cube"):
                addGoalCube()
            elif commands[1] == "moves":
                addMoves()
        elif commands[0] == "load":
            if commands[1].startswith("goal") or commands[1].startswith("cube"):
                loadGoalCubes()
            elif commands[1] == "moves":
                loadMoves()
        elif commands[0] == "write":
            if commands[1] == "moves":
                writeMoves()
            elif commands[1].startswith("goal") or commands[1].startswith("cube"):
                writeGoals()
            if commands[1] == "command":
                writeCommandFile()
        elif commands[0] == "display":
            if commands[1].startswith("goal") or commands[1].startswith("cube"):
                displayCubes()
            if commands[1] == "moves":
                displayMoves()
        elif commands[0] == "config":
        	handleConfigCommand(commands)
        elif commands[0].startswith("exit") or commands[0].startswith("quit"):
            return
        else:
            print("Invalid Command Cuhz")

main()
        
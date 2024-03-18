
#	@@@@@@@  @@@  @@@   @@@@@@   @@@  @@@  @@@  @@@   @@@@@@      @@@@@@@@   @@@@@@   @@@@@@@      @@@  @@@   @@@@@@   @@@  @@@  @@@   @@@@@@@@
#	@@@@@@@  @@@  @@@  @@@@@@@@  @@@@ @@@  @@@  @@@  @@@@@@@      @@@@@@@@  @@@@@@@@  @@@@@@@@     @@@  @@@  @@@@@@@   @@@  @@@@ @@@  @@@@@@@@@
#	  @@!    @@!  @@@  @@!  @@@  @@!@!@@@  @@!  !@@  !@@          @@!       @@!  @@@  @@!  @@@     @@!  @@@  !@@       @@!  @@!@!@@@  !@@
#	  !@!    !@!  @!@  !@!  @!@  !@!!@!@!  !@!  @!!  !@!          !@!       !@!  @!@  !@!  @!@     !@!  @!@  !@!       !@!  !@!!@!@!  !@!
#	  @!!    @!@!@!@!  @!@!@!@!  @!@ !!@!  @!@@!@!   !!@@!!       @!!!:!    @!@  !@!  @!@!!@!      @!@  !@!  !!@@!!    !!@  @!@ !!@!  !@! @!@!@
#	  !!!    !!!@!!!!  !!!@!!!!  !@!  !!!  !!@!!!     !!@!!!      !!!!!:    !@!  !!!  !!@!@!       !@!  !!!   !!@!!!   !!!  !@!  !!!  !!! !!@!!
#	  !!:    !!:  !!!  !!:  !!!  !!:  !!!  !!: :!!        !:!     !!:       !!:  !!!  !!: :!!      !!:  !!!       !:!  !!:  !!:  !!!  :!!   !!:
#	  :!:    :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!      !:!      :!:       :!:  !:!  :!:  !:!     :!:  !:!      !:!   :!:  :!:  !:!  :!:   !::
#	   ::    ::   :::  ::   :::   ::   ::   ::  :::  :::: ::       ::       ::::: ::  ::   :::     ::::: ::  :::: ::    ::   ::   ::   ::: ::::
#	   :      :   : :   :   : :  ::    :    :   :::  :: : :        :         : :  :    :   : :      : :  :   :: : :    :    ::    :    :: :: :


#	@@@@@@@@   @@@@@@    @@@@@@   @@@ @@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@  @@@@@@@  @@@
#	@@@@@@@@  @@@@@@@@  @@@@@@@   @@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@
#	@@!       @@!  @@@  !@@       @@! !@@  !@@       @@!  @@@  @@!  @@@  @@!         @@!    @@!
#	!@!       !@!  @!@  !@!       !@! @!!  !@!       !@!  @!@  !@!  @!@  !@!         !@!    !@
#	@!!!:!    @!@!@!@!  !!@@!!     !@!@!   !@!       @!@!!@!   @!@!@!@!  @!!!:!      @!!    @!@
#	!!!!!:    !!!@!!!!   !!@!!!     @!!!   !!!       !!@!@!    !!!@!!!!  !!!!!:      !!!    !!!
#	!!:       !!:  !!!       !:!    !!:    :!!       !!: :!!   !!:  !!!  !!:         !!:
#	:!:       :!:  !:!      !:!     :!:    :!:       :!:  !:!  :!:  !:!  :!:         :!:    :!:
#	 :: ::::  ::   :::  :::: ::      ::     ::: :::  ::   :::  ::   :::   ::          ::     ::
#	: :: ::    :   : :  :: : :       :      :: :: :   :   : :   :   : :   :           :     :::


import subprocess, sys, time, zipfile, shutil, os, datetime, glob, config

# Important global variables
args = sys.argv

bindings = config.config["bindings"]

config = config.config

# ANSI color codes
class Colors:
	RESET = "\033[0m"
	RED = "\033[91m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	BLUE = "\033[94m"
	PURPLE = "\033[95m"
	CYAN = "\033[96m"
	WHITE = "\033[97m"
	GRAY = "\033[90m"

print(f"{Colors.CYAN}====== Easycraft v1.0 - A Minecraft Java Server Manager By hw2007 ======{Colors.RESET}")

# Check if a certain screen session exists
def screen_session_exists(session):
	try:
		# Run the screen -list command and capture its output
		output = str(subprocess.run(['screen', '-list'], stdout=subprocess.PIPE))

		# This simply searches for a term in the output string
		if f".{session}" in output:
			return True
		else:
			return False

	except: # If the command runs into an error, we assume the session doesn't exist
		return False

# Runs a command in a screen session
def run_in_screen(session, command):
	try:
		# Runs the command in desired screen session
		subprocess.run(["screen", "-S", session, '-X', "stuff", command + "\n"], check = True)
	except:
		print(f"Failed to run '{command}' in screen session '{session}'")

# Writes stylized output to the terminal
def output(type, message):
	if type == "info":
		print(f"{Colors.GRAY}[INFO] {message}{Colors.RESET}")
	elif type == "error":
		print(f"{Colors.RED}[ERROR] {message}{Colors.RESET}")
	elif type == "done":
		print(f"{Colors.YELLOW}[DONE] {message}{Colors.RESET}")

# Gets the value of a command-line flag
def check_for_flag(flag):
	if flag in args:
		return True
	else:
		return False

def get_flag_value(flag):
	if not check_for_flag(flag):
		return None

	value = args[args.index(flag) + 1]
	return value


# Start the server
def start_server(server):
	if not screen_session_exists(server): # Make a new screen session if one doesn't already exist
		output("info", f"Starting screen session '{server}'")
		subprocess.run(["screen", "-d","-m", "-S", server])

	run_in_screen(server, f"cd '{os.path.dirname(bindings[server])}'")

	# Start the server
	output("info", f"Starting server '{server}'...")

	memory = get_flag_value("-m")
	if memory == None:
		memory = config["default_memory_allocation"]

	nogui = get_flag_value("-nogui")
	if nogui == None:
		nogui = config["no_gui"]

	command = f"java -jar -Xmx{memory}G -Xms{memory}G '{bindings[server]}'"
	if nogui == "1":
		command = f"{command} nogui"

	run_in_screen(server, command)

	output("done", f"Finished starting the server! Use 'screen -r {server}' to access the console.")

# Stop the server
def stop_server(server):
	if not screen_session_exists(server): # If there is no screen session, assume the server isn't running
		output("error", f"Couldn't find screen session '{server}'!")
		return False

	warn_timer = get_flag_value("-w")
	if warn_timer == None:
		warn_timer = int(config["shutdown_warning_timer"])
	else:
		warn_timer = int(warn_timer)

	if warn_timer > 0:
		output("info", f"Warning players of shutdown {warn_timer}s in advance...")
		run_in_screen(server, 'tellraw @a {"text":"Server closing in ' + str(warn_timer) + ' seconds!","bold":true,"color":"red"}')
		if warn_timer > 5:
			time.sleep(warn_timer - 5)
			for i in range(0, 5):
				run_in_screen(server, 'tellraw @a {"text":"Closing in ' + str(5 - i) + ' seconds...","italic":true,"color":"gray"}')
				time.sleep(1)
		else:
			time.sleep(warn_timer)

	# Run the "stop" command in the server console
	output("info", f"Running stop on server '{server}'...")
	run_in_screen(server, "stop")

	# Wait 15s, then do ctrl-C (^C) to force close the server
	force_close_timer = get_flag_value("-fc")
	if force_close_timer == None:
		force_close_timer = int(config["force_close_timer"])
	else:
		force_close_timer = int(force_close_timer)

	if force_close_timer > 0:
		output("info", f"Waiting {force_close_timer}s, then force closing the server.")
		time.sleep(force_close_timer)
		run_in_screen(server, "^C")

	output("done", "The server has been stopped!")

# Backup the server
def backup_server(server):
	name = datetime.datetime.now()
	name = time.strftime(f"{server}_%Y-%m-%d_%H-%M-%S")
	path = f"{os.path.expanduser(config['backups_path'])}/{name}.zip"

	# Make a ZIP archive of the server directory
	output("info", f"Backing up server '{server}' to {path}...")
	if not os.path.exists(os.path.expanduser(config['backups_path'])):
		os.mkdir(os.path.expanduser(config['backups_path']))

	with zipfile.ZipFile(path, 'w') as zipf:
		for root, dirs, files in os.walk(os.path.dirname(bindings[server])):
			for file in files:
				zipf.write(os.path.join(root, file),
					os.path.relpath(os.path.join(root, file),
					os.path.join(os.path.dirname(bindings[server]), '..')))

	output("done", "Backup complete!")

# Restore the server from a backup
def restore_server(server, backup):
	output("info", f"Deleting current contents of '{os.path.dirname(bindings[server])}'...")
	shutil.rmtree(os.path.dirname(bindings[server]))
	os.mkdir(os.path.dirname(bindings[server]))

	output("info", f"Extracting file '{os.path.expanduser(backup)}'...")
	with zipfile.ZipFile(os.path.expanduser(backup), "r") as zip_ref:
			zip_ref.extractall(os.path.dirname(os.path.dirname(bindings[server])))

	output("done", "The server has been restored!")

# Clean the backups folder
def clean_backups(days):
	output("info", f"Deleting backups from more than {days} days ago...")

	# Get the current time
	current_time = datetime.datetime.now()

	# Calculate the cutoff date
	cutoff_time = current_time - datetime.timedelta(days=days)

	# Iterate through files in the directory
	for root, dirs, files in os.walk(config["backups_path"]):
		for file in files:
			file_path = os.path.join(root, file)
			# Get the modification time of the file
			file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
			# If the file is older than cutoff_time, delete it
			if file_time < cutoff_time:
				os.remove(file_path)
				output("info", f"Deleted '{file_path}'")

	output("done", "Backups have been cleaned!")


if args[1] == "help":
	print("BEFORE YOU BEGIN, MAKE SURE TO:")
	print("• Setup a binding for your server(s) in the Easycraft config.")
	print("LIST OF ACTIONS:")
	print("• help: Show this page.\n	Usage: './easycraft.sh help'")
	print("• config: Opens the Easycraft configuration file in vim.\n	Usage: './easycraft.sh config'")
	print("• start: Starts the server.\n	Usage: './easycraft.sh start <server_binding>'")
	print("	Flags:\n	-m <amount>: Amount of memory to allocate, in gibibytes\n	-nogui <0 for false, 1 for true>: Wether or not to start the server with GUI enabled")
	print("• stop: Stops the server.\n	Usage: './easycraft.sh stop <server_binding>'")
	print("	Flags:\n	-fc <seconds>: Amount of time to wait before force closing the server. Use 0 to disable force closing.\n	-w <seconds>: Warn players this amount of time before shutting down. Use 0 to disable this.")
	print("• restart: Stops then starts the server.\n	Usage: './easycraft.sh restart <server_binding>'")
	print("	Flags:\n	All start & stop flags also apply to this command\n	-b <seconds>: Amount of time to wait before starting again. Use 0 to disable this. Not needed if force closing is enabled.")
	print("• backup: Stops, backs up, then starts the server.\n	Usage: './easycraft.sh backup <server_binding>'")
	print("	Flags:\n	All start, stop, and restart flags also apply to this command\n	-nostop: Disables stopping the server before backing up\n	-nostart: Disables starting the server after backup is complete")
	print("• restore: Stops, backs up, restores from a specified backup, then starts the server.\n	Usage: './easycraft.sh restore <server_binding> <path_to_backup_file>'")
	print("	Flags:\n	All start, stop, restart, and backup flags also apply to this command\n	-nobackup: Disables backing up the server before restoring")
	print("• clean_backups: Deletes backups that are older than a certain amount of days.\n	Usage: './easycraft.sh clean_backups <#_of_days>'")
	sys.exit()
elif args[1] == "config":
	output("done", "Opened config.py in vim!")
	subprocess.run(["vim", f"{os.path.dirname(os.path.realpath(__file__))}/config.py"])
	sys.exit()

# Get which server we are working with
if len(args) < 2:
	output("error", "No action given! Use './easycraft help' for a list of actions.")
	sys.exit()
elif len(args) < 3:
	if not args[1] == "clean_backups":
		output("error", "Server not specified!")
	else:
		output("error", "You must specify how many days to keep backups for!")
	sys.exit()

action = args[1]
server = args[2]

try:
	if action == "start":
		start_server(server)
	elif action == "stop":
		stop_server(server)
	elif action == "restart":
		stop_server(server)
		buffer_timer = get_flag_value("-b")
		if buffer_timer == None:
			buffer_timer = int(config["restart_buffer_timer"])
		else:
			buffer_timer = int(buffer_timer)

		if buffer_timer > 0:
			output("info", f"Waiting {buffer_timer}s before starting...")
			time.sleep(buffer_timer)

		start_server(server)
	elif action == "backup":
		should_not_stop = check_for_flag("-nostop")
		should_not_start = check_for_flag("-nostart")
		if not should_not_stop:
			stop_server(server)

		backup_server(server)

		if not should_not_start:
			buffer_timer = get_flag_value("-b")
			if buffer_timer == None:
				buffer_timer = int(config["restart_buffer_timer"])
			else:
				buffer_timer = int(buffer_timer)

			if buffer_timer > 0:
				output("info", f"Waiting {buffer_timer}s before starting...")
				time.sleep(buffer_timer)

			start_server(server)
	elif action == "restore":
		if len(args) < 4:
			output("error", "You must specify which backup to restore from!")
			sys.exit()

		backup_path = args[3]

		should_not_stop = check_for_flag("-nostop")
		should_not_start = check_for_flag("-nostart")
		if not should_not_stop:
			stop_server(server)

		# Backup server before restoring
		should_not_backup = check_for_flag("-nobackup")
		if not should_not_backup:
			backup_server(server)

		# Restore the server
		restore_server(server, backup_path)

		if not should_not_start:
			buffer_timer = get_flag_value("-b")
			if buffer_timer == None:
				buffer_timer = int(config["restart_buffer_timer"])
			else:
				buffer_timer = int(buffer_timer)

			if buffer_timer > 0:
				output("info", f"Waiting {buffer_timer}s before starting...")
				time.sleep(buffer_timer)

			start_server(server)
	elif action == "clean_backups":
		clean_backups(int(server))
	else:
		output("error", f"Invalid action '{action}'")
except:
	output("error", f"An unknown issue occured while performing the action '{action}' on the server '{server}'")

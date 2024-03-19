config = {
	### EASYCRAFT CONFIG FILE ###

	# Make the script recognize your server.
	# Use the format "server_name": "launch_jar",
	# where "server_name" is the name you will type in the command line to reference your server,
	# and "launch_jar" is the path to the .jar file you use to start your server.
	# Example: "my-server": "/Users/johndoe/My Server/launch.jar". In this case I would use "my-server" to reference my server in the command line.
	# Make sure to separate each entry with a comma, and use proper indentation!!
	"bindings": {
		"remove-this-binding": "/this/is/an/example/path.jar"
	},

	# The path where you want server backups to be stored
	"backups_path": "~/EASYCRAFT_BACKUPS",

	# The default amount of memory to grant a server when it starts (in gibibytes)
	# You can use the -m <memory_in_gibibytes> flag to override this
	"default_memory_allocation": "2",

	# When a server is being stopped, a ^C command will be used to forcefully shut it down after this amount of seconds
	# Use 0 as the value to disable this behaviour
	# If you choose to disable this, it is highly recommended to enable "restart_buffer_timer"
	# You can use the -fc <seconds> flag to override this
	"force_close_timer": "15",

	# When a server is being stopped, it will warn players online this amount of seconds before actually stopping the server.
	# Use 0 as the value to disable this behaviour
	# You can use the -w <seconds> flag to override this
	"shutdown_warning_timer": "20",

	# When a server is being restarted or backed up, it will first stop, then it will wait this amount of seconds before starting again.
	# If the "force_close_timer" setting is greater than 0, this may be disableable without issues. However, I recommend at least setting it to 1.
	# Use 0 as the value to disable this behaviour
	# You can use the -b <seconds> flag to override this
	"restart_buffer_timer": "1",

	# Wether or not to open the server without GUI
	# Use 1 for true, and 0 for false
	# You can use the -nogui <0 or 1> flag to override this
	"no_gui": "1"
}


######## Make this the path to your Easycraft directory ########
EASYCRAFT_PATH=Easycraft
################################################################


# Start script begins down here!
#							|
#							|
#							|
#							V





















###### EASYCRAFT START SCRIPT ######

# Initialize an empty string to hold the remaining arguments
remaining_args=""

# Iterate over the remaining arguments
while [[ $# -gt 0 ]]; do
	# Append each argument to the remaining_args string
	remaining_args="$remaining_args $1"
	# Shift to the next argument
	shift
done

# Remove leading and trailing whitespace
remaining_args=$(echo $remaining_args | xargs)

# Output the remaining arguments as a single string
python3 "$EASYCRAFT_PATH/main.py" $remaining_args

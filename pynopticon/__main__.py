# Assuming you have already defined the Pynopticon class
import time

# Initialize Pynopticon with the correct camera index and resolution
pynopticon = Pynopticon(record_frames=100, width=640, height=480, cam=2)  # Adjust cam index as needed

# Start capturing video
pynopticon.start()

# Record for a few seconds (e.g., 10 seconds)
time.sleep(10)

# Stop capturing
#pynopticon.stop()

# Save the captured video to a file named "output.avi"
pynopticon.save(outname="output.avi", fps=10)

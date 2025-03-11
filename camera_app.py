import cv2
import os
from datetime import datetime

class CameraApp:
    def __init__(self):
        self.camera = None
        self.is_running = False
        self.output_dir = "captured_photos"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def start(self):
        # Initialize the camera
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            print("Error: Could not open camera")
            return

        self.is_running = True
        flipflag = False;
        print("Camera started. Press 'q' to quit, 's' to save photo")

        while self.is_running:
            # Read frame from camera
            ret, frame = self.camera.read()
            if not ret:
                print("Error: Can't receive frame")
                break

            # Display the frame
            if (True == flipflag):
                frame = cv2.flip(frame, 1)  # 1 flips horizontally, 0 flips vertically
            cv2.imshow('Camera App', frame)

            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):  # Quit
                self.is_running = False
            elif key == ord('s'):  # Save photo
                self.save_photo(frame)
            elif key == ord('f'): #Flip left and right of photo for self view
                flipflag = not flipflag    
#                frame = cv2.flip(frame, 1)  # 1 flips horizontally, 0 flips vertically
#                cv2.imshow('Camera App', frame)
            elif key == ord('r'): # record video
                self.record_video(frame)

        # Clean up
        self.camera.release()
        cv2.destroyAllWindows()

    def save_photo(self, frame):
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.output_dir, f"photo_{timestamp}.jpg")
        
        # Save the frame as an image
        cv2.imwrite(filename, frame)
        print(f"Photo saved: {filename}")

    def record_video(self, frame):
        # Initialize video writer
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.output_dir, f"video_{timestamp}.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (frame.shape[1], frame.shape[0]))       #specify output file name
        
        print("Video recording started")
        while self.is_running:
            ret, frame = self.camera.read() # read frame from camera
            if not ret:
                print("Error: Can't receive frame")
                break

            out.write(frame) # write frame to video file
            print(f"number of frames written: {out.get(cv2.CAP_PROP_POS_MSEC)}")
            # Display the frame
            cv2.imshow('Camera App', frame)

            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            if key == ord('t'): # stop recording
                self.is_running = False
            
        
        # Clean up  
        self.camera.release()
        out.release()
        cv2.destroyAllWindows()
        print("Video recording stopped")

if __name__ == "__main__":
    app = CameraApp()
    app.start() 
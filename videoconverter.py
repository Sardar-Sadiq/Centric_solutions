import os
import time

class VideoConverter:
    """
    A simulated Video Converter Tool.
    Note: Real video conversion requires heavy libraries like moviepy or ffmpeg-python.
    This implementation focuses on the logic, UI, and file handling aspects.
    """
    def __init__(self):
        self.supported_formats = ['.mp4', '.mkv', '.avi', '.mov']

    def validate_file(self, filepath):
        """Checks if file exists and has a valid video extension."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"The file '{filepath}' does not exist.")
        
        _, ext = os.path.splitext(filepath)
        if ext.lower() not in self.supported_formats:
            raise ValueError(f"Unsupported format: {ext}. Supported: {self.supported_formats}")
        
        return True

    def convert(self, input_path, target_format):
        """Simulates the conversion process."""
        try:
            self.validate_file(input_path)
            
            if not target_format.startswith('.'):
                target_format = '.' + target_format
            
            file_name, _ = os.path.splitext(input_path)
            output_path = f"{file_name}_converted{target_format}"
            
            print(f"Starting conversion: {input_path} -> {output_path}")
            
            # Simulate a progress bar
            for i in range(1, 6):
                time.sleep(0.5)
                print(f"Progress: {i * 20}%...")
            
            # Simulate creating the new file
            with open(output_path, 'w') as f:
                f.write("Simulated video data content.")
                
            print(f"Successfully converted to {output_path}")
            
        except (FileNotFoundError, ValueError) as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    tool = VideoConverter()
    print("--- Video Converter Tool (Simulated) ---")
    
    path = input("Enter path to video file (e.g., test.mp4): ")
    fmt = input("Enter target format (mp4, mkv, avi, mov): ")
    
    # Pre-create a dummy file for the demonstration if it doesn't exist
    if not os.path.exists(path) and path.endswith(tuple(tool.supported_formats)):
        with open(path, 'w') as f: f.write("Dummy video file")

    tool.convert(path, fmt)

if __name__ == "__main__":
    main()
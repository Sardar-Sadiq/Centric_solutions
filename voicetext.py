import time

class VoiceNoteApp:
    """
    Simulates a Voice-to-Text conversion and note-taking app.
    Real implementation uses 'SpeechRecognition' library.
    """
    def __init__(self):
        self.notes_file = "voice_notes.txt"

    def capture_voice(self):
        """Simulates listening to audio and converting to text."""
        print("Listening... (Speak now)")
        time.sleep(2) # Simulating audio duration
        print("Processing audio...")
        time.sleep(1)
        
        # Simulated speech result
        simulated_speech = "This is a voice note recorded for my project."
        return simulated_speech

    def save_note(self, content):
        """Appends the transcribed text to a file."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.notes_file, "a") as f:
                f.write(f"[{timestamp}] {content}\n")
            print("Note saved to file.")
        except Exception as e:
            print(f"File handling error: {e}")

    def run(self):
        print("--- Voice to Text Note App ---")
        while True:
            cmd = input("\nPress 'r' to record, 'v' to view notes, 'q' to quit: ").lower()
            if cmd == 'r':
                text = self.capture_voice()
                print(f"Transcribed: \"{text}\"")
                confirm = input("Save this note? (y/n): ")
                if confirm.lower() == 'y':
                    self.save_note(text)
            elif cmd == 'v':
                self.view_notes()
            elif cmd == 'q':
                break
            else:
                print("Invalid command.")

    def view_notes(self):
        """Reads and displays all saved notes."""
        try:
            if not os.path.exists(self.notes_file):
                print("No notes found.")
                return
            with open(self.notes_file, "r") as f:
                print("\n--- Your Voice Notes ---")
                print(f.read())
        except Exception as e:
            print(f"Error reading notes: {e}")

import os # Required for path checking in view_notes

if __name__ == "__main__":
    app = VoiceNoteApp()
    app.run()
# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Function to set reminders
def set_reminder():
    speak("Please specify the reminder time and message.")
    reminder_time = listen()
    # Use regex or date parsing to extract the time
    # Schedule a reminder using a timer or calendar API
    # Example: Use the `schedule` library to schedule a function to run at the specified time

# Function to create a to-do list
def create_todo():
    speak("What task would you like to add to your to-do list?")
    task = listen()
    # Append the task to a to-do list (e.g., a text file)

# Function to search the web
def search_web():
    speak("What would you like to search for?")
    query = listen()
    query = re.sub(r'\s+', '+', query)  # Replace spaces with '+' for a web query
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

    while True:
    speak("How can I assist you?")
    user_input = listen()
    
    if "reminder" in user_input:
        set_reminder()
    elif "to-do list" in user_input:
        create_todo()
    elif "search" in user_input:
        search_web()
    elif "exit" in user_input:
        speak("Goodbye!")
        break
    else:
        speak("I didn't understand your request. Please try again.")
 
        <script>
    // Your existing Three.js code here

    // Function to update subtitles
    function updateSubtitle(text) {
        const subtitleElement = document.getElementById('subtitle');
        subtitleElement.innerText = text;
    }

    // Example usage to update the subtitles when your assistant speaks
    speak("Hello, I am your voice assistant.");
    updateSubtitle("Hello, I am your voice assistant.");
</script>
# Virtual Assistant README

## Introduction
Welcome to your personal virtual assistant coded in Python! This robust virtual assistant is designed to facilitate seamless interaction through voice commands, employing advanced speech recognition and text-to-speech technologies. Whether you need to check the time, inquire about the date, or simply engage in casual conversation, this assistant is here to make your tasks more convenient and enjoyable.

## Features

1. **Voice Interaction**: Communicate naturally with the assistant using voice commands for a hands-free and intuitive experience.

2. **Warm Greetings**: The assistant starts every interaction with a friendly greeting, creating a welcoming environment for users.

3. **Time and Date**: Stay informed about the current time and date by asking the assistant. It provides accurate and up-to-date information instantly.

4. **Continuous Interaction Loop**: The program operates in a continuous loop, enabling you to ask multiple questions or issue commands without restarting the application.

5. **Polite Farewell**: When you're ready to conclude the interaction, a polite farewell message is delivered, ensuring a positive and courteous user experience.

## Getting Started

### Prerequisites
- Ensure you have Python installed on your system.
- Install required libraries using `pip install speech_recognition pyttsx3`.

### How to Run
1. **Clone the Repository**: Begin by cloning the repository to your local machine.

    ```bash
    git clone https://github.com/your-username/virtual-assistant.git
    ```

2. **Navigate to Project Directory**: Move into the project directory.

    ```bash
    cd virtual-assistant
    ```

3. **Run the Python Script**: Execute the Python script to start the virtual assistant.

    ```bash
    python virtual_assistant.py
    ```

4. **Interact with the Assistant**: Use voice commands to interact with the virtual assistant and explore its functionalities.

## Customization

Feel free to customize the assistant to align with your preferences and requirements. The code is modular and easily extensible, allowing you to modify greetings, add new commands, or enhance existing features.

## Integrating OpenAI API with Environment Variables

For a more secure integration of OpenAI API keys, consider using environmental variables to store and access these keys. This approach ensures that API keys are kept confidential and allows for easy deployment on different machines.

### Steps to Integrate OpenAI API with Environment Variables (Windows)

1. **Get OpenAI API Key**: Obtain an API key from OpenAI by following their documentation.

2. **Open Environment Variables Settings**:
   - Click on the **Windows Start** button.
   - Type "Environment Variables" in the search bar and select the "Edit the system environment variables" option that appears at the top.

3. **Open Environment Variables Window**:
   - In the System Properties window, click on the "Environment Variables..." button.

4. **Create a New User Variable**:
   - In the Environment Variables window, under the "User variables for [YourUsername]" section, click on the "New..." button.

5. **Set Variable Name and Value**:
   - Enter a desired name for the variable (e.g., `OPENAI_API_KEY`) in the "Variable name" field.
   - Enter your OpenAI API key in the "Variable value" field.

6. **Save the Variable**:
   - Click "OK" to save the new user variable.
   - Click "OK" again to close the Environment Variables window.

7. **Access API Key in Code**:
   - In your Python code, access the API key using the `os` module:

     ```python
     import os

     openai_api_key = os.environ.get("OPENAI_API_KEY")

     # Use openai_api_key in your OpenAI API calls
     ```

8. **Run the Virtual Assistant**:
   - Run your virtual assistant, and it will now utilize the OpenAI API key stored as an environmental variable.

---

Experience the convenience of having a virtual assistant at your service! For any questions or further assistance, don't hesitate to reach out. Your feedback is valuable!

Happy coding! 🚀

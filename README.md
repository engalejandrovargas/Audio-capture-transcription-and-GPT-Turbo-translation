# Audio capture transcription using Flask and GPT Turbo for translation

This Python script is a web application that uses Flask and aiohttp to create a server with WebSocket functionality. The purpose of the application is to be a real-time audio transcription and translation from Japanese to English using Deepgram and OpenAI's GPT-4 model.

Here's a brief breakdown of the main components:

1. Imports: The script imports necessary libraries such as dotenv for environment variable loading, aiohttp for asynchronous HTTP requests, Flask for web application framework, and modules like Deepgram and OpenAI for audio transcription and language translation.
2. Setting up Flask: The Flask app is created with the name 'aioflask', and environment variables are loaded using dotenv.
3. Deepgram Configuration: The script checks if the Deepgram API key is set in the environment variables. If not, it raises a ValueError. The Deepgram client is then configured using the API key.
4. WebSocket Connection: The process_audio function is an asynchronous function that sets up a WebSocket connection with Deepgram. It receives audio data, sends it to Deepgram for transcription, and then sends the transcript back to the client.
5. Translation to English: The translate_to_english function utilizes OpenAI's GPT-4 model to translate a Japanese transcript to English.
6. WebSocket Server: The socket function is an asynchronous WebSocket handler. It prepares the WebSocket connection and initiates the process of audio transcription and translation using the Deepgram WebSocket.

The main functionality is to be providing a real-time audio transcription service through a WebSocket, with an additional feature of translating the Japanese transcripts to English using OpenAI's GPT-4 model. 

# How to install

To run this project create a virtual environment by running the below commands. You can learn more about setting up a virtual environment in this article.

```
mkdir [% NAME_OF_YOUR_DIRECTORY %]
cd [% NAME_OF_YOUR_DIRECTORY %]
python3 -m venv venv
source venv/bin/activate
```

Make sure your virtual environment is activated and install the dependencies in the requirements.txt file inside.

`pip install -r requirements.txt`

Add the corresponding API's from Deepgram and OpenAI.
Make sure you're in the directory with the main.py file and run the project in the development server.

`python main.py`

Pull up a browser and go to your localhost, `(http://localhost:8081/)`.

Allow access to your microphone and start speaking. A transcript of your audio will appear in the browser.

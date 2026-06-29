# Luna_s1
# Overview
Luna is a voice-activated personal assistant that runs locally on your machine. It listens for spoken commands, understands them via Google Speech Recognition, and responds either with pre-defined answers, live data from external APIs, or AI-generated responses powered by a locally hosted LLM via Ollama.
This is Season 1 (S1) — the foundational prototype that establishes the core voice loop and interaction model for the project.
# Features
🎙️ Voice Input — Listens continuously via your microphone using speech_recognition
🔊 Voice Output — Responds in a female voice using pyttsx3 text-to-speech
🤖 AI Responses — Falls back to a local llama3.2 model via Ollama for general queries
🚀 NASA APOD Integration — Fetches a random Astronomy Picture of the Day with an explanation when space-related keywords are detected
🧠 Hardcoded Identity — Responds to "What is your name?" / "Who are you?" with a fixed identity response

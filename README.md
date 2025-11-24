# 🎵 AI Music Composer

An intelligent music composition system powered by Large Language Models. Generate melodies, harmonies, and rhythms through natural language prompts, with support for multiple musical styles and real-time audio synthesis.

## 🌟 Features

- **AI-Powered Melody Generation**: Uses LLM to create musical melodies from text descriptions
- **Harmony Creation**: Automatically generates complementary chord progressions
- **Rhythm Synthesis**: Intelligent beat and duration suggestions
- **Style Adaptation**: Transform compositions to match different musical styles (Classical, Jazz, Rock, etc.)
- **Real-time Audio Playback**: Convert musical notes to WAV audio instantly
- **Dual LLM Support**: Switch between cloud-based (GROQ) and local (Ollama) models
- **Interactive Web Interface**: User-friendly Streamlit application

## 🛠️ Tech Stack

- **LLM**: GROQ API (Llama 3.3 70B) / Ollama (local models)
- **Music Processing**: music21 library
- **Audio Synthesis**: synthesizer, scipy
- **Frontend**: Streamlit
- **Language**: Python 3.12
- **Containerization**: Docker
- **Deployment**: Google Cloud Platform (GCP)

## 📁 Project Structure

```
AI Music Composer/
├── app/                        # Core application modules
│   ├── __init__.py            # Package initialization
│   ├── main.py                # LLM integration & music generation
│   └── utils.py               # Audio synthesis utilities
├── app.py                     # Streamlit application entry point
├── setup.py                   # Package setup configuration
├── requirements.txt           # Python dependencies
├── pyproject.toml            # Project metadata
├── Dockerfile                # Docker configuration
├── .env                      # Environment variables (not in repo)
├── .gitignore               # Git ignore rules
└── .python-version          # Python version specification
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12.10 or higher
- GROQ API key ([Get one here](https://console.groq.com)) OR
- Ollama installed locally ([Install Ollama](https://ollama.ai))

### Installation

1. **Clone the repository**

   ```bash
   git clone https://gitlab.com/BWayne1290/music.git
   cd music
   ```

2. **Install dependencies**

   Using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Or using uv (recommended):
   ```bash
   uv add -r requirements.txt
   ```

   Or editable install:
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   # For cloud-based LLM (GROQ)
   GROQ_API_KEY=your_groq_api_key_here
   USE_OLLAMA=false

   # OR for local LLM (Ollama)
   USE_OLLAMA=true
   ```

4. **Run the application**

   ```bash
   streamlit run app.py
   ```

   Or with uv:
   ```bash
   uv run streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 💡 Usage

### Step 1: Describe Your Music
Enter a natural language description of the music you want to create:
- *"Create a happy melody in C major"*
- *"Generate a sad piano piece"*
- *"Make an upbeat jazz tune"*

### Step 2: Generate Melody
The AI will generate a sequence of musical notes (e.g., `C4 D4 E4 F4 G4`)

### Step 3: Add Harmony
The system creates complementary chord progressions to enrich the melody

### Step 4: Apply Rhythm
Rhythmic durations are assigned to each note for proper timing

### Step 5: Choose Style
Adapt your composition to different musical styles:
- Classical
- Jazz
- Rock
- Pop
- Electronic

### Step 6: Listen
Play the generated music as a WAV audio file directly in your browser

## 🐳 Docker Deployment

Build and run with Docker:

```bash
# Build the image
docker build -t ai-music-composer .

# Run the container (with GROQ)
docker run -p 8501:8501 -e GROQ_API_KEY=your_api_key ai-music-composer

# Run the container (with Ollama - requires Ollama running on host)
docker run -p 8501:8501 -e USE_OLLAMA=true --network=host ai-music-composer
```

Access at `http://localhost:8501`

## ☁️ GCP Deployment

Deploy to Google Cloud Run:

```bash
# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/ai-music-composer

# Deploy to Cloud Run
gcloud run deploy ai-music-composer \
  --image gcr.io/YOUR_PROJECT_ID/ai-music-composer \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GROQ_API_KEY=your_api_key
```

## 📊 How It Works

1. **User Input**: User provides a natural language description of desired music
2. **LLM Processing**: The description is sent to the LLM (GROQ or Ollama)
3. **Melody Generation**: AI generates a sequence of musical notes
4. **Harmony Creation**: System creates complementary chord progressions
5. **Rhythm Assignment**: Durations are assigned to create proper timing
6. **Style Adaptation**: Music is adapted to match the selected style
7. **Audio Synthesis**: Notes are converted to frequencies and synthesized into WAV audio
8. **Playback**: User can listen to the generated composition

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your GROQ API key (required if USE_OLLAMA=false)
- `USE_OLLAMA`: Set to `true` for local Ollama, `false` for cloud GROQ (default: false)

### LLM Configuration

**Cloud Mode (GROQ)**:
- Model: `llama-3.3-70b-versatile`
- Fast inference, requires API key
- Best for production deployment

**Local Mode (Ollama)**:
- Model: `qwen3-vl:30b-a3b-instruct` (configurable in `app/main.py`)
- Runs locally, no API key needed
- Best for development and privacy

### Audio Synthesis

Configure in `app/utils.py`:
- Waveform: `Waveform.sine` (can change to square, sawtooth, etc.)
- Sample Rate: `44100 Hz`
- Note Duration: `0.5 seconds` (configurable)

## 📦 Dependencies

- **streamlit**: Web application framework
- **music21**: Music theory and notation processing
- **langchain-core**: LLM prompt management
- **langchain-groq**: GROQ API integration
- **langchain-ollama**: Ollama local LLM integration
- **synthesizer**: Audio waveform synthesis
- **scipy**: Signal processing and WAV file generation
- **numpy**: Numerical operations
- **python-dotenv**: Environment variable management

## 🚧 Troubleshooting

### "ModuleNotFoundError: No module named 'langchain'"
- Run: `pip install -r requirements.txt` or `uv add -r requirements.txt`
- Make sure you're using the correct Python environment

### "Invalid API Key" Error
- Verify your GROQ API key in the `.env` file
- Check that the key is active at [GROQ Console](https://console.groq.com)

### "Connection Error" with Ollama
- Ensure Ollama is installed and running: `ollama serve`
- Verify the model is downloaded: `ollama pull qwen3-vl:30b-a3b-instruct`
- Check that `USE_OLLAMA=true` in your `.env` file

### Audio Playback Issues
- Ensure your browser supports WAV audio playback
- Check that scipy and synthesizer are properly installed
- Verify the generated notes are valid musical notes (e.g., C4, D#5)

## 🎯 Use Cases

- **Music Education**: Learn music theory through AI-generated examples
- **Composition Assistant**: Get inspiration for your own compositions
- **Game Development**: Generate background music for games
- **Content Creation**: Create royalty-free music for videos and podcasts
- **Experimentation**: Explore different musical styles and combinations

## 🔮 Future Enhancements

- [ ] MIDI file export
- [ ] Multiple instrument support
- [ ] Longer composition generation
- [ ] Music visualization (sheet music display)
- [ ] Tempo and key signature control
- [ ] Save and share compositions
- [ ] Integration with DAWs (Digital Audio Workstations)
- [ ] Real-time collaborative composition
- [ ] Music genre classification
- [ ] Advanced music theory analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Powered by GROQ's fast LLM inference and Ollama's local models
- Built with Streamlit for rapid prototyping
- Uses music21 for music theory processing
- Audio synthesis by synthesizer library

---

**Made with ❤️ and 🎵 for music enthusiasts and AI developers**


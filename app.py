import streamlit as st
from app.main import MusicLLM
from app.utils import *
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

st.set_page_config(page_title="AI Music Composer", page_icon=":musical_note:", layout ="centered")
st.title("AI Music Composer")
st.markdown("Generate AI Music by describing the style and content")


music_input = st.text_input("Describe the music you want to compose")
style = st.selectbox("Select the style of the music", ["Classical", "Jazz", "Rock", "Pop", "Hip-Hop", "Electronic", "Country", "Reggae", "Soul", "Funk", "Blues", "R&B", "Metal", "Punk", "Folk", "Salsa", "Latin", "Reggaeton", "Mariachi", "Bachata", "Samba", "Tango", "Jazz", "Rock", "Pop", "Hip-Hop", "Electronic", "Country", "Reggae", "Soul", "Funk", "Blues", "R&B", "Metal", "Punk", "Folk", "Salsa", "Latin", "Reggaeton", "Mariachi", "Bachata", "Samba", "Tango"])

if st.button("Generate Music") and music_input:
    generator = MusicLLM()
    with st.spinner("Generating music..."):
        melody = generator.generate_melody(music_input)
        harmony = generator.generate_harmony(melody)
        rhythm = generator.generate_rhythm(melody)

        composition = generator.adapt_style(style, melody, harmony, rhythm)

        melody_notes = melody.split()
        melody_freqs = note_to_frequencies(melody_notes)

        harmony_chords = harmony.split()
        harmony_notes =[]
        for chord in harmony_chords:
            harmony_notes.extend(chord.split("-"))
        
        harmony_freqs = note_to_frequencies(harmony_notes)

        all_freqs = melody_freqs + harmony_freqs

        wav_bytes = generate_wav_bytes_from_notes_freq(all_freqs)

    st.audio(BytesIO(wav_bytes), format="audio/wav")

    st.success("Music generated successfully!")

    with st.expander("Composition summary"):
        st.text(composition)


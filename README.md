🎵 MusicApp - OOP-Based Music Streaming Simulation in Python
MusicApp is a Python-based simulation of a music streaming platform that showcases clean Object-Oriented Programming (OOP) design. It allows you to create and manage songs, live versions, singles, playlists, and user interactions such as liking and playing tracks.

💡 Features
🎶 Song Class with attributes like title, artist, duration, and stream count.

🔁 LiveVersion and Single subclasses to handle concert recordings and single releases.

📃 PlayList class to manage song collections, support merging, duration calculation, and safe navigation.

👤 User class to simulate user behavior (liking songs, playing tracks, and simple recommendation).

🧠 Operator overloading (+, len, str) for intuitive class behavior.

🛠️ Utility methods: ID generation, duration validation, echo effect simulation.

✅ Fully written in Python using standard libraries (random, string).

📁 Structure
Song – Base class for all types of songs.

Single, LiveVersion – Specialized song types.

PlayList – Supports song addition, removal, combination, and playback.

User – Allows interaction with songs (like/play/recommend).

Operator overloads: __str__, __add__, __len__.

🧪 Example Use Cases
Build custom playlists and combine them.

Simulate live version effects like echo and crowd noise.

Recommend the least-streamed song a user has liked.

Dynamically generate song IDs for uniqueness.

📦 Dependencies
Pure Python — no third-party libraries required.

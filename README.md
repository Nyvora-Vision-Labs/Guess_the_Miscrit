# Guess_the_Miscrit?! 🎮❓

A nostalgic, interactive web game where players test their knowledge by guessing the names of Miscrits based on their silhouettes—inspired by the classic "Who's that Pokémon?!" intermission.

**Play the live game here:** [Guess the Miscrit!](https://nyvora-vision-labs.github.io/Guess_the_Miscrit/)

---

## 🌟 Features

- **Two Game Modes:**
  - _Easy:_ Multiple-choice selection.
  - _Hard:_ Type the exact name of the Miscrit.
- **Customizable Length:** Play rounds of 5, 10, 25, 50, or up to 100 Miscrits.
- **Responsive UI:** Mobile-friendly design with anime-style sunburst effects, custom fonts, and interactive feedback.
- **Social Sharing:** Integrated buttons to instantly share your final score and time to Twitter (X) and Reddit, or copy a generated "Score Card" image directly to your clipboard for Discord using `html2canvas`.

---

## 📁 Project Structure

```text
├── index.html                             # The main game web page (HTML/CSS/JS)
├── get_msicrits.py                        # Utility script to generate the array of Miscrit names
├── scrape_image.py                        # Web scraper for collecting original Miscrit sprites
├── silhouette_miscrits.py                 # Image processing script to generate silhouettes
├── images_scraped_from_miscripedia/       # Original, full-color Miscrit images + index.csv
└── miscrits_silhouettes/                  # Processed, solid-black silhouette images used in-game
```

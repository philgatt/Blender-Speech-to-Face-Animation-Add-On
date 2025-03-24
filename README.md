# Blender Speech-to-Face Animation Add-On

## 🚧 Work in Progress 🚧

This Blender add-on allows you to input an audio file (spoken or sung words) and automatically generate facial animation. It supports every type of face control rig since it operates using reference poses.

## ✨ Features
- Converts speech audio into facial animations.
- Supports all facial control rigs through reference poses.
- Allows user corrections of detected words.
- Simple UI coming soon!

## 🎭 Phoneme Reference Poses
To achieve accurate animation, the user must define reference poses for the following phonemes:

![Phoneme Reference](https://github.com/user-attachments/assets/4ac8a08a-6c4f-4bb8-acd4-3d5110437907)

## 🔧 How It Works
1. Install the required dependencies (see [Installation](#installation)).
2. Set up reference poses for phonemes.
3. Run the add-on and input an audio file.
4. The detected words will be listed in the Blender console for review and corrections.

## 📌 Installation
Ensure Blender's Python executable has the necessary dependencies. Install them using:

```bash
pip install -r requirements.txt
```

## 📅 Upcoming Features
- Graphical User Interface (GUI) for easier corrections.
- Improved word recognition and phoneme mapping.

## 🛠 Prerequisites
- Blender with Python enabled.
- Required dependencies from `requirements.txt`.

---

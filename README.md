# THIS PROGRAM USES VOSK MODEL TO RECOGNIZE RUSSIAN SPEECH.

1) Press the 'ALT+WIN' key combination  
2) Wait for 2 sec to let audio stream to be created and started
3) Speak
4) When text is appeared in a current cursor place, release keys
5) If you want to continue your speech with backspace and comma,
        press the key combination again and continue your speech within 3 sec, 
   Another way, your next speech will start with no backspace and in uppercase



# NOTES
1. Your current project directory shouls contain vosk-model-small-ru-0.22 (downloaded from https://alphacephei.com/vosk/models)
2. Executable file (or .py script) must be added to antivirus exceptions to work properly.



# PYINSTALLER-BUILD FOR NOCONSOLE EXECUTE

pyinstaller --onefile --noconsole --hidden-import vosk --add-data "vosk-model-small-ru-0.22;vosk-model-small-ru-0.22" --collect-all vosk AltX_VoiceRec.py



# SYSTEM REQUIREMENTS FOR VOSK MODELS (SMALL MODEL IS USED BY DEFAULT):

vosk-model-small-ru-0.22
1. **Random Access Memory (RAM):** About 50-100 MB.
2. **Processor:** Suitable even for weak processors such as Intel Atom or ARM Cortex-A.
3. **Disk space:** About 50 MB for the model itself.
4. **Operating system:** Windows, Linux, macOS, Android are supported.
5. **Software:** Python 3.6 or higher, PyAudio, Vosk library.
vosk-model-ru-0.42
1. **Random Access Memory (RAM):** About 500-700 MB.
2. **Processor:** It is recommended to use more powerful processors such as Intel Core i3/i5/i7 or the quivalent from AMD.
3. **Disk space:** About 1.8 GB for the model itself.
4. **Operating system:** Windows, Linux, macOS, Android are supported.
5. **Software:** Python 3.6 or higher, PyAudio, Vosk library.



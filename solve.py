import speech_recognition as sr
import pyttsx3

from bomb import Bomb
from solvers import perplexingwires

import solvers.knobs as knobs
import solvers.mazes as mazes
import solvers.wires as wires
import solvers.morse as morse
import solvers.button as button
import solvers.memory as memory
import solvers.keypads as keypads
import solvers.passwords as passwords
import solvers.simonsays as simonsays
import solvers.complicated as complicated
import solvers.whosonfirst as whosonfirst
import solvers.wiresequences as wiresequences
import solvers.perplexingwires as perplexingwires
import solvers.simonscreams as simonscreams

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

newBomb = Bomb()

def select_module():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.3)
                audio2 = r.listen(source2)
                MyText = r.recognize_sphinx(audio2, grammar="./grammars/solve.gram")
                MyText = MyText.lower()

                match MyText:
                    # Defuse modules
                    case "defuse wires":
                        SpeakText("Simple Wires")
                        wires.solve_wires(newBomb, "./grammars/wires.gram")
                    case "defuse button":
                        SpeakText("Button")
                        button.solve_button(newBomb, "./grammars/button.gram")
                    case "defuse keypads":
                        SpeakText("Keypads")
                        keypads.solve_keypads("./grammars/keypads.gram")
                    case "defuse simon says":
                        SpeakText("Simon Says")
                        simonsays.solve_simonsays(newBomb, "./grammars/simonsays.gram")
                    case "defuse memory":
                        SpeakText("Memory")
                        memory.solve_memory(newBomb, "./grammars/memory.gram")
                    case "defuse morse code":
                        SpeakText("Morse code")
                        morse.solve_morse(newBomb, "./grammars/morsecode.gram")
                    case "defuse complicated":
                        SpeakText("Complicated Wires")
                        complicated.solve_complicated(newBomb, "./grammars/complicatedwires.gram")
                    case "defuse who's on first":
                        SpeakText("Who's on first")
                        whosonfirst.solve_whosonfirst("./grammars/whosonfirst.gram")
                    case "defuse sequence":
                        SpeakText("Wire sequences")
                        wiresequences.solve_wiresequences(newBomb, "./grammars/wiresequences.gram")
                    case "defuse maze":
                        SpeakText("Mazes")
                        mazes.solve_mazes("./grammars/mazes.gram")
                    case "defuse password":
                        SpeakText("Password")
                        passwords.solve_password(newBomb,"./grammars/passwords.gram")

                    # Needy Modules
                    case "defuse knobs":
                        SpeakText("Knobs")
                        knobs.solve_knobs("./grammars/knobs.gram")

                    # Modded Modules
                    case "defuse perplexing":
                        SpeakText("Perplexing wires")
                        perplexingwires.solve_perplexingwires(newBomb, "./grammars/perplexingwires1.gram", "./grammars/perplexingwiresarrows.gram")   
                    case "defuse screams":
                        SpeakText("Simon Screams")
                        simonscreams.solve_simonscreams(newBomb, "./grammars/simonscreams.gram")

                    # Undo mistakes
                    case "undo last memory":
                        if newBomb.memory_round == 1 and not newBomb.memory_positions[0] == 0:
                            newBomb.memory_round = 5
                            SpeakText("undoing last memory round")
                        elif newBomb.memory_round > 1:
                            newBomb.memory_round = newBomb.memory_round - 1
                        else:
                            pass
                    case "undo last sequence":
                        wiresequences.undo_last_sequence(newBomb)

                    # Reset modules
                    case "reset memory":
                        newBomb.memory_round = 1
                        SpeakText("Memory reset")
                    case "reset wire sequences":
                        newBomb.wire_sequences_black_count = 0
                        newBomb.wire_sequences_blue_count = 0
                        newBomb.wire_sequences_red_count = 0
                        SpeakText("Wire sequences reset")
                    case "reset morse code":
                        newBomb.morse_num = 1
                        SpeakText("Morse code reset")
                    case "reset password":
                        newBomb.password_num = 1
                    case "reset screams":
                        newBomb.simon_screams_round = 1
                        SpeakText("Simon screams reset.")

                    # Strike commands
                    case "add a strike":
                        if newBomb.strikes < 2:
                            newBomb.strikes += 1
                        SpeakText("bomb has {} strikes".format(newBomb.strikes))
                    case "remove a strike":
                        if newBomb.strikes > 0:
                            newBomb.strikes -= 1
                        SpeakText("bomb has {} strikes".format(newBomb.strikes))
                    case "reset strikes":
                        newBomb.strikes = 0
                        SpeakText("Strikes reset.")

                    # Other commands
                    case "please stop":
                        SpeakText("stopping")
                        break
                    case _:
                        SpeakText("unknown command: {}".format(MyText))
                        print(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")
            
select_module()
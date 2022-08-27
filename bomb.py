import solvers.solverSpeech as solverSpeech
class Bomb:
    def __init__(self):
        # Vanilla requirements
        self.vowel = None
        self.final_digit_odd = None
        self.battery_count = None
        self.indicator_car = None
        self.indicator_frk = None
        self.parallel_port = None
        self.strikes = 0
        self.memory_round = 1
        self.memory_positions = [0] * 4
        self.memory_labels = [0] * 4
        self.wire_sequences_black_count = 0
        self.wire_sequences_blue_count = 0
        self.wire_sequences_red_count = 0
        self.wire_sequences_moves = []
        self.password_num = 1
        self.password_options = []
        self.morse_num = 1
        self.morse_options = []

        # Modded requirements
        self.indicator_count = None
        self.port_count = None
        self.usb_port = None
        self.simon_screams_round = 1
        self.digit_serial_count = None
        self.battery_holder_count = None
        self.simon_screams_color_order = []
        self.simon_screams_sequence = []

    # Vanilla checks
    def spontaneous_vowel_check(self):
        solverSpeech.SpeakText("Is there a vowel?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/binarycheck.gram")

        match words:
            case "yes":
                self.vowel = True
            case "no":
                self.vowel = False
            case _:
                solverSpeech.SpeakText("Please say yes or no.")
                self.spontaneous_vowel_check()
    
    def spontaneous_final_digit_check(self):
        solverSpeech.SpeakText("Is the last digit odd or even?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/binarycheck.gram")

        match words:
            case "odd":
                self.final_digit_odd = True
                solverSpeech.SpeakText("Odd")
            case "even":
                self.final_digit_odd = False
                solverSpeech.SpeakText("Even")
            case _:
                solverSpeech.SpeakText("Please say odd or even.")
                self.spontaneous_final_digit_check()

    def spontaneous_battery_check(self):
        solverSpeech.SpeakText("How many batteries?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/numbercheck.gram")

        match words:
            case "zero":
                self.battery_count = 0
            case "one":
                self.battery_count = 1
            case "two":
                self.battery_count = 2
            case "three":
                self.battery_count = 3
            case "four":
                self.battery_count = 4
            case "five":
                self.battery_count = 5
            case "six":
                self.battery_count = 6
            case "seven":
                self.battery_count = 7
            case "eight":
                self.battery_count = 8
            case "nine":
                self.battery_count = 9
            case _:
                solverSpeech.SpeakText("Please say a number.")
                self.spontaneous_battery_check()
        solverSpeech.SpeakText(words)

    def spontaneous_indicator_car_check(self):
        solverSpeech.SpeakText("Is there a lit car indicator?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/binarycheck.gram")

        match words:
            case "yes":
                solverSpeech.SpeakText("car")
                self.indicator_car = True
            case "no":
                solverSpeech.SpeakText("no car")
                self.indicator_car = False
            case _:
                solverSpeech.SpeakText("Please say yes or no.")
                self.spontaneous_indicator_car_check()
    
    def spontaneous_indicator_freak_check(self):
        solverSpeech.SpeakText("Is there a lit freak indicator?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/binarycheck.gram")

        match words:
            case "yes":
                solverSpeech.SpeakText("freak")
                self.indicator_freak = True
            case "no":
                solverSpeech.SpeakText("no freak")
                self.indicator_freak = False
            case _:
                solverSpeech.SpeakText("Please say yes or no.")
                self.spontaneous_indicator_freak_check()

    def spontaneous_parallel_port_check(self):
        solverSpeech.SpeakText("Is there a parallel port?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/binarycheck.gram")

        match words:
            case "yes":
                solverSpeech.SpeakText("parallel port")
                self.parallel_port = True
            case "no":
                solverSpeech.SpeakText("no parallel port")
                self.parallel_port = False
            case _:
                solverSpeech.SpeakText("Please say yes or no.")
                self.spontaneous_parallel_port_check()

    # Modded checks
    def spontaneous_port_count_check(self):
        solverSpeech.SpeakText("How many ports?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/numbercheck.gram")

        match words:
            case "zero":
                self.port_count = 0
            case "one":
                self.port_count = 1
            case "two":
                self.port_count = 2
            case "three":
                self.port_count = 3
            case "four":
                self.port_count = 4
            case "five":
                self.port_count = 5
            case "six":
                self.port_count = 6
            case "seven":
                self.port_count = 7
            case "eight":
                self.port_count = 8
            case "nine":
                self.port_count = 9
            case _:
                solverSpeech.SpeakText("Please say a number.")
                self.spontaneous_port_count_check()
        solverSpeech.SpeakText(words)

    def spontaneous_indicator_count_check(self):
        solverSpeech.SpeakText("How many indicators?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/numbercheck.gram")

        match words:
            case "zero":
                self.indicator_count = 0
            case "one":
                self.indicator_count = 1
            case "two":
                self.indicator_count = 2
            case "three":
                self.indicator_count = 3
            case "four":
                self.indicator_count = 4
            case "five":
                self.indicator_count = 5
            case "six":
                self.indicator_count = 6
            case "seven":
                self.indicator_count = 7
            case "eight":
                self.indicator_count = 8
            case "nine":
                self.indicator_count = 9
            case _:
                solverSpeech.SpeakText("Please say a number.")
                self.spontaneous_indicator_count_check()
        solverSpeech.SpeakText(words)
    
    def spontaneous_battery_holder_count_check(self):
        solverSpeech.SpeakText("How many battery holders?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/numbercheck.gram")

        match words:
            case "zero":
                self.battery_holder_count = 0
            case "one":
                self.battery_holder_count = 1
            case "two":
                self.battery_holder_count = 2
            case "three":
                self.battery_holder_count = 3
            case "four":
                self.battery_holder_count = 4
            case "five":
                self.battery_holder_count = 5
            case "six":
                self.battery_holder_count = 6
            case "seven":
                self.battery_holder_count = 7
            case "eight":
                self.battery_holder_count = 8
            case "nine":
                self.battery_holder_count = 9
            case _:
                solverSpeech.SpeakText("Please say a number.")
                self.spontaneous_battery_holder_count_check()
        solverSpeech.SpeakText(words)
    
    def spontaneous_serial_digit_count_check(self):
        solverSpeech.SpeakText("How many digits in serial number?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/numbercheck.gram")

        match words:
            case "zero":
                self.digit_serial_count = 0
            case "one":
                self.digit_serial_count = 1
            case "two":
                self.digit_serial_count = 2
            case "three":
                self.digit_serial_count = 3
            case "four":
                self.digit_serial_count = 4
            case "five":
                self.digit_serial_count = 5
            case "six":
                self.digit_serial_count = 6
            case _:
                solverSpeech.SpeakText("Please say a number six or less.")
                self.spontaneous_serial_digit_count_check()
        solverSpeech.SpeakText(words)
    
    def spontaneous_usb_check(self):
        solverSpeech.SpeakText("Is there a you s b port?")
        words = ""
        words = solverSpeech.CollectText(words, "./grammars/binarycheck.gram")

        match words:
            case "yes":
                solverSpeech.SpeakText("you s b")
                self.usb_port = True
            case "no":
                solverSpeech.SpeakText("no you s b")
                self.usb_port = False
            case _:
                solverSpeech.SpeakText("Please say yes or no.")
                self.spontaneous_usb_check()
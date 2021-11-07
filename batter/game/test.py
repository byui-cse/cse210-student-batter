while True:
            _initial_Text = Actor()
            _initial_Text.set_color("yellow")
            _initial_Text.set_text(
                "\t\t\tWelcome to Bat - Old Bricks -!.\n\n\t\t\t more text here. ")
            x = int((constants.MAX_X * 2/3) - len(_initial_Text.get_text()))
            y = (constants.MAX_Y // 2) - 1
            position = Point(x, y)
            _initial_Text.set_position(position)

            self._cast["ini_Text"] = [_initial_Text]
            self._cue_action("output")

        sleep(constants.INI_MESSAGES_LAPSE_TIME)
        self._cast = {}

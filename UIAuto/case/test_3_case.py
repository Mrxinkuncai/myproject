from UIAuto.case.main import Main


class Testwait():
    def setup(self):
        main=Main()
        main.click_first_link().title()
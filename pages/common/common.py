from selenium import webdriver
from pyvirtualdisplay import Display


class Driver:
    __driver_instance = None


    @classmethod
    def get(cls):
        if not cls.__driver_instance:

            display = Display(visible=0, size=(1280, 800))
            display.start()
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")    # Fukcing chrome. Doesn't work without this one
            chrome_options.add_argument("--disable-dev-shm-usage")



            cls.__driver_instance = webdriver.Chrome(options=chrome_options)
            cls.__driver_instance.maximize_window()

        return cls.__driver_instance


class BaseTest:
    def teardown_class(self):
        Driver.get().close()

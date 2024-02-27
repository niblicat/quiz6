from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        raise NotImplementedError("implement in subclass")

class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print("console: " + message + "\n")

class FileLogger(Logger):
    def log(self, message: str) -> None:
        with open("log.txt", "a") as file:
            file.write("file: " + message + "\n")

# this could be implemented by a given logger very easily
# application class does not care which specific file logger class is used

class Application:
    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def perform_an_activity(self) -> None:
        self.logger.log("i am doing something very entertaining")

def main() -> None:
    consoleLogger = ConsoleLogger()
    fileLogger = FileLogger()

    coolApp = Application(consoleLogger)
    coolApp.perform_an_activity()

    oneDriveTwoElectricBoogaloo = Application(fileLogger)
    oneDriveTwoElectricBoogaloo.perform_an_activity()

if __name__ == "__main__":
    main()

"""
SRP: satisfied by creating separate classes for user, activity, activity monitor, data storage, and display, each responsible for a specific system aspect

OCP: display is notified whenever the activity monitor collects new data about the user's activity, allowing for the addition of new activity types without modifying existing classes

LSP: ensured by making sure that activity class and its subclasses adhere to the observer pattern's contracts, making them compatible with the notification mechanism

ISP: defined separate interfaces for data collection and display, namely activity and Ddsplay classes that have distinct functionalities

DIP: injected dependencies like datastorage and display into the activity monitor constructor for loose coupling and easier testing
"""

from dataclasses import dataclass
from abc import ABC, abstractclassmethod

@dataclass
class User:
    id: int
    name: str
    address: str

@dataclass
class Module:
    name: str

class Calories(Module):
    def __init__(self) -> None:
        super().__init__("Calories")
        self.calories = 0

class WristRotations(Module):
    def __init__(self) -> None:
        super().__init__("Movement")
        self.wRotations = 0
    
    def new_rotation(self) -> None:
        self.wRotations += 1

class Activity(ABC):
    """abstract base class defining the contract for activities"""
    def __init__(self, name):
        self.name = name
        self.moduleDependencies: list[str] = []

    def attach_security_monitor(self, sm):
        """attaches a security monitor to the activity"""
        self.sm = sm
    
    def add_dependency(self, dependency: str):
        """adds a module dependency"""
        self.moduleDependencies.append(dependency)

    @abstractclassmethod
    def ongoing_action(self) -> None:
        """abstract method representing ongoing action for an activity"""
        return NotImplementedError

class Swimming(Activity):
    """swimming class that inherits from activity"""
    def __init__(self):
        super().__init__(name="Swimming")
        self.hasPerms = False
        self.add_dependency("WristRotations")
        self.add_dependency("Calories")

    def ongoing_action(self) -> None:
        """swimming ongoing system actions"""
        if not self.hasPerms:
            self.sm.request_permissions(self)
        
class DataStorage:
    """manages data storage"""
    def __init__(self) -> None:
        self.modules: Module = []

    def add_module(self, module: Module) -> None:
        """adds a module to data storage"""
        self.modules.append(module)

    def remove_module(self, module: Module) -> None:
        """removes a module from data storage"""
        self.modules.remove(module)

class Display:
    """manages display functionality"""
    def __init__(self, resolutionX: str, resolutionY: str):
        self.rx = resolutionX
        self.rY = resolutionY

    def collect_new_data(self, activity: Activity) -> None:
        """is called when an acitivity needs to request for new permissions"""
        print("notification: activity", activity.name, "wants to collect data")
        print("permissions needed:")
        for permission in activity.moduleDependencies:
            print("\t", permission)

class ActivityMonitor:
    """monitors activities and notifies the display"""
    def __init__(self, ds: DataStorage, display: Display) -> None:
        self.ds = ds
        self.display = display
        self.activities: list[Activity] = []

    def add_activity(self, activity) -> None:
        """adds an activity to be monitored"""
        activity.attach_security_monitor(self)
        self.activities.append(activity)

    def remove_activity(self, activity) -> None:
        """removes an activity from monitoring"""
        self.activities.remove(activity)

    def request_permissions(self, activity: Activity) -> None:
        """requests permissions for an activity and notifies the display"""
        self.display.collect_new_data(activity)

    def tick(self) -> None:
        """performs monitoring tasks every tick"""
        for activity in self.activities:
            activity.ongoing_action()
        # wait some time then call self.tick(self)

def main():
    print("start program")

    dan = User(24, "Dan", "Street St")

    myDisplay = Display(800, 800)

    myDS = DataStorage()
    calorieModule = Calories()
    wrModule = WristRotations()
    myDS.add_module(calorieModule)
    myDS.add_module(wrModule)
    
    swimming = Swimming()
    myAM = ActivityMonitor(myDS, myDisplay)
    myAM.add_activity(swimming)
    myAM.tick() # testing tick

    print("end program")

if __name__ == "__main__":
    main()

# filename: lagchain_agent.py

class LagchainAgent:
    def __init__(self, name):
        self.name = name
        self.status = 'Green'

    def set_status(self, status):
        if status.lower() == 'red':
            self.status = 'Red'
        elif status.lower() == 'amber':
            self.status = 'Amber'
        elif status.lower() == 'green':
            self.status = 'Green'
        else:
            print("Invalid status. Please choose from Red, Amber, or Green.")

    def get_status(self):
        return self.status

# Example usage:
agent = LagchainAgent('Agent1')
print(agent.get_status())  # Output: Green

agent.set_status('Amber')
print(agent.get_status())  # Output: Amber

agent.set_status('Invalid')
print(agent.get_status())  # Output: Amber (Invalid status message will be printed)

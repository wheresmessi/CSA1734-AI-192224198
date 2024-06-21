class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.location = 'A'  
        self.performance_score = 0

    def sense(self):
        return self.environment[self.location]

    def act(self, action):
        if action == 'CLEAN':
            if self.environment[self.location] == 'DIRTY':
                self.environment[self.location] = 'CLEAN'
                self.performance_score += 1
        elif action == 'RIGHT':
            self.location = 'B'
        elif action == 'LEFT':
            self.location = 'A'

    def run(self):
        for _ in range(5):  # Limit the number of actions to prevent infinite loops
            if self.sense() == 'DIRTY':
                self.act('CLEAN')
            elif self.location == 'A':
                self.act('RIGHT')
            elif self.location == 'B':
                self.act('LEFT')
        return self.performance_score

# Define the initial environment
environment = {
    'A': 'DIRTY',
    'B': 'DIRTY'
}

# Create a vacuum cleaner instance
vacuum_cleaner = VacuumCleaner(environment)

# Run the vacuum cleaner
score = vacuum_cleaner.run()

# Print the final state of the environment and the performance score
print("Final Environment State:", environment)
print("Performance Score:", score)

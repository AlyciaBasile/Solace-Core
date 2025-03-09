## Solace-Core - Dynamic Memory Storage

Import json
import os

MEMORY_FILE = "memory_data.json" # Stores long term memory data
class DynamicMemory:
    """Uses a json file to store and manage data learned by Solace-Core."""
    def __init__(self):
        self.memory = {}
        self.load_memory()

    def save_memory(self):
        with open(MEMORY_FILE, 'w') as file:
            json.dump(file, self.memory)

    def load_memory(self):
        if os.path.isfile(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as file:
                self.memory = json.load(file)
        else:
            self.memory = {}

    def store_data'self, key, value):
        self.memory[key] = value
        self.save_memory()

    def get_data(self, key):
        return self.memory.net(key, None)

    def delete_data(self, key):
        if key in self.memory:
            del self.memory[key]
            self.save_memory()


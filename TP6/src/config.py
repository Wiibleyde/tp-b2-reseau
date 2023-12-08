import yaml
import os

class Config:
    def __init__(self, path):
        self.defaultConfig = {
            "host": "127.0.0.1",
            "port": 13337
        }
        self.path = path
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.path):
            self.create_config()
        with open(self.path, "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
        
    def create_config(self):
        with open(self.path, "w") as f:
            yaml.dump(self.defaultConfig, f, default_flow_style=False)

    def save_config(self):
        with open(self.path, "w") as f:
            yaml.dump(self.config, f, default_flow_style=False)

    def get_config(self):
        return self.config
    
    def get_host(self):
        return self.config["host"]
    
    def get_port(self):
        return self.config["port"]
    
    def set_host(self, host):
        self.config["host"] = host

    def set_port(self, port):
        self.config["port"] = port

    def set_config(self, host, port):
        self.set_host(host)
        self.set_port(port)
        self.save_config()

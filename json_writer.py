import json


class JSONWriterTool:
    def __init__(self, json_path: str, config: dict):
        self.json_path = json_path
        self.config = config
        self.write_mode = config.get('writer', {}).get(
            'config', {}).get('write_mode', 'overwrite')
        self.indent = config.get('writer', {}).get(
            'config', {}).get('indent', 4)

    def write(self, data: dict):
        """
        Writes the provided data to the specified JSON file.
        If the mode is 'overwrite', it will replace the file's content.
        If the mode is 'append', it will append the data to the existing file.
        """
        if self.write_mode == 'overwrite':
            # Overwrite the JSON file with new data
            with open(self.json_path, 'w') as json_file:
                json.dump(data, json_file, indent=self.indent)
        elif self.write_mode == 'append':
            # Append new data to the existing JSON file
            try:
                # Read the existing data from the file
                with open(self.json_path, 'r') as json_file:
                    existing_data = json.load(json_file)
                # Combine existing data with new data
                if isinstance(existing_data, dict):
                    existing_data.update(data)
                else:
                    existing_data.append(data)
            except FileNotFoundError:
                # If the file does not exist, treat it like an empty file
                existing_data = data
            # Write the updated data back to the file
            with open(self.json_path, 'w') as json_file:
                json.dump(existing_data, json_file, indent=self.indent)
        else:
            raise ValueError(f"Invalid write_mode: {self.write_mode}")

    def set_json_path(self, new_path: str):
        """Allows updating the file path where the JSON is written."""
        self.json_path = new_path

    def set_write_mode(self, mode: str):
        """Allows updating the write mode (overwrite or append)."""
        if mode not in ['overwrite', 'append']:
            raise ValueError("write_mode must be 'overwrite' or 'append'")
        self.write_mode = mode

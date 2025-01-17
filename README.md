# WinRotate

WinRotate is a Python-based program designed to automatically rotate the screen orientation for tablets and monitors on Windows systems. It uses predefined settings to adjust the orientation based on the time of day, allowing for seamless transitions between different orientations as needed.

## Features

- Automatically rotates screen orientation.
- Predefined settings for time-based orientation changes.
- Supports multiple orientations: landscape, portrait, landscape flipped, and portrait flipped.

## Requirements

- Windows operating system
- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/winrotate.git
   ```

2. Navigate to the directory:
   ```bash
   cd winrotate
   ```

3. Ensure you have Python installed on your system.

## Usage

1. Open the `winrotate.py` file.
2. Define your desired settings by modifying the `predefined_settings` dictionary within the script. Use the format `(hour, minute): Orientation`.
3. Run the script:
   ```bash
   python winrotate.py
   ```

## Configuration

Customize the `predefined_settings` dictionary in `winrotate.py` to set specific times and orientations. For example:

```python
predefined_settings = {
    (9, 0): Orientation.LANDSCAPE,
    (12, 0): Orientation.PORTRAIT,
    (15, 0): Orientation.LANDSCAPE_FLIPPED,
    (18, 0): Orientation.PORTRAIT_FLIPPED
}
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This script modifies system settings. Use caution and ensure you have backups of your data before running this program.
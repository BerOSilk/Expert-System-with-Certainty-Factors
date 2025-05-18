# Expert System with Certainty Factors

## Overview
This expert system implements a rule-based decision-making framework that uses certainty factors to handle uncertainty in knowledge representation. The system provides an intuitive graphical user interface for users to input evidence and view hypothesis results in real-time.

## Features
- **Modern User Interface**
  - Clean, responsive design with consistent styling
  - Real-time validation and feedback
  - Color-coded results for easy interpretation
  - Intuitive layout with clear visual hierarchy

- **Certainty Factor Management**
  - Input validation for values between -1 and 1
  - Real-time calculation of complementary values
  - Automatic distribution of certainty factors
  - Natural language translation of certainty levels

- **Rule Processing**
  - Support for complex rule structures (AND/OR combinations)
  - Real-time rule evaluation
  - Dynamic hypothesis updates
  - Comprehensive evidence handling

## Technical Requirements
- Python 3.x
- Tkinter (included in standard Python distribution)

## Installation
1. Ensure Python 3.x is installed on your system
2. Clone or download this repository
3. No additional dependencies are required

## Usage
1. Start the application by running `Main.py`
2. Input evidence with certainty factors (-1 to 1)
3. View real-time hypothesis results
4. Interpret results using the color-coded display:
   - Green: Positive certainty (likely true)
   - Red: Negative certainty (likely false)
   - Gray: Neutral certainty (uncertain)

## Certainty Factor Scale
- 1.0: Definitely true
- 0.8 to 0.99: Almost certainly true
- 0.6 to 0.79: Probably true
- 0.4 to 0.59: Maybe true
- -0.2 to 0.39: Unknown
- -0.4 to -0.21: Maybe not
- -0.6 to -0.41: Probably not
- -0.99 to -0.61: Almost certainly not
- -1.0: Definitely not

## Project Structure
```
├── Main.py             # Application entry point
├── expert
|   ├── Rule.py         # Rule processing implementation
|   └── Expert.py       # Expert system core logic
└── gui/
    ├── GUIBuilder.py   # GUI implementation
    └── Block.py        # Block class for UI components
```

## Development
- The project uses a modular architecture for easy maintenance and extension
- The GUI is built using Tkinter with custom styling
- The expert system core is separated from the interface for better maintainability
- Real-time updates ensure immediate feedback to user inputs

## Author
Baraa AbuKhalil

## Copyright
© 2025 Baraa AbuKhalil. All rights reserved.

## License
This project is proprietary software. Unauthorized copying, modification, distribution, or use is strictly prohibited.

## Support
For support or inquiries, please contact the author.

## Version
1.0.0
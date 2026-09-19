import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Image, Table, TableStyle
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
OUTPUT_FILE = os.path.join(BASE_DIR, "report.pdf")

NAME = "Kirezi Hirwa Aldo"
REG_NO = "2401000842"
COURSE = "Mobile Application Development"
PROJECT = "Movie Watchlist"
DATE = "19 September 2026"

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleCustom",
    parent=styles["Title"],
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
    spaceAfter=20,
)

subtitle_style = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontSize=14,
    leading=20,
    alignment=TA_CENTER,
    spaceAfter=12,
)

heading_style = ParagraphStyle(
    "HeadingCustom",
    parent=styles["Heading1"],
    fontSize=18,
    leading=22,
    spaceBefore=10,
    spaceAfter=12,
)

subheading_style = ParagraphStyle(
    "SubHeadingCustom",
    parent=styles["Heading2"],
    fontSize=14,
    leading=18,
    spaceBefore=8,
    spaceAfter=8,
)

body_style = ParagraphStyle(
    "BodyCustom",
    parent=styles["BodyText"],
    fontSize=10.5,
    leading=16,
    alignment=TA_LEFT,
    spaceAfter=10,
)

caption_style = ParagraphStyle(
    "Caption",
    parent=styles["BodyText"],
    fontSize=9,
    leading=12,
    alignment=TA_CENTER,
    textColor=colors.grey,
    spaceAfter=12,
)

center_style = ParagraphStyle(
    "Center",
    parent=styles["BodyText"],
    fontSize=11,
    leading=16,
    alignment=TA_CENTER,
)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.drawString(
        2 * cm,
        1 * cm,
        f"{NAME} | {REG_NO}"
    )
    canvas.drawRightString(
        A4[0] - 2 * cm,
        1 * cm,
        f"Page {doc.page}"
    )
    canvas.restoreState()

def add_screenshot(story, number, caption):
    image_path = os.path.join(
        SCREENSHOT_DIR,
        f"M{number}.png"
    )

    if os.path.exists(image_path):
        img = Image(image_path)

        max_width = 16 * cm
        max_height = 18 * cm

        width = img.imageWidth
        height = img.imageHeight

        scale = min(
            max_width / width,
            max_height / height
        )

        img.drawWidth = width * scale
        img.drawHeight = height * scale

        story.append(img)
        story.append(Spacer(1, 0.3 * cm))
        story.append(
            Paragraph(
                f"Figure M{number}: {caption}",
                caption_style
            )
        )
    else:
        story.append(
            Paragraph(
                f"M{number} screenshot was not found.",
                caption_style
            )
        )

def add_milestone(story, number, title, learning, caption):
    story.append(
        Paragraph(
            f"M{number}: {title}",
            heading_style
        )
    )

    story.append(
        Paragraph(
            learning,
            body_style
        )
    )

    add_screenshot(
        story,
        number,
        caption
    )

    story.append(PageBreak())

doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    rightMargin=2 * cm,
    leftMargin=2 * cm,
    topMargin=2 * cm,
    bottomMargin=1.7 * cm,
)

story = []

# COVER PAGE
story.append(Spacer(1, 4 * cm))

story.append(
    Paragraph(
        "MOVIE WATCHLIST",
        title_style
    )
)

story.append(
    Paragraph(
        "Mobile Application Development Project",
        subtitle_style
    )
)

story.append(Spacer(1, 1.5 * cm))

cover_data = [
    ["Student Name", NAME],
    ["Registration Number", REG_NO],
    ["Course", COURSE],
    ["Project", "Project 10"],
    ["Application", PROJECT],
    ["Date", DATE],
]

table = Table(
    cover_data,
    colWidths=[6 * cm, 9 * cm]
)

table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ])
)

story.append(table)
story.append(Spacer(1, 2 * cm))

story.append(
    Paragraph(
        "University of Kigali – Musanze Campus",
        center_style
    )
)

story.append(PageBreak())

# 1 INTRODUCTION
story.append(
    Paragraph(
        "1. Introduction",
        heading_style
    )
)

story.append(
    Paragraph(
        "Movie Watchlist is a Flutter mobile application designed to help users organize "
        "movies they want to watch. The application allows users to view movies, open "
        "movie details, add new movies, mark movies as watched, remove movies, and keep "
        "their movie information saved locally.",
        body_style
    )
)

story.append(
    Paragraph(
        "The application is intended for people who want a simple way to organize their "
        "personal movie collection. It demonstrates important mobile application "
        "development concepts including Flutter widgets, Dart programming, Riverpod "
        "state management, navigation, form validation, animations, JSON serialization, "
        "and local persistence.",
        body_style
    )
)

story.append(
    Paragraph(
        "The project also demonstrates how a mobile application can provide useful "
        "functionality through a clean interface while maintaining application state "
        "between sessions.",
        body_style
    )
)

story.append(PageBreak())

# 2 PROBLEM
story.append(
    Paragraph(
        "2. Problem Statement",
        heading_style
    )
)

story.append(
    Paragraph(
        "Movie lovers may have difficulty remembering movies they want to watch and "
        "keeping track of which movies they have already watched. Using informal notes "
        "or relying only on memory can make the collection difficult to manage.",
        body_style
    )
)

story.append(
    Paragraph(
        "The Movie Watchlist application addresses this problem by providing a simple "
        "digital watchlist where users can store movie information, view details, "
        "mark movies as watched, and maintain the collection using local storage.",
        body_style
    )
)

story.append(PageBreak())

# 3 OBJECTIVES
story.append(
    Paragraph(
        "3. Objectives",
        heading_style
    )
)

story.append(
    Paragraph(
        "<b>General Objective</b>",
        subheading_style
    )
)

story.append(
    Paragraph(
        "To develop a functional Flutter mobile application that allows users to "
        "manage and organize a personal movie watchlist.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Specific Objectives</b>",
        subheading_style
    )
)

objectives = [
    "Create a user-friendly movie watchlist interface.",
    "Implement navigation between the movie list and movie detail screens.",
    "Allow users to add movies through a validated form.",
    "Allow users to mark movies as watched and remove movies.",
    "Use Riverpod for application state management.",
    "Use JSON serialization and SharedPreferences for local persistence.",
    "Implement Flutter animations including Hero and implicit animations.",
]

for objective in objectives:
    story.append(
        Paragraph(
            f"• {objective}",
            body_style
        )
    )

story.append(PageBreak())

# 4 TECHNOLOGIES
story.append(
    Paragraph(
        "4. Tools and Technologies",
        heading_style
    )
)

technologies = [
    ("Flutter", "Used to build the mobile application interface and application structure."),
    ("Dart", "Programming language used to implement the application logic."),
    ("Riverpod", "Used for state management and sharing movie data between screens."),
    ("SharedPreferences", "Used to store movie information locally on the device."),
    ("JSON", "Used for serialization and deserialization of movie data."),
    ("Git", "Used for version control and milestone commits."),
    ("GitHub", "Used to host and submit the project repository."),
    ("Android Studio / Android SDK", "Used for Android development and testing."),
    ("BlueStacks / Android Emulator", "Used to test the application on an Android environment."),
]

tech_table = Table(
    [["Technology", "Purpose"]] + technologies,
    colWidths=[5 * cm, 10 * cm]
)

tech_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ])
)

story.append(tech_table)
story.append(PageBreak())

# 5 DESIGN
story.append(
    Paragraph(
        "5. Application Design",
        heading_style
    )
)

story.append(
    Paragraph(
        "<b>Home Screen:</b> Displays movies in a grid and provides access to the "
        "add-movie functionality.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Movie Detail Screen:</b> Displays the selected movie's poster, title, "
        "genre, year, description, and watched status.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Add Movie Screen:</b> Provides a validated form for entering a movie's "
        "title, genre, year, poster URL, and description.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Navigation:</b> Users move from the Home Screen to the Movie Detail "
        "Screen by selecting a movie. The Add Movie button opens the movie form.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Data Model:</b> Each movie contains an ID, title, poster URL, description, "
        "genre, year, and watched status.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>State Management:</b> MovieNotifier manages the movie list using Riverpod. "
        "Changes such as adding, removing, or marking movies as watched update the "
        "application state and are saved locally.",
        body_style
    )
)

story.append(PageBreak())

# MILESTONES
add_milestone(
    story,
    1,
    "Project Setup and Custom Launcher Icon",
    "During M1, the Flutter project was created and the basic project structure was "
    "prepared. Required dependencies were configured and a custom launcher icon was "
    "added. This milestone helped establish the foundation of the application and "
    "introduced the process of configuring a Flutter project before implementing "
    "application features.",
    "Flutter project setup, environment verification, and custom application icon."
)

add_milestone(
    story,
    2,
    "Movie Model",
    "During M2, the Movie model was created. The model contains the information "
    "required by each movie, including its ID, title, poster URL, description, genre, "
    "year, and watched status. JSON conversion methods were also implemented. This "
    "milestone helped demonstrate how Dart classes represent structured application "
    "data.",
    "Movie model and JSON serialization implementation."
)

add_milestone(
    story,
    3,
    "Riverpod Provider",
    "During M3, Riverpod was introduced for state management. MovieNotifier was "
    "implemented to manage the movie list and provide operations for adding, removing, "
    "and updating movies. This milestone helped demonstrate how application state can "
    "be managed independently from the user interface.",
    "Riverpod MovieNotifier and movie provider."
)

add_milestone(
    story,
    4,
    "Home Screen and Empty State",
    "During M4, the first major user interface was created. Movies were displayed "
    "using a GridView and an empty state was provided when no movies were available. "
    "This milestone helped develop skills in Flutter layouts, widgets, and conditional "
    "user interface rendering.",
    "Movie grid and empty-state interface."
)

add_milestone(
    story,
    5,
    "Movie Detail Screen and Navigation",
    "During M5, a second screen was created to display complete movie information. "
    "Navigation was implemented so that a selected Movie object could be passed from "
    "the home screen to the detail screen. This milestone helped demonstrate Flutter "
    "navigation and passing data between screens.",
    "Movie detail screen and navigation from the movie collection."
)

add_milestone(
    story,
    6,
    "Animations",
    "During M6, the application interface was improved with AnimatedContainer, "
    "AnimatedOpacity, and Hero animations. These animations provide visual feedback "
    "and smoother transitions when users interact with movie cards and open details. "
    "This milestone improved understanding of Flutter's animation capabilities.",
    "Animated movie cards and Hero transition."
)

add_milestone(
    story,
    7,
    "Persistence, Validation and Error Feedback",
    "During M7, local persistence was implemented using SharedPreferences. Movie data "
    "is converted to JSON before being stored and reconstructed when the application "
    "loads. The add-movie form also validates user input and displays feedback using "
    "a SnackBar. This milestone demonstrated the importance of data persistence and "
    "input validation.",
    "Add movie form, validation, local persistence, and user feedback."
)

add_milestone(
    story,
    8,
    "Final Polish and Release Build",
    "During M8, the application was tested and prepared for final submission. The "
    "project was analyzed, the release APK was generated, and the final application "
    "was tested in an Android environment. This milestone helped demonstrate the "
    "complete process from development to application delivery.",
    "Final Movie Watchlist application and release build."
)

# TESTING
story.append(
    Paragraph(
        "7. Testing",
        heading_style
    )
)

tests = [
    ("Application launch", "Application launched successfully."),
    ("Movie list", "Movies were displayed correctly on the home screen."),
    ("Empty state", "Empty-state interface was displayed when there were no movies."),
    ("Movie details", "Selecting a movie opened its detail screen."),
    ("Add movie", "A new movie could be added through the form."),
    ("Validation", "Invalid form data was rejected with validation messages."),
    ("Watched status", "Movies could be marked as watched."),
    ("Remove movie", "Movies could be removed from the collection."),
    ("Persistence", "Saved movie information remained available after restarting."),
    ("Animations", "Hero and implicit animations were visible during interaction."),
    ("Release APK", "The release APK was successfully generated and tested."),
]

test_table = Table(
    [["Test", "Result"]] + tests,
    colWidths=[6 * cm, 9 * cm]
)

test_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ])
)

story.append(test_table)
story.append(PageBreak())

# CHALLENGES
story.append(
    Paragraph(
        "8. Challenges Encountered",
        heading_style
    )
)

challenges = [
    (
        "State management",
        "Managing movie data across different screens was initially challenging. "
        "Riverpod was introduced to provide a central state management solution."
    ),
    (
        "Data persistence",
        "Keeping movie information after restarting the application required local "
        "storage. SharedPreferences and JSON serialization were used to solve this."
    ),
    (
        "Form validation",
        "User input needed to be checked before adding a movie. Validation rules "
        "were added for the required fields and poster URL."
    ),
    (
        "Animations",
        "Implementing Hero and implicit animations required understanding how "
        "widgets change state and how animation tags must match between screens."
    ),
]

for title, description in challenges:
    story.append(
        Paragraph(
            f"<b>{title}:</b> {description}",
            body_style
        )
    )

story.append(PageBreak())

# LIMITATIONS
story.append(
    Paragraph(
        "9. Limitations",
        heading_style
    )
)

limitations = [
    "The application does not provide user accounts or cloud synchronization.",
    "Movie information is entered manually rather than being retrieved from a full movie database API.",
    "The application depends on valid poster image URLs for online movie posters.",
]

for limitation in limitations:
    story.append(
        Paragraph(
            f"• {limitation}",
            body_style
        )
    )

story.append(PageBreak())

# CONCLUSION
story.append(
    Paragraph(
        "10. Conclusion",
        heading_style
    )
)

story.append(
    Paragraph(
        "The Movie Watchlist project successfully demonstrates the development of a "
        "functional Flutter mobile application. The application combines a structured "
        "movie model, Riverpod state management, navigation, form validation, "
        "animations, JSON serialization, and local persistence.",
        body_style
    )
)

story.append(
    Paragraph(
        "The project also provided practical experience in using Git and GitHub, "
        "testing a Flutter application on an Android environment, and producing a "
        "release APK for submission.",
        body_style
    )
)

story.append(
    Paragraph(
        "In a future version, the application could be extended with a movie database "
        "API, user accounts, cloud synchronization, search, categories, and additional "
        "movie information.",
        body_style
    )
)

story.append(PageBreak())

# REFERENCES
story.append(
    Paragraph(
        "11. References",
        heading_style
    )
)

references = [
    "Flutter Documentation – Flutter framework and widgets.",
    "Dart Documentation – Dart programming language.",
    "Riverpod Documentation – State management for Flutter and Dart.",
    "SharedPreferences Documentation – Local key-value storage.",
    "Git Documentation – Version control.",
    "GitHub Documentation – Repository hosting and collaboration.",
]

for reference in references:
    story.append(
        Paragraph(
            f"• {reference}",
            body_style
        )
    )

story.append(Spacer(1, 1 * cm))

story.append(
    Paragraph(
        "<b>Project Repository</b>",
        subheading_style
    )
)

story.append(
    Paragraph(
        "https://github.com/aldohirwakirezi/2401000842_Aldo_flutter_weekend",
        body_style
    )
)

doc.build(
    story,
    onFirstPage=footer,
    onLaterPages=footer
)

print("=" * 45)
print("REPORT CREATED SUCCESSFULLY")
print("=" * 45)
print(f"File: {OUTPUT_FILE}")
print()
print("Checking screenshots:")

for i in range(1, 9):
    path = os.path.join(
        SCREENSHOT_DIR,
        f"M{i}.png"
    )

    if os.path.exists(path):
        print(f"M{i}.png  - FOUND")
    else:
        print(f"M{i}.png  - NOT FOUND")
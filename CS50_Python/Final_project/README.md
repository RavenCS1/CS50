# YouTube Playlist Manager 📱🎵

Console tool for managing YouTube playlists saved in CSV files. Created as backup for lost playlists after a hacked Google account.

## ✨ Features

| Operator | Action |
|----------|--------|
| `view` | Display full playlist in table |
| `find` | Find song URL by author and title |
| `add` | Add YouTube song (fetches author/title, avoids duplicates) |
| `change` | Change playlist filename |
| `create` | Create new empty CSV file |
| `remove` | Remove specific song by author/title |
| `clear` | Clear all songs (with confirmation) |
| `delete` | Delete entire file (with confirmation) |
| `exit` | Exit program |

## 🚀 Quick Start

Install dependencies
pip install -r requirements.txt

Run
python project.py

### Program flow:
1. Enter filename (must end with `.csv`)
2. Select action from menu (`view`, `find`, `add`, etc.)
3. Follow interactive prompts

Built-in input validation and infinite loops - errors don't crash the app.

## 📄 CSV File Structure

- **id**: Auto-incremented
- **author**: Artist/performer
- **title**: Song title
- **url**: Full YouTube link

## 🧪 Tests

python test_project.py

Tests validate:
- Menu action validation
- YouTube URL format
- `.csv` filenames

## 📁 Project Files

| File | Description |
|------|-------------|
| `project.py` | Main program (9 action functions) |
| `test_project.py` | Unit tests for functions |
| `starting_menu.csv` | Startup menu data |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation |

## 📦 Dependencies

pytube # YouTube metadata fetching
pyfiglet # Fancy startup text
tabulate # Pretty tables
unicodecsv # Unicode CSV handling

## 🔧 Input Validation

- **Filename**: `r".*.csv"` (regex)
- **YouTube URL**: `r"https?://www\.?youtube\.com/.*"` (regex)
- **Actions**: 9 allowed commands list

## 💡 Special Features

- **Automatic duplicate detection** when adding
- **ASCII tables** via `tabulate`
- **Fancy menu** via `pyfiglet`
- **Confirmations** for destructive actions (`clear`, `delete`)
- **Empty file handling** and Unicode error handling


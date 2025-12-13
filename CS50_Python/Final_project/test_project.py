from project import validate_action
from project import validate_url
from project import validate_name

def test_validate_action():
    assert validate_action("view")==True
    assert validate_action("find")==True
    assert validate_action("add")==True
    assert validate_action("remove")==True
    assert validate_action("exit")==True
    assert validate_action("clear")==True
    assert validate_action("change")==True
    assert validate_action("delete")==True
    assert validate_action("create")==True
    assert validate_action("invalid_operator")==False
    assert validate_action("not as planned")==False
    assert validate_action("idk")==False

def test_validate_url():
    assert validate_url("https://www.youtube.com/watch?v=hTWKbfoikeg")==True
    assert validate_url("https://www.youtube.com/watch?v=4JKG-i1hTV4")==True
    assert validate_url("https://www.youtube.com/watch?v=eJO5HU_7_1w")==True
    assert validate_url("http://www.youtube/com/efdbqwyg")==True
    assert validate_url("http://youtube/com/efdbqwyg")==True
    assert validate_url("youtube/com/efdbqwyg")==False
    assert validate_url("www.youtube/com/efdbqwyg")==False
    assert validate_url("http://youtube/com/")==False

def test_validate_name():
    assert validate_name("playlist.csv")==True
    assert validate_name("playlist.CSV")==False
    assert validate_name("PLAYLIST.CSV")==False
    assert validate_name("PLAYLIST.csv")==True
    assert validate_name("playlist")==False
    assert validate_name("playlistcsv")==False
    assert validate_name("playlist.txt")==False
    assert validate_name("playlist.py")==False

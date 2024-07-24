import os
import folderstats

def test__folders(generated_folderpath):
    df = folderstats.folderstats(
        generated_folderpath)

    assert len(df) == 18 if os.name == 'posix' else 17
    assert df['folder'].sum() == 5 if os.name == 'posix' else 4

def test__filter_extension(generated_folderpath):
    df = folderstats.folderstats(
        generated_folderpath,
        filter_extension=['py'])
    
    assert len(df) == 9 if os.name == 'posix' else 8
    assert df['folder'].sum() == 5 if os.name == 'posix' else 4

def test__exclude(generated_folderpath):
    df = folderstats.folderstats(
        generated_folderpath,
        exclude=['file.txt','folder_01'])
    
    assert len(df) == 8 if os.name == 'posix' else 7
    assert df['folder'].sum() == 3 if os.name == 'posix' else 2

def test__ignore_hidden(generated_folderpath):
    df = folderstats.folderstats(
        generated_folderpath,
        ignore_hidden=True)
    
    assert len(df) == 17 if os.name == 'posix' else 16
    assert df['folder'].sum() == 5 if os.name == 'posix' else 4

def test__follow_links(generated_folderpath):
    df = folderstats.folderstats(
        generated_folderpath,
        follow_links=True)

    assert len(df) == 19 if os.name == 'posix' else 17
    assert df['folder'].sum() == 6 if os.name == 'posix' else 4

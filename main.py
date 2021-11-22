import sqlalchemy


def filling_database():
    '''
    Fills the database with some information
    '''
    db = ''
    engine = sqlalchemy.create_engine(db)
    query = engine.connect()
    # this clears the DB prior to filling, avoids collisions
    query.execute("""TRUNCATE artists CASCADE;""")
    query.execute("""TRUNCATE genre CASCADE;""")
    query.execute("""TRUNCATE artist_genre CASCADE;""")
    query.execute("""TRUNCATE albums CASCADE;""")
    query.execute("""TRUNCATE albums_artists CASCADE;""")
    query.execute("""TRUNCATE tracks CASCADE;""")
    query.execute("""TRUNCATE comps CASCADE;""")
    query.execute("""
       INSERT INTO artists
           VALUES
               (0, 'Boy Pablo'),
               (1, 'Roy Pablo'),
               (2, 'Poy Rablo'),
               (3, 'Toy Roy'),
               (4, 'Girl Padme'),
               (5, 'Chowder'),
               (6, 'Troy Gizmo'),
               (7, 'GiztheWiz');
       """)
    query.execute("""
       INSERT INTO genre
           VALUES
               (0, 'Rock'),
               (1, 'Pop'),
               (2, 'Metal'),
               (3, 'Hip-Hop'),
               (4, 'Jazz'),
               (5, 'Soul');
       """)
    query.execute("""
       INSERT INTO artist_genre
           VALUES
               (0, 0, 1),
               (1, 1, 3),
               (2, 2, 0),
               (3, 3, 2),
               (4, 4, 4),
               (5, 5, 3),
               (6, 6, 4),
               (7, 7, 5),
               (8, 7, 4),
               (9, 5, 2);
       """)
    query.execute(("""
       INSERT INTO albums
           VALUES
               (0, 'Hybrid', 2020),
               (1, 'The One and Only', 2017),
               (2, 'Escape The Plan', 2021),
               (3, 'Courage of the Beholder', 2011),
               (4, 'March the Third', 2019),
               (5, 'Colonial', 2009),
               (6, 'Uphill Climb', 2015),
               (7, 'System Meltdown', 2018),
               (8, 'Sweet & Sour', 2020),
               (9, 'Twisted Helix', 2019);
       """))
    query.execute("""
       INSERT INTO albums_artists
           VALUES 
               (0, 0, 1),
               (1, 1, 2),
               (2, 2, 3),
               (3, 3, 4),
               (4, 4, 5),
               (5, 1, 6),
               (6, 6, 7),
               (7, 3, 8),
               (8, 7, 9),
               (9, 4, 0);
       """)
    query.execute("""
       INSERT INTO tracks
           VALUES
               (0, 'Keeping My Promise', 180, 1),
               (1, 'My Own', 200, 2),
               (2, 'Far Away Land', 160, 3),
               (3, 'Double my fee', 221, 4),
               (4, 'Create the Creator', 90, 5),
               (5, 'Surge', 190, 6),
               (6, 'Keepsake', 301, 7),
               (7, 'Fly, You FOOLS!', 280, 8),
               (8, 'Stranger and Stranger', 101, 9),
               (9, 'Tiny Giant', 166, 4),
               (10, 'Knightmare', 170, 8),
               (11, 'Festive Shower of Gifts', 208, 4),
               (12, 'Thermonuclear', 381, 7),
               (13, 'A Dull Switchblade', 100, 1),
               (14, 'Twin Winds of the Savannah', 199, 9),
               (15, 'Heavy Metal Machinery', 331, 9),
               (16, 'Scratch Card', 80, 2),
               (17, 'Cold Flame, Hot Snow', 119, 0),
               (18, 'Labyrinth of Thoughts', 142, 6),
               (19, 'Stay a Little More', 240, 0);
       """)
    query.execute("""
       INSERT INTO comps
           VALUES
               (0, 'State of Art', 2020),
               (1, 'For a Rainy Day', 2019),
               (2, 'Piece of Peace', 2021),
               (3, 'Unusual', 2021),
               (4, 'Work Your Body', 2018),
               (5, 'Moody and Sad', 2018),
               (6, 'Stories', 2010),
               (7, 'Bright Sunshine', 2019),
               (8, 'Jolly Good!', 2020),
               (9, 'One of Many, One of the Best', 2017),
               (10, 'Beach, Sand, Summer', 2016);

       """)
    query.execute("""
       INSERT INTO comps_tracks
           VALUES
               (0, 0, 1),
               (1, 1, 2),
               (2, 2, 1),
               (3, 3, 4),
               (4, 4, 8),
               (5, 5, 6),
               (6, 6, 0),
               (7, 7, 8),
               (8, 7, 19),
               (9, 10, 10);

       """)


def main():
    db = ''
    engine = sqlalchemy.create_engine(db)
    query = engine.connect()
    filling_database()

    result = query.execute("""
    SELECT album_name, album_release_year 
    FROM albums
    WHERE album_release_year >= 2018
    ORDER BY album_release_year
    """).fetchall()
    print('\nAlbums from 2018 and onward:\n', result)

    result = query.execute("""
    SELECT track_title, track_runtime
    FROM tracks
    ORDER BY track_runtime DESC
    LIMIT 1
    """).fetchall()
    print('\nLongest track:\n', result)

    result = query.execute("""
    SELECT track_title
    FROM tracks
    WHERE track_runtime >= 210
    ORDER BY track_runtime
    """).fetchall()
    print('\nTracks longer than 3.5 minutes:\n', result)

    result = query.execute("""
    SELECT comp_name 
    FROM comps
    WHERE comp_release_date BETWEEN 2018 AND 2020
    """).fetchall()
    print('\nCompilations 2018-2020:\n', result)

    result = query.execute("""
    SELECT artist_name 
    FROM artists
    WHERE artist_name NOT LIKE '%% %%'
    """).fetchall()
    print('\nArtists with one word name:\n', result)

    result = query.execute("""
    SELECT track_title 
    FROM tracks
    WHERE track_title iLIKE '%%my%%'
    """).fetchall()
    print('\nTrack title with "my" in the name:\n', result)



if __name__ == '__main__':
    main()



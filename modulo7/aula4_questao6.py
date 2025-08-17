import csv

with open("spotify-2023.csv", encoding="latin-1") as f:
    reader = csv.reader(f)

    # Lendo o cabeçalho
    header = next(reader)

    track_idx = header.index("track_name")
    artist_idx = header.index("artist(s)_name")
    artist_count_idx = header.index("artist_count")
    year_idx = header.index("released_year")
    streams_idx = header.index("streams")

    mais_tocadas = {}

    for row in reader:
        try:
            if len(row) < len(header):
                continue

            track = row[track_idx]
            artist = row[artist_idx]
            artist_count = int(row[artist_count_idx])
            year = int(row[year_idx])
            streams = int(row[streams_idx])

            if artist_count > 1:
                continue

            if 2012 <= year <= 2022:
                if (year not in mais_tocadas) or (streams > mais_tocadas[year][3]):
                    mais_tocadas[year] = [track, artist, year, streams]

        except ValueError:
            continue

resultado = [mais_tocadas[ano] for ano in sorted(mais_tocadas.keys())]

print(resultado)
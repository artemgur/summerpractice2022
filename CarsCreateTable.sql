CREATE TABLE cars (
    id serial PRIMARY KEY,
    price int,
    year int,
    condition int,
    cylinders int,
    odometer int,
    title_status text,
    transmission text,
    drive text,
    size text,
    lat float,
    long float,
    weather_f float
)
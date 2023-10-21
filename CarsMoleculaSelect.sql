SELECT id AS id__Int, price AS price__Int, year AS year__Int, condition AS condition__Int, cylinders AS cylinders__Int, odometer AS odometer__Int, title_status AS title_status__String, transmission AS transmission__String, drive AS drive__String, size AS size__String, lat AS lat__Decimal, long AS long__Decimal, (weather_f - 32) / 1.8 AS weather_c__Decimal
FROM CARS
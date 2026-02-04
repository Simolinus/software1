import mariadb
connection = mariadb.connect(

    host="127.0.0.1",
    port=3306,
    user="johslo",
    password="password",
    database="flight_game",
    autocommit=True
)
print("Connection established")
def get_airport_by_icao(connection, icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchall()
    if result:
        for record in result:
            print(f"{icao}: {record[0], record[1]}")
    else:
        print(f"\nNo airport such as {icao}")
    cursor.close()

airport_icao = input("Enter airport ICAO: ")
print("\n")
get_airport_by_icao(connection, airport_icao)

def get_name_type_by_area_code(connection, iso_country):
    sql = "SELECT name, type FROM airport WHERE iso_country = ? ORDER BY type DESC"
    cursor = connection.cursor()
    cursor.execute(sql, (iso_country,))
    result = cursor.fetchall()
    if result:
        for record in result:
            print(f"{iso_country}: {record[0], record[1]}")
    else:
        print(f"\nNo country such as {iso_country}")
    cursor.close()

input_iso_country = input("Enter country area code: ")
get_name_type_by_area_code(connection, input_iso_country)
print("\n")

from geopy import distance

def get_distance_between_airports(connection, icao, icao2):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ? OR ident = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (icao, icao2))
    result = cursor.fetchall()
    airport1 = result[0]
    airport2 = result[1]
    print(f"distance between {icao} and {icao2} is {distance.distance(airport1, airport2).km:.3f}km")
    cursor.close()

print("Compare distance between two airports.")
icao1 = input("Enter airport ICAO: ")
icao2 = input("Enter airport ICAO: ")

get_distance_between_airports(connection, icao1, icao2)
connection.close()
print("\nConnection closed")
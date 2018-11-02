from imdb import IMDb
import mysql.connector
from mysql.connector import Error



def main():
    
    movieIdList = ["0118715", "0362270", "0456554", "3416742"]
    ia = IMDb()
    
    
    def dbConnect():    
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='bmdb',
                                           user='python_connector',
                                           password='sudo')
                
        except Error as e:
            print(e)
            
        return conn
    
    def fetchMovieData(movieID):
        
        movie = ia.get_movie(movieID)
        
        return movie
    
    
    def printMovieData():
        movie = fetchMovieData("0362270")
        title = movie['title']
        genre = movie['genre'][0]
        rating = movie['rating']
        year = movie['year']
        director = movie['director'][0]
        for artist in movie['cast'][0:9]:
            firstName, lastName = artist['name'].split(' ')
            print(firstName, lastName)
    
    

#     conn = dbConnect()
#     conn.close()

    printMovieData()
    
    
if __name__ == "__main__": main()
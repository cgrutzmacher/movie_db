from imdb import IMDb
import mysql.connector
from mysql.connector import Error



def main():
    
    movieIdList = ["0118715", "0362270", "0456554", "3416742", "0107048", "0208092", "0120735", "0375912"]
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
    
    def getMovieData(movieID):
        
        movie = ia.get_movie(movieID)
        
        return movie
    
    def getTop250Movies():
        
        topMovies = ia.get_top250_movies()
        
        return topMovies
    
    
    def printMovieData(movie):
        title = movie['title']
        genre = movie['genre']
        rating = movie['rating']
        year = movie['year']
        director = movie['director'][0]
        for artist in movie['cast'][0:9]:
            name = artist['name']
    
    def insertMovieData(movie, conn):
        movieQuery = """INSERT INTO movie VALUES (NULL, %s, %s, %s, %s, %s);"""
        artistQuery = """INSERT INTO artist VALUES (NULL, '{0}');"""
        creditQuery = """INSERT INTO credit VALUES (NULL, %s, %s);"""
        artistCheckQuery = """SELECT ID, COUNT(*) FROM artist WHERE artistName = '{0}';"""
        movieID = 0;
        artistID = 0;
        
        title    = str(movie['title'])
        genre    = str(movie['genre'][0])
        rating   = str(movie['rating'])
        year     = str(movie['year'])
        director = str(movie['director'][0])
        
        cursor = conn.cursor()
        
        cursor.execute(movieQuery, (title, genre, rating, year, director))
        movieID = cursor.lastrowid
        print(title, " added to database")
        
        for artist in movie['cast']:      
            name = artist['name'].replace("'", " ")
            asq = artistCheckQuery.format(name)
            cursor.execute(asq)
            row_count = cursor.fetchall()
            
            if row_count[0][1] == 1:       
                artistID = row_count[0][0]
            else:
                aq = artistQuery.format(name)     
                cursor.execute(aq)
            
                artistID = cursor.lastrowid
             
            cq = creditQuery%(movieID, artistID)
            cursor.execute(cq)     
        

    conn = dbConnect()
    for i in movieIdList:
        movie = getMovieData(i)    
        insertMovieData(movie, conn)
    conn.commit()
    conn.close()

    print("finished")
    
    
if __name__ == "__main__": main()
from media import Movie
import fresh_tomatoes
# init of the Movie class

# initializes the first movie information values
Rab_Ne_Bana_Di_Jodi = Movie("Rab Ne Bana Di Jodi",
                  "A Unique Love story between man and girl ",
                  "http://2.bp.blogspot.com/_8pI3k3LUfEU/SRRhxZt-aXI/AAAAAAAAADg/-4Hl9EbLWMA/s400/srk.jpg",
                  "https://www.youtube.com/watch?v=s5AV_qtMuLQ")
# second movie
avatar = Movie("Avatar",
               "A story about an alien on a planet",
               "http://2.bp.blogspot.com/_XRN97bhAado/TTBpS_TYL2I/AAAAAAAAACI/wgAxitA2o4g/s1600/avatar-oridginal.jpg",  # noqa
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

star_trek = Movie("Star Trek",
                  "An amazing adventure on the space ?",
                  "http://www.letswatchstartrek.com/wp-content/uploads/2013/05/star-trek-2009.jpg",  # noqa
                  "https://www.youtube.com/watch?v=dCyv5xKIqlw")

b_f_g = Movie("Big Friendly Giant",
                     "Lovely Girl meets the friendly Giant who tried to protect her !",
                     "http://i0.wp.com/alpha-omegagaming.de/wp-content/uploads/2016/01/Big-friendly-Giant.png",
                     "https://www.youtube.com/watch?v=50Ek2vkwv64")

dont_step_back= Movie("Don't Step Back",
                     "a stupid man facing a lot of trouble situation .",
                     "http://1.bp.blogspot.com/-Yc-mcfPmALY/TcGaxscZJrI/AAAAAAAAAKc/6iZaQBlyuxg/s1600/La+Tarago3+Wa+La+Estislam.jpg",  # noqa
                     "https://www.youtube.com/watch?v=76yBTNDB6vU")

wanted = Movie("Wanted",
                  "Ordinary Man turned into a super hero and discovered unbelievable things about his father ;)",
                  "http://img03.deviantart.net/6e60/i/2008/068/e/6/wanted_movie_poster_by_tylerbxgroz.jpg",
                  "https://www.youtube.com/watch?v=-TJ0o4oB0gc")

# Creating a list that contain all info about the movies mentioned above.
movies = [Rab_Ne_Bana_Di_Jodi, avatar, star_trek, b_f_g, dont_step_back, wanted]
# passing the previous lis  of movies to the fresh_tomatoes.py file to open it in a html page .
fresh_tomatoes.open_movies_page(movies)

# printing a valid rating and string doc and name and module of the Movie Class
"""print(Movie.VALID_RATINGS)

print(Movie.__doc__)
print(Movie.__name__)
print(Movie.__module__) """